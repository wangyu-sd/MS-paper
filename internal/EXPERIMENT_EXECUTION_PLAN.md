# Experiment Execution Plan

The manuscript now depends on a two-stage proof:

1. **Paradigm/capability:** a shared molecular fragmentation World must support useful Free, Guided and Inverse inference and produce stronger evidence than direct ranking.
2. **Discovery:** that evidence hierarchy must resolve enough dark chemistry at scale to reveal structural and biological organization.

Execution is ordered by what can invalidate this combined Nature story earliest.

---

# Phase 0 — Freeze system semantics and data boundaries

## E0.1 Canonical WGV release
Freeze the exact PR81-derived system used for all manuscript experiments:
- World state schema;
- explicit atom/H/charge/electron/exact-mass semantics;
- charged + neutral component bookkeeping;
- sparse electron-flow action language;
- ionization ensemble;
- Free/Guided/Inverse task conditions;
- action masks and typed chemistry compiler;
- model sizes/checkpoints;
- inference budgets;
- code commit hashes.

No later manuscript result may silently switch action/state semantics.

## E0.2 Data splits
Freeze:
- molecule-disjoint training/calibration/test partitions;
- public library snapshots;
- repository dark corpus;
- mouse cohort;
- perturbation cohorts.

## E0.3 Leakage audit
Audit exact structures and close analogues against:
- molecular pretraining;
- spectral training;
- synthetic/simulated spectra;
- route/action supervision;
- candidate libraries.

## E0.4 Observation contract
Freeze what counts as:
- observed mass;
- observed intensity;
- ordered parent→child transition;
- unobserved/unlabeled;
- negative evidence.

The default rule is:
[
	ext{unobserved World state} 
eq 	ext{false state}.
]

---

# Phase 1 — WGV paradigm gates

These experiments decide whether the paper can lead with a fragmentation-world paradigm.

## E1 — World versus direct spectrum prediction

Compare the learned multibranch World against a direct structure→spectrum baseline under matched molecule-disjoint data and compute.

Primary World endpoints:
- observed mass coverage;
- intensity-weighted coverage;
- ordered-transition coverage;
- multistage-added coverage;
- probability conservation;
- coverage-vs-expanded-states AUC.

Direct predictor endpoints:
- conventional spectral similarity;
- peak/intensity metrics where applicable.

The purpose is not to force one metric across incompatible outputs. Test whether representing the latent reaction world yields additional experimentally testable structure that direct prediction cannot provide.

**Gate:** the World must add meaningful transition/path-level explanatory power while maintaining competitive spectral observation quality.

---

## E2 — Multi-branch versus single-path World

Same transition model; same compute budget.

Compare:
- full sibling expansion + branch-local STOP + reconvergent flow;
- greedy/single-child rollout;
- optional beam-like path baseline.

Primary endpoints:
- observed mass/intensity coverage;
- ordered-transition coverage;
- number of experimentally supported sibling branches;
- censored frontier mass;
- probability-flow conservation.

**Gate:** the multibranch representation must provide measurable value beyond a single mechanism/path story.

---

## E3 — Chemical legality audit

Challenge the state/action system with:
- random legal actions;
- deliberately invalid mass/formula/charge/valence/H actions;
- forward/inverse round trips;
- neutral coproduct retention;
- H-group compression equivalence;
- canonical inverse-state merge.

Report:
- atom conservation;
- electron conservation;
- charge conservation;
- exact-mass conservation;
- formula/H closure;
- RDKit/materialization success;
- inverse round-trip identity where defined.

**Gate:** hard chemistry violations must be rejected by the action/compiler layer rather than learned statistically.

---

# Phase 2 — Free / Guided / Inverse scientific capability

## E4 — Free World evaluation

Run the frozen Free World on a molecule-disjoint held-out cohort.

Report:
- case-level and transition-level coverage;
- intensity-weighted coverage;
- multistage contribution;
- calibration/NLL/Brier/ECE of branch/STOP probabilities where supported;
- compute/throughput;
- action-space ceiling separately from realized-network coverage.

Do not use target spectrum as policy input.

---

## E5 — Guided matched-budget comparison

Free and Guided use:
- identical molecule;
- identical chemistry/action space;
- identical maximum expansions/wall time.

Only Guided receives the target spectrum.

Primary endpoints:
- intensity-weighted coverage-vs-budget AUC;
- ordered-transition coverage;
- states needed to reach matched coverage;
- coherent explanatory path coverage;
- wall time.

Ablations:
- no DAgger;
- no goal conditioning;
- weak mean frontier summary versus Set Transformer;
- greedy versus value-guided expansion.

**Gate:** Guided must improve explanation or compute efficiency under matched resources.

---

## E6 — Inverse molecule recovery

Molecule-disjoint evaluation.

Report:
- chemical validity;
- formula validity;
- Exact@1/@5/@10 or Recall@K;
- best Tanimoto/MCES@K;
- posterior diversity;
- number of unique canonical states;
- SMC ESS / collapse diagnostics;
- runtime.

Compare against:
- direct de novo model where executable;
- retrieval-only baseline;
- construction without World guidance;
- no forward-replay baseline.

**Gate:** Inverse must recover a useful diverse posterior, not merely valid molecules.

---

## E7 — Bidirectional structure evidence

Construct matched GT + hard-decoy candidate pools.

For every candidate:
[
S ightarrow M ightarrow mathcal W(M) ightarrow hat S.
]

Measure:
- World forward likelihood/flow;
- mass coverage;
- intensity coverage;
- parent-child path support;
- candidate-specific discriminative evidence;
- cycle/bidirectional consistency.

Stratify:
- same formula;
- near isomers;
- same scaffold;
- remote decoys.

**Gate:** stronger bidirectional evidence must separate GT from hard alternatives beyond mass/formula compatibility alone.

---

# Phase 3 — Evidence hierarchy and credibility

## E8 — Freeze evidence levels

Before repository-scale analysis, freeze definitions for:

1. mass/formula compatible;
2. chemically valid candidate;
3. World-reachable;
4. executable path support;
5. candidate-specific evidence;
6. bidirectional consistency;
7. calibrated bounded statement;
8. authentic-standard confirmation.

Do not tune these levels on the dark corpus.

---

## E9 — Reliability by evidence level

On known-structure cohorts, measure:
- true-structure containment;
- exact recovery;
- calibration;
- candidate-set size;
- structural-distance error;

as a function of evidence level.

Primary claim:
[
	ext{stronger evidence level} Rightarrow 	ext{higher structural reliability}
]
with explicit coverage trade-offs.

---

## E10 — Prospective library-growth validation

Reconstruct historical GNPS/MassBank/MoNA snapshot.

Eligibility:
- dark/unannotated at freeze;
- structure first deposited later;
- no exact or close analogue available at freeze;
- depositing group independent of this work.

Freeze WGV and calibration before revealing outcomes.

Report:
- containment;
- calibration error;
- structural-distance stratification;
- evidence-level distribution;
- comparator calibration.

This is the main external credibility experiment.

---

# Phase 4 — Repository-scale dark-matter resolution

## E11 — Frozen dark-corpus inference

Run the frozen WGV pipeline over all eligible dark spectra.

For every spectrum record:
- strongest evidence level reached;
- bounded structural statement;
- surviving candidates;
- World paths/receipts;
- confidence;
- compute/censoring status.

Headline output is an **evidence-level funnel**, not one annotation rate.

---

## E12 — Entity collapsing

Freeze and validate:
- adduct collapse;
- isotope collapse;
- charge-state collapse;
- in-source-fragment handling;
- redundant acquisition collapse.

Measure over-/under-merging on known compounds and propagate uncertainty into dark-entity counts.

---

## E13 — Recurrence

Define independent dataset/laboratory units.

For every high-evidence entity/family:
- recurrence count;
- independent dataset count;
- organism/tissue breadth where appropriate.

Technical spectra are never independent replicates.

---

## E14 — Evidence × recurrence interaction

Test whether recurring dark chemistry tends to achieve stronger evidence than singletons.

This can strengthen the resource claim by showing that the most reproducible dark signals are also the most structurally resolvable.

---

# Phase 5 — Structural organization of resolved dark chemistry

## E15 — Freeze known-metabolite reference space

Freeze characterized metabolites, structural standardization and distance metrics.

## E16 — Freeze near-known boundary

Predefine:
- structural-distance threshold(s);
- allowed transformation vocabulary;
- handling of bounded isomer/class statements.

## E17 — Global structural landscape

Build structure-based graph/embedding over:
- characterized metabolites;
- high-evidence recurrent dark entities.

Quantify:
- nearest-known distance;
- local density;
- family size;
- recurrence;
- evidence level.

## E18 — Near-known versus remote families

Report:
- near-known halo fraction;
- remote recurrent family fraction;
- insufficient-resolution fraction.

Use sensitivity analyses across reference sets/metrics.

## E19 — Representative remote families

Select by frozen combination of:
- evidence strength;
- recurrence;
- distance from known chemistry;
- family size.

Do not select based on biological significance.

---

# Phase 6 — Biological-source organization

## E20 — Public perturbation inventory

Manually verify mouse datasets containing:
- germ-free/gnotobiotic contrasts;
- antibiotics;
- defined diet perturbation.

Freeze sample manifests and study metadata.

## E21 — Positive-control gate

Known source-dependent metabolites must recover expected perturbation directions.

Include:
- label permutation;
- study permutation where appropriate;
- between-study heterogeneity.

## E22 — Family source dependence

Using structural families frozen in Phase 5, classify:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed;
- unresolved.

## E23 — Structure–source coupling

Test:
- local source-label autocorrelation on structural graph;
- motif/class enrichment;
- cross-study effect consistency;
- permutation null.

This is the main Figure 4 inferential endpoint.

---

# Phase 7 — Biological value of structural families

## E24 — Freeze contrasts and family membership

Before outcome analysis:
- hash family membership;
- freeze eligible biological contrasts/cohorts;
- pre-register one primary global endpoint.

Preferred primary endpoints:
- cross-cohort replication rate;
- effect-sign concordance.

## E25 — Paired feature-versus-family test

Same samples, preprocessing and covariates.

Arm A:
anonymous dark features.

Arm B:
frozen structural families.

Report:
- primary endpoint;
- replication;
- sign concordance;
- multiplicity-controlled association yield;
- effect stability.

**Gate:** structural-family analysis must show a systematic advantage; one cherry-picked family is insufficient.

## E26 — Principal programme

Only after E25 is frozen, select a family satisfying:
- high evidence;
- recurrence;
- replicated biological effect;
- robust family membership.

## E27 — Replication / sensitivity

Require:
- independent cohort or leave-one-cohort-out;
- metadata permutation;
- confidence/evidence threshold sensitivity;
- family-definition perturbation sensitivity.

---

# Phase 8 — Orthogonal anchors

## E28 — Freeze anchor-selection rule
Commercially available structures only.

## E29 — Authentic-standard validation
Report:
- precursor;
- MS/MS;
- retention/coelution;
- pass/fail;
- remaining alternatives.

Failures stay in the denominator.

## E30 — Explicit unresolved dossier
For at least one representative high-evidence case:
- surviving isomers;
- evidence eliminating the rest;
- why current data cannot separate survivors;
- predicted next measurement.

---

# Parallel outer-loop agent track

The MS-agent may improve:
- World state representation;
- action language;
- training objective;
- search/planning;
- candidate construction;
- observation model.

But every proposal must pass:
1. typed compilation;
2. conservation tests;
3. local causal replay;
4. molecule-disjoint paired gate;
5. full held-out scientific KPI gate.

Agent activity is not itself a paper endpoint.

---

# Critical path

[
E0 ightarrow (E1,E2,E3) ightarrow (E4,E5,E6,E7)
ightarrow (E8,E9,E10)
ightarrow E11	ext{--}E14
ightarrow E15	ext{--}E19
ightarrow E20	ext{--}E23
ightarrow E24	ext{--}E27
ightarrow E29.
]

The paper should not begin full dark-corpus biological interpretation before the evidence hierarchy is frozen.

---

# Standing execution rules

1. One World, three conditional inference modes.
2. Free never reads the target spectrum.
3. Chemistry legality is hard-constrained.
4. Unobserved is not automatically negative.
5. Compute budgets are censoring, not chemical depth.
6. Candidate recall and evidence quality are separate.
7. Evidence levels are frozen before dark-corpus analysis.
8. Biological families are frozen before phenotype/source testing.
9. Negative results remain in denominators.
10. No training-log number becomes a scientific claim without frozen held-out evaluation.
