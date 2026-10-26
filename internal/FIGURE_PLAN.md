# Figure Plan

The five main figures follow a Nature-style argument:

`headline result → why the World works → chemical discovery → biological organization → biological consequence`.

The paper should not open with a full-page methods diagram. Figure 1 must already show the central scientific result.

---

# Figure 1 | A molecular fragmentation world enables high-evidence resolution of dark spectra

## Role
Headline figure. Establish the World concept briefly, then immediately show that it models real fragmentation, improves difficult structure discrimination, yields more reliable structural conclusions, and resolves dark spectra at repository scale.

## Layout
- Top row: A 38% + B 52%
- Middle row: C 45% + D 45%
- Lower row: E full width
- Bottom strip: F full width

## A | Core concept
Draw only the minimal concept:
[
M,c ightarrow mathcal W_{m frag} ightarrow S_{m obs}.
]
Show precursor, latent multi-branch reaction World and observed MS/MS. Small labels for Free / Guided / Inverse are sufficient.

**Question answered:** what is the scientific object?

## B | Does the World recover real fragmentation?
One benchmark molecule with an observed fragmentation hierarchy. Overlay World-predicted ions/edges/chains and report:
- intensity-weighted coverage;
- ordered-transition recall;
- complete-chain rate;
- optional comparison to direct/single-path baselines.

**Question answered:** is the World a meaningful latent model of fragmentation?

## C | Can the World resolve hard structures?
Use one hard same-formula / near-isomer set. Show GT and 2–4 decoys with candidate-level World receipts:
- intensity coverage;
- ordered-transition recall;
- complete-chain support;
- unresolved World mass where useful.

**Question answered:** can reaction-level evidence distinguish structures that peak similarity struggles to separate?

## D | Structural reliability increases with World evidence
Do not use an invented fixed “8-level hierarchy”. Instead stratify known-structure predictions by empirically defined evidence completeness, for example:
- peak support only;
- + ordered transitions;
- + complete-chain support;
- + low unresolved World mass.

Plot GT containment / correct-candidate rate versus evidence group. Add a small temporal-prospective validation inset if available.

**Question answered:** does richer World evidence correspond to more trustworthy structural conclusions?

## E | Repository-scale resolution of dark spectra
Dominant full-width Sankey/funnel:
[
	ext{dark spectra}
ightarrow
	ext{candidate generation succeeds}
ightarrow
	ext{World-evaluable candidates}
ightarrow
	ext{World-discriminative evidence}
ightarrow
	ext{calibrated structural statements}.
]

Final reporting categories:
- unique putative structure;
- bounded isomer set;
- shared substructure/class;
- unresolved.

Always show denominators and unresolved cases.

**Question answered:** how much dark chemistry becomes structured molecular knowledge?

## F | Representative dark chemistry
3–4 examples only:
- unique putative structure;
- bounded isomer set;
- remote recurrent family;
- authentic-standard anchor if available.

For each: structure, evidence type, recurrence and novelty/distance-to-known.

**Question answered:** what does the headline resolution result look like chemically?

---

# Figure 2 | Learning and inverting a probabilistic fragmentation world

## Role
Mechanistic/methodological figure explaining why the World formulation works.

## Layout
- Top row: A 30% + B 30% + C 34%
- Middle row: D 45% + E 45%
- Bottom: F full width

## A | Autoregressive 1e event language
Show:
- source → target → 1e;
- STOP / REPEAT / NEW;
- repeated 1e events recovering conventional 2e transfer;
- distinct targets producing radical/rearrangement patterns.

**Question answered:** what is the primitive chemical action?

## B | Multi-branch reaction DAG
Show:
- sibling branches;
- branch-local STOP;
- deeper fragmentation;
- reconvergent trajectories;
- distinction between edge/path probability and canonical state probability.

**Question answered:** why is fragmentation represented as a stochastic reaction network rather than a single path?

## C | Probability-mass semantics
Visualize:
[
P_{m valid}+P_{m invalid}+P_{m censored}+P_{m unsampled}+P_{m stop}=1.
]

Meanings:
- invalid = chemical/compiler failure;
- censored = compute truncated;
- unsampled = unexplored;
- stop = learned termination.

**Question answered:** how does the system preserve uncertainty rather than redistributing missing mass to successful chemistry?

## D | Free and Guided inference
Matched chemistry and matched compute:
- Free expands from molecule only;
- Guided conditions frontier allocation on the observed spectrum.

Plot coverage versus expanded states / wall time.

**Question answered:** does spectrum conditioning improve where finite computation is spent?

## E | Inverse molecular inference
Show:
- observed fragments / transitions;
- leaf→parent→precursor shaping where available;
- partial graph growth;
- multiple candidate molecules;
- completed-candidate forward World replay.

**Question answered:** how is structure elucidation formulated as inversion through the World?

## F | Key ablations
Only conceptually essential ablations:
- no multibranch World;
- no spectrum guidance;
- no ordered-transition shaping;
- no forward replay / no shared World semantics.

**Question answered:** which components are essential to the paradigm?

---

# Figure 3 | The dark metabolome contains recurrent and remote molecular families

## Role
Chemical discovery figure. Once dark spectra are structurally bounded, ask what the hidden chemistry actually looks like.

## Layout
- A full width
- B 45% + C 45%
- D 45% + E 45%
- F full width

## A | From dark spectra to structural entities
Show the population transformation:
dark spectra → structural statements → collapsed structural entities → recurrent families.

Keep spectra, statements and entities explicitly distinct.

## B | Feature inflation collapses to molecular entities
Show collapse of:
- adducts;
- isotopologues;
- charge states;
- redundant acquisitions;
- in-source fragments.

Include over-/under-merging validation and entity-count uncertainty.

## C | Recurrence across independent datasets
Show recurrence over independent studies/laboratories, not repeated technical spectra.

## D | Distance to known chemistry
Use a frozen known-metabolite reference space and show:
- distance distribution;
- near-known halo;
- remote chemistry.

## E | Structural landscape
Global structure-based map of:
- characterized metabolites;
- resolved dark entities;
- family clusters;
- remote recurrent islands.

Avoid relying only on spectral embeddings.

## F | Representative remote recurrent families
3–5 families selected for:
- recurrence;
- strong World support;
- distance from known references.

---

# Figure 4 | Biological source organizes dark chemical space

## Role
Ask whether resolved dark chemistry is biologically structured rather than merely chemically structured.

## Layout
- A full-width cohort strip
- B 38% + C 52%
- D 52% + E 38%
- F full width

## A | Perturbation evidence base
Summarize manually verified:
- germ-free/gnotobiotic;
- antibiotic;
- defined-diet studies;
with study/sample/platform counts.

## B | Positive controls
Recover expected source-linked known metabolites before interpreting dark families.

## C | Biological labels across dark families
Summarize:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed;
- unresolved.

## D | Structural map annotated by biological source
Reuse Figure 3E coordinates exactly and overlay source/dependence labels.

## E | Structure–source coupling statistics
Quantify:
- local autocorrelation;
- motif/class enrichment;
- cross-study consistency;
- permutation/null distribution.

## F | Worked family
One remote recurrent family with:
- structures;
- recurrence;
- perturbation effects;
- source label;
- structural evidence.

Use dependence/association language unless biosynthesis is directly established.

---

# Figure 5 | Molecular families improve the reproducibility and interpretability of dark-metabolome biology

## Role
Final payoff: show that resolving chemistry changes biological inference rather than merely producing annotations.

## Layout
- A 48% + B 42%
- C 40% + D 50%
- E 45% + F 45%

## A | Global feature-versus-family analysis
Same samples, preprocessing and covariates:
- anonymous feature arm;
- frozen molecular-family arm.

Pre-register one primary endpoint, ideally:
- cross-cohort replication, or
- effect-sign concordance.

## B | Reproducibility gain across eligible contrasts
Show paired changes in:
- replication;
- sign concordance;
- multiplicity-controlled association yield;
- effect stability.

## C | Principal biological programme
One family selected only after the global analysis is frozen:
- discovery effect;
- independent replication;
- effect size and adjusted significance.

## D | Family chemistry
Show member structures or bounded structural statements with:
- World evidence;
- recurrence;
- structural differences;
- confidence.

## E | Authentic-standard anchors
Show orthogonal validation separately from model evidence:
- sample vs standard MS/MS;
- precursor agreement;
- retention/coelution.

## F | Explicitly unresolved case
Show:
- surviving isomers;
- evidence eliminating rejected candidates;
- why current MS/MS cannot separate survivors;
- predicted next discriminating measurement.

This is a required credibility panel, not a limitation footnote.

---

# Evidence language used across figures

Avoid a fabricated ordinal “evidence hierarchy”. Use three directly interpretable candidate-level evidence families:

1. **Spectral support**
   - intensity-weighted coverage;
   - probability-weighted intensity coverage;
   - generated-peak precision / forward fit where appropriate.

2. **Fragmentation-topology support**
   - ordered-transition recall;
   - complete-chain rate;
   - root/deeper transition recall;
   - multistage support.

3. **Exploration completeness**
   - frontier/unresolved mass;
   - event-budget-censored mass;
   - unsampled mass;
   - invalid-transition mass;
   - probability-conservation error.

Candidate discrimination compares these receipts across competing structures. A calibrated structural statement is then learned/frozen on known-structure data and is not treated as a native PR81 output.

Authentic-standard confirmation is orthogonal experimental validation, not the last rung of a model-evidence ladder.

---

# Visual style

- Low-saturation palette.
- Figure 1 must feel result-led, not architecture-led.
- Figure 2 can carry most method detail.
- Use paired distributions, ECDFs, confidence intervals and calibration plots instead of bars where possible.
- Avoid heatmaps unless matrix structure itself is important.
- Reuse the same structural-map coordinates in Fig.3E and Fig.4D.
- Every fraction has a denominator.
- Every structural example states the reporting granularity/remaining ambiguity.
- Biological samples/cohorts, not spectra, are the unit of biological inference.
- Main figures should be understandable without knowing SubTB, IQL, SMC or WGV.
