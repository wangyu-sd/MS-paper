# ORBIT-MS Figure 1 native vector sources

The master is [orbit_ms_nmi_figure1_vector.svg](../orbit_ms_nmi_figure1_vector.svg). The chemical-atlas layout uses editable text, RDKit paths, native spectrum sticks, graph nodes and connector paths. The [before/after preview](../orbit_ms_nmi_figure1_atlas_before_after.png) uses the prior native PDF as the baseline. `selected_reference.png` preserves the earlier selection; `revision_reference.png` preserves the latest author comparison. Both are QA assets only. The current editorial design and caption scope are documented in the [visual audit](../orbit_ms_nmi_figure1_vector_validation.md). The SVG and exported PDF contain no image objects.

## Source inventory

| Panel | Reconstructed objects | Scientific source |
| --- | --- | --- |
| a | Measured spectrum and two same-formula candidates | MassSpecGym 0002114, original query and candidate ranking in `data/case_manifest.json`; candidate depictions appear in e |
| b | G/W/V overview and c/d/e reference labels | Manual SVG text and paths arranged against the reference; PR95 architecture and PR96 model promotion |
| c | Source parent, connected motif and ion lookup | Reused archived `library_parent.svg`; final-size, reference-oriented motifs are regenerated from the identical case-manifest SMILES. Ion key, source groups and mass constraints remain source-derived |
| d | Global sample and six-node zoom | Canonical structures, extracted records and containment matches in `data/motif-topology.json`; final node coordinates in `data/reference_graph_layout.json`; final chemical drawing specifications in `data/reference_drawing_specs.json` |
| d | Atom alignment | Explicit source atom correspondence in `case_manifest.json`; independently editable `atom-level-alignment.svg`, included in d at the recorded motif and partial-graph atom correspondence |
| d | One motif attachment | Reused `growth_2.svg` and `growth_3.svg`, reference-conditioned deterministic action replay. The after state adds nine heavy atoms to the before state |
| e | Structure-conditioned W and V evidence | Archived same-case predictions and scores; full emitted objects/posteriors in `data/frozen_wv_case.json.gz` |
| f | Paired and single-modality data | RDKit depictions and original centroid pairs for the archived Sleep, Wake and Hindsight records in the case manifest. The measured paired TRAIN example is MassSpecGymID0000570 in `data/paired_training_example.json`. |
| g | Acquisition signal and update mechanism | Native qualitative schematic of entropy/scarcity/source-priority weighting in `train_pr93_peak_ladder_hybrid.py`; the plotted bars are illustrative, not archived sample-specific acquisition measurements |
| h | Controlled experiment, promotion and reflection | Native text/path objects implementing PR96's FIT → hypothesis → intervention → matched CAL → promotion/retention and episode-memory protocol. No autonomous performance measurements are plotted |

The archived case manifest retains original private archive paths, source-line identities and hashes. Those records are provenance; access to the private archive is unnecessary for rebuilding the committed artwork.

## Scientific boundaries

- The containment sample has 91 plotted nodes and 102 RDKit-verified edges, including the six local nodes. These are display-sample counts, not resource-wide statistics. Twenty-nine canonical structures occur in the recovered indexed-motif records. The remaining nodes are verified connected subgraphs of the committed case's source molecules. Edges were computed for this illustration. A persisted production-wide containment graph was unavailable.
- The local IDs are 1 phenylalanine, 2 phenethylamine, 3 N-ethylaniline, 4 ethylbenzene, 5 aniline and 6 benzene. An edge means atom/bond subgraph containment with implicit hydrogen valence completed by RDKit. It does not assert a fragmentation reaction.
- The 427 and 107 support labels count source groups in the recovered mining shards. The neutral motif skeletons have formula C8H11N. C8H10N+ labels the ion-index key, with theoretical m/z 120.0807757401.
- The source sketch is reference-conditioned replay of an archived candidate. An original beam parent chain is unavailable. The reconstruction preserves this limitation explicitly in the replay caption.
- W/V evidence is source-derived. No nonzero support is assigned to the unexplained 90.9773 peak. Candidate A's 120.0893 support is weak. This peak alone does not explain the candidates' archived rank difference.
- Complete TRAIN frequency profiles and the original per-sample acquisition weights were unavailable. Panel g presents the implemented selection mechanism as a qualitative diagram. Updating knowledge, G and V are distinct task routes.
- The PR96 controller holds W fixed and uses matched calibration cases for promotion. Episode reflection changes the decision context, without training the Agent LLM.

## Rebuild

Use Python 3 with the packages in `requirements.txt`, Playwright with Chromium, Poppler and locally licensed Arial/Times New Roman fonts. The fonts are used from the operating system and are not redistributed.

From the repository root:

```sh
python scripts/draw_orbit_ms_nmi_figure1_vector.py
node scripts/export_orbit_ms_nmi_figure1_vector.cjs
pdftoppm -png -singlefile -scale-to-x 3340 -scale-to-y 1884 \
  figures/orbit_ms_nmi_figure1_vector.pdf \
  figures/orbit_ms_nmi_figure1_vector_preview
python scripts/verify_orbit_ms_nmi_figure1_vector.py
```

For a system Chromium, set `CHROME_PATH`. If Node cannot find Playwright, set `NODE_PATH` to the installed module directory. Set `PYTHON` if the exporter should use a specific Python executable. The validator accepts `--poppler-dir` and `--reference`; the latter defaults to `revision_reference.png`.

Standalone spectrum SVGs are regenerated by the native plotting function in the assembly script. The source m/z arrays are committed in the case manifest and the paired TRAIN record. Sticks use linear m/z and base-peak-normalized intensity. Orange identifies experimental spectra; teal identifies W-simulated spectra. The inset plots intentionally omit numeric ticks and retain axes. Their local m/z ranges are independent across rows. The renderer recreates the local motif SVGs with RDKit at their final placement size and records the exact source canonical SMILES, canvas size, rotation and font size. Archived parent, candidate and replay SVGs are reused. It does not perform OCR, image tracing, spectrum extraction from pixels, or neural image generation.

## Editing

The master contains named `panel-a` through `panel-h` groups, individually identified graph nodes/edges, separate spectral paths, editable Arial/Times text and independent molecular SVG groups. Chemical element glyphs in RDKit assets are vector outlines. Other labels remain searchable PDF text.

The validation directory contains image/font/path checks, same-size overlay and difference images, all eight side-by-side panel crops and a 180 mm screen-scale preview. Review those comparisons for the scientific corrections and the remaining typography density. The page uses the selected PNG's exact aspect ratio.
