#!/usr/bin/env python3
"""Model and retune the G0KSC SC42014W 14-element 70 cm OWA yagi for other element diameters."""
import re, subprocess, tempfile, os

NAMES = ["Ref", "DE"] + [f"D{i}" for i in range(1, 13)]

# Published design (G0KSC SC42014W), metres. Boom positions and element half-lengths.
SPACING = [0.0, .129, .180, .291, .425, .606, .730, .869, 1.018, 1.167, 1.393, 1.58, 1.686, 1.843]
HALFLEN = [.168, .165, .146, .140, .1355, .135, .1275, .129, .118, .1315, .1355, .131, .132, .1295]

SEGS = 15
DRIVEN = 1


def deck(halflen, radius, title, freqs=(420.0, 21, 1.0), full_pattern=True, spacing=None,
         radii=None):
    f0, nf, df = freqs
    L = ["CM " + title,
         f"CM Element diameter {2000*radius:.2f} mm; elements insulated above boom, no boom correction",
         f"CM {SEGS} segments per element, extended thin-wire kernel, free space",
         "CE"]
    for i, (x, h) in enumerate(zip(spacing or SPACING, halflen)):
        a = (radii or {}).get(i, radius)
        L.append(f"GW {i+1:3d} {SEGS:3d} {x: .5f} {-h: .5f}  0.00000 "
                 f"{x: .5f} {h: .5f}  0.00000 {a: .6f}")
    L += ["GE 0", "EK",
          f"EX 0 {DRIVEN+1} {SEGS//2+1} 0 1.0 0.0",
          f"FR 0 {nf} 0 0 {f0:.3f} {df:.3f}"]
    L += (["RP 0   1 361 1000 90.0  0.0 0.0 1.0",
           "RP 0 361   1 1000  0.0  0.0 1.0 0.0"] if full_pattern else
          ["RP 0   1  37 1000 90.0  0.0 0.0 10.0"])
    return "\n".join(L + ["EN"]) + "\n"


def run(text):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, "a.nec"), os.path.join(d, "a.out")
        open(i, "w").write(text)
        subprocess.run(["nec2c", "-i" + i, "-o" + o], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return parse(open(o).read())


def parse(out):
    res = []
    for blk in out.split("--------- FREQUENCY --------")[1:]:
        f = float(re.search(r"FREQUENCY\s*:\s*(\S+)\s*MHz", blk).group(1))
        m = re.search(r"ANTENNA INPUT PARAMETERS.*?\n.*\n.*\n\s*(?:\S+\s+){6}(\S+)\s+(\S+)", blk)
        res.append(dict(f=f, r=float(m.group(1)), x=float(m.group(2)),
                        swr=swr(float(m.group(1)), float(m.group(2))), **_pattern(blk)))
    return res


def _pattern(blk):
    rows = []
    for ln in blk.splitlines():
        t = ln.split()
        if len(t) >= 5 and re.fullmatch(r"-?\d+\.\d+", t[0]) and re.fullmatch(r"-?\d+\.\d+", t[1]):
            rows.append((float(t[0]), float(t[1]), float(t[4])))
    az = [(p, g) for th, p, g in rows if abs(th - 90.0) < 1e-6]
    fwd = next(g for p, g in az if abs(p) < 1e-6)
    b180 = next(g for p, g in az if abs(p - 180) < 1e-6)
    rear = [g for p, g in az if 90 < p < 270]
    return dict(gain=max(g for _, g in az), fwd=fwd, fb=fwd - b180,
                fbworst=fwd - max(rear))


def swr(r, x, z0=50.0):
    g = abs((complex(r, x) - z0) / (complex(r, x) + z0))
    return (1 + g) / (1 - g)


def evaluate(halflen, radius, fast=False):
    return run(deck(halflen, radius, "eval",
                    freqs=(420.0, 5, 5.0) if fast else (420.0, 21, 1.0),
                    full_pattern=not fast))


def report(res, label):
    print(f"\n=== {label}")
    print(f"{'MHz':>7} {'R':>7} {'X':>8} {'SWR':>6} {'Gain dBi':>9} {'F/B dB':>8} {'worst rear':>11}")
    for e in res:
        print(f"{e['f']:7.1f} {e['r']:7.1f} {e['x']:8.1f} {e['swr']:6.2f} "
              f"{e['gain']:9.2f} {e['fb']:8.1f} {e['fbworst']:11.1f}")
    print(f"  max SWR {max(e['swr'] for e in res):.3f} | gain {min(e['gain'] for e in res):.2f}"
          f"-{max(e['gain'] for e in res):.2f} dBi | F/B >= {min(e['fb'] for e in res):.1f} dB")


if __name__ == "__main__":
    report(evaluate(HALFLEN, 0.00635), "SC42014W as published, 12.7 mm elements")
