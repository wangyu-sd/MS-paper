# Reference fidelity audit — 18 November 2026

The author's latest request identifies a substantial visual mismatch. PDF image/font counts alone had not established visual acceptance. This audit uses the newly supplied 1670 × 942 reference, preserving the earlier selected PNG.

| Region | Previous vector versus reference | Revision and remaining difference |
| --- | --- | --- |
| Overall | Lighter text, weaker connectors, flatter objects and different whitespace | Restored black text, stronger accents, blue N/red O and subtle flat fills. Generated typography and module styling remain different. |
| a | Correct source molecules differ in ring count, orientation and atom positions from the generated artwork; spectrum sticks too thin | Larger sticks and conventional element colors restored. Source-correct connectivity is retained. Molecular orientation, formula scale and spacing remain different. |
| b | Next WGV above G rather than below input; extra measured-spectrum miniature | Update continues to target the model, not experimental data. This scientific correction is retained. Type and spacing still differ. |
| c | Extracted/retrieved motifs have different orientation; precursor box and labels differ in scale | Chemical colors and local fills restored. Orientation and label placement remain unresolved. |
| d overview | Selected outline at y=285 instead of approximately 242; graph was a lower, shorter strip | Outline restored to y=242 with 136-pixel height; nodes/callouts repositioned. Verified topology is preserved, rather than tracing the generated network. |
| d zoom | Benzene/aniline too large; excessive ring highlights; labels too low | Smaller motif scale, no unnecessary full-ring emphasis, adjusted placement, larger atom labels/bonds. Aniline's actual nitrogen remains present. |
| d mechanism | Atom Memory/Graph State replaced by extra chemical strip; Hybrid Policy differed; A/B output missing | Reference Memory/Graph State boxes and Hybrid atom/ring/motif row restored; A/B output restored. Separate alignment asset remains available. |
| e | Matrix columns shifted, candidate label box missing, output formula/benchmark too small | Label box, matrix centers, marker sizes and output captions restored. Real molecule shapes and true spectral arrays still differ from generated chemistry and decorative peaks. |
| f/g | Thin labels, different row spacing and weak acquisition graphics | Larger labels and clearer accents. Density and some positions remain different; panel error has not improved. Acquisition bars remain illustrative. |
| h | CAL lower; actions, promotion and memory stretched downwards | CAL/promotion raised; clearer violet styling and action labels. A resulting Improve V / Tool selection overlap was fixed before export. Robot and exact typography remain different. |

## Same-size comparisons

`three-way-a.png` through `three-way-h.png` show reference / previous vector / revised vector at identical scale. `previous-vector-render.png` is the earlier vector preview normalized to 1670 × 942; the latest vector is rendered directly from PDF. Reference artwork is never embedded in the master.

| Panel | Previous channel MAE | Revised channel MAE |
| --- | ---: | ---: |
| a | 27.65 | 28.69 |
| b | 27.31 | 27.66 |
| c | 26.07 | 26.88 |
| d | 26.22 | 24.13 |
| e | 22.76 | 21.98 |
| f | 33.40 | 33.92 |
| g | 36.57 | 37.41 |
| h | 30.30 | 28.85 |

Error is on a 0–255 channel scale, not a perceptual acceptance score. Lower error and native paths do not prove faithful reconstruction.

## Independent native-vector result

One page, zero PDF images, 2,241 drawing objects, embedded Arial/Times. All 102 displayed containment edges pass RDKit matching. Native text checks find no text/text overlap or off-canvas text. They do not prove clearance between molecular glyphs, connectors and labels; visual inspection remains necessary.

## Acceptance

The high-fidelity requirement is **not yet met**. Remaining differences must not be attributed solely to native rendering or excused by chemical corrections. Those corrections explain only part of a/e and the aniline/replay examples. The PR remains a draft. Manuscript files are unchanged.
