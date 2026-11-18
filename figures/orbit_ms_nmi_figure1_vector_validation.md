# ORBIT-MS Figure 1 reference-based revision

The revision uses the vector artwork at PR #17 commit `404af30` and the selected author reference as its layout baseline. The [same-width comparison](orbit_ms_nmi_figure1_reference_comparison.png) shows the reference, the baseline vector and the revised vector. Their aspect ratios and panel boundaries were held fixed for comparison.

| Area | Targeted change |
| --- | --- |
| a, b | Retained the benchmark spectrum, candidate drawings and WGV overview as they appear in the baseline. |
| c, d | Clarified the two motif labels and routed local containment links away from the chemical glyphs and retrieval box. |
| e | Routed both A/B candidates to the same W input. Added a compact key for the evidence markers. |
| f, g | Separated the pseudo-pair label from the plot, increased acquisition header type and opened a margin around the weighted sampling label. TRAIN composition is abbreviated C/N/O. |
| h | Enlarged the FIT, hypothesis and intervention labels. Made the memory output to the next hypothesis explicit. |

The PDF was reviewed at full page size, 180 mm width and as enlarged c–e and f–h crops. It is one 180 × 101.53 mm page with 2,320 drawing objects, 37 embedded font records and zero raster image objects. The source and geometry checks verified the 102 containment edges, true vector text, and no native text overflow, overlap or sampled connector/label crossings.

The chemical identities and actual spectrum arrays come from the existing manifest, so their appearance differs from the hand-rendered benchmark examples in the reference PNG. The lower strip remains compact, particularly the CAL table, and the visual comparison should be reviewed at its intended reading size. The [source inventory](orbit_ms_nmi_figure1_sources/README.md) records the scope of the archived graph, replay and acquisition illustrations.
