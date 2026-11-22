# ORBIT-MS Figure 1 native vector validation

## Current delivered revision

The editable [SVG](orbit_ms_nmi_figure1_vector.svg), native [PDF](orbit_ms_nmi_figure1_vector.pdf), and [3340 × 1884 preview](orbit_ms_nmi_figure1_vector_preview.png) implement the reference-layout corrections. No manuscript files or selected reference PNGs are changed.

The reference is `orbit_ms_nmi_figure1_sources/revision_reference.png`, SHA-256 `b3b7b474981ba4284cf0a35a4c0ba7d27dd31aca42b2450af2017d31ac3da4f1`. The earlier `selected_reference.png` is also retained unchanged. Both are QA inputs only; neither is embedded in the master.

## Executed reconstruction changes

- b: aligned all inference modules at the reference height, restored Next WGV below the left input region, retained its update into G, and removed the extra spectrum thumbnail above V. W still receives candidate structures only.
- c: redrew the same source SMILES at final drawing size and in the reference orientation, corrected the extracted/retrieved motif scale, enlarged mining labels, and retained the true ion lookup key and 427/107 source-group counts. The ion is labeled as a mass/composition lookup, rather than presenting C8H10N+ as the precursor's formula.
- d: fitted the recorded graph to the reference overview bounds, preserved the selected six identities, redrew local motifs with consistent atom-label size, fitted captions inside the chemical-neighborhood column, retained Memory/Graph State boxes and A/B output, and cleared the backbone-to-policy arrow from the Hybrid label.
- e: increased fragment-evidence labels and the measurement heading; cleared the output molecules from the formula row. Correct source candidates and actual spectrum values are retained.
- f: moved the source/operation rows to the reference positions and restored modality-specific measured/simulated spectrum colors. Structure-only data retain distinct motif-mining and Sleep routes.
- g: restored the compact header, matrix spacing, selected-pair positions and task-specific update ports. The heatmap is an illustrative acquisition diagram, not measured sample weights.
- h: enlarged intervention/evaluation labels and routed the action-selection fork outside the Hypothesis text. W remains frozen; CAL remains an evaluation source, not training labels.
- Ordinary text uses embedded Arial; notation uses embedded Times New Roman, with proper formula subscripts/superscripts. Ordinary labels remain editable text rather than bitmap glyphs or stroked Type 3 substitutes.

## Native vector checks

- One page: 180 × 101.53294 mm, exactly the reference aspect ratio.
- **0 embedded PDF images**; no SVG image or foreignObject elements.
- **2,315 PDF drawing objects**, 2,676 extracted text characters, 42 embedded subset-font records.
- Independently editable panel groups, chemical SVGs, 91 graph-node groups, containment paths, spectrum sticks, model boxes, acquisition cells and agent paths.
- Native text: no page overflow and no text/text overlaps. Connector centerlines were additionally sampled against native label bounds; no label crossings remain.
- All 102 displayed containment edges pass RDKit substructure matching. All ten newly oriented/sized motif SVGs retain the exact canonical SMILES of their recorded source.
- `pdfinfo`, `pdfimages -list`, `pdffonts`, PyMuPDF object checks, text bounds and connector checks are recorded in [verification](orbit_ms_nmi_figure1_sources/verification).

## Visual verification

The PDF was rendered at 1670 × 942 and 3340 × 1884. The [same-size render](orbit_ms_nmi_figure1_sources/verification/render-reference-size.png), [overlay](orbit_ms_nmi_figure1_sources/verification/overlay.png), [difference](orbit_ms_nmi_figure1_sources/verification/difference-x3.png), all eight panel comparisons and a [180 mm review](orbit_ms_nmi_figure1_sources/verification/review-180mm-100dpi.png) are included.

The three-way sheets show reference / preceding iteration / current revision. `previous-iteration-render.png` preserves the revision at commit 3be4501 before this execution round; the still earlier `previous-vector-render.png` is preserved separately.

| Panel | Preceding iteration MAE | Current MAE |
| --- | ---: | ---: |
| a | 28.29 | 29.40 |
| b | 27.69 | 24.60 |
| c | 26.74 | 27.19 |
| d | 24.02 | 24.43 |
| e | 21.83 | 22.22 |
| f | 34.18 | 27.38 |
| g | 37.25 | 36.75 |
| h | 28.91 | 29.81 |

The full-image channel MAE is 26.48/255, and 93.47% of pixels differ at any nonzero threshold. Those raw values include background/antialiasing differences and are not an acceptance score. This is not a claim of pixel identity or author approval.

## Scientific preservation and remaining source boundaries

A/e candidates are real archived structures with formula C28H36N4O4 and distinct connectivity. Their correct connectivity and associated W evidence are retained instead of copying malformed generated molecules. The local aniline retains its nitrogen, and the replay retains the actual source states. The reference's decorative dense spectra are replaced by the actual available peak arrays, not invented peaks.

The overview is a reproducible source-based containment display sample, not a recovered full production graph. The original beam parent chain is unavailable; the example remains labeled reference-conditioned replay. Complete sample-specific acquisition weights are unavailable; acquisition graphics remain qualitative. These limits are preserved in the [source inventory](orbit_ms_nmi_figure1_sources/README.md).

The 180 mm render retains the dense approved composition. Body text spans approximately 3.6–5.5 pt depending on location, with smaller notation; vector sharpness does not establish print legibility. Author visual review remains necessary. The PR stays a draft rather than asserting final submission acceptance.
