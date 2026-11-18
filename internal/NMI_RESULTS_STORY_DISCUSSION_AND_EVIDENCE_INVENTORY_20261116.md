# ORBIT-MS | NMI Results storyline and evidence-inventory discussion (2026-11-16)

> **Status: discussion document only — not a manuscript edit, not an experiment completion claim, not a final figure specification.**
>
> This note records the current author discussion about a results-first NMI narrative and the evidence that should be organized before deciding what new experiments, plots, or prose are needed. Do **not** modify `main.tex`, figures, supplementary tables, or the current NMI manuscript plan in this PR. Nothing here is represented as a validated new result.

## 1. Scientific positioning and possible title

**Working title:** *ORBIT-MS: Agent-Driven Recursive Self-Improvement for Molecular Structure Elucidation*.

**Central proposition to test:** Molecular structure elucidation becomes a recursively improving scientific inference process when (i) peak-level fragmentation information is converted into reusable, executable chemical structure knowledge by **mass-matched substructure alignment (MMA)**, (ii) unlabeled or model-generated molecular experience is selected and assimilated through **information- and structural-scarcity-guided semi-supervised learning**, and (iii) a **Scientific Improver Agent** diagnoses changing failure modes and chooses targeted interventions to MMA/G/V based on measured outcomes.

This is an intended scientific claim, **not an already demonstrated full autonomous learning curve**. The title and exact claim strength will be revisited after the data inventory and matched comparisons.

### Narrative decision

Do **not** introduce each module first. Lead with the strongest end-to-end molecular recovery results, uncover the *generation–discrimination tension*, and then use MMA, selective self-learning, and agent-directed intervention to explain progressively deeper insights. Close with independent chemical relevance.

**Proposed reading order: achievement → bottleneck → information-guided learning → autonomous scientific improvement → chemical application.**

## 2. Five provisional Results sections (results-first, progressively deeper insights)

### R1. ORBIT-MS expands molecular structure recovery across challenging chemical space

**Opening evidence, before architecture:** frozen-protocol overall structure recovery (Exact@1, Exact@10, candidate-pool Reach, structural similarity), external datasets, and stratified performance on difficult chemical structures. An honest view of the current achievement must come first.

**Proposed insight:** Molecular candidate *reachability* and successful final *identification* are distinct capabilities; the gap is especially important for difficult isomers, low-homology structures, and novel ring topologies.

**Potential Figure 1:** (a) main benchmark against comparable methods under the same information-access regime; (b) generated/reachable/correctly-ranked molecular identities; (c) complexity or homology strata, including macrolides, glycosides, MCES distance and ring novelty; (d) real benchmark molecule/spectrum examples; (e) optional same-protocol before/after recovery plot if genuinely paired. Avoid a large method diagram as the dominant first panel.

**Current evidence:** PR95 benchmark coverage and two external datasets (inventory below). **Required reconciliation:** single frozen checkpoint versus mixed-generation candidate aggregates; exact measured denominators and source split; blind observable precursor grouping versus any GT-grouped multi-energy result; distinct de novo, MMA-/homology-assisted, and database-assisted settings. Without comparable external baselines, do not claim new state of the art.

### R2. Stronger molecular hypotheses expose an evidence-discrimination bottleneck

**Scientific question:** Does increasing candidate coverage produce increasingly difficult structural alternatives and expose insufficient distinguishing spectral evidence?

**Core mechanism:** MMA is not generic knowledge augmentation. It performs **observed peak → ion formula → mass-matched structural subfragment → evidence-supported graph/motif action**, with source-group exclusion and structural support tracking. MMA can act through peak-level memory, atom/ring/motif actions, multi-peak starts, partial-core completion, and MMA-aware verification. W proposes fragment evidence from *candidate structures* and V evaluates evidence relative to the *measured* spectrum; W must not be depicted as receiving the target experimental peak list during forward simulation.

**Proposed insight to investigate:** Expanding chemically plausible hypothesis space can improve Reach but worsen rank competition; structure-specific fragment evidence must resolve this gap. Do not assume a universal monotonic tradeoff from a few configuration points.

**Potential Figure 2:** (a) one real spectrum with chemically valid MMA fragment-ion/formula and molecular-graph alignment; (b) strict same-checkpoint MMA on/off, decomposing reach, action accuracy, trajectory length; (c) matched candidate-pool G versus G+W/V ranking; (d) candidate fidelity versus separability, with genuine same-formula/isomer alternatives and peak-specific discriminatory evidence; (e) ablation by MMA injection route and chemical complexity if available.

**Current evidence:** CAL200 known-reference-formula MMA on/off Exact@1 1.50% → 6.00%, Reach 6.50% → 19.00% (same-checkpoint table); separate component protocol: MMA features with G ranking Reach 16.00% / Exact@1 7.00%; MMA starts with G ranking Reach 19.00% / Exact@1 5.50%; identical MMA-start pool with W/V ranking Exact@1 10.00%. These are **known-formula calibration / distinct component settings**, not overall blind TEST effects. The Canonical Hybrid trajectory study and fixed-pool verifier study support distinct mechanism claims.

### R3. Information-guided semi-supervised learning expands the frontier of recoverable chemistry

**Scientific question:** Under limited paired-spectrum supervision, which new molecular experiences contribute genuinely new chemical capability rather than just increasing sample count?

**Three complementary streams:** **Sleep** on unpaired molecules → frozen W simulated spectra; **Wake** on real unlabeled GeMS spectra → G/W/V-filtered pseudolabels; **Hindsight** on generated molecules → counterfactual W-produced spectrum–structure pairs (and hard negatives). Spectral entropy, TRAIN formula/ring scarcity, evidence quality and Murcko diversity are proposed experience-selection signals.

**Proposed insight to test:** Chemically informative and structurally underrepresented learning experiences can outperform simple data volume expansion at equal cost. Shannon spectral entropy is a sampling proxy, **not proof of actual structural information gain or a solved maximum-entropy objective**.

**Potential Figure 3:** (a) same-budget incremental *newly recovered structures*, rather than solely counts of synthetic spectra; (b) random vs entropy vs scarcity vs joint acquisition at fixed effective sample/compute budget; (c) Sleep-only, Wake-only, Hindsight-only, combined ablation; (d) structural novelty / ring/formula coverage and non-collapse; (e) source-linked case of transferable newly learned fragment/motif knowledge.

**Current evidence:** PR95 reports MMA library growth 4.23M → 12.98M → 31.11M alignments, 224,546 simulated Sleep spectra and 227,126 aggregate experiences, plus Wake/Hindsight examples. The actual `build_pr93_unlabeled_gems_rsi_cycle.py` implements pseudo-label gates, Murcko cap and a Shannon entropy gate for Hindsight spectra; the controller records scarcity-informed training choices. **Missing:** a clean equal-budget experiment isolating entropy/scarcity, the three streams, their causal effect on held-out structural recovery, and raw artifact-level lineage for all claimed corpus totals.

### R4. Scientific agents turn changing failures into targeted recursive improvement

**Scientific question:** Can a Scientific Agent diagnose evolving structural bottlenecks and choose better interventions than a fixed curriculum, scripted routing or no-memory policy?

**Two coupled loops:** (i) improvement of MMA/G/V chemical capabilities via executed training/evidence interventions; (ii) improvement of subsequent *agent decisions* through evidence-backed episode reflection and persistent memory. Do not imply language-model weight training.

**Proposed insight to test:** Successful learning changes the system's dominant failure mode; scientific intervention is therefore a sequential decision problem over nonstationary bottlenecks.

**Potential Figure 4:** (a) cumulative *net* independently recovered molecule identities versus actual autonomous generation, with newly gained and forgotten compounds; (b) matched fixed-update / rule-based / agent-selected interventions at identical starting state and resource envelope; (c) failure diagnosis → chosen action → measured outcome; (d) agent memory versus no memory; (e) real molecule case and transfer to independent structures. The prominent panel should be the measured recovery curve, not an agent framework cartoon.

**Current evidence:** PR95 includes a verified LLM Principal decision receipt (2,536 tokens, selected EXPAND_NP_AND_WAKE), training/evaluation controller and historical engineering versions; PR96 has bounded Scientific Improver implementation and evaluation checks. PR95 reports hard-isomer V-g10 win rate 50.78% → 56.00% in its separate verifier-training setting. **Not demonstrated yet:** 3+ completed independent sequential agent-selected episodes, matched-budget agent-vs-fixed net recovery, measured promotion and no-memory effects. **Do not re-label historical Gen0–Gen11 manual/scripted engineering as autonomous Agent generations.**

### R5. Recursive molecular learning enables evidence-supported exploration of metabolomic dark matter

**Scientific question:** What new, independently testable *chemical information* does progressive molecular elucidation recover from real reference-unmatched spectra?

**Proposed insight:** A useful chemical discovery system should improve the *supported structural resolution* of unassigned observations, not merely generate more plausible SMILES or more spectral clusters.

**Potential Figure 5:** (a) population denominator and reference-match status for source-audited public data; (b) calibrated output tiers — unresolved → formula/class → shared core → bounded isomers → putative 2D connectivity; (c) newly supportable hypotheses after learning, retaining regressions/uncertainty; (d) 2–3 real molecular-family/candidate cases with actual measured fragmentation, RDKit connectivity differences and independent spectral support; (e) independent MS/MS or MSn, and authentic-standard results only where actually obtained.

**Current evidence:** the MS-paper / PR94 draft reports 835,953 QC-eligible biological MS/MS queries and 613,331 without an accepted reference match from three studies; 2,255 recurrent *spectral* communities are reported, not chemically confirmed molecular families. **Missing:** frozen inference on the source-audited entities, valid structural-resolution tier counts, supported graph relationships and independent chemical corroboration. Do not equate scans with unique molecules; do not claim discovery from spectral recurrence or an unverified candidate graph.

## 3. Working evidence inventory (provenance and limitations)

| Evidence block | Reported quantitative outcome | Source and interpretation | Status for manuscript |
|---|---|---|---|
| Main full-scale MassSpecGym | Latest JSON (2026-11-16 11:02 UTC): **17,548 / 17,556 spectra; 2,994 molecules; single-spectrum Exact@1 1.65%; blind observable-cluster Exact@1 3.52%; multi-energy Exact@1 3.58%; Exact@10 8.01%; Reach 22.90%** | PR95 `docs/results/pr93_multi_regime_benchmark_summary.json`, head `4bc2d77a`; aggregate may combine checkpoint generations and grouping modes | Consolidate per-case data and exact protocol before final main figure |
| Full-scale report discrepancy | Markdown benchmark still gives **16,893 spectra, 627 Exact@1 (3.71%), 1,230 Exact@10 (7.28%), Reach 3,873 (22.93%)** | PR95 `docs/results/pr93_multi_regime_benchmark_and_rsi_results.md`, blob `9904850`; older than latest JSON | **Do not mix** the two population snapshots; reconcile from raw results |
| NPLIB1 official | 813/813; Exact@1 16.73%; Exact@10 31.98%; Reach 41.82% | PR95 official-test report; confirm candidate supply, checkpoint and the formula regime | Usable as attributed reported outcome, pending aligned final comparison |
| CASMI 2022 | 237/237; Exact@1 4.64%; Exact@10 11.39%; Reach 16.46% | PR95 official-test report; formula@K reported 90.30% | Usable as attributed reported outcome, pending aligned final comparison |
| Strict MMA mechanism | Known-formula CAL200 same-checkpoint: Exact@1 1.50% → 6.00%; Reach 6.50% → 19.00% | MS-paper `supplementary/ORBIT_WGV_RSI_Results.tex` strict MMA table | Strong current mechanism evidence; NOT unknown-formula TEST |
| Fixed G-pool reranking | CAL G-only Exact@1 7.00% vs G+W/V 8.50%, Reach 16.00% fixed | Same supplement, fixed pool ranking | Supports discrimination effect, not increased generation coverage |
| MMA knowledge growth | 4.23M / 12.98M / 31.11M entries (successive library versions) | PR95 historical development and reported assets | Knowledge inventory; not proof of new chemical recovery |
| Self-learning data | PR95 claims 224,546 W Sleep spectra; 227,126 combined; plus GeMS Wake and Hindsight | PR95 report and self-learning scripts | Corpus receipts and ablations should be collated separately |
| Hard-isomer V | V-g10 reported hard negative win rate 50.78% → 56.00%, n=1,609 | PR95 discussion/report; specialized V metric | Not end-to-end exact structure recovery |
| Historic engineering sequence | Gen0–Gen10 / Gen13 artifacts reported, e.g. paired Gen9 → Gen13 on 779 overlapping TEST spectra: single Reach 7.96% → 11.94% | PR95 evolution ledger and PR discussion | Engineering development evidence, **not** autonomous RSI |
| Scientific Agent | One verified LLM Principal decision, 2,536 tokens, EXPAND_NP_AND_WAKE; PR96 agent source | PR95 `outputs/pr93_rsi_daemon/llm_principal_gen10_receipt.json`; PR96 `scientific_improver.py` | Real decision evidence, **not** completed matched autonomous episode |
| Unassigned biological MS/MS | 835,953 eligible spectra/queries; 613,331 reference-unmatched | MS-paper current `main.tex` and 2026-11-12 plan | Useful application substrate, not number of unknown molecules |

**Integrity notes**

1. Freeze and report numerator, denominator and molecular unit: spectrum, unique connectivity, precursor cluster, candidate pool, or chemical family. Never treat those as interchangeable.
2. Distinguish blind clustering by observed neutral mass + **predicted** formula from multi-energy analyses that use GT molecule-group IDs. Only the former is deployable as a blind strategy.
3. Separate target formula availability and chemical prior: known-formula CAL; blind formula-prediction de novo; MMA-assisted starts; non-test homology Macro-Core; database-assisted fixed candidate pool; cross-generation pooled candidates.
4. Distinguish `Reach` from `Exact@k`; the purported historical TEST cohort with Exact@10 331/1,996 and Reach 306/1,996 is **internally inconsistent** and must not be copied into figures.
5. Full-test evaluation was consulted during iterative historical development. Avoid presenting the historical development sweep as a perfectly untouched final blind estimate; document model-selection provenance.
6. Neither a higher MMA entry count nor an LLM action receipt demonstrates improved autonomous molecular elucidation.

## 4. Data-organization contract before deciding the manuscript

**Immediate objective: inventory what already exists, not launch a large new training matrix.** Build a compact evidence index where each figure-eligible result has an actual run ID, artifact paths, provenance, cohort, model versions and denominators.

### A. Standardized result record (one row per actual evaluation)

- `claim_id` / `figure_panel_candidate` / `evidence_status` (verified raw / reported summary / planned).
- `run_id`, source repo PR/commit SHA, date, run command, machine/source path, optional artifact checksum.
- `G_checkpoint`, `W_checkpoint`, `V_checkpoint`, `MMA_library`, prior/re-rank version and whether cross-generation pools were merged.
- TRAIN provenance and anti-leakage split, number of training pairs, Sleep/Wake/Hindsight counts, acquisition strategy, fitting budget.
- Benchmark version, fold, unique molecule groups / spectra, precursor formula regime, independent vs GT-based groupings, same candidate budget, raw vs repaired vs posthoc ranked results.
- Exact@1, Exact@10, Reach, Tanimoto, formula@K, compute/time, and recovered/lost molecular IDs where available.
- Comparator run IDs, interpretation, confounders, failure to reproduce, and links to **raw** per-case outputs (not merely paper tables).

### B. Generation bookkeeping

Produce two **separate** tables, both with explicit missing cells:

1. `engineering_generation_ledger`: historic G0–G11+ interventions, code/commit, distinct checkpoint, evaluation regime, samples, observed metrics, evidence path, and whether numbers are actually comparable on a common cohort. Do not invent G11 figures from Gen13 pooled results.
2. `autonomous_episode_ledger`: sequential agent episodes only, initial state, fresh TRAIN-FIT diagnosis, selected action and rationale, action execution receipts, CAL before/after, promotion/rollback, new/lost held-out molecular identities, reflection memory, GPU cost, and evidence for next decision. At this snapshot a full autonomous G0–G11 ledger is **not established**.

### C. Figure-readiness decision after inventory

- **R1 ready when:** official TEST and external result provenance and comparable frozen protocol are reconciled.
- **R2 ready when:** strict MMA plus equal-pool generation/discrimination analysis and a chemically valid worked example are assembled.
- **R3 ready when:** matched-budget entropy/scarcity and separate self-learning stream effects on new structural recovery are available.
- **R4 ready when:** genuine agent-selected sequential episodes and a matched fixed/scripted comparison are measured.
- **R5 ready when:** source-linked real-spectrum structural hypotheses and independent evidence support a bounded chemical claim.

No result should be upgraded from *planned* to *observed* without run evidence. Do not choose new experiment scope until this inventory identifies the most decisive missing comparison.

## 5. Figure and writing constraints for future discussion

- Each Results section **starts with its strongest scientific outcome** and only then expands into mechanistic analysis. Avoid organizing the main text as a sequence of modules or implementation milestones.
- Every main figure has **one dominant empirical panel**, with small subpanels explaining *why* the trend happens; real measured spectra and RDKit molecular graphs where chemical examples are needed.
- Use exact evaluated chemical identities, avoid repeated-scan inflation, and report negative/ambiguous chemical assignments at their actual evidentiary tier.
- The paper remains NMI-focused on an **agent-directed scientific learning paradigm**, with molecular structure elucidation as its testbed; dark-metabolomics resource/application is an important endpoint, not a substitute for evidence of autonomous learning.
- Preserve the current manuscript until the data inventory and scientific story are jointly reviewed. The revised Results order is **provisional**, not yet an instruction to rewrite `main.tex`.

## 6. Source-of-truth links (snapshot)

- [MS-paper manuscript](https://github.com/wangyu-sd/MS-paper/blob/main/main.tex) — unchanged by this PR.
- [Existing Nov 12 NMI Results plan](https://github.com/wangyu-sd/MS-paper/blob/main/internal/NMI_CHEMICAL_ELUCIDATION_RESULTS_PLAN_20261112.md) — unchanged by this PR.
- [MS-paper WGV/RSI supplement](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/ORBIT_WGV_RSI_Results.tex).
- [ORBIT-MS PR95](https://github.com/wangyu-sd/orbit-ms/pull/95) — evidence/report snapshot head `4bc2d77a9ce02351d4d33c23166b1cec56b0f7e0` (2026-11-16).
- [PR95 latest machine-readable summary](https://github.com/wangyu-sd/orbit-ms/blob/4bc2d77a9ce02351d4d33c23166b1cec56b0f7e0/docs/results/pr93_multi_regime_benchmark_summary.json).
- [PR95 earlier full-scale Markdown report](https://github.com/wangyu-sd/orbit-ms/blob/4bc2d77a9ce02351d4d33c23166b1cec56b0f7e0/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md).
- [PR95 MMA generalization report](https://github.com/wangyu-sd/orbit-ms/blob/4bc2d77a9ce02351d4d33c23166b1cec56b0f7e0/docs/results/pr93_test_generalization_and_mma_ablation_20261109.md).
- [PR95 Agent decision receipt](https://github.com/wangyu-sd/orbit-ms/blob/4bc2d77a9ce02351d4d33c23166b1cec56b0f7e0/outputs/pr93_rsi_daemon/llm_principal_gen10_receipt.json).
- [ORBIT-MS PR96 Scientific Improver](https://github.com/wangyu-sd/orbit-ms/pull/96).

**Next discussion:** reconcile the available data first, then decide the opening headline result, the strongest non-obvious evidence-discrimination insight, the information-learning ablation, and what minimum autonomous RSI comparison earns the paper's main claim. No manuscript changes in this PR.
