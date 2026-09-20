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
