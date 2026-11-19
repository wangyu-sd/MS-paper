# ORBIT-MS — source-linked comprehensive results inventory

**Snapshot:** 2026-11-19. Pinned orbit-ms PR95 commit `6237697c8f7c505b50c2d0df5640b62fdc09d245`. Current manuscript: `main.tex` five Results subsections plus preceding separate method overview figure.

**51 results assets** are indexed below. Existing numerical results are preserved and mapped to a specific panel; `x` denotes planned, not yet observed, experimental outcomes. “Main-text ready” means a measured result is available for writing/plotting with its protocol; final visuals can still require original experimental peaks and structures.

| ID | Results | Experiment / existing result | Key measured outcome | Original evidence location | Target | Preparation | Scientific role |
|---|---|---|---|---|---|---|---|
| E01 | R1 | Three-study source-linked MS/MS | 835,953 QC-eligible spectra | PR94 full scan QC + NMI plan | R1a-b | Main-text ready | Resource scale |
| E02 | R1 | Reference-unmatched spectra | 613,331 no accepted library match | PR94 reference matching + NMI plan | R1b | Main-text ready | Dark spectrum population |
| E03 | R1 | Full matching composition | 13,884 unambiguous accepted; 14,289 ambiguous; 194,449 unassessable | PR94 reference controls + editorial ledger | ED1 | Extended-data ready | Complete denominator accounting |
| E04 | R1 | Cross-study spectral communities | 2,255 recurrent in ≥2 studies; 98 in 3 | PR94 full recurrence Figure 1d | R1c | Main-text ready | Repeated independent spectral patterns |
| E05 | R1 | Public-source accession audit | cross-repository accession/USI joins, source/byte audit | PR94 pan_repository directories | ED1 | Extended-data ready | Reference population reproducibility |
| E06 | R1 | GeMS four candidate-evidence tiers | A 7; B 47; C 240; D 706 (n=1,000) | PR95 GeMS biological mechanisms JSON | R1d | Main-text ready | Structural-support landscape |
| E07 | R2 | Formula prediction | Top1 87.87%; Top16 98.44%; n=8,401 | SI development Table formula | R2b | Extended-data ready | Molecular composition |
| E08 | R2 | Formula–topology bottleneck | 93.11% formula coverage; 6.28% structural reach (historical graph model) | SI development graph generation | R2b | Main-text ready | Unsolved connectivity |
| E09 | R2 | World 3-cut fragmentation | 72.19% intensity-weighted fragment mass recall | SI development fragment coverage | ED2 | Extended-data ready | Structure-linked simulated fragments |
| E10 | R2 | Verifier matched spectrum effect | 62.79% fragment recall; +7.70 pp matched vs shuffled | SI development V evaluation | ED2 | Extended-data ready | Experimental spectral discrimination |
| E11 | R2 | Fixed-pool PubChem retrieval | World Top1 14.44%; score baseline 3.64% | SI development retrieval | ED2 | Extended-data ready | Measured-spectrum reranking |
| E12 | R2 | MMA same-checkpoint off/on | Exact@1 1.50→6.00%; Top10 4.50→14.50%; Reach 6.50→19.00% | SI WGV/RSI MMA strict | R2c | Main-text ready | Motif improves generation |
| E13 | R2 | MMA action supervision | Teacher@1 69.1→76.0%; Start@1 76.4→86.3% | SI WGV/RSI action diagnostic | ED3 | Extended-data ready | Correct molecular graph edits |
| E14 | R2 | MMA fixed-pool W/V reranking | G only 7.00%; G+WV 8.50%, Reach 16.00% | SI WGV/RSI C2/C3 | R2d | Main-text ready | Rank improves at same reach |
| E15 | R2 | MMA starts + W/V | G only 5.50%; G+WV 10.00%, Reach 19.00% | SI WGV/RSI C4/C5 | R2d | Main-text ready | Generator–Verifier complementarity |
| E16 | R2 | Canonical Hybrid best CAL200 | Exact@1 12.50%; Top10 21.50%; Reach 22.50% | SI WGV/RSI C7 | R2e | Main-text ready | Unified atom/ring/motif construction |
| E17 | R2 | Canonical Hybrid construction efficiency | 24.5 mean decisions; 84.7% valid constructible | SI WGV/RSI policy ablation | ED3 | Extended-data ready | Search efficiency |
| E18 | R2 | MassSpecGym full-horizon bio prior | Full TEST 31.57%/56.70%/64.77% Exact1/10/Reach | PR95 report setting I | R2f | Main-text ready | Database-assisted inference |
| E19 | R2 | Uniform isomer prior control | Full TEST 24.47%/53.29%/64.77% Exact1/10/Reach | PR95 report setting I uniform | ED5 | Extended-data ready | Structure prior contribution |
| E20 | R2 | Strict partial-core TEST development | Gen13-14 6.81%/12.68%/22.89% Exact1/10/Reach | PR95 report setting II | R2f | Main-text ready | Novel partial-core construction |
| E21 | R2 | NPLIB1/CANOPUS external split | 813 spectra; 16.73%/31.98%/41.82% | PR95 external benchmark | R2f | Main-text ready | Transfer to external spectra |
| E22 | R2 | CASMI 2022 | 237 spectra; 4.64%/11.39%/16.46% | PR95 external benchmark | R2f | Main-text ready | Blind challenge comparison |
| E23 | R2 | 10-axis complete generalization | 5 structure axes + 5 spectrum axes across 17,556 | PR95 multi_regime_benchmark_summary.json | ED4 | Extended-data ready | Chemistry/spectrum generalization |
| E24 | R2 | Chemical superclass breakdown | six families including macrolide 24.11% multi-energy Exact@1 | PR95 multi_regime_benchmark_summary.json | ED4 | Extended-data ready | Family-specific behavior |
| E25 | R2 | Multi-observation settings | single-spectrum, blind consensus, identity-assisted multi-energy metrics | PR95 multi_regime_benchmark_summary.json | ED5 | Extended-data ready | Information aggregation benefit |
| E26 | R2 | H0/H1 MCS diagnostic ranking | 7.48→8.52% Exact@1; +181 spectra | PR95 deep_mechanistic_perturbation_results.json | R2g | Main-text ready | Distinguishable ions |
| E27 | R2 | H2 fragmentation-cascade reranking | H0/H1/H2 Exact@1 8.99%, Top10 14.41%; +84 spectra from H2 | PR95 deep_mechanistic_perturbation_results.json | R2g | Main-text ready | Spectral hierarchy |
| E28 | R2 | Three real H1/H2 case groups | macrolide 139, alkaloid 84, peptide 42 spectra | PR95 diagnostic sample receipts | R2h | Needs final plot | Diagnostic mass evidence on competing structures |
| E29 | R2 | Published competitive comparisons | ORBIT, GEMS, FRIGID, MS-GPT etc; settings separated | SI MassSpecGym_DeNovo_Literature_Comparison.tex | ED5 | Extended-data ready | Method positioning |
| E30 | R3 | MMA vocab growth | 4.23M→12.98M→31.11M entries | SI WGV/RSI + PR95 | R3a | Main-text ready | Accumulated knowledge |
| E31 | R3 | HMDB-W Sleep source | 129,146 generated spectra; 32,229 structures | SI WGV/RSI | ED6 | Extended-data ready | Structure-only learning |
| E32 | R3 | Full TEST Gen0–19 development curve | 0→8.99% Exact@1; 0→14.41% Exact@10 | PR95 agent archive JSON | R3b | Main-text ready | Multi-generational recovery |
| E33 | R3 | Per-episode CAL200 Gen0–4 curve | 10.5→47.5% Gen1 Exact@1; Gen2–4 44–44.5% | PR95 rsi_ledger.jsonl | R3c | Main-text ready | Actual episode evolution |
| E34 | R3 | Promotion-gate acceptance | Gen1 selected; Gen0,2,3,4 rejected | PR95 rsi_ledger.jsonl | R3c | Main-text ready | Selection using measured feedback |
| E35 | R3 | Two-Episode paired-only | Exact@1 15.67→17.35% | SI external comparisons | R3d | Main-text ready | Multiple learning interventions |
| E36 | R3 | Two-Episode HMDB/CoCoNut | Exact@1 17.58→19.01% | SI external comparisons | R3d | Main-text ready | Cross-resource learning |
| E37 | R3 | Live newly recovered groups | latest pinned receipt +41 molecular groups / +201 spectra | PR95 live_wave_progress.json | R3e | Needs final plot | Incremental unique molecule recovery |
| E38 | R3 | Live newly promoted rank-one groups | latest pinned receipt 35 molecular groups | PR95 live_wave_progress.json | R3e | Needs final plot | Reach to identification |
| E39 | R3 | LLM Scientific Improver decision records | Gen10/11/16/17/18/19 plans and reflections | PR95 llm_principal_* receipts | R3f | Needs final plot | Episode intervention decisions |
| E40 | R3 | Failure-mode partition | 13,391 unreached; W/V/H1H2 ranking strata | PR95 Gen19 principal input | ED6 | Extended-data ready | Failure-directed training target |
| E41 | R4 | GeMS analyzed 1,000 spectra | 294 Tier A/B/C candidates | PR95 GeMS JSON | R4a | Main-text ready | Unknown chemical candidate landscape |
| E42 | R4 | Six mass transformation categories | 68/30/23/18/16/13 edges; total 168 | PR95 GeMS JSON | R4b | Main-text ready | Transformation-mass enrichment |
| E43 | R4 | Random chemical mass comparison | 168 vs 43.04±7.71, 3.90× enrichment | PR95 deep perturbation JSON | R4c | Main-text ready | Non-random network organization |
| E44 | R4 | Five biological chemistry theme analyses | host/microbe, ECM peptides, glutathione, membrane lipids, exposome | PR95 full report section 7 | R4d | Needs final plot | Chemical hypothesis families |
| E45 | R4 | Cross-study recurrence links | 2,255 spectral communities, 98 across three studies | PR94 Fig1d receipt | R4e | Extended-data ready | Multi-study chemical context |
| E46 | R5 | Cross-adduct available measurement groups | 390 H/Na double-adduct groups | PR95 deep perturbation JSON | R5a | Needs final plot | Cross-ion spectral evidence |
| E47 | R5 | Model-defined MS equivalence | 399 model tie spectra; 11.27% class-adjusted Exact@1 | PR95 deep perturbation JSON | R5b | Extended-data ready | Bounded structural uniqueness |
| E48 | R5 | Top3 bond environment agreement | 63.32% mean overlap | PR95 deep perturbation JSON | R5c | Extended-data ready | Local structural consensus |
| E49 | R5 | Computed cLogP consistency | top1 abs delta 0.6233 vs decoy 0.6891 | PR95 deep perturbation JSON | R5d | Extended-data ready | Physicochemical plausibility |
| E50 | R5 | Computed TPSA consistency | top1 abs delta 11.26 vs decoy 13.41 Å² | PR95 deep perturbation JSON | R5d | Extended-data ready | Polarity plausibility |
| E51 | R5 | Independent experimental structure anchors | x MS/MS or standard-confirmed hypotheses | main.tex Results placeholder slots | R5e | Needs final plot | External test of identity |

## Data provenance

**PR95 result sources:** [full experiment report](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md), [10-axis machine results](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_multi_regime_benchmark_summary.json), [generation archive](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_agent_generations_io_archive.json), [per-episode ledger](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_agent_receipts/rsi_ledger.jsonl), [H₁/H₂ mechanics](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_deep_mechanistic_perturbation_results.json), [GeMS chemical candidates](https://github.com/wangyu-sd/orbit-ms/blob/6237697c8f7c505b50c2d0df5640b62fdc09d245/docs/results/pr93_spectral_dark_matter_biological_mechanisms.json). Related PR94 source-linked spectrum study: [PR94](https://github.com/wangyu-sd/orbit-ms/pull/94).

**Manuscript sources:** [development tables](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/MassSpecGym_Development_Results.tex), [WGV/RSI tables](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/ORBIT_WGV_RSI_Results.tex), and [published comparator table](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/MassSpecGym_DeNovo_Literature_Comparison.tex).

**Separation of experimental contracts:** (i) known-formula CAL200, (ii) predicted-formula full TEST with target-disjoint construction, (iii) biodiversity/database-assisted retrieval, (iv) external NPLIB1/CASMI, (v) true CAL200 RSI episodes, (vi) identity-assisted multi-spectrum grouping, and (vii) GeMS unannotated data are distinct. The inventory places each in the paper without merging unlike denominators. The R3 Gen17–19 Reach endpoint remains blank in the vector preview until one frozen source reconciles late archive snapshots; all other data remain available and unchanged.
