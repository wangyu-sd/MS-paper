# ORBIT-MS method figure

Open [the high-resolution preview](orbit_ms_nmi_framework.png), [editable master](orbit_ms_nmi_framework.svg), [vector PDF](orbit_ms_nmi_framework.pdf), or [previous versus redesigned comparison](old_vs_new.png). The artwork measures 180 × 101.25 mm. All text, spectral sticks, comparators, paths and molecular artwork in the SVG are vector objects. The PDF has no raster images. The four regions follow the redesign brief: a chemical and neural MMA mechanism, b molecular generation and spectral evidence, c acquisition of training experience, and d bounded scientific intervention.

## Evidence in the artwork

- **Measured spectrum and candidate pair.** MassSpecGym `0002114` is a benchmark cyclic tetrapeptide. A and B are both present in the original G candidate pool and have the same elemental formula and different connectivity. Ranks 1 and 3 are from one archived candidate-pool ranking. They are not a rank-1-versus-rank-2 comparison or a claim of a confirmed unknown identity.
- **MMA.** Two drawable motifs are selected from four underlying mined source shards for the candidate run's fragment library. The labels 427 and 107 count supporting HMDB groups within those shards. The previews do not show the merged library's retrieval rank or learned attention weights. The ion formula labels the library key; motif structures are neutral skeletons. Matching bonds in the zoom are drawn from the explicit atom correspondence in the manifest.
- **Construction.** The top sequence on the right uses the PR95 deterministic Canonical Hybrid reference replay for the logged rank-1 candidate, using drawable motif records. The highlighted step attaches nine heavy atoms and a new connecting bond. The replay is labeled reference-conditioned and the original beam parent chain remains unavailable. The MMA zoom uses a documented partial graph from the same case.
- **W and V.** The frozen W and V checkpoints are matched by SHA-256 to the original evaluation receipt. Single-case replay reproduces the original whole-spectrum W/V scores. Each displayed W fragment is an exported atom-mask/ion-channel proposal from its candidate. Ion mass labels are the model outputs; the drawings are neutral skeletons. The matrix projects V's whole-spectrum posterior through its 2.5 mDa Gaussian mass kernel, truncated at 3σ for the display. Dot radius scales with square-root projected support; teal indicates candidate-specific support in this pair. The teal dot at 120.0893 represents weak support. It does not account for the rank difference by itself.
- **Experience and decisions.** Sleep uses an archived simulated pair. Wake shows actual experimental spectra and the generated structure in an archived accepted pseudo-label. Hindsight uses an archived generated structure and its counterfactual W spectrum, joined by connectivity. The agent depicts the bounded controller and a curriculum-proposal route. The four actions map to `EXPAND_KNOWLEDGE`, `IMPROVE_GENERATOR`, `IMPROVE_VERIFIER` and `COLLECT_EVIDENCE`. Phase-specific gates and decision receipts do not establish autonomous performance improvement.

The source manifest records the commit IDs, private archive paths, selected rows, SHA-256 values, projected evidence and atom mappings. The article, Results and existing artwork live outside this directory.

## Rebuild artwork

From this directory, install `requirements.txt`, install Playwright and its Chromium browser, and make Poppler available. Set `CHROME_PATH` if using a system Chromium executable.

```sh
python draw.py
node export.cjs
pdftoppm -scale-to-x 3840 -scale-to-y 2160 -png -singlefile \
  orbit_ms_nmi_framework.pdf orbit_ms_nmi_framework
python compare.py /path/to/previous.png orbit_ms_nmi_framework.png old_vs_new.png
```

`assemble_evidence.py` extracts the plotted data from the frozen source exports. `export_scored_case.py` reproduces W and V structural evidence given the original query, ranking, submission receipt and matching checkpoints. `replay_construction.py` reproduces the reference-conditioned trajectory with the same two motif templates. The archived model checkpoints are not required to rebuild the artwork from the committed manifest.

The compressed [single-case W/V export](evidence/frozen_wv_case.json.gz) retains the two complete fragment-object sets and V posteriors. It contains predictions for this figure's two benchmark candidates, not model weights. In the controlled workflow, collect-only episodes record diagnostic evidence without a trained trial. The curriculum arrow shows the separate experience-selection mechanism.
