# Build sheet — G0KSC 7-el 2 m LFA, 12 mm loop, retuned for 144–146

G0KSC's "7el 144MHz Low Noise LFA EU", modified:

- loop in **12 mm** tube instead of 13 mm, end pieces also 12 mm, joined to the long sides
  by sliding 10 mm sleeves
- parasitics **10 mm**, as published
- parasitic lengths and loop retuned so one antenna covers **144–146** (CW, SSB and FM);
  the published design is optimised for 144–145
- boom **20 × 20 mm** aluminium, elements on 3D-printed Nylon 12 clamps, **3 mm clear** of
  the boom

Model: `lfa.py`, optimiser: `lfa_tune.py`.

## Cut list

Full element lengths, **including +2.2 mm boom correction** (DL6WU, halved for elements
standing a few mm off the boom; see the README). Positions are measured **from the
reflector**.

| Element | Boom pos | Full length | Published (no correction) |
|:--|---:|---:|---:|
| Ref | 0 | 1038 | 1040 |
| DE1 (loop, fed) | 88 | loop, see below | 870 |
| DE2 (loop) | 261 | loop, see below | 870 |
| D1 | 399 | 955 | 952 |
| D2 | 809 | 922 | 922 |
| D3 | 1471 | 899 | 898 |
| D4 | 2200 | 873 | 876 |
| D5 | 2894 | 873 | 868 |

All mm. Boom: span is 2894, so allow ~2.95–3.0 m for clamp material beyond each end.

## Loop — set it on the analyser, don't trust a cut length

G0KSC's loop dimension is measured **outer edge to outer edge** with the end pieces
inserted. The end pieces slide; the published dimension is a starting point, and the
final setting is by SWR.

In the model, the loop's absolute length is the least reliable number. How the corners are
represented, sharp or chamfered, at 0–40 mm bend radius, swings feed reactance by 10–30 Ω.
The sharp-corner model sits ~5 Ω more inductive than G0KSC's own EZNEC plot
(50.4 − j4.3 Ω at 144.0). So the cut length can't be predicted to better than ~10 mm, but
the loop is easy to adjust.

1. Cut the long sides so that with the end pieces pushed fully home, edge to edge is
   **≤ 850 mm**. Slide the ends out to set anything up to ~880 mm (published: 870).
2. DE1 is split at the centre for the feed; DE2 is continuous.
3. Adjust **both ends equally**. Shorter loop → SWR minimum moves up.
4. Target: **SWR minimum at ~145.2 MHz**, not at 144. The modelled curve then reads
   1.18 at 144.0, 1.01 at 145.2 and 1.23 at 146.0.
5. Fix the ends with a small self-tapper or clamp.

Tune with the antenna in clear space (e.g. pointing up, a few metres off the ground),
measured at the feedpoint through a short jumper, with a ferrite choke on the coax at the
feedpoint. Not through the long run to the shack: its loss hides the mismatch.

## Expected performance (modelled, free space)

| | worst SWR 144–146 | Gain | Worst rear |
|:--|--:|:--|--:|
| Published, 13 mm loop | 1.66 | 12.86–12.95 dBi | 20.2 dB |
| Published lengths, 12 mm loop | 1.71 | 12.82–12.92 | 20.1 |
| Published parasitics, loop set best | 1.35 | 12.84–12.95 | 21 |
| **This build** | **1.23** | 12.80–12.93 | 19.5 |

The 12 mm loop alone costs nothing: within 0.05 of SWR and 0.03 dB of gain, the same
result as the SC42014W 12 mm retune. Covering 2 MHz is what needs the retune: above
145.5 the feed resistance rises however the loop is set, and that is fixed only by the
parasitics. The retune costs ~0.04 dB of gain and ~1.5 dB of F/B at 144.0.

## Modelling notes

- NEC-2 (`nec2c`) **without** the extended thin-wire kernel. With `EK`, equal-radius wires
  meeting at the loop corners give an average gain of ~2.1 and an impossible 16 dBi.
  Without it, average gain is 1.01–1.02. Check average gain on any change to the loop.
- 58 mm segments (> 8× tube radius, needed without `EK`), matched at the loop corners.
  Gain is converged to 0.04 dB from 29 to 70 mm segments; reactance moves ±2 Ω.
- Free space, no boom; the boom correction above is applied by hand.
- Optimiser bounds ±10 mm per half; no element moved more than 3.5 mm per half.
