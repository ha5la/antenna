#!/usr/bin/env python3
"""Retune the G0KSC 7el LFA (12 mm loop, 10 mm parasitics) for 144-146 MHz.

Boom positions fixed. Goal: SWR <= 1.2 across the band, worst rear lobe >= 20 dB,
gain no worse than the published design.
"""
import numpy as np
from scipy.optimize import minimize
import gen, lfa

FREQS = (144.0, 5, 0.5)
LIMIT = 0.010
SWR_MAX, FB_MIN, GAIN_AIM = 1.20, 20.0, 12.95


def lengths(x):
    h = list(x[:1]) + [x[1], x[1]] + list(x[2:])
    return h


def cost(x):
    c = 0.0
    for e in gen.run(lfa.deck(lengths(x), loop_r=0.006, end_r=0.006,
                              freqs=FREQS, full_pattern=False)):
        c += (max(0.0, e["swr"] - SWR_MAX) / 0.03) ** 2
        c += (max(0.0, FB_MIN - e["fbworst"]) / 1.0) ** 2
        c += (max(0.0, GAIN_AIM - e["gain"]) / 0.10) ** 2
    return c


if __name__ == "__main__":
    h = lfa.HALFLEN
    x0 = np.array([h[0], .429] + h[3:])
    print("start", cost(x0), flush=True)
    res = minimize(cost, x0, method="Powell",
                   bounds=[(v - LIMIT, v + LIMIT) for v in x0],
                   options=dict(xtol=2e-5, ftol=1e-3, maxfev=3000))
    x = np.round(res.x * 2000) / 2000
    print("final", res.fun, "nfev", res.nfev, "| rounded:", cost(x), flush=True)
    names = ["Ref", "Loop"] + lfa.NAMES[3:]
    pub = [h[0], h[1]] + h[3:]
    for n, a, b in zip(names, pub, x):
        print(f"{n:>4} {1000*a:7.1f} -> {1000*b:7.1f} mm half  ({1000*(b-a):+.1f})", flush=True)
    np.save("lfa_tuned.npy", x)
    gen.report(gen.run(lfa.deck(lengths(x), loop_r=0.006, end_r=0.006,
                                freqs=(143.8, 13, 0.2))), "retuned, 143.8-146.2")
