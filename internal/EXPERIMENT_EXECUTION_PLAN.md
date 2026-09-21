# Experiment Execution Plan

Execution is ordered by **what can invalidate the Nature story earliest and cheapest**, not by manuscript order.

The current paper requires four independent scientific pillars:

1. bounded structural measurement is trustworthy;
2. feature counts collapse to a defensible structural census;
3. recurrent dark chemistry has non-trivial global organization;
4. structural-family analysis exposes reproducible biology.

If any pillar fails, reframe before spending heavily downstream.

---

## Phase 0 — Freeze definitions and inventory

### E0.1 Library snapshots
Reconstruct GNPS/MassBank/MoNA at a historical freeze date and at the evaluation date. Record per-structure first appearance, accession and depositing group.

### E0.2 Corpus inventory
Freeze manifests for repository spectra, mouse spectra, benchmark/calibration sets and all public perturbation cohorts. Record raw-file hashes, sample identities, acquisition metadata and preprocessing versions.

### E0.3 Leakage audit
Audit exact-structure and close-analogue overlap between all evaluation chemistry and:
- molecular pretraining corpora;
- spectrum-model training corpora;
- simulator-generated training data;
- candidate libraries available at the freeze date.

### E0.4 Dark-subset definition
Freeze the exact spectral-library search protocol and threshold that define “dark”. Validate false accepted library hits on known spectra.

### E0.5 Structural-entity definition
Before viewing dark-atlas counts, freeze rules for:
- adduct collapse;
- isotope collapse;
- charge-state collapse;
- in-source-fragment handling;
- redundant acquisition collapse;
- merging by unique structure / bounded isomer set / shared structural statement.

---

# Phase 1 — Three go/no-go experiments

## E1 — Soundness–resolution curve
On leakage-controlled known-structure spectra with matched candidate pools, sweep the structural-elimination operating point.

Report:
- false exclusion of the true structure;
- unique/isomer-set/class/formula/unresolved fractions;
- candidate recall separately from conditional evidence performance;
- sensitivity to mass tolerance, noise peaks and acquisition metadata.

**Pass condition:** a practically useful fraction of spectra can be resolved above formula while keeping false exclusion low enough to support a resource. Do not hard-code a favourable threshold after looking; freeze the selected operating point from the calibration set.

**Failure:** replace elimination-defined outputs with calibrated/conformal candidate sets and rewrite Figure 1.

---

## E2 — Prospective-set constructibility
Construct the historical-library-growth cohort:
- dark under the freeze snapshot;
- structure first deposited after freeze;
- no exact or close analogue available at freeze;
- depositing group independent of this work.

Report count, chemical coverage and structural-distance distribution.

**Pass condition:** large/diverse enough to estimate prospective containment and calibration with meaningful confidence intervals.

**Failure:** prospective validation becomes supporting rather than headline credibility; use scaffold-disjoint held-out evaluation and explicitly weaken claims.

---

## E3 — Entity-collapsing validity
Run the proposed feature-to-entity pipeline on known compounds for which multiple adducts, isotopologues, charge states, in-source fragments and replicate acquisitions are available.

Primary endpoints:
- over-merging rate;
- under-merging rate;
- entity-count bias;
- uncertainty propagation from collapsing error.

**Pass condition:** collapsing error is low enough that the final census interval is scientifically informative.

**Failure:** do not report a headline “number of dark molecules”; restrict the paper to structural-family organization.

---

# Phase 2 — Figure 1: credibility of structural statements

## E4 — Matched-pool structural discrimination
Identical spectra and candidate pools for:
- exact precursor/formula matching;
- forward-spectrum similarity;
- CFM-ID;
- SIRIUS/CSI:FingerID or executable comparable system;
- ORBIT-MS structural statement pipeline.

Report same-formula and near-isomer strata separately.

## E5 — Spectrum-identity controls
Correct spectrum / matched shuffled spectrum / no-spectrum control with chemical priors fixed.

## E6 — Prospective validation
Freeze model, fragmentation World/rules, candidate generator, calibration mapping and evaluation code before revealing E2 outcomes.

Report:
- containment versus stated confidence;
- calibration error;
- performance by structural distance from freeze chemistry;
- chemical class, instrument and collision energy strata.

## E7 — Comparator calibration
Give each comparator a fair calibration mapping fitted only on its calibration set, then evaluate on the identical prospective cohort.

## E8 — Worked evidence cases
Preselect cases by frozen difficulty criteria, not aesthetic appeal:
- one unique-resolution success;
- one bounded-isomer outcome;
- one failure/unresolved outcome.

---

# Phase 3 — Figure 2: structural census

## E9 — Repository and mouse dark-subset run
Run the frozen structural pipeline over the complete eligible dark corpora. No phenotype/source labels may be exposed to candidate selection or entity definition.

## E10 — Feature-to-entity collapse
Apply the frozen E0.5 rules. Propagate E3 error into a confidence interval for total entity count.

Primary outputs:
- dark feature/spectrum count;
- structurally usable statement count;
- distinct structural entity count;
- feature-to-entity contraction factor.

## E11 — Recurrence
For every entity/family, count recurrence across **independent datasets**, not spectra.

Audit:
- shared samples;
- duplicated datasets;
- same laboratory re-depositions;
- technical replicates.

## E12 — Resolution-depth census
Partition the recurrent census into:
- unique putative structures;
- bounded isomer sets;
- substructure/classes;
- formula-only;
- unresolved.

Never relabel the first category as confirmed identification.

---

# Phase 4 — Figure 3: chemical organization

## E13 — Freeze reference metabolite space
Freeze the characterized-metabolite reference set before calculating dark-space distance.

## E14 — Freeze near/remote definition
Predefine:
- structural-distance metric(s);
- permitted interpretable transformation vocabulary;
- threshold defining the “near-known halo”.

Run sensitivity with at least one independent structural-distance definition.

## E15 — Global structural landscape
Build a structural relationship graph / embedding for recurrent entities and characterized metabolites using structural information, not only spectral embeddings.

Quantify:
- density and family-size distributions;
- nearest-reference distance;
- recurrence as a function of distance;
- uncertainty as a function of structural resolution.

## E16 — Near-known versus remote census
Primary Figure 3 headline:
- fraction in near-known halo;
- fraction in remote recurrent families;
- fraction excluded because resolution is insufficient to assign a precise distance.

## E17 — Chemical-class composition
Compare recurrent dark chemistry with reference libraries. Stratify/sensitivity-test by acquisition mode where possible.

## E18 — Remote recurrent families
Freeze ranking criteria based on recurrence and resolution before selecting representative families for the main figure.

## E19 — World/program coverage analysis
Measure how World/action/program evolution changes coverage across chemical classes and whether the gain transfers to the census. Keep this in ED6 unless it changes a headline scientific count.

---

# Phase 5 — Figure 4: biological-source organization

## E20 — Perturbation-dataset assembly
Identify public mouse datasets with:
- germ-free/gnotobiotic controls;
- antibiotic perturbation;
- defined dietary perturbation.

Every accession must be manually verified against the associated publication.

## E21 — Positive-control gate
Known metabolites with established perturbation dependence are processed through the identical harmonization/attribution pipeline.

Require:
- correct effect direction/recovery;
- label-permutation null;
- acceptable between-study heterogeneity.

Interpret no dark family before this passes.

## E22 — Family source attribution
Using frozen structural families from Phase 4, classify evidence as:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed;
- unresolved.

Model study/platform/batch explicitly.

## E23 — Structure–source coupling
Test whether source assignments are non-randomly organized over structural space:
- motif/class enrichment;
- local source-label autocorrelation;
- cross-dataset effect consistency.

This is the central Figure 4 result, not the raw category count.

---

# Phase 6 — Figure 5: global biological value

## E24 — Freeze biological contrasts and family definitions
Before any feature-versus-family comparison:
- hash family membership;
- pre-register eligible cohorts/phenotypes;
- select the primary global comparison metric.

Preferred primary endpoints:
- cross-cohort effect-sign concordance;
- independent replication rate;
- family-level multiplicity-controlled association yield.

Use one primary endpoint and treat the others as secondary.

## E25 — Feature-versus-family global comparison
Run the same biological data twice:
1. anonymous spectral features;
2. frozen structural families.

Do not change preprocessing, samples or covariates between arms.

This is a paired analysis. Report the distribution across all eligible families/contrasts, not only positive examples.

## E26 — Principal biological programme
Only after E25 is frozen, select the strongest pre-defined family meeting:
- recurrent structural membership;
- independent-cohort replication;
- acceptable structural confidence;
- biological effect robustness.

## E27 — Independent replication and sensitivity
Require:
- independent cohort or dataset;
- leave-one-cohort-out analysis;
- metadata permutation;
- confidence-threshold sensitivity.

## E28 — Standard-anchor selection
Freeze anchor criteria before purchase. Restrict to commercially available compounds.

## E29 — Orthogonal validation
For every selected anchor, report:
- precursor mass;
- MS/MS match;
- retention/coelution;
- alternative structures;
- success or failure.

Failures stay in the denominator.

## E30 — Explicit unresolved case
For at least one family member, show:
- surviving isomers;
- evidence eliminating all others;
- why current data cannot separate survivors;
- specific additional measurement predicted to resolve them.

---

# Parallel engineering track — does not define the paper's scientific chronology

The ORBIT-MS code can continue developing in parallel:

- conservation-preserving fragmentation World;
- mass-aware/H-aware state and action representation;
- Free/Guided/Inverse policies;
- candidate generation;
- verified reasoning;
- programme/rule evolution;
- compute optimization.

Engineering promotion uses scientific held-out KPIs, but manuscript claims are only promoted when they improve or enable C1–C14.

---

# Critical path

`Phase 0 → (E1 || E2 || E3) → Fig.1 credibility → Fig.2 census → Fig.3 chemical organization → Fig.4 source organization → Fig.5 global biology → standards`

Standards should be ordered as soon as E28 freezes because procurement may dominate calendar time.

---

# Standing execution rules

1. Freeze definitions before looking at headline counts.
2. Report every numerator with its denominator.
3. Propagate uncertainty in entity counting.
4. Keep unresolved entries in all denominators.
5. Separate candidate recall from evidence discrimination.
6. Biological sample is the inferential unit for biology.
7. Families are frozen before phenotype/source testing.
8. A negative result changes the story; it is not hidden by moving thresholds.
9. No main-text number comes from a training log.
10. The strongest Nature story is determined by the resulting census/organization/biology, not by the complexity of the model.
