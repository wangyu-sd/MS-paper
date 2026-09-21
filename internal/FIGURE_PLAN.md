# Figure Plan

Five main figures. The paper is designed as **2 capability figures + 3 discovery figures**.

The visual chain is:

`partial spectrum → fragmentation World → W/G/V inference → graded structural evidence → high-evidence dark chemistry → structural/source organization → biology`.

Each main figure should read as one visual argument rather than six independent panels. Panel widths below are approximate fractions of the usable figure width and are intended to guide the final Illustrator/Figma/PowerPoint composition.

---

# Figure 1 | A molecular fragmentation world unifies prediction, explanation and inverse inference

## Overall composition

**Three horizontal bands.**

- **Top row:** A 56% width + B 38% width.
- **Middle row:** C 30% + D 34% + E 30%.
- **Bottom strip (about 15%):** F full width.
- Leave ~5% for panel labels/spacing.

**Dominant panel:** A.  
The editor should understand “spectrum = partial observation of a fragmentation world” before reading any other panel.

## A | Spectrum as partial observation — 57% width

**Visual form:** mechanistic schematic, not a flowchart full of text.

Draw:
1. one precursor molecule;
2. several ionization microstates;
3. a multi-branch gas-phase reaction network;
4. charged fragments and neutral coproducts;
5. an observation/instrument layer;
6. the resulting sparse MS/MS spectrum.

Use solid edges for explored/materialized chemistry and faint/dashed edges for valid but unobserved/unresolved regions.

Place the equation prominently:

[
M,c ightarrow mathcal W(M,c) ightarrow S_{mathrm{obs}}.
]

Key visual message:

> The spectrum is a partial observation of the latent reaction world.

Do **not** imply that every unobserved World state is false.

## B | One World, three modes of inference — 43% width

**Visual form:** central World with three directional query arrows.

Center:
**Molecular Fragmentation World**

Around it:

- **Free / prediction:** molecule → reaction network / spectrum
  [
  p(mathcal T,Smid M,c)
  ]
- **Guided / explanation:** molecule + spectrum → explanatory subnetwork
  [
  p(mathcal Tmid M,S_{mathrm{obs}},c)
  ]
- **Inverse / structure inference:** spectrum → molecular posterior → World replay
  [
  p(M,mathcal Tmid S_{mathrm{obs}},c)
  ]

Keep the visual symmetrical enough that these look like three queries over one object, not three disconnected models.

## C | Autoregressive 1e event language — 31% width

**Visual form:** three small electron-pushing microexamples.

Show the primitive:

[
	ext{source} ightarrow 	ext{target} ightarrow 1e
]

followed by:

[
	ext{STOP / REPEAT / NEW}.
]

Examples:
- two repeated same-direction 1e events → conventional 2e transfer;
- different electron destinations → homolytic/radical event;
- sequential distinct events → rearrangement.

Caption phrase:
**Elementary electron events, not a fragmentation-template catalogue.**

## D | Probability-mass semantics — 35% width

**Visual form:** probability ledger / flow partition.

Show a single parent state splitting into:

- valid reaction mass;
- invalid chemistry mass;
- event-budget-censored mass;
- unsampled mass;
- learned STOP mass.

Equation:

[
P_{m valid}+P_{m invalid}+P_{m censored}
+P_{m unsampled}+P_{m stop}=1.
]

Use visual grouping:
- chemistry failure = terminal failure;
- STOP = learned terminal chemistry;
- censored/unsampled = unresolved epistemic mass.

This panel should make the principle obvious:

> Uncomputed is not impossible, and failed chemistry is not redistributed to successful hypotheses.

## E | Multi-branch reaction DAG — 31% width

**Visual form:** compact reaction DAG.

Show:
- one precursor;
- 3–4 sibling reactions;
- branch-local STOP;
- one deeper branch;
- two distinct trajectories reconverging to one canonical state.

Annotate:
- conditional probability on edges;
- path probability;
- summed reach probability at reconvergent node.

Avoid a large network hairball.

## F | Outer-loop scientific evolution — full-width strip

**Visual form:** thin left-to-right strip.

[
	ext{systematic failure}
ightarrow
	ext{bounded agent proposal}
ightarrow
	ext{typed compiler + conservation checks}
ightarrow
	ext{held-out gate}
ightarrow
	ext{promoted World}.
]

Keep visually subordinate. The agent is not the online chemistry policy.

---

# Figure 2 | World-based inference establishes graded structural evidence

## Overall composition

**Three rows, two columns.**

- **Top row:** A 45% + B 45%.
- **Middle row:** C 38% + D 52%.
- **Bottom row:** E 58% + F 32%.

**Dominant panels:** D and E.  
The reader should leave the figure understanding why World-based inference creates stronger evidence than candidate ranking.

## A | Free World performance — 50%

**Visual form:** one reaction-network example + 2–3 compact quantitative distributions.

Show:
- observed mass coverage;
- intensity-weighted coverage;
- ordered parent-child transition coverage;
- multistage-added coverage;
- probability conservation.

Prefer paired distributions / ECDFs over bars.

The network example should visually link observed peaks to World states.

## B | Guided explanation under matched compute — 50%

**Visual form:** paired coverage-versus-compute curves.

Same molecule, chemistry and compute budget:
- Free;
- Guided.

Only Guided sees the target spectrum.

Primary plots:
- intensity/path coverage vs expanded states;
- states or wall time needed to reach matched coverage.

Optional inset:
one frontier where Guided chooses an evidence-bearing branch that Free postpones.

Do not label DAgger/HER as production components unless implemented before manuscript freeze.

## C | Inverse posterior structure inference — 44%

**Visual form:** spectrum on left → 4–6 candidate molecular structures on right.

For each candidate show:
- posterior/evidence weight;
- formula validity;
- structural distance to GT in benchmark illustration.

Below/adjacent:
- Exact/Recall@K;
- best Tanimoto/MCES;
- diversity or ESS.

The visual point is **multi-modal posterior**, not Top-1 generation.

## D | Bidirectional consistency — 56%

**Visual form:** closed-loop mechanistic comparison.

[
S_{mathrm{obs}}
ightarrow M
ightarrow mathcal W(M)
ightarrow hat S.
]

Use one GT and 2–3 same-formula/near-isomer decoys.

For each candidate show:
- executable paths supporting discriminative peaks;
- intensity/path consistency;
- unresolved World probability mass;
- ordered-transition consistency.

This should be the strongest “why the answer is credible” panel.

## E | Evidence hierarchy — 63%

**Visual form:** horizontal ladder/funnel spanning most of the width.

Levels:

1. mass/formula compatible;
2. chemically valid;
3. World reachable;
4. executable path support;
5. candidate-specific evidence;
6. bidirectional consistency;
7. calibrated bounded statement;
8. authentic-standard confirmation.

Overlay two quantities across the ladder:
- **coverage** decreases;
- **reliability/containment** increases.

A small unresolved-mass icon can indicate World exploration completeness.

## F | Prospective credibility — 37%

**Visual form:** historical timeline above, calibration plot below.

Timeline:
freeze library/system → dark-at-freeze spectra → later independent structure deposition → blind evaluation.

Plot:
reported confidence vs observed containment, plus structural-distance stratification.

Comparator calibration should be compact and fair.

---

# Figure 3 | High-evidence inference resolves the dark metabolome at scale

## Overall composition

**Four visual bands.**

- **Top:** A full width, ~25% height.
- **Second row:** B 45% + C 45%.
- **Third row:** D 45% + E 45%.
- **Bottom:** F full-width example strip.

**Dominant panel:** A.

## A | Repository-scale evidence funnel — full width

**Visual form:** Sankey/funnel.

Start with all eligible dark spectra and move through:

[
	ext{mass/formula}
ightarrow
	ext{World reachable}
ightarrow
	ext{path supported}
ightarrow
	ext{candidate specific}
ightarrow
	ext{bidirectional}
ightarrow
	ext{calibrated bounded structure}.
]

At every stage show:
- numerator/denominator;
- unresolved branch;
- computationally censored branch where relevant.

Do not make the funnel visually imply that every spectrum must progress to a unique structure.

## B | Spectral observations to structural entities — 50%

**Visual form:** collapse Sankey.

Show contribution from:
- adducts;
- isotopologues;
- charge states;
- in-source fragments;
- redundant acquisitions.

End at high-evidence structural entities with an uncertainty interval.

Inset:
known-compound over-/under-merging validation.

## C | Recurrence across independent datasets — 50%

**Visual form:** ECDF/rank-frequency distribution.

x-axis:
number of independent datasets/laboratories.

y-axis:
fraction/count of entities/families.

Differentiate:
- single-study;
- recurrent;
- highly recurrent.

## D | Evidence level versus recurrence — 50%

**Visual form:** ordinal distribution / ridge / violin / box-free distribution.

x-axis:
recurrence category.

y-axis:
evidence level or reliability.

Test whether recurrent chemistry is more structurally resolvable.

## E | Near-known versus remote chemistry — 50%

**Visual form:** distance-to-known distribution with frozen threshold.

Partition:
- near-known halo;
- remote recurrent families;
- insufficient-resolution cases.

If possible, pair a density curve with a small structural map rather than using a pie chart.

## F | Representative high-evidence dark chemistry — full-width strip

Show 3–5 cases:
- World-resolved structure;
- bounded isomer set;
- remote recurrent family member;
- standard-confirmed anchor if available.

For each:
structure + representative spectrum/evidence icon + recurrence + evidence level + remaining uncertainty.

---

# Figure 4 | Resolved dark chemistry reveals structural and biological organization

## Overall composition

**A and D are the main visual anchors and should reuse the same coordinate system.**

- **Top:** A 58% + B 32%.
- **Middle strip:** C full width.
- **Bottom:** D 58% + E 32%.
- **Footer:** F full width.

## A | Structural landscape — 60%

**Visual form:** global structure-based map/graph.

Include:
- characterized metabolites;
- high-evidence recurrent dark entities;
- family boundaries;
- near-known halo;
- remote islands.

Do not use spectral embeddings alone for this panel.

Use density contours/family hulls rather than plotting every edge.

## B | Recurrent family architecture — 40%

**Visual form:** two compact distributions.

Possible:
- family size distribution;
- recurrence distribution;
- remote vs near-known composition.

Prefer ECDF/ridgeline/dot distributions to bars.

## C | Public perturbation evidence — full-width strip

**Visual form:** cohort design strip.

Three branches:
- germ-free/gnotobiotic;
- antibiotic;
- defined diet.

For each:
number of studies, samples and platforms.

This is evidence provenance, not a result-heavy panel.

## D | Source dependence over chemical space — 60%

Reuse A's map coordinates.

Overlay:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed;
- unresolved.

The reader should visually see whether source labels partition the structural landscape.

## E | Structure–source coupling — 40%

**Visual form:** statistical distributions with nulls.

Show:
- local source-label autocorrelation;
- motif/class enrichment;
- cross-study effect consistency;
- permutation distribution/confidence interval.

## F | Worked remote family — full-width strip

Show:
- 3–6 bounded structures;
- independent-dataset recurrence;
- perturbation effect mini-plots;
- source-dependence label;
- evidence levels.

Use “dependent/associated”, not “biosynthesized”, absent direct evidence.

---

# Figure 5 | Dark molecular families reveal biology hidden from feature-level metabolomics

## Overall composition

**Three rows, two columns.**

- **Top:** A 47% + B 43%.
- **Middle:** C 39% + D 51%.
- **Bottom:** E 45% + F 45%.

**Dominant panel:** A.  
The paper needs a global biological principle before a case study.

## A | Global feature-versus-family analysis — 52%

**Visual form:** paired global result.

Same samples, preprocessing and covariates:
- anonymous features;
- frozen structural families.

Primary endpoint should be visually dominant:
- cross-cohort replication rate, or
- effect-sign concordance.

Prefer paired cohort/family dots and confidence intervals.

## B | Reproducibility gain — 48%

**Visual form:** distributions across all eligible contrasts.

Show:
- replication;
- sign concordance;
- multiplicity-controlled yield;
- effect-size stability.

Avoid a single aggregate bar.

## C | Principal biological programme — 45%

**Visual form:** biological sample-level effect + cohort meta-effect.

Show:
- discovery cohort;
- replication cohort(s);
- adjusted significance;
- effect direction/CI.

## D | Family chemistry — 55%

Show the molecular family:
- structures or bounded statements;
- evidence level;
- recurrence;
- confidence;
- interpretable structural differences.

Structural adjacency should not be labelled as an enzymatic pathway without evidence.

## E | Authentic-standard anchors — 50%

**Visual form:** sample vs standard.

- MS/MS overlay;
- retention/coelution;
- precursor match;
- acceptance criteria.

Keep the standard-confirmed evidence visually distinct from model-derived evidence.

## F | Explicitly unresolved member — 50%

Show:
- surviving isomer set;
- evidence eliminating other candidates;
- why current MS/MS cannot separate survivors;
- predicted next measurement.

This is a required honesty panel, not a limitation footnote.

---

# Extended Data allocation

| ED | Main purpose |
|---|---|
| ED1 | Corpora, molecule-disjoint splits, leakage, library snapshots and observation contract |
| ED2 | Bond-electron state, explicit H/charge, 1e event language, compiler and conservation |
| ED3 | Free World training, multibranch DAG, STOP/valid/invalid/censored/unsampled mass and direct/single-path baselines |
| ED4 | Guided matched-budget inference, spectrum-conditioned value policy and auxiliary IQL diagnostics |
| ED5 | Factorized inverse construction, leaf→parent→precursor shaping, SMC, Recall@K and posterior diversity |
| ED6 | Evidence hierarchy, hard-decoy bidirectional tests and prospective calibration |
| ED7 | Outer-loop scientific program evolution and held-out promotion gates |
| ED8 | Complete dark-resolution funnel, entity-collapse validation and recurrence sensitivity |
| ED9 | Structural-landscape robustness, near/remote definitions and biological-source attribution |
| ED10 | Complete feature-versus-family biological analysis |
| ED11 | All authentic-standard successes/failures and unresolved dossiers |

---

# Visual style

- Low-saturation palette.
- No generic AI icons, glowing nodes or decorative gradients.
- Reaction arrows should look chemically meaningful, not like generic network arrows.
- Molecule bond lengths and line weights should be consistent across panels.
- Use the same structural-map coordinates in Fig.4A and Fig.4D.
- Prefer distributions, ECDFs, paired dots and confidence intervals over bars.
- Avoid heatmaps unless the matrix structure itself is scientifically essential.
- Every fraction includes its denominator.
- Every structural example includes its evidence level.
- Every biological panel uses biological samples/cohort estimates, not spectra as pseudo-replicates.
- Main figures should be understandable without knowing the acronyms SubTB, IQL, SMC or WGV.
