# ORBIT-MS: two distinct generation curves and their data

**Source pin:** orbit-ms PR95 `6237697c8f7c505b50c2d0df5640b62fdc09d245` (2026-11-19), plus actual episode promotion receipts. **Figure target:** Results R3b/R3c.

## A. Full-test historical cumulative archive (Gen0–19)

From [PR95 generation archive](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_agent_generations_io_archive.json): **17,556** MassSpecGym TEST spectra, 2,998 molecules, historical development snapshots.

| Checkpoint | Exact@1 | Exact@10 | Reach | Main intervention |
|---|---:|---:|---:|---|
| Gen 0 | 0% | 0% | 0% | Initial atom-only |
| Gen 1-3 | 0.52% | 2.72% | 6.14% | MMA libv1 / fragment starts |
| Gen 4-5 | 0.72% | 3.32% | 10.45% | HMDB Sleep / MMA libv2 |
| Gen 6-7 | 1.65% | 3.94% | 12.6% | Partial-core W/V |
| Gen 8-10 | 3.58% | 8.01% | 22.89% | Dual Wake–Sleep / multienergy |
| Gen 11-14 | 7.48% | 13.58% | 22.89% | V_g10 / isomer ranking |
| Gen 15-16 | 7.48% | 13.58% | 23.33% | SMARTS priors / refreshed candidate reach |
| Gen 17-19 + H1/H2 | 8.99% | 14.41% | — | MCS diagnostic-ion and cascade ranking |

The archive's late Gen17–19 rows contain combined H₁/H₂ reranking. Their exact1/10 points are recorded and plotted, with a *separate mechanistic inset* reporting H₀→H₁→H₂ = 7.48→8.52→8.99% (source [diagnostic JSON](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_deep_mechanistic_perturbation_results.json)). The late archive writes `23.72%+ (4207/17556)` for cumulative Reach while the later corrected commit `48715967e` reports `23.94% / 4203`; the last Reach value is intentionally empty in `gen_curve_main.csv` rather than assigning an inconsistent point.

This curve is an **aggregate engineering and recursive-learning development history**, including previous human/scripted changes. Do not interpolate missing intermediate Gen labels or present all checkpoint gains as independently executed Scientific Improver decisions.

## B. Actual per-episode CAL200 promotion ledger (Gen0–4)

From [PR95 RSI ledger](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_agent_receipts/rsi_ledger.jsonl), with known formula and 200 independent molecular cases:

| Episode | Exact@1 | Exact@10 | Reach | Promoted? | Mean candidates |
|---|---:|---:|---:|---|---:|
| Gen0 | 10.5% | 17.0% | 20.5% | no | 80.0 |
| Gen1 | 47.5% | 71.0% | 90.0% | yes | 2584.7 |
| Gen2 | 44.5% | 66.0% | 90.0% | no | 2584.7 |
| Gen3 | 44.0% | 67.0% | 90.0% | no | 2584.9 |
| Gen4 | 44.0% | 67.0% | 90.0% | no | 2584.8 |

Gen1 is promoted; other candidate episodes are not promoted. For the figure, annotate accepted/rejected model proposals and show a subtle secondary strip for candidate-count changes. The CAL200 episode Gen index is **not** the historical full-TEST generation index.

## Other generation assets

- Knowledge vocabulary: 4.23M → 12.98M → 31.11M entries (WGV SI).
- Two-Episode performance: paired-only 15.67→17.35%; HMDB+COCONUT 17.58→19.01% Exact@1 (MassSpecGym literature SI).
- Latest live refresh at pinned PR95 head: 41 newly reached molecule groups / 201 spectra and 35 promoted rank-first groups; active wave progress is a separate in-progress receipt.
- Gen10/11/16/17/18/19 Principal receipts provide the next-generation action, diagnosis and retained experience history.

CSV files are `figures/data/gen_curve_main.csv` and `figures/data/gen_curve_rsi.csv`. SVG previews are in `figures/previews/`, and the build command is `python scripts/render_paper_result_previews.py --out figures/previews`.
