#!/usr/bin/env python3
"""G0KSC 7-element 2 m LFA (European version): published design and a 12 mm loop."""
import gen

# Boom positions and half-lengths, metres. DE1 and DE2 are the long sides of the loop.
SPACING = [0.0, .088, .261, .399, .809, 1.471, 2.2, 2.894]
HALFLEN = [.52, .435, .435, .476, .461, .449, .438, .434]
NAMES = ["Ref", "DE1", "DE2", "D1", "D2", "D3", "D4", "D5"]
RETUNED = [.518, .4315, .4315, .4765, .460, .4485, .4355, .4355]  # lfa_tune.py, 144-146
PARASITIC_R = 0.005

SEG = 0.058  # matched at loop corners; >8x radius, since EK is unusable here


def nseg(length, seg, odd=False):
    n = max(1, round(length / seg))
    return n + (1 - n % 2) if odd else n


def deck(halflen=HALFLEN, loop_r=0.0065, end_r=0.005, spacing=SPACING,
         freqs=(144.0, 11, 0.2), title="G0KSC 7el LFA", seg=SEG, full_pattern=True):
    lines = ["CM " + title,
             f"CM loop {2000*loop_r:.1f} mm, ends {2000*end_r:.1f} mm, sharp corners on the "
             f"centreline, parasitics {2000*PARASITIC_R:.0f} mm; free space, no boom",
             "CE"]
    tag = 0

    def gw(a, b, r, n):
        nonlocal tag
        tag += 1
        lines.append(f"GW {tag:3d} {n:3d} {a[0]: .5f} {a[1]: .5f} 0 {b[0]: .5f} {b[1]: .5f} 0 {r:.6f}")

    for i, (x, hl) in enumerate(zip(spacing, halflen)):
        if i not in (1, 2):
            gw((x, -hl), (x, hl), PARASITIC_R, nseg(2 * hl, seg, odd=True))
    x1, x2, y = spacing[1], spacing[2], halflen[1]
    pts = [(x1, -y), (x1, y), (x2, y), (x2, -y)]
    for k, (a, b) in enumerate(zip(pts, pts[1:] + pts[:1])):
        n = nseg(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5, seg, odd=(k == 0))
        gw(a, b, loop_r if k in (0, 2) else end_r, n)
        if k == 0:
            fed, n_fed = tag, n
    f0, nf, df = freqs
    lines += ["GE 0", f"EX 0 {fed} {n_fed // 2 + 1} 0 1.0 0.0",
              f"FR 0 {nf} 0 0 {f0:.3f} {df:.3f}",
              *(["RP 0   1 361 1000 90.0  0.0 0.0 1.0",
                 "RP 0 361   1 1000  0.0  0.0 1.0 0.0"] if full_pattern else
                ["RP 0   1  37 1000 90.0  0.0 0.0 10.0"]), "EN"]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    band = (144.0, 11, 0.2)
    gen.report(gen.run(deck(freqs=band)), "published: 13 mm loop, 10 mm ends + parasitics")
    gen.report(gen.run(deck(freqs=band, loop_r=0.006, end_r=0.006)), "12 mm loop, published lengths")
    gen.report(gen.run(deck(RETUNED, loop_r=0.006, end_r=0.006, freqs=band)),
               "12 mm loop, retuned for 144-146")
