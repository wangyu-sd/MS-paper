# Figure Plan

Five main figures. The narrative is **2 capability figures + 3 discovery figures**.

The visual chain must be obvious without reading the paper:

`partial spectrum → latent fragmentation World → Free/Guided/Inverse inference → graded structural evidence → dark-matter resolution → chemical families → biology`.

Implementation details such as optimizer names, agent prompts and low-level training losses belong in Extended Data unless they are necessary to understand the scientific mechanism.

---

## Figure 1 | A molecular fragmentation world unifies prediction, explanation and inverse inference

**Purpose:** establish the conceptual object of the paper. A spectrum is a partial observation of a latent gas-phase fragmentation world, not the object being directly modelled.

### a. Spectrum as partial observation
Show a molecule under fixed ionization/collision conditions producing a latent multi-branch gas-phase reaction network. Only a subset of charged products is observed as peaks. Neutral coproducts, low-abundance branches and unobserved states remain part of the World.

Visual statement:
[
M,c ightarrow mathcal W(M,c) ightarrow S_{mathrm{obs}}
]

Explicitly annotate:
- ionization microstates;
- electron-flow events;
- H transfer;
- charged + neutral components;
- competing branches;
- STOP/halted probability;
- observation/instrument layer.

The key caption sentence is:
**A tandem mass spectrum is an incomplete observation of a probabilistic molecular fragmentation world.**

### b. One World, three modes of inference
Place one central **Fragmentation World** and three queries around it:

**Free / prediction**
[
p(mathcal T,Smid M,c)
]
Molecule → probabilistic fragmentation network → predicted spectrum.

**Guided / explanation**
[
p(mathcal Tmid M,S_{mathrm{obs}},c)
]
Molecule + observed spectrum → explanatory subnetwork / evidence paths.

**Inverse / structure inference**
[
p(M,mathcal Tmid S_{mathrm{obs}},c)
]
Spectrum → multiple molecular hypotheses → World consistency.

Use the phrase:
**One chemical world, three modes of inference.**

### c. Chemistry defines legality; learning defines preference
Compact executor panel:
- atom conservation;
- electron conservation;
- charge;
- explicit H;
- exact mass;
- valence/formula closure.

Invalid actions do not receive a penalty; they are not executable.

Beside this, show learned quantities:
- transition propensity;
- branch probability;
- frontier value;
- posterior molecular probability.

### d. Multi-branch probabilistic reaction world
Worked precursor example showing:
- multiple sibling fragmentation branches;
- branch-local STOP;
- reconvergent paths into the same fragment state;
- probability-flow conservation.

Contrast against a single-path mechanism or a direct structure→spectrum predictor.

### e. Adaptive inference under finite compute
Show a large latent reaction frontier. Free distributes probability over plausible branches; Guided reallocates expansion toward spectrum-relevant branches; Inverse SMC/GFlowNet preserves multiple molecular modes.

Do not draw generic “RL” arrows. The scientific message is **adaptive allocation of finite computation in a combinatorial chemical world**.

### f. Outer-loop scientific evolution
Small supporting panel only:
systematic W/G/V failure → agent proposes bounded change → typed compiler/conservation tests → held-out gate → promoted World.

The agent remains outside online inference.

*Main claims:* spectrum-as-partial-observation; shared World; three conditional inference modes; hard chemistry/learned preference.

---

## Figure 2 | World-based inference establishes graded structural evidence

**Purpose:** demonstrate what the WGV paradigm enables that direct prediction/ranking does not.

### a. Free World performance
On a molecule-disjoint cohort, quantify:
- observed mass coverage;
- intensity-weighted coverage;
- parent→child transition coverage;
- multistage contribution;
- probability conservation;
- coverage-vs-expanded-states AUC.

Show the learned World as a network, not only a spectrum cosine score.

### b. Guided explanation under matched compute
Free and Guided receive the same molecule and compute budget; only Guided receives the target spectrum.

Compare:
- intensity/mass/path coverage;
- states expanded to reach matched coverage;
- wall time;
- explanatory-path coherence.

The claim is not that Guided changes chemistry. It changes **where computation is spent**.

### c. Inverse posterior structure inference
Spectrum → multiple candidate structures.

Report:
- Recall@K / Exact@K;
- best structural similarity/MCES;
- posterior diversity;
- formula/chemical validity;
- candidate collapse/ESS where relevant.

Show several posterior modes, not one Top-1 molecule.

### d. Bidirectional consistency
For generated candidates:
[
S_{mathrm{obs}}
ightarrow M
ightarrow mathcal W(M)
ightarrow hat S
]

Compare correct versus hard-decoy candidates using:
- forward intensity/path coverage;
- candidate-specific evidence;
- cycle/trajectory consistency.

This panel is the bridge from “prediction” to “evidence”.

### e. Evidence hierarchy
A single vertical ladder:

1. mass/formula compatible;
2. structurally valid;
3. World-reachable;
4. executable path support;
5. candidate-specific discriminative evidence;
6. bidirectional spectrum–structure consistency;
7. calibrated bounded structural statement;
8. authentic-standard confirmation.

For the benchmark/prospective cohort, show what fraction reaches each level.

### f. Prospective credibility
Historical library freeze → system frozen → spectra dark at freeze → structures independently deposited later.

Report:
- containment at stated confidence;
- calibration error;
- structural-distance shift;
- fair comparator calibration.

*Main claim:* WGV converts structure prediction into auditable, graded evidence.

*Move to ED:* detailed DAgger/IQL/SubTB ablations, policy losses, action-space ablations, full calibration tables.

---

## Figure 3 | High-evidence inference resolves the dark metabolome at scale

**Purpose:** show what becomes possible once evidence, not rank, is the output.

### a. Repository-scale resolution funnel
[
	ext{dark spectra}
ightarrow
	ext{formula-level}
ightarrow
	ext{class/substructure}
ightarrow
	ext{bounded isomer sets}
ightarrow
	ext{World-resolved structures}
ightarrow
	ext{standard-confirmed anchors}
]

Every level has a denominator. Do not imply that all lower levels are unique structures.

### b. Feature-to-entity contraction
Validate and apply collapsing of:
- adducts;
- isotopologues;
- charge states;
- in-source fragments;
- redundant acquisitions.

Show dark spectral observations → bounded structural entities with uncertainty.

### c. Recurrence across independent datasets
Number of entities/families recurring across 1, 2, 3, ... independent datasets/laboratories.

This separates reproducible dark chemistry from one-study artefacts.

### d. Evidence level versus recurrence
Ask whether recurrent chemistry receives stronger structural evidence than singletons. This can become a central result if positive.

### e. Near-known versus remote chemistry
Using a frozen characterized-metabolite reference and frozen structural-distance definition, partition high-evidence recurrent entities into:
- near-known halo;
- remote recurrent families;
- insufficient-resolution cases.

### f. Representative high-evidence dark entities
3–5 examples spanning:
- high-confidence World-resolved candidate;
- bounded isomer set;
- remote recurrent family member;
- standard-confirmed anchor if available.

*Main claims:* a large fraction of dark chemistry can be moved to stronger structural evidence levels; the resulting population is recurrent and chemically interpretable.

---

## Figure 4 | Resolved dark chemistry reveals structural and biological organization

**Purpose:** move from “we resolved dark spectra” to “we learned something about dark chemistry”.

### a. Structural landscape
Global graph/layout of high-evidence recurrent entities and characterized metabolites based on structural relationships.

Show:
- known metabolite neighbourhood;
- near-known halo;
- remote recurrent islands/families.

### b. Recurrent family architecture
Family-size and recurrence distributions. Highlight repeated remote families rather than isolated candidate structures.

### c. Public perturbation design
Compact map of germ-free/gnotobiotic, antibiotic and diet perturbation datasets with manually verified study/sample counts.

### d. Source dependence over chemical space
Overlay:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed;
- unresolved.

The central visual should show biological source partitioning the structural landscape, not a detached pie chart.

### e. Structure–source coupling
Quantify:
- local source-label autocorrelation;
- class/motif enrichment;
- cross-study effect consistency;
- permutation null.

### f. Worked remote family
One recurrent family showing:
- bounded structures;
- independent dataset recurrence;
- perturbation effects;
- source label;
- evidence level.

Use “dependent/associated”, not “biosynthesized”, unless direct evidence exists.

*Main claim:* the newly resolved dark chemical population has non-random structural and biological organization.

---

## Figure 5 | Dark molecular families reveal biology hidden from feature-level metabolomics

**Purpose:** demonstrate that structural resolution changes biological discovery.

### a. Global paired feature-versus-family analysis
Same samples, same preprocessing, same covariates:
- anonymous dark features;
- frozen structural families.

Pre-register one primary global endpoint:
- cross-cohort replication rate, or
- effect-sign concordance.

### b. Reproducibility gain
Across all eligible contrasts/families, show paired distribution of:
- replication;
- sign concordance;
- multiplicity-controlled association yield;
- effect stability.

Do not rely on one successful family.

### c. Principal biological programme
One strongest pre-defined family after the global analysis is frozen.

Show:
- biological sample-level effects;
- independent cohort estimates;
- adjusted significance.

### d. Family chemistry
Structures/bounded statements for family members with:
- evidence level;
- confidence;
- recurrence;
- interpretable structural differences.

Avoid calling a structural series a pathway without direct biosynthetic evidence.

### e. Authentic-standard anchors
Sample vs standard:
- precursor;
- MS/MS;
- retention/coelution.

Report failures in ED and denominator.

### f. Explicitly unresolved member
Show surviving isomers and the additional experiment predicted to distinguish them.

*Main claim:* WGV-based structural evidence converts anonymous dark features into reproducible molecular programmes.

---

# Extended Data

| # | Title | Contents |
|---|---|---|
| ED1 | Corpora, splits, leakage and observation model | Data provenance; molecule-disjoint splits; library snapshots; exact/analogue leakage; instrument/adduct distributions; dark-subset definition |
| ED2 | Fragmentation World state, actions and conservation | BE state; exact mass; explicit H; charged/neutral coproducts; sparse electron events; ionization ensemble; materialization; conservation tests |
| ED3 | Free World learning and probabilistic network evaluation | SubTB/GFlowNet; multibranch probability flow; STOP/censoring; coverage; calibration; compute scaling; direct predictor baselines |
| ED4 | Guided inference | DAgger/IQL; matched-budget Free vs Guided; frontier representations; explanatory paths; coverage-vs-compute; no target leakage into Free |
| ED5 | Inverse structure inference | Construction GFlowNet/SMC; canonical state merge; formula/charge/H constraints; Exact@K; similarity; diversity; posterior/cycle diagnostics |
| ED6 | Evidence hierarchy and prospective calibration | Hard-decoy discrimination; cycle consistency; bounded statements; historical library-growth validation; comparator calibration |
| ED7 | Outer-loop program evolution | Failure localization; typed changes; rejected/promoted revisions; causal replay; held-out gates; compute |
| ED8 | Dark-resolution scale and entity collapse | Evidence-level funnel; collapse validation; uncertainty; recurrence; census sensitivity |
| ED9 | Structural landscape and source attribution | Near/remote definitions; reference-set sensitivity; family graph; public perturbations; positive controls; permutation nulls |
| ED10 | Feature-versus-family biology | Complete global paired results; replication; concordance; multiplicity; threshold sensitivity; leave-one-cohort-out |
| ED11 | Standard validation and unresolved dossiers | All anchors including failures; spectra; retention; candidate alternatives; predicted discriminating measurements |

---

## Visual style

- Low saturation.
- No decorative network hairballs.
- Use reaction-network visuals only when probability flow or mechanistic branching is readable.
- Prefer distributions, paired comparisons and uncertainty intervals over bars.
- Every fraction carries a denominator.
- Every structure carries its evidence level.
- Every biological effect uses biological samples/cohort estimates, not spectra as pseudo-replicates.
- Main figures should remain understandable without the acronyms SubTB, IQL, DAgger or SMC.
