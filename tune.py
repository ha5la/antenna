#!/usr/bin/env python3
"""Optimise SC42014W element lengths for 12 mm tubing on the unchanged 1.843 m boom.

Goal is performance, not a copy of the 12.7 mm response: SWR <= 1.05 and worst rear
lobe >= 20 dB down across 420-440 MHz, with gain pushed as high as the boom allows.
"""
import numpy as np
from scipy.optimize import minimize
import gen

FREQS = (420.0, 6, 4.0)
RADIUS = 0.006
LIMIT = 0.003
SWR_MAX, FB_MIN, GAIN_AIM = 1.05, 20.0, 14.70


def cost(halflen):
    c = 0.0
    for e in gen.run(gen.deck(halflen, RADIUS, "opt", freqs=FREQS, full_pattern=False)):
        c += (max(0.0, e["swr"] - SWR_MAX) / 0.03) ** 2
        c += (max(0.0, FB_MIN - e["fbworst"]) / 1.0) ** 2
        c += ((GAIN_AIM - e["gain"]) / 0.10) ** 2
    return c


if __name__ == "__main__":
    x0 = np.array(gen.HALFLEN)
    print("start", cost(x0), flush=True)
    res = minimize(cost, x0, method="Powell",
                   bounds=[(h - LIMIT, h + LIMIT) for h in gen.HALFLEN],
                   options=dict(xtol=2e-5, ftol=1e-3, maxfev=20000))
    rounded = np.round(res.x * 2000) / 2000
    print("final", res.fun, "nfev", res.nfev, "| rounded to 0.5mm:", cost(rounded), flush=True)
    for n, a, b in zip(gen.NAMES, gen.HALFLEN, rounded):
        print(f"{n:>4} {1000*a:8.2f} -> {1000*b:8.2f} mm  ({1000*(b-a):+.2f})", flush=True)
    np.save("tuned12_perf.npy", rounded)
