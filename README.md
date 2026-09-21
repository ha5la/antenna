# SC42014W — G0KSC 14-element 70 cm OWA Yagi

NEC2 models of Justin Johnson G0KSC's SC42014W (14 elements, 1.843 m boom, 420–440 MHz,
direct 50 Ω feed), and a version retuned for 12 mm tubing available from sin-us.hu.

Open either `.nec` file in `xnec2c`, or run `nec2c -i<file> -o<file>.out`.

Note: SC42014W is an **OWA** (Optimised Wideband Array) with a straight dipole driven
element — not an LFA, which uses a rectangular loop feed.

## Files

| File | Elements | Notes |
|:--|:--|:--|
| `sc42014w_12.7mm.nec` | 12.7 mm (1/2 in) | G0KSC's published dimensions, unchanged |
| `sc42014w_12mm.nec`   | 12 mm            | retuned, same boom positions |
| `gen.py`              | — | deck generation + nec2c result parsing |
| `tune.py`             | — | the optimisation that produced the 12 mm lengths |

Both are free-space models. Elements are modelled in isolation: G0KSC states they sit high
enough above the boom on insulators that no boom correction is needed.

## Model validation

15 segments per element with the extended thin-wire kernel (`EK`); converged — 21 segments
changes gain by <0.01 dB. The published deck reproduces G0KSC's figures exactly:

| @430 MHz | G0KSC | model |
|:--|--:|--:|
| Forward gain | 14.62 dBi | 14.62 dBi |
| Front to back | 26.8 dB | 26.8 dB |

His F/B figure is the 180° value. The worst rear lobe is 23.0 dB down at 430 MHz and
18.3 dB at 420 MHz. His "SWR no more than 1.1" holds to 438 MHz; the model gives 1.16 at
440 MHz.

## Element diameter

sin-us.hu stocks no 12.7 mm and no 13 mm round tube. Nearest ODs are 12 mm and 14 mm, so
12 mm is the closest match. Available as drawn `12 × 1` (AlMgSi0.7, 4 m) or extruded
`12 × 1.5` (AlMgSi0.5 F22, 6 m); wall thickness is electrically irrelevant, choose on
stiffness. 28 element halves are needed.

**12 mm with the published lengths works as-is** — max SWR 1.11 (better than the original's
1.16), same 14.6 dBi, F/B within 0.2 dB. This matches G0KSC's own note that 13 mm needs no
change. The retune below is a refinement, not a fix.

## Cut lengths

Total element length; the design tables give halves. Boom positions are unchanged.

| Element | Boom pos | 12.7 mm | 12 mm retuned |
|:--------|---------:|--------:|--------------:|
| Ref     |      0   |  336.0  |  339.0 |
| DE      |    129   |  330.0  |  328.0 |
| D1      |    180   |  292.0  |  292.0 |
| D2      |    291   |  280.0  |  282.0 |
| D3      |    425   |  271.0  |  272.0 |
| D4      |    606   |  270.0  |  274.0 |
| D5      |    730   |  255.0  |  253.0 |
| D6      |    869   |  258.0  |  263.0 |
| D7      |   1018   |  236.0  |  241.0 |
| D8      |   1167   |  263.0  |  261.0 |
| D9      |   1393   |  271.0  |  272.0 |
| D10     |   1580   |  262.0  |  260.0 |
| D11     |   1686   |  264.0  |  265.0 |
| D12     |   1843   |  259.0  |  259.0 |

All in mm. No change exceeds 5 mm on the full element.

## Results over 420–440 MHz

| | 12.7 mm published | 12 mm published lengths | 12 mm retuned |
|:--|--:|--:|--:|
| max SWR | 1.16 | 1.11 | **1.09** |
| gain | 14.32–14.64 dBi | 14.24–14.65 | **14.36–14.68** |
| worst rear lobe | 18.3 dB | 17.9 | **19.4** |

The retune buys ~0.05 dB of SWR margin, +0.12 dB of gain at the band edges and +1.5 dB of
worst-case F/B. Marginal, but it costs nothing to cut to the new numbers.

Build tolerance is unchanged: over 40 randomised builds with ±0.5 mm per element half and
±1 mm per boom position, worst-case SWR stayed below 1.20 and gain within 0.05 dB for both
length sets. G0KSC's "minor errors will not have a big impact" holds.

---

# DK7ZB 10-element 28 Ω Yagi for 70 cm

`dk7zb_10el_70cm.nec` — 10 elements on a 2.0 m boom, designed for 432 MHz.
Source: <https://www.qsl.net/dk7zb/70cm/10.htm>

Modelled with the same method as the OWA (15 segments/element, `EK`, free space,
elements insulated above the boom). Converged; 21 segments changes nothing.

DK7ZB's claim of 13,1 dBd = 15.25 dBi is confirmed: the model gives 15.24 dBi at 432 MHz.

## Dimensions (10 mm elements)

| Element | Boom pos | Length |
|:--|---:|---:|
| Ref | 0 | 327 |
| Rad | 140 | 315 |
| D1 | 235 | 300 |
| D2 | 425 | 287 |
| D3 | 650 | 281 |
| D4 | 920 | 272 |
| D5 | 1205 | 269 |
| D6 | 1495 | 269 |
| D7 | 1780 | 274 |
| D8 | 1995 | 269 |

All in mm. Buildable straight from sin-us.hu drawn tube — no retune, unlike the OWA.

DK7ZB publishes three parasitic diameters; **the radiator is always 10 mm** in all of
them. All three model equivalently (15.2–15.4 dBi, SWR under 1.25 across 430–436), so
pick on what you can buy. His standard for this series is 8 mm parasitics with a 10 mm
radiator — that is `dk7zb_10el_70cm_8mm.nec`.

| Parasitics | SWR @433 | Gain @433 | F/B @433 |
|:--|---:|---:|---:|
| 10 mm | 1.10 | 15.29 dBi | 27.9 dB |
| 8 mm  | 1.03 | 15.30 | 28.7 |
| 6 mm  | 1.02 | 15.28 | 27.7 |

## Modelled performance

SWR is referenced to 50 Ω *through* the matching section; Z is the bare feedpoint.

| MHz | Z feedpoint | SWR 50 Ω | Gain dBi | worst rear dB |
|---:|:--|---:|---:|---:|
| 430 | 25.6-4.5j | 1.22 | 15.11 | 25.8 |
| 431 | 25.4-2.9j | 1.16 | 15.18 | 26.7 |
| 432 | 25.3-1.2j | 1.12 | 15.24 | 27.4 |
| 433 | 25.5+0.6j | 1.10 | 15.29 | 27.9 |
| 434 | 26.2+2.3j | 1.12 | 15.34 | 28.1 |
| 435 | 27.3+3.8j | 1.16 | 15.37 | 28.1 |
| 436 | 29.3+4.7j | 1.19 | 15.40 | 27.3 |
| 437 | 31.8+4.0j | 1.21 | 15.40 | 23.6 |
| 438 | 34.1+0.6j | 1.21 | 15.40 | 20.8 |
| 439 | 32.9-5.7j | 1.26 | 15.37 | 18.6 |
| 440 | 25.6-11.0j | 1.49 | 15.33 | 16.8 |

Excellent to about 437; above that the rear lobe climbs and the match degrades. Not a
repeater antenna.

The `.nec` file feeds the radiator directly, so xnec2c will show SWR against 50 Ω and
look wrong — **set the SWR reference impedance to 28 Ω** in xnec2c, or read the table above.

## The DK7ZB match

Two 75 Ω coax quarter-wave lines in parallel = 37.5 Ω, and 37.5² / 28 = 50.2 Ω.
Both braids joined at each end, both inner conductors joined at each end; the 50 Ω end
goes to a socket grounded to the boom. The two cables must run exactly parallel.

Quarter wave at 432 MHz:

| Coax velocity factor | Length |
|---:|---:|
| 0.66 (solid PE, RG-59) | 114.5 mm |
| 0.81 | 140.5 mm |
| 0.82 (foam SAT cable, DK7ZB's preference) | 142.3 mm |
| 0.85 | 147.5 mm |

Measure your cable's actual velocity factor rather than trusting the datasheet, and trim
with an analyser.

## Element mounting and boom correction

DK7ZB's published lengths assume **polyamide clamps (Konni type) holding the element
2–3 mm clear above the boom**, fastened with a 3 mm stainless screw. Built that way they
need **no correction** — cut to the table.

Any other mounting needs the DL6WU correction, which DK7ZB tabulates as
`C = (12.5975 - 114.5 B) B²` per element half, C and boom diameter B in wavelengths.
Added to the full element length:

| Boom | Elements through boom, metal contact | Insulated through boom, or bonded directly on top |
|---:|---:|---:|
| 10 mm | +3 mm | +1.5 mm |
| 15 mm | +7 mm | +3.5 mm |
| 20 mm | +11 mm | +5.5 mm |

DK7ZB does not say whether these are round or square booms, and his own antennas use
square 15×15 or 20×20. SM5BSZ finds a square boom behaves like a round one ~18% larger,
so if the table is for round booms a 20×20 square would want somewhat more than +11 mm.
Another reason to use the clamps and sidestep the question.

The correction is *added* — a metal boom makes an element behave electrically short, so
an uncorrected build resonates high.

At 70 cm this is not a detail: +11 mm on a 280 mm director is 3.9%, about 17 MHz at
435 MHz. The same boom on 2 m costs only ~4 mm, or 0.4% — which is why a mounting error
that is invisible on 2 m ruins a 70 cm antenna.

The screw must not form a metal path from element to boom. In the clamp method it
fastens the element into the plastic body only.

## The DK7ZB match — his own figures

Quarter-wave lengths for 432 MHz, from DK7ZB:

| Cable | V | Length |
|:--|---:|---:|
| Full-PE (RG-59) | 0.67 | 115 mm |
| Foam-PE (SAT cable) | 0.82 | 141 mm |
| PTFE (RG-179) | 0.70 | 120 mm |

He warns that cheap TV coax is often not 75 Ω — measured examples came out at 68, 70 and
80 Ω. Use decent cable with good screening.

## Versus the SC42014W

| | DK7ZB 10-el | SC42014W OWA |
|:--|:--|:--|
| Boom | 2.00 m | 1.84 m |
| Gain @433 | 15.29 dBi | 14.68 dBi |
| Worst rear @433 | 27.9 dB | 23.9 dB |
| Feed | 28 Ω + quarter-wave match | direct 50 Ω |
| Usable | ~430–437 | 420–440 |
| Tubing from sin-us | 10 × 1, as published | 12 × 1, retuned |

For 432–434 (CW/SSB plus FM simplex) the DK7ZB is better by 0.6 dB of gain and 4 dB of
F/B. The OWA wins if you also want the 438–440 repeaters, and it needs no matching section.
