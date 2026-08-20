# ORBIT-MS manuscript experiment execution plan

## Purpose

This document is the executable experimental plan for the manuscript **Adaptive fragmentation evidence for molecular structure elucidation**. It is intentionally organized by execution priority rather than manuscript order. The central rule is that the paper is not allowed to become a collection of model improvements. Every experiment must answer one of the manuscript's scientific questions and must produce an immutable artifact that can be bound to the claim–evidence matrix.

The execution order is:

1. **P0 — Freeze the study substrate and evaluation contracts.**
2. **P1 — Prove or falsify candidate-specific fragmentation evidence (Figure 2).**
3. **P2 — Establish the cross-model evidence bottleneck (Figure 1).**
4. **P3 — Separate experimental-spectrum information from chemical prior (Figure 3).**
5. **P4 — Test reciprocal adaptation, external transfer and risk-controlled resolution (Figure 4).**
6. **P5 — Run the independent mouse deployment (Figure 5).**
7. **P6 — Nature-main-track extension: evidence-guided acquisition of a new MS measurement.**

P1 is deliberately executed before P2. If candidate-specific pLSE does not outperform strong non-candidate-specific evidence on hard same-formula alternatives, the manuscript's central object is not yet established and later experiments should not be used to disguise that failure.

---

# 0. Global rules before any confirmatory experiment

## 0.1 Separate development, calibration and final test roles

Use molecule groups, not spectra, as the independent unit. All spectra belonging to the same standardized 2D molecular identity must remain in one partition.

For every public benchmark used in the manuscript, freeze four logical roles:

- **development/train** — chemistry-rule development, METEOR training, pLSE implementation and debugging;
- **validation** — scorer selection, ablation design, hyperparameter choice, baseline integration and experiment debugging;
- **calibration** — conformal/risk-control thresholds only; never used to change METEOR or pLSE;
- **final test** — read once after all analysis code, candidate pools, metrics and model/evidence snapshots are frozen.

If the benchmark does not provide four native partitions, split the original training/development side into development/validation/calibration while leaving the official test untouched.

The preferred public benchmark is the audited MassSpecGym release selected for the paper (freeze the exact version and checksum before execution; use v1.5 if that is the release adopted by the project). Do not silently mix candidate pools or labels from older benchmark releases.

## 0.2 Freeze molecular standardization

Before generating any candidate pool, freeze one standardization function and apply it to GT and every external candidate source:

1. RDKit parse and sanitization;
2. remove disconnected counterions only under one preregistered rule;
3. standardize charge state only when justified by the analytical representation;
4. canonicalize the 2D connectivity identity used for molecule grouping;
5. compute molecular formula and exact neutral mass from the standardized structure;
6. compute Morgan fingerprint and MCES-compatible representation;
7. deduplicate identical 2D structures within each candidate pool;
8. keep stereochemical information in the raw record but do not claim stereochemical resolution from ordinary MS/MS unless independently supported.

Write a manifest row for every molecule containing at minimum:

`molecule_group_id, canonical_smiles, formula, exact_mass, source, source_id, split, standardization_version, structure_hash`.

## 0.3 Freeze leakage audit

For every structure-only pretraining source and every benchmark test molecule, report:

- exact 2D-structure overlap;
- nearest-neighbour Morgan Tanimoto;
- MCES distance when computationally feasible;
- formula overlap separately from structure overlap.

No final test molecule within the manuscript's frozen exclusion radius may remain in a structure-only corpus used to claim de novo generalization. The exclusion rule itself must be chosen before final test evaluation.

## 0.4 Freeze acquisition metadata authority

Use the ORBIT acquisition authority model already implemented in the codebase: metadata are **observed**, **default prior** or **missing**. Instrument/collision-energy/adduct strata are allowed in scientific analysis only when they are source-verifiable. Never convert a default prior into a measured stratum.

## 0.5 Freeze scientific snapshots by content digest

The current Protocol-v2 starting objects are suitable engineering anchors:

- evidence start: `plse-firstprinciples-v3`;
- hypothesis start: `meteor-rest-r199`;
- frozen candidate anchor: Legacy SFT-10;
- initial live candidate frontier: METEOR R199-10.

The manuscript may ultimately use later snapshots, but every reported snapshot must be identified by content/checkpoint digest, not by a mutable path or human-readable name alone.

## 0.6 Baseline reproducibility gate

Before a baseline enters a main figure, create a frozen environment/command record containing version, checkpoint, candidate-generation settings and score definition.

Core evidence comparators for Figure 2 should include:

1. exact-mass / formula-compatible simple scoring;
2. opportunity-normalized mass matching;
3. one global forward-spectrum similarity score;
4. **CFM-ID 4.x candidate ranking / predicted-spectrum similarity**;
5. one additional executable fragmentation-aware or learned forward comparator when a reproducible implementation/checkpoint is available;
6. pLSE ablations and full candidate-specific pLSE.

SIRIUS/CSI-derived scoring may be included when a reproducible candidate-level score can be extracted under identical candidate pools. Do not force a method into the main figure if the software interface does not support a fair same-pool comparison.

## 0.7 Primary statistical unit and inference

The molecule group is the primary unit for public benchmark claims. Repeated collision energies or spectra of one molecule are aggregated inside the molecule group before population inference.

Default inference for paired method comparisons:

- report molecule-group mean/median effect as appropriate;
- 10,000 molecule-group bootstrap resamples for a 95% confidence interval;
- paired sign-flip/permutation test for the preregistered primary endpoint when practical;
- correct only the small set of confirmatory primary comparisons, not every exploratory panel.

Do not use spectrum count as `n` when multiple spectra represent one molecule.

## 0.8 Artifact layout

Large raw data and checkpoints should remain in durable experiment storage, not in `MS-paper`. Every confirmatory run must nevertheless produce a small immutable manifest that can later be archived.

Recommended logical layout in the ORBIT project/output store:

```text
paper_v1/
  freeze/
    dataset_manifest.json
    split_manifest.json
    standardization_receipt.json
    pretraining_leakage_audit.json
    baseline_versions.json
    snapshot_digests.json
  fig1_evidence_bottleneck/
  fig2_candidate_evidence/
  fig3_spectral_identity/
  fig4_adaptation_transfer_resolution/
  fig5_mouse/
  fig6_active_acquisition/        # only if P6 is executed
```

Each figure directory should contain:

`config.json`, `input_manifest.json`, `scores.parquet`, `molecule_group_summary.csv`, `statistics.json`, `source_data.csv`, `run_receipt.json`.

The final `source_data.csv` for each main panel can later be copied into the paper repository.

---

# P1 — Figure 2 first: candidate-specific fragmentation evidence

## Scientific question

Does atom-traceable, competitor-relative fragmentation evidence discriminate the correct molecule from hard same-formula alternatives better than mass matching, global forward-spectrum agreement and non-candidate-specific fragmentation scoring?

This is the decisive viability experiment for the entire paper.

## P1.1 Freeze the exact evidence objects

Separate two quantities explicitly.

### Candidate-intrinsic peak support

For candidate `M_j` and observed peak `p`, define

```text
s_jp = best high-authority support that M_j can provide for p
```

using only the frozen reaction basis and information available to the deployed scorer. `s_jp` belongs to the spectrum–candidate pair and must not change merely because irrelevant candidates are added.

The implementation must record the winning trajectory and its evidence authority:

- reaction family;
- reaction centre;
- parent and product graph hashes;
- atom/component lineage;
- broken/formed/bond-order changes;
- formal-charge changes;
- charge carrier;
- explicit H/proton/hydride transfer when represented;
- theoretical ion mass and ppm/Da error;
- reaction/source provenance;
- search truncation flag.

### Candidate-relative peak specificity

For a frozen decision set `C`, derive the extent to which the supported peak distinguishes `M_j` from relevant competitors. The manuscript currently uses the target form

```text
d_jp = s_jp - max_{k != j} s_kp
```

but the **actual deployed implementation must be frozen before confirmatory evaluation**. Any opportunity correction and all coefficients/weights must be explicit.

Critical rule: because the reaction basis is incomplete,

```text
no generated trajectory != chemical contradiction
```

unless recall for that reaction/chemical regime has independently been validated to justify negative evidence.

## P1.2 Chemistry-validity gate before ranking

Before measuring ranking performance, validate that high-authority traces are chemically and computationally self-consistent.

Automated checks for every production trajectory:

1. atom lineage is complete for represented atoms;
2. elemental composition is conserved across parent/products after explicitly represented transfers;
3. formal charge and charge carrier are consistent with the recorded event;
4. hydrogen accounting closes whenever a proton/H transfer is claimed;
5. theoretical mass is recomputed from the product graph rather than copied from a target peak;
6. spectrum information is not used to invent a reaction centre before theoretical products are generated;
7. safety-cap/search truncation is reported separately from chemical impossibility.

Then create a chemistry audit set stratified by reaction family. For all reaction families that contribute materially to final discrimination, manually inspect a preregistered sample of trajectories and retain the full trace. The purpose is not to prove that every observed fragment follows one unique gas-phase mechanism; it is to verify that the computation does not claim a reaction-level authority it cannot replay.

**Gate P1-A:** no main-text mechanistic claim is allowed for a reaction family that fails conservation/replay audits.

## P1.3 Construct the hard-decoy benchmark

Use only validation/calibration data during development; reserve final test groups for the one-shot confirmatory run.

For each GT molecule:

1. identify all valid candidate structures satisfying the frozen precursor/formula rule;
2. create a primary **same-formula** candidate pool;
3. compute GT–decoy Morgan Tanimoto and MCES distance;
4. retain candidates from independent sources where possible (METEOR, external generator, database/retrieval);
5. construct a fixed primary pool size, recommended `K = 50` including GT when at least 49 valid decoys exist;
6. if a case has fewer than 49 same-formula decoys, keep it in a separately labelled smaller-pool stratum rather than silently padding with easy molecules;
7. record candidate-source provenance and generator rank before any pLSE score is seen.

Primary inferential subset: molecule groups with GT present and a sufficiently populated same-formula pool.

Secondary strata:

- high-similarity near isomers;
- shared-scaffold alternatives;
- local-connectivity alternatives;
- formula-compatible but structurally distant alternatives.

Use structural similarity continuously for inference; bins are mainly for visualization.

## P1.4 Run all evidence methods on the **same frozen candidate pools**

For every `(spectrum, candidate)` pair, collect:

- exact-mass/formula score;
- opportunity-normalized peak-mass score;
- global forward-spectrum similarity;
- CFM-ID candidate-ranking/spectral-similarity score;
- additional reproducible comparator if available;
- pLSE intrinsic support score;
- pLSE candidate-relative score;
- pLSE ablations.

Do not let any baseline generate an easier private candidate set for its own evaluation. Candidate generation and candidate scoring are separate experiments.

## P1.5 Required pLSE ablations

Run the following under identical pools:

1. mass-only matching;
2. mass matching + candidate-opportunity normalization;
3. generic structural reachability / graph-cut diagnostic score where scientifically appropriate;
4. reaction-centre eligibility without full trace authority;
5. + atom/formula conservation;
6. + charge-carrier accounting;
7. + explicit H/proton-transfer constraints where represented;
8. full high-authority trajectory support but candidate-isolated aggregation;
9. full candidate-specific aggregation.

This ladder distinguishes whether the gain comes from chemistry, bookkeeping, opportunity control or the competitor-relative evidence object.

## P1.6 Primary metrics

Report at molecule-group level:

1. **pairwise GT win rate** against all decoys in the frozen pool;
2. **normalized GT rank / reciprocal rank**;
3. **top-1 candidate accuracy conditional on GT being present**;
4. **false-strong rate** — fraction of molecule groups in which at least one decoy is scored above GT;
5. score margin `GT - best decoy`;
6. results restricted to same-formula and high-similarity subsets.

Do not make global explained peak intensity the primary endpoint. It is an explanatory secondary variable.

## P1.7 Candidate-pool-dependence stress test

Because specificity is decision-context dependent, explicitly test stability.

For the same GT and core hard neighbourhood:

- `C10`: GT + 9 nearest hard decoys;
- `C25`: preserve the same core and add decoys;
- `C50`: primary pool;
- `C100` or larger when available: append lower-priority formula-compatible decoys.

Measure:

- intrinsic support `s_jp` invariance;
- GT rank stability;
- candidate-relative score/rank correlation;
- whether adding easy irrelevant candidates changes the leading hard alternatives;
- whether removing the single strongest competitor changes only specificity, not claimed intrinsic support.

The manuscript must state explicitly that **support is pair-intrinsic whereas specificity is decision-context dependent**.

## P1.8 Discriminative evidence versus peak coverage

For each molecule group, decompose the final GT–decoy margin by observed peak.

Rank peaks by contribution to discrimination and calculate:

- fraction of total discriminative margin captured by top 1/3/5 peaks;
- fraction of total observed intensity represented by those peaks;
- global explained-intensity fraction for each method.

The desired scientific test is whether a small number of high-authority peaks can carry disproportionate structural information. This is exploratory until the exact decomposition is frozen; do not pre-specify a desired numerical outcome.

## P1.9 Case-study selection without cherry-picking

Predefine case eligibility before viewing final-test results:

- GT present in the frozen candidate pool;
- same-formula or high-similarity decoy exists;
- trace passes chemistry-validity gate;
- competing methods disagree or the case illustrates genuine ambiguity;
- reaction families are chemically distinct across selected cases.

Select illustrative cases only after the population result is frozen. State that examples are explanatory, not independent evidence. Publish the complete ranked case table in Extended Data/Supplementary material.

## P1.10 P1 go/no-go rule

**GO:** full candidate-specific pLSE improves the preregistered primary hard-decoy endpoint over the strongest non-candidate-specific comparator with a paired molecule-group CI excluding zero, and the gain is not explained solely by candidate opportunity or one reaction family.

**REVISE:** overall gain exists but disappears in the same-formula/high-similarity subset. Improve the evidence object before proceeding with a Nature-level story.

**NO-GO for current central claim:** candidate-specific evidence does not outperform strong simple/forward/fragmentation baselines on hard alternatives. Do not compensate by adding more agent or generator experiments.

Deliverable: `TBD:C2_candidate_specific_evidence`.

---

# P2 — Figure 1: establish a cross-model evidence bottleneck

## Scientific question

As molecular alternatives become more faithful, does the discriminative power of **multiple fixed evidence systems** systematically deteriorate even when candidate-set size and precursor constraints are controlled?

The goal is not to show the trivial statement that a manually selected similar molecule is harder than a dissimilar molecule. The goal is to show a reproducible regime shift across independent candidate sources and evidence systems.

## P2.1 Freeze candidate sources

Use at least three logically distinct sources when feasible:

1. multiple frozen METEOR snapshots/generations;
2. one independent peer-reviewed de novo generator with reproducible inference (for example DiffMS; add another only if access is reliable);
3. formula/mass-matched database or retrieval candidates independent of both generators.

External sources must be generated **without pLSE-guided sampling or reranking**.

## P2.2 Create matched difficulty datasets

For each molecule group and candidate source:

1. require GT inclusion for the discrimination analysis;
2. fix the candidate count `K` for the primary comparison;
3. hold the precursor/formula rule fixed;
4. compute structural difficulty independently of all evidence scores;
5. characterize nearest-decoy Tanimoto, MCES, same-formula status and scaffold relation;
6. use continuous hardness as the primary variable;
7. create easy/medium/hard visualization strata only after the continuous definition is frozen.

To demonstrate that the phenomenon is not a sampling artifact, create a matched analysis in which candidate pools at different difficulty levels have the same `K`, formula constraint and source-composition rule.

## P2.3 Frozen evidence systems

Evaluate at minimum:

- exact/simple mass-compatible score;
- global forward-spectrum similarity;
- CFM-ID ranking/similarity;
- initial frozen pLSE `E0`;
- another reproducible evidence system if available.

No evidence model may be retrained separately for each hardness stratum.

## P2.4 Primary analysis

For each evidence system, model/plot discrimination as a function of candidate hardness using molecule-group summaries.

Primary endpoints:

- pairwise GT win rate;
- normalized GT rank;
- GT-best-decoy margin;
- false-strong rate.

Primary phenomenon test: the within-method change/slope in discrimination as the nearest alternatives become structurally more faithful, with molecule-group bootstrap CIs.

Also test whether the trend persists in the strict same-formula subset and when candidate-source identity is included as a stratification variable.

## P2.5 Sensitivity analyses

Repeat with:

- `K = 10, 25, 50` where enough candidates exist;
- Morgan and MCES hardness definitions;
- excluding exact shared scaffolds versus restricting to them;
- removing each candidate source in turn;
- one spectrum per molecule versus aggregated repeated spectra.

## P2.6 P2 go/no-go rule

**GO:** a consistent loss of discrimination with increasing candidate fidelity is observed across multiple fixed evidence systems and independent candidate sources after matching the candidate construction.

**DOWNGRADE CLAIM:** only pLSE or only METEOR candidate populations show the trend. Then write it as an ORBIT-specific diagnostic, not a field-level evidence bottleneck.

Deliverable: `TBD:C1_evidence_bottleneck`.

---

# P3 — Figure 3: experimental spectrum versus chemical prior

## Scientific question

Does the decisive structural evidence depend on the identity of the measured spectrum, or can the same result be produced from chemical plausibility alone?

## P3.1 Freeze matched Chemical-World and Spectral-Reality records

For every paired experimental molecule:

- Chemical-World view: structure-derived proposal graph only; no invented observation/intensity labels;
- Spectral-Reality view: same structural prior plus the measured MS/MS and deterministic mass-compatible links.

The proposal backend/version must be identical between the two views.

## P3.2 Construct the three spectrum conditions

For every recipient molecule group:

1. **true spectrum** — its measured MS/MS;
2. **no spectrum** — preserve all non-spectral chemical/mass inputs but remove observed peak information;
3. **shuffled spectrum** — donor from another molecule group, matched on observed adduct and neutral mass within a preregistered window; additionally match peak count/complexity if needed to prevent an obvious shortcut.

The shuffled donor mapping is generated once and frozen before model scoring.

## P3.3 Evaluate two distinct endpoints

### METEOR hypothesis endpoint

- GT rank / likelihood under frozen candidate evaluation;
- same-formula ranking;
- candidate recall if free generation is part of the tested snapshot.

### pLSE evidence endpoint

- GT candidate-specific evidence;
- GT-best-decoy margin;
- amount of evidence classified as spectrum-specific versus shared chemical prior.

Define:

```text
spectral lift = true-spectrum endpoint - no-spectrum endpoint
identity lift = true-spectrum endpoint - shuffled-spectrum endpoint
```

Aggregate at molecule-group level.

## P3.4 Evidence-authority decomposition

For every explanation/trajectory used downstream, classify it as:

- high-authority and spectrum-supported;
- chemically possible but non-specific/shared;
- unsupported by the trace;
- beyond current evidence authority.

Quantify how much each category contributes to candidate discrimination.

## P3.5 Supporting CoT experiment

Keep the parent/pilot × normal/no-reasoning/shuffled-reasoning six-arm experiment as **Extended Data only**. It may support an implementation claim but must not define the manuscript's scientific novelty.

## P3.6 P3 go/no-go rule

**GO:** true-spectrum identity provides positive held-out lift over both no-spectrum and matched shuffled-spectrum controls on the central molecular/evidence endpoint.

**FAILURE MODE:** chemical-prior-only and shuffled-spectrum conditions perform similarly to the true spectrum. Then the model is not yet demonstrating spectrum-specific reasoning/evidence, regardless of how plausible its mechanisms look.

Deliverable: `TBD:C3_spectral_identity_lift`.

---

# P4 — Figure 4: reciprocal adaptation, transfer and risk-controlled structural resolution

## Scientific questions

1. Does adapting both hypothesis and evidence models help beyond adapting either side alone?
2. Is the evidence improvement transferable outside the opponent that created it?
3. Can uncertainty be converted into candidate sets with controlled empirical coverage rather than forced top-1 answers?

## P4.1 Freeze the four factorial snapshots

Select a frozen initial pair `(H0, E0)` and a frozen final pair `(HT, ET)` produced by the governed ORBIT process.

Evaluate all four combinations on the **same final held-out cases and candidate-construction rule**:

- `(H0, E0)` — frozen baseline;
- `(HT, E0)` — hypothesis adaptation only;
- `(H0, ET)` — evidence adaptation only;
- `(HT, ET)` — reciprocal final system.

The causal endpoint must not be the training reward. Use a held-out molecular endpoint such as candidate recall + conditional discrimination/end-to-end resolution.

Compute the interaction contrast:

```text
Delta_int = Y(HT,ET) - Y(HT,E0) - Y(H0,ET) + Y(H0,E0)
```

A positive interaction is the strongest support for synergy, but the paper should report the observed effect rather than requiring synergy by definition.

## P4.2 Equal-compute ungated control

Implement a blind/ungated alternation control with a matched number of update opportunities or comparable training/engineering budget.

The ungated control must not receive more test feedback than ORBIT. Compare:

- final held-out endpoint;
- frozen-anchor retention;
- non-target regression;
- false-strong rate;
- number of accepted/rejected/no-op changes;
- run-to-run stability.

Run independent ORBIT/ungated replicates when computationally feasible; target at least three independent runs for a dynamics claim.

## P4.3 Post-freeze cross-generation matrix

After all snapshots are frozen, evaluate

```text
A_ij = discrimination of evidence snapshot E_i on hypothesis frontier H_j
```

The matrix is descriptive evidence for challenge–recovery. It must not be used to choose or tune intermediate snapshots.

Retain rejected rounds in the ledger so the final figure does not present only successful adaptation steps.

## P4.4 External-transfer benchmark

Freeze external candidate sets that were never used to adapt pLSE. Recommended hierarchy:

1. an independent de novo generator (for example DiffMS);
2. formula-matched database/retrieval hard negatives;
3. a second independent generator if reproducibly accessible;
4. optional MIST/CSI-style retrieval candidates when candidate-level outputs can be frozen fairly.

For each source:

- canonicalize and deduplicate identically;
- record GT recall before scoring;
- evaluate `E0` and `ET` on the identical candidate pool;
- report overall, same-formula and near-isomer subsets;
- test whether evidence improvement transfers despite never seeing this generator during adaptation.

**Core claim requires improvement on more than one independent external candidate distribution; otherwise describe transfer narrowly.**

## P4.5 Separate generator recall from evidence discrimination

For every candidate source report three quantities:

### Candidate recall

```text
P(GT in C_K)
```

### Conditional structural resolution

Performance only among cases where GT is actually present in `C_K`.

### End-to-end resolution

Treat generator misses as end-to-end failures, not pLSE failures.

This decomposition is mandatory for Figure 4 and the mouse anchor analysis.

## P4.6 Split-conformal candidate sets

Do not call a simple tuned margin threshold “risk controlled”. Use a disjoint calibration split.

A concrete default construction for a frozen candidate pool is:

1. compute candidate scores `D_j` for each calibration molecule group;
2. define nonconformity of candidate `j` as `a_j = max_k D_k - D_j` (or another score frozen before calibration);
3. for each calibration group record `a_GT`;
4. compute the finite-sample split-conformal quantile `q_alpha` for target error level `alpha`;
5. on test, output

```text
C_hat_alpha = {j : max_k D_k - D_j <= q_alpha}
```

6. report conditional coverage **given GT is present in the generator pool**, median/mean set size and fraction of singleton sets;
7. separately report end-to-end coverage after generator misses are included.

Use target levels such as 90% and 95% only after freezing them in the analysis plan; do not select the level that looks best on test.

If exchangeability is materially violated across instruments/adducts, either calibrate on the intended deployment distribution or use stratified/Mondrian calibration only when each stratum has enough independent molecule groups.

## P4.7 P4 go/no-go rules

- **C4 supported:** reciprocal final system improves the held-out endpoint beyond both fixed-side adaptations; interaction effect is reported with CI.
- **C5 supported:** gated adaptation is more stable/non-regressive than ungated control and the post-freeze matrix shows challenge–recovery.
- **C6 supported:** `ET` improves over `E0` on genuinely external candidate distributions, especially same-formula/near-isomer subsets.
- **C7 supported:** conformal candidate sets meet the preregistered empirical coverage target within sampling uncertainty on final held-out data, with candidate recall reported separately.

If the interaction is null but both sides improve independently, downgrade “reciprocal synergy” to “complementary adaptation”; this does not invalidate Figures 1–3.

Deliverables: `TBD:C4_factorial_adaptation`, `TBD:C5_gated_challenge_recovery`, `TBD:C6_external_transfer`, `TBD:C7_risk_controlled_resolution`.

---

# P5 — Figure 5: independent private mouse deployment

## Scientific question

Can the frozen system narrow real unlabelled biological spectra without lowering the evidentiary standard for structural identification?

The mouse cohort is an **external deployment/discovery cohort**, not a substitute for public GT benchmarks.

## P5.1 Freeze the cohort before ORBIT inspection

Create an immutable manifest containing:

- raw-file names and hashes;
- animal/sample identifiers;
- biological replicate structure;
- tissue/condition metadata that existed before ORBIT analysis;
- instrument, polarity, acquisition mode and collision-energy metadata;
- blanks/QCs;
- preprocessing version;
- feature/spectrum identifiers.

No spectrum may enter the main paper merely because ORBIT produced an attractive structure.

## P5.2 QC and spectrum consolidation

Freeze rules for:

- blank subtraction;
- minimum precursor/fragment quality;
- chimeric/isolation contamination filtering when measurable;
- duplicate feature/spectrum merging;
- technical replicate consolidation;
- adduct assignment;
- recurrence across biological samples.

Retain raw and processed IDs so every displayed spectrum is traceable back to a raw acquisition.

## P5.3 Create blinded anchor and dark branches

### Anchor branch

Anchor spectra have independent reference support (library/reference/standard evidence) that can be hidden before ORBIT analysis.

Procedure:

1. define anchor eligibility before prediction;
2. hide the identity from candidate generation/scoring and from threshold calibration;
3. run the frozen pipeline;
4. reveal identity only after predictions and candidate sets are written;
5. report candidate recall, conditional discrimination, conformal set coverage and end-to-end resolution;
6. compare with applicable established annotation methods.

### Dark branch

Dark spectra have no accepted exact spectral-library annotation under one frozen search protocol.

“Dark” means unannotated spectrum, not necessarily a molecule absent from PubChem/HMDB.

## P5.4 Do not hide formula uncertainty

For mouse spectra, do not silently provide the true formula as an oracle.

Create two clearly separated analyses:

### Controlled structure-resolution track

Use spectra for which a formula is independently supported at the manuscript's predefined confidence level. This track isolates structure discrimination within a formula.

### End-to-end track

Propagate formula uncertainty:

1. run the selected formula inference method(s) (for example SIRIUS/BUDDY or another frozen pipeline);
2. retain top formula hypotheses under a preregistered rule rather than forcing one if uncertainty is substantial;
3. generate candidates across retained formulas;
4. report formula recall on anchors separately from structure discrimination;
5. for dark spectra, preserve formula ambiguity in the final evidence dossier.

This prevents an unreported formula oracle from inflating mouse structure-resolution claims.

## P5.5 Frozen dark-spectrum pipeline

For each high-quality dark spectrum:

1. infer/retain plausible formula set;
2. generate/retrieve molecular candidates without using dark outcomes to modify METEOR or pLSE;
3. deduplicate/standardize candidates;
4. compute pLSE intrinsic support and candidate-specific evidence;
5. produce a calibrated candidate set when the calibration assumptions are applicable;
6. record remaining unresolved structural alternatives;
7. map candidate-specific evidence to observed peaks and replayable trajectories;
8. quantify recurrence of the spectrum/evidence pattern across independent mouse samples.

Output one evidence dossier per feature containing:

`feature_id, precursor/adduct, formula hypotheses, candidate set, candidate scores, high-authority peaks, trajectories, unresolved alternatives, recurrence, annotation level, validation status`.

## P5.6 Case-study prioritization before orthogonal validation

Freeze prioritization criteria before ordering standards or performing targeted follow-up:

- recurrent across independent samples or otherwise scientifically prioritized before structure revelation;
- no accepted exact library hit;
- manageable residual candidate set;
- at least one high-authority candidate-specific trajectory;
- complete alternative-candidate dossier;
- enough remaining sample/material for validation where relevant.

Prioritize both a potentially resolvable case and an intentionally ambiguous case. The paper should show that ORBIT can say “insufficient evidence”.

## P5.7 Orthogonal validation hierarchy

Strong structure-level identification should use, where feasible:

1. authentic/synthetic standard with matching MS/MS;
2. retention/coelution agreement;
3. targeted MSn evidence;
4. NMR or another comparably strong orthogonal route when material permits.

A blinded independent library reveal can validate an anchor but should not be described as prospective discovery of a new structure.

Database occurrence, biological plausibility or recurrence alone support a hypothesis but do not upgrade it to standard-confirmed identification.

## P5.8 Mouse reporting outcomes

Every dark feature must end in one of the following, not a forced SMILES:

- unresolved;
- formula only;
- class/structural family;
- bounded candidate set;
- unique high-confidence 2D hypothesis;
- orthogonally confirmed structure.

Never merge the last two levels.

## P5.9 P5 go/no-go rules

**C8 supported:** blinded anchors demonstrate usable external-domain candidate recall/discrimination/calibration and the dark analysis is executed without adapting the model to the cohort.

**C9 strong:** multiple prioritized dark hypotheses receive orthogonal evidence, or unresolved cases are explicitly retained without claim inflation.

If no dark case has orthogonal validation, Figure 5 remains a strong deployment/candidate-contraction figure but should not claim discovery of identified metabolites.

Deliverables: `TBD:C8_mouse_deployment`, `TBD:C9_mouse_validation`.

---

# P6 — Nature-main-track extension: evidence-guided new measurement

## Scientific question

When MS2 leaves several plausible structures unresolved, can ORBIT identify an additional mass-spectrometric measurement that is predicted **before acquisition** to distinguish the surviving candidates and then demonstrate candidate-space contraction after the new measurement is collected?

This is the preferred route from adaptive evidence interpretation to true hypothesis–experiment co-design.

## P6.1 Retrospective development before prospective mouse use

Develop the selection policy on public MSn data only. Use a benchmark/source with measured fragmentation trees or higher-order spectra (for example a frozen MSn benchmark if adopted by the project).

For each case:

1. expose only the MS2 observation and candidate set to the selector;
2. hide the measured MS3+ branch used as the retrospective outcome;
3. identify residual candidate pairs/sets after MS2;
4. enumerate experimentally feasible next measurements available in the dataset (precursor fragment/branch and, where represented, collision-energy condition);
5. score each possible acquisition by predicted candidate separation;
6. select one action without seeing the hidden outcome;
7. reveal the corresponding measured MSn data;
8. re-score candidates and quantify set-size/rank reduction.

## P6.2 Acquisition utility without pretending to know reaction probabilities

Until empirical fragment probabilities are calibrated, do not use an overconfident expected-information formula based on invented probabilities.

A conservative default utility can use the **predicted partition of surviving candidates by high-authority descendant evidence**. For an action `a`, compute how strongly candidate predictions disagree under the current chemistry/evidence model and favour actions that split the largest hard-candidate groups while remaining experimentally observable.

Possible deterministic utility terms:

- minimum pairwise separation among surviving candidates;
- expected/worst-case residual candidate-set size under equal candidate weights;
- number of candidate pairs with distinct high-authority predicted descendants;
- observability/practicality gate based only on measured precursor intensity and instrument constraints.

Freeze the utility before prospective testing.

## P6.3 Baseline acquisition policies

Compare against:

- random feasible fragment selection;
- highest-intensity fragment selection;
- most commonly fragmented/heuristic branch;
- optional forward-model uncertainty/disagreement selection.

Primary endpoint: reduction in calibrated candidate-set size or increase in GT separation after the revealed/acquired next measurement, with GT recall tracked separately.

## P6.4 Prospective mouse case

Only after the retrospective selector is frozen:

1. choose a dark/anchor-like mouse spectrum that remains unresolved after MS2 and satisfies sample/instrument feasibility;
2. freeze its candidate set and evidence dossier;
3. preregister the selected next MSn/CE action and baseline alternatives;
4. acquire the new spectrum without changing the selector;
5. process it with the frozen pipeline;
6. measure candidate-space contraction;
7. where possible, confirm the final candidate with authentic standard/RT or another orthogonal route.

The strongest closing chain is:

```text
MS2 -> several plausible candidates -> ORBIT selects missing evidence -> new MSn measurement -> one/smaller candidate set -> orthogonal confirmation
```

## P6.5 P6 claim gate

C10 is supported only if the experiment is selected **before** observing the new outcome and the new measurement produces measurable held-out candidate-space contraction beyond baseline acquisition policies.

A retrospective-only MSn result is still valuable but must be described as retrospective validation, not prospective autonomous discovery.

Deliverable: `TBD:C10_active_acquisition`.

---

# 1. Final test unlock checklist

The official final test may be opened only after all items below are true:

- [ ] dataset version and hashes frozen;
- [ ] molecule-group split frozen;
- [ ] standardization and leakage audit frozen;
- [ ] candidate-generation settings frozen;
- [ ] all main baselines reproduce on validation;
- [ ] pLSE reaction basis frozen;
- [ ] pLSE candidate-specific score equation/implementation frozen;
- [ ] primary metrics and statistical tests frozen;
- [ ] candidate-pool sizes and hardness definitions frozen;
- [ ] correct/no-spectrum/shuffled-spectrum mapping frozen;
- [ ] H0/E0/HT/ET snapshot digests frozen;
- [ ] conformal nonconformity score and target coverage levels frozen;
- [ ] figure scripts consume only frozen source tables;
- [ ] no official-test metric has been used to authorize an intervention.

If any item changes after test reveal, the change must be documented and the affected result cannot be presented as a clean one-shot confirmatory test without an independent untouched set.

---

# 2. Minimal execution order and resource priority

## Priority A — must do before spending on the rest

1. P0 freeze infrastructure.
2. P1 chemistry validity audit.
3. P1 same-formula hard-decoy benchmark.
4. P1 external baselines and candidate-pool robustness.

**Decision:** if Figure 2 is not strong, improve pLSE rather than launching more ORBIT rounds.

## Priority B — establish the paper's field-level proposition

5. P2 cross-generator/cross-evidence bottleneck.
6. P3 spectrum/no-spectrum/shuffled-spectrum experiment.

## Priority C — establish adaptation rather than one strong scorer

7. P4 factorial `H/E` experiment.
8. gated versus ungated/equal-budget control.
9. external candidate transfer.
10. split-conformal candidate sets.

## Priority D — real-world closing evidence

11. freeze and QC mouse cohort.
12. blinded anchor analysis.
13. dark-spectrum candidate contraction.
14. orthogonal validation of prioritized cases.

## Priority E — Nature-main-track upgrade

15. retrospective MSn acquisition selector.
16. prospective mouse MSn/CE ambiguity-resolution case if material/instrument access permits.

---

# 3. Figure-to-artifact contract

| Figure | Core artifact | Minimum content before manuscript number replacement |
|---|---|---|
| Fig. 1 | `C1_evidence_bottleneck` | matched candidate pools; >=2 independent candidate sources; multiple frozen evidence systems; molecule-group slope/effect statistics |
| Fig. 2 | `C2_candidate_specific_evidence` | frozen pLSE equation/implementation; chemistry audit; strong external/simple baselines; same-formula results; ablations; pool-dependence stress |
| Fig. 3 | `C3_spectral_identity_lift` | true/no/shuffled spectrum arms; frozen donor map; spectral/identity lift; evidence-authority decomposition |
| Fig. 4 | `C4-C7` bundle | factorial H/E controls; ungated control; post-freeze matrix; external transfer; generator recall decomposition; conformal candidate sets |
| Fig. 5 | `C8-C9` bundle | frozen mouse manifest/QC; blinded anchors; dark candidate contraction; recurrence; validation dossiers and explicit unresolved cases |
| Nature extension | `C10_active_acquisition` | hidden-outcome MSn development; frozen selector; baseline policies; prospective acquisition if feasible |

---

# 4. Failure taxonomy to report rather than hide

Every final error should be assigned, where possible, to one layer:

1. **formula failure** — correct formula not retained;
2. **candidate-coverage failure** — GT absent from generated/retrieved candidate pool;
3. **evidence-ranking failure** — GT present but scored/ranked below decoys;
4. **observation-limited ambiguity** — GT and alternatives remain indistinguishable under high-authority MS2 evidence;
5. **chemistry-basis failure** — potentially discriminative fragment not represented by the current reaction basis;
6. **search/truncation failure** — chemistry may be reachable but computation hits explicit safety/search limits;
7. **domain-shift failure** — performance/calibration degrades by instrument/adduct/sample domain;
8. **validation gap** — dark hypothesis cannot be elevated because orthogonal evidence is unavailable.

This taxonomy should appear in Extended Data because it demonstrates where future progress is actually required and prevents all errors from being attributed vaguely to “the model”.

---

# 5. Manuscript language gates tied to experiments

Use strong wording only after the corresponding experiment is complete:

- **“evidence bottleneck”** — only after P2 shows cross-source, cross-evidence-system deterioration;
- **“candidate-specific fragmentation evidence”** — only after P1 freezes the score and shows hard-decoy benefit;
- **“spectrum-grounded”** — only after P3 true-spectrum > no-spectrum and shuffled-spectrum controls;
- **“reciprocal adaptation”** — factual description of the protocol; **“synergy”** only if the factorial interaction supports it;
- **“transferable evidence improvement”** — only after P4 external candidate sources improve;
- **“risk-controlled”** — only after an actual conformal/risk-control procedure is used; otherwise write “calibrated selective resolution”;
- **“resolved mouse structure”** — only at the confidence level supported by the mouse validation hierarchy;
- **“identified metabolite”** — only with orthogonal evidence meeting the frozen identification standard;
- **“co-evolving experimental evidence” / “adaptive evidence acquisition”** — only after P6 obtains a new measurement selected before observing the outcome.

---

# 6. Definition of a submission-ready experiment package

A result is ready to replace a manuscript placeholder only when all of the following exist:

1. immutable input manifest;
2. exact code commit and environment/version receipt;
3. model/evidence snapshot digests;
4. frozen candidate pools;
5. raw per-candidate/per-spectrum score table;
6. molecule-group aggregation table;
7. statistical output with confidence interval and test;
8. failure/exception table including timeouts and search truncation;
9. plot source-data table;
10. one short text file stating the exact claim the artifact supports and what it does **not** support.

The goal is that every number in `main.tex` can be traced to one reproducible artifact without consulting a transient training log or reconstructing an analysis from memory.
