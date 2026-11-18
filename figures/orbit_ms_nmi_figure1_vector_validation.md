# ORBIT-MS Figure 1 editorial audit

The baseline was the vector PDF at `404af30`. It was rendered at full canvas width, at 180 mm with 100 and 200 dpi sampling, and as enlarged c–e and f–h crops. The [before/after preview](orbit_ms_nmi_figure1_before_after.png) shows both versions at equal width.

| Panel | Baseline observation | Editorial change |
| --- | --- | --- |
| a | Precursor metadata and candidate formulas crowded the experimental spectrum. | Use one spectrum and one shared formula to explain ambiguity. |
| b | Several box baselines and the model update line competed with the inference route. | Align the WGV chain; distinguish the measured-spectrum branch to V and reference c–e beneath it. |
| c | Every mining action occupied a box and the online ion lookup had little breathing room. | Separate offline mining and online retrieval with a rule; use the source molecule and two numbered motifs as anchors. |
| d | Large overview and a dense sequence of small boxes gave equal visual weight to every step. | Compact the 91-node overview, enlarge the six-motif neighborhood, and place atom correspondence above a single alignment block and the action replay. |
| e | Duplicate A/B drawings and an oversized gap separated the evidence from the output. | Keep one pair of large candidate drawings in e and align fragment masses, measurement, evidence matrix and hypothesis output on a vertical axis. |
| f | Repeated miniature molecules and spectra made the four source routes hard to distinguish. | Use consistent modality symbols and four evenly spaced source rows. |
| g | Dense headers, sampled-pair icons and three output boxes overwhelmed the acquisition matrix. | Use uniform bars, open margins and three typographic task ports. |
| h | Intervention boxes and the CAL, promotion and memory paths occupied the same space. | Separate decisions from evaluation. Route episodic feedback through the gutter and distinguish violet decision flow from teal model work. |

The 16:9 grid gives the middle row 49% of the available height and d about half of that row's width. The lower row takes 33% of the canvas. Panel titles share 22 design units (7.0 pt at 180 mm). Standard labels use 16–19 units (5.1–6.1 pt). Panel letters are larger. Chemical subscripts retain a smaller typographic size. The colors follow the specified neutral, slate, teal, copper and violet palette. Separators are lighter than inference and update arrows. The letter-size target follows the [NMI figure guide](https://www.nature.com/natmachintell/submission-guidelines/aip-and-formatting).

The first render confirmed the grid, whitespace and reading order. The detail pass rerouted the episode feedback around CAL, added the archived motif–atom correspondence, separated acquisition headers from the bars and aligned the evidence symbols. The final was checked as a [3200 × 1800 render](orbit_ms_nmi_figure1_vector_preview.png) and a [180 mm-width render](orbit_ms_nmi_figure1_sources/verification/review-180mm-150dpi.png), with close inspection of chemistry, arrows and formula typography.

Extracted English tokens fell from 334 to 257 (23% fewer). Examples of removed detail include duplicate candidate drawings in e, repeated model names, training-pair miniatures, one label per motif in the local neighborhood and inline protocol qualifications. The [source inventory](orbit_ms_nmi_figure1_sources/README.md) retains the motif identities, spectrum source, calibration roles and experimental scope for caption preparation.

The PDF is 180 × 101.25 mm and has zero image objects, 1,392 vector drawing objects and searchable embedded Arial and Times New Roman. SVG text, paths, graph nodes, spectra and chemical drawings remain independently editable. Automated checks found no text overlap, panel overflow or sampled connector centerlines crossing labels. The source checks validated 102 containment edges and the nine regenerated motif drawings. See [statistics.json](orbit_ms_nmi_figure1_sources/verification/statistics.json).

The most compact elements at 180 mm remain the chemical atom labels and formula indices. The containment overview intentionally shows an archived sample, and the g matrix is qualitative. The atom correspondence and attachment replay use separately documented source states. CAL is a paired evaluation, W is frozen during the controlled trial, and only a promoted system feeds the next generation. The caption and manuscript remain outside this change.
