# ORBIT-MS | Complete Results → visualization production masterplan

**Created:** 2026-11-19. **Immutable input snapshot:** ORBIT-MS PR95 `6237697c8f7c505b50c2d0df5640b62fdc09d245`, PR94 source audits, and MS-paper's already existing supplementary tables. **Goal:** maximize the scientific presentation of the current complete experimental asset collection without changing models or rewriting the manuscript.

The existing five Results follow one coherent proposition: source-linked reference-unmatched spectra (R1) are connected to candidate graphs by fragment-guided molecular generation and verification (R2); feedback-driven model and knowledge updates expand recoverable chemical space (R3); the recovered hypotheses reveal structural organization (R4); and independent spectral evidence can test the specificity of the claims (R5).

## Deliverables in this PR

| Artifact | Implemented output | Primary use |
|---|---|---|
| [Full results inventory](ORBIT_MS_RESULTS_INVENTORY_20261119.md) | **51** source-indexed experiment assets; main/ED/SI placement and status | manuscript writing coordination |
| [Main figure panel designs](ORBIT_MS_MAINFIGURES_LAYOUT_20261119.md) | R1–R5 detailed panels and 8 Extended Data bundles | figure production |
| [Gen curve protocol](ORBIT_MS_GEN_CURVES_20261119.md) | historical full-test and true CAL200 episode curve | Fig R3 |
| `figures/data/gen_curve_main.csv` | 8 cumulative generation snapshots, 17,556 TEST spectra | R3b |
| `figures/data/gen_curve_rsi.csv` | 5 actual CAL200 RSI episode candidates with promotion gate | R3c |
| `figures/data/benchmark_summary.csv` | MassSpecGym, NPLIB1, CASMI, known-formula and full-horizon settings | R2f |
| `figures/data/ablation_summary.csv` | MMA/WV/Canonical Hybrid/H₁/H₂ rows | R2c/d/g |
| `figures/data/chemical_family_generalization.csv` | six chemical classes | ED4 |
| `figures/data/ten_axis_profile.csv` | **37 strata** across 10 full TEST evaluation axes | ED4 |
| `figures/data/gems_tiers.csv` | four structural evidence grades | R1d |
| `figures/data/gems_mass_deltas.csv` | six relation-mass categories | R4b |
| `figures/previews/gen_curve_main.svg`, `gen_curve_rsi.svg` | checked-in vector previews | immediate viewing and review |
| `scripts/render_paper_result_previews.py` | reproducible SVG/PDF generation from committed CSV | editable publication plots |
| `supplementary/ORBIT_Results_Visualization_Roadmap.tex` | manuscript-compiled five-Results cross-reference map | supplementary traceability |

## Production sequence

**Step 1: freeze reproducible quantitative figures.** Render the two Gen curves and GeMS mass-shift/evidence-grade summaries. These immediately establish R2–R4 statistical content. The figure previews use only actual pinned CSV rows.

**Step 2: extract representative molecules and original spectra.** For R2h, R3f, R4d/e and R5a/e, attach original scans/USIs, their raw experimental m/z–intensity arrays, ion identities, actual candidate SMILES, calculated fragments and pre/post action ranks. Use RDKit SVG instead of approximating a chemical structure in a drawing tool.

**Step 3: assemble five coherent Results figures.** Use main-text panels for the strongest observed effects and mechanistic examples; move repeated baselines, full ten-axis analyses and implementation details into eight Extended Data bundles. Keep final five figure asset filenames and original TeX captions stable.

**Step 4: finish text/legend alignment.** Write each Results paragraph from its evidence panel and its source path in the inventory. Preserve existing Methods, quantitative source, and future `x` placeholders until measured results fill them.

## Figure typography and color system

Academic, precise and restrained: white backgrounds, dark navy `#25465D`, muted teal `#397D83`, graphite `#858B90`, modest rust `#A66E55`. Distinguish measured spectrum peaks from simulated fragments with clear stroke styles; keep molecular bonds black. No visual decoration, fake peaks, repeated three-card layouts or oversized schematic arrows.

## Generate editable previews

```bash
python -m pip install matplotlib
python scripts/render_paper_result_previews.py --out figures/previews
```

The generator creates SVG and PDF quantitative figures but does **not** overwrite the existing manuscript PDF figure placeholders. Data are fixed to the pinned PR95 source. For reproducibility, individual denominators and protocol names remain in the CSV and the source-linked inventory.

## Paper numbering convention

`main.tex` currently contains one method-overview figure before the five results figure assets. Thus R1–R5 are Results **asset slots**, not guaranteed printed Fig. 1–5. Use existing LaTeX `\\ref` labels instead of renumbering the manuscript in this PR.
