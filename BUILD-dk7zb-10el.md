# Build sheet — DK7ZB 10-el 28 Ω, 70 cm, 2.0 m boom

Boom **20 × 20 mm** aluminium. Elements on **polyamide clamps, 2–3 mm clear above the
boom**, 3 mm stainless screw. At that clearance the boom still loads the elements, so the
cut list below is DK7ZB's table **plus the +5.5 mm correction for a 20 mm boom**.

Whether the screw bridges element to boom makes no measurable difference — the clearance
is what matters. Mount the element as high in the clamp as the clamp allows.

Built and measured this way the radiator sits at 27.4 - 1.4j at 433 MHz against a modelled
27.4 - 1.8j. See *Measured* in the README.

## Cut list — includes the +5.5 mm boom correction

Radiator is **10 mm** in both columns. Pick one parasitic diameter.

| Element | Boom pos | 8 mm parasitics | 10 mm parasitics |
|:--|---:|---:|---:|
| Ref | 0 | 335.5 | 332.5 |
| Rad | 140 | 319.5 *(10 mm)* | 320.5 *(10 mm)* |
| D1 | 235 | 307.5 | 305.5 |
| D2 | 425 | 296.5 | 292.5 |
| D3 | 650 | 290.5 | 286.5 |
| D4 | 920 | 282.5 | 277.5 |
| D5 | 1205 | 279.5 | 274.5 |
| D6 | 1495 | 279.5 | 274.5 |
| D7 | 1780 | 284.5 | 279.5 |
| D8 | 1995 | 279.5 | 274.5 |

All mm. Positions are measured **from the reflector**, not from the end of the boom.
±1 mm on a length is ±1 MHz, so the half-millimetres are not worth chasing — but apply
the same rounding to all ten.

## Order and cut plan

Drawn tube comes in 4 m lengths; sin-us will cut. Allowing 2 mm of kerf per cut:

**8 mm build** — nothing over 2 m:

| Order | Cut into |
|:--|:--|
| 8 × 1, 2 m | 335.5 + 307.5 + 296.5 + 290.5 + 284.5 + 282.5 (1809 mm used) |
| 8 × 1, 1 m | 279.5 + 279.5 + 279.5 (845 mm used) |
| 10 × 1, 0.5 m | radiator 319.5 mm |

**All-10 mm build:**

| Order | Cut into |
|:--|:--|
| 10 × 1, 2 m | 332.5 + 320.5 + 305.5 + 292.5 + 286.5 + 279.5 (1829 mm used) |
| 10 × 1, 1.2 m | 277.5 + 274.5 + 274.5 + 274.5 (1109 mm used) |

A single 3 m length holds all ten with 62 mm to spare, which is not enough room for a
mistake.

**Boom:** 20 × 20 square, about 2.05–2.10 m. DK7ZB specifies a 2.00 m boom and the last
director sits at 1995 mm, so the element span itself is 1995 — but the reflector and D8
clamps need material under them, so allow 30–50 mm of boom beyond each end element.
The boom is the only item over 2 m.

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

The cut list already carries the right-hand 20 mm figure. For anything else, start from
DK7ZB's published lengths (cut list minus 5.5 mm) and add instead:

| Boom | Through boom, metal contact | Insulated through boom, or standing within a few mm of it |
|---:|---:|---:|
| 15 mm | +7 mm | +3.5 mm |
| 20 mm | +11 mm | +5.5 mm |

Uncorrected on a metal boom, the antenna resonates **high** — +11 mm missing on a 280 mm
director is 3.9%, about 17 MHz at 435. The same error on 2 m is only ~4 mm / 0.4%, which
is why it hides on 2 m and wrecks 70 cm.

Lengthening all ten elements together moves the array at **1.025 MHz per mm** of full
length. The radiator alone moves it at 0.43 MHz/mm, so a length error found on SWR cannot
be corrected on the radiator — the whole set has to move.
