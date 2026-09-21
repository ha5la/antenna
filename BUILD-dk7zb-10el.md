# Build sheet — DK7ZB 10-el 28 Ω, 70 cm, 2.0 m boom

Boom **20 × 20 mm** aluminium. Elements on **polyamide clamps, 2–3 mm clear above the
boom**, 3 mm stainless screw. Built this way: **no boom correction, cut to the table.**

The screw must not make metal contact between element and boom.

## Cut list

Radiator is **10 mm** in both columns. Pick one parasitic diameter.

| Element | Boom pos | 8 mm parasitics | 10 mm parasitics |
|:--|---:|---:|---:|
| Ref | 0 | 330 | 327 |
| Rad | 140 | 314 *(10 mm)* | 315 *(10 mm)* |
| D1 | 235 | 302 | 300 |
| D2 | 425 | 291 | 287 |
| D3 | 650 | 285 | 281 |
| D4 | 920 | 277 | 272 |
| D5 | 1205 | 274 | 269 |
| D6 | 1495 | 274 | 269 |
| D7 | 1780 | 279 | 274 |
| D8 | 1995 | 274 | 269 |

All mm. Totals: 8 mm column needs 2.596 m of 8 × 1 plus 314 mm of 10 × 1.
10 mm column needs 2.863 m of 10 × 1 — one 4 m stick does the lot.

Make the boom ~2.1 m so the Ref and D8 are not right at the tube ends.

## DK7ZB match

Two 75 Ω coax quarter-wave lines in parallel (37.5 Ω), 37.5² / 28 = 50.2 Ω.
Both braids joined at each end, both inners joined at each end, run exactly parallel.
50 Ω end to a socket grounded to the boom.

| Cable | V | Length |
|:--|---:|---:|
| Full-PE (RG-59) | 0.67 | 115 mm |
| Foam-PE, SAT cable | 0.82 | 141 mm |
| PTFE (RG-179) | 0.70 | 120 mm |

Cheap TV coax is often not 75 Ω — DK7ZB measured 68, 70 and 80 Ω examples.

## Expected performance (modelled, 8 mm parasitics)

| MHz | SWR 50 Ω | Gain | Worst rear |
|---:|---:|---:|---:|
| 430 | 1.25 | 15.11 dBi | 26.2 dB |
| 432 | 1.11 | 15.24 | 28.1 |
| 433 | 1.03 | 15.30 | 28.7 |
| 435 | 1.13 | 15.39 | 28.8 |

## If you use a different mounting

Add to the **full** element length:

| Boom | Through boom, metal contact | Insulated through boom, or bonded on top |
|---:|---:|---:|
| 15 mm | +7 mm | +3.5 mm |
| 20 mm | +11 mm | +5.5 mm |

Uncorrected on a metal boom, the antenna resonates **high** — +11 mm missing on a 280 mm
director is 3.9%, about 17 MHz at 435. The same error on 2 m is only ~4 mm / 0.4%, which
is why it hides on 2 m and wrecks 70 cm.
