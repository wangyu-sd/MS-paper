# ORBIT-MS MMA-centric method framework

This standalone method figure implements the five-region layout in [MS-paper PR #13](https://github.com/wangyu-sd/MS-paper/pull/13). The figure starts at panel a and uses the measured spectrum and chemical graphs to carry the story. The ImageGen composition study informed the placement and spacing. The master was then rebuilt from vector text, paths, source records and RDKit diagrams.

- `orbit_ms_nmi_method_overview.svg` contains editable text, routes, spectra and molecule paths; named groups identify panels a–e.
- `orbit_ms_nmi_method_overview.pdf` is the vector export at nominal 180 mm width. The PNG is the 3600 × 2025 review render.
- `case_manifest.json` pins the data file, exact spectrum row, PR heads, code hashes, candidate identities, alignment features and missing receipts. `assets/` includes the standalone RDKit molecular components.

## Evidence boundaries

The experimental spectrum is MassSpecGymID0002114, a known-reference benchmark example. The initial linear-side-chain candidate and branch-repaired counterpart come from the pinned PR95 illustration source. Their formula and connectivity were checked with RDKit. The candidate pair spans two refinement stages. The source drawing script supplies the G construction states, which are structural illustrations. A saved generation rollout and a pairwise before/after W/V ranking receipt were not available. The figure does not treat the refined structure as an inference input or claim that the illustrated pair was a frozen G pool.

Panel b links the measured 120.0808 peak to one mass-compatible elemental composition and uses the graph from the source's depicted motif start. PR95's `motif_graph` and `template_features` were executed on that reference motif and the next source-depicted partial graph. The result is an atom/bond correspondence probe, not a checkpoint's learned attention or a record that the motif was retrieved at that peak. The neutral motif and the suggested ion composition have different hydrogen counts. Source support, alternate motifs and per-candidate W/V peak matches are left unpopulated. The full four-peak experimental array is drawn in a. The two peaks near 120.08 overlap at this scale, and c labels three selected peaks for the verification layout.

Panel d separates W simulation, pseudo-label gating and candidate-conditioned counterfactual experience. Shannon entropy thresholds, scaffold caps and evidence gates come from the PR95 builder. Scarcity is shown as a scheduling criterion described in PR95. Panel e shows the PR96 controlled protocol schematically. Its selected action is an illustration, the memory path goes to decision context, and W remains frozen. A collect-only episode returns diagnostic evidence and does not promote a model. Paired CAL evaluation applies when comparing an eligible trial against baseline.

## Rebuild

Run from this directory. Use Python 3.12, RDKit 2025.9.3, NetworkX and NumPy, plus Node with Playwright and Chromium, and Poppler.

```sh
python -m pip install rdkit==2025.9.3 networkx numpy
npm install --no-save playwright
npx playwright install chromium
python draw_framework.py
node export_framework.cjs
pdftoppm -scale-to-x 3600 -scale-to-y 2025 -png -singlefile \
  orbit_ms_nmi_method_overview.pdf orbit_ms_nmi_method_overview
```

Optionally point `CHROME_PATH` to a local Chromium executable. To regenerate the manifest, download the pinned MassSpecGym TSV from the manifest's recorded URL, fetch ORBIT-MS PR95 and PR96 into an authorized local clone, then run:

```sh
python prepare_case.py /path/to/MassSpecGym.tsv /path/to/orbit-ms
```

The manuscript figure slot remains provisional. This directory can be reviewed independently of manuscript layout.
