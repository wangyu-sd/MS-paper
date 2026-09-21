# Figure Plan

Five main figures. The fixed logic is **1 credibility figure + 4 discovery figures**. After Figure 1, every main figure must state a fact about the dark metabolome rather than about implementation.

The visual sequence should read without the paper text:

`dark spectra → bounded structure → entity census → chemical organization → biological source → biological programme`.

No main figure is reserved for the agent, training loss, World ablations, structured-CoT, rule evolution or representation analysis.

---

## Figure 1 | A calibrated fragmentation World turns dark spectra into bounded structural statements

**Purpose:** earn the right to treat model-derived outputs as measurements in Figures 2–5.

**a. The measurement problem.** One compact schematic: millions of tandem spectra, a small library-identified fraction and a large dark fraction. Contrast the conventional output (ranked candidate list with an uncalibrated score) with the paper's output (the most specific bounded structural statement supported by the spectrum).

**b. A same-formula worked example.** One experimental spectrum and 3–5 close structural alternatives with identical precursor formula. Shared peaks are muted. One or two candidate-specific peaks are connected to atom-balanced/electron-consistent fragmentation trajectories. Show which candidates are eliminated and why. Include one unresolved example beside it so the reader immediately learns that the system is allowed to stop at an isomer set.

**c. Soundness–resolution operating curve.** False exclusion of the true structure on the x-axis, fraction of spectra resolved above formula on the y-axis. Mark the frozen operating point used for the atlas. This is the central quantitative contract, not raw benchmark rank.

**d. Prospective library-growth validation.** Compact freeze timeline plus the prospective result: system frozen against an earlier library snapshot; spectra dark at freeze; structures independently deposited later; predicted confidence versus observed containment at evaluation. Put calibration error and denominator directly in the panel.

**e. Comparative credibility.** On the identical prospective set, compare containment/calibration of the bounded structural statements against calibrated outputs from major comparator families. Do not claim mechanism is intrinsically more accurate; show whether the stated confidence remains honest under structural distance shift.

**f. Output hierarchy.** Distribution at the frozen operating point: unique putative structure, bounded isomer set, substructure/class, formula only, unresolved. This is the legend for every later figure.

*Main claims:* the system produces structural statements with a measurable soundness–resolution trade-off and prospectively testable reliability.

*Move to ED:* complete benchmark table, shuffled-spectrum controls, METEOR trace verification, per-peak information analysis, all calibration stratifications.

---

## Figure 2 | The dark metabolome contains far fewer recurrent chemical entities than spectral features imply

**Purpose:** establish the first field-level census.

**a. Census funnel.** The largest visual element in the figure. Show:
`all tandem spectra → dark spectra → reproducible dark features → structurally resolvable statements → distinct structural entities`.
Every arrow carries a denominator and a frozen exclusion/merging rule.

**b. Feature-to-entity contraction.** Distribution of the number of spectral features/acquisitions that collapse onto one structural entity. Separate contributions from adducts, isotopologues, charge states, in-source fragments and redundant acquisitions. Inset: validation of these collapsing rules on known compounds.

**c. Entity-count estimate.** Final dark-entity count with uncertainty propagated from measured collapsing error. Show mouse and public-repository estimates separately and jointly; avoid presenting a single exact count without an interval.

**d. Recurrence across independent datasets.** Number of structural entities/families observed in 1, 2, 3, ... independent datasets. Distinguish recurrence across spectra from recurrence across datasets/laboratories.

**e. Resolution depth of the census.** For all recurrent entities, show how many are resolved to unique putative structure, bounded isomer set, substructure/class or formula only. This prevents the entity count from being mistaken for N unique identifications.

**f. Representative recurrent entities.** A small set spanning the resolution hierarchy, each with recurrence count and source datasets. Prefer chemically diverse examples over the visually most attractive structures.

*Headline number:* `N_dark features → N_recurrent structural entities`.

*Main claims:* the feature count materially overstates the number of distinct dark chemical entities, and a reproducible subset can be enumerated with explicit structural resolution.

---

## Figure 3 | Dark chemistry forms a structured landscape beyond known metabolism

**Purpose:** show that the dark metabolome is organized rather than a random cloud of unassigned spectra.

**a. Global structural landscape.** Low-dimensional visualization or graph layout built from structural relationships, not spectral embeddings alone. Overlay characterized metabolites and recurrent dark entities. The visual question is whether dark chemistry forms neighbourhoods/islands relative to known metabolism.

**b. Near-known halo versus remote dark chemistry.** Predefine a structural/transformation neighbourhood of characterized metabolites. Report the fraction of recurrent entities in:
- characterized/overlapping space;
- one-step or near-known halo;
- remote recurrent families beyond the predefined neighbourhood;
- unresolved-at-class-level entries excluded from this calculation.

**c. Distance distribution.** Continuous distribution of structural distance to the nearest characterized metabolite, with confidence/resolution strata shown separately. Do not force class-level statements into a precise distance.

**d. Recurrent structural families.** Family-size and recurrence distributions. Highlight whether remote chemistry is dominated by isolated singletons or repeated families.

**e. Chemical composition.** Compare class composition of recurrent dark entities with reference libraries, with detectability/ionization caveats and appropriate normalization.

**f. Representative remote families.** 3–5 recurrent families lacking a reference-library representative, each showing the bounded structural core, family size, dataset recurrence and uncertainty. Do not infer a biosynthetic pathway from a mass-difference series.

*Headline number:* fraction of recurrent dark chemistry outside the predefined neighbourhood of characterized metabolism.

*Main claims:* dark chemistry is non-randomly organized into a near-known halo plus recurrent structural families that are poorly represented in current libraries.

---

## Figure 4 | Biological sources partition dark chemical space

**Purpose:** connect chemical organization to biology without overclaiming biosynthesis.

**a. Perturbation evidence map.** Public germ-free/gnotobiotic, antibiotic and dietary-intervention datasets used, with independent dataset counts, sample counts and platform coverage. Keep this compact.

**b. Positive-control gate.** Known microbiota-, diet- and host-associated metabolites must recover the expected direction under the same pipeline. Show the label-permutation null alongside.

**c. Global family attribution.** Recurrent dark families partitioned into microbiota-dependent, diet-dependent, host-associated, mixed and unresolved categories. Always show the unresolved denominator.

**d. Origin over structural landscape.** Project the attribution labels onto the Figure 3 structural map. This is the core visual: biological source should organize chemical space rather than appear as a detached pie chart.

**e. Structure–source concordance.** Compare chemical motifs/classes enriched across attribution groups, with cross-dataset effect consistency rather than one-study significance.

**f. Worked family.** One family showing structural members and its presence/absence or effect pattern across multiple independent perturbation datasets. State "dependent/associated", not "biosynthesized by", unless direct biosynthetic evidence exists.

*Headline number:* fraction of recurrent structural families with reproducible source dependence.

*Main claim:* biological source is coupled to the structural organization of the dark metabolome.

---

## Figure 5 | Structural families reveal biological programmes hidden at feature level

**Purpose:** establish that structural resolution changes biological inference, not merely annotation.

**a. Global feature-versus-family test.** Across all preregistered biological contrasts/cohorts, compare anonymous feature-level analysis with frozen structural-family analysis for:
- cross-cohort effect-sign concordance;
- replication rate;
- variance explained or predictive stability, if appropriate;
- multiplicity-controlled association yield.
The primary endpoint must be chosen before looking at the comparison.

**b. Replication gain.** Show the distribution of replication outcomes for families versus their constituent features. The figure should demonstrate a systematic effect, not only one favourable case.

**c. Principal biological programme.** One strongest frozen family associated with a phenotype/contrast, with biological samples as points and effect estimates across independent cohorts.

**d. Family chemistry.** Draw all resolved members or a representative subset, annotated by resolution level and confidence. Structural edits may define a transformation series, but do not label them enzymatic reactions without evidence.

**e. Orthogonal anchors.** Authentic-standard MS/MS and retention/coelution for preselected commercially available anchors. Report failed anchors in the accompanying table/ED.

**f. Deliberately unresolved member.** Show the surviving isomer set and the exact measurement predicted to separate it. This panel makes the paper's uncertainty contract visible.

*Headline result:* structural-family analysis recovers reproducible biological organization that anonymous-feature analysis disperses.

*Main claims:* structure is not merely a label; it changes the statistical object used to discover biology.

---

# Extended Data

| # | Title | Contents |
|---|---|---|
| ED1 | Corpora, snapshots, leakage audit and dark-subset construction | Dataset provenance; library snapshots; exact/analogue leakage; adduct/instrument distributions; frozen dark-search protocol |
| ED2 | Complete fragmentation-World benchmark | Matched candidate pools; same-formula/near-isomer strata; generator recall vs conditional discrimination vs end-to-end resolution; runtime; World/action-space coverage |
| ED3 | Soundness, calibration and prospective validation | Full stringency sweep; held-out and prospective calibration; structural-distance stratification; comparator calibration; freeze hashes; independence audit |
| ED4 | Spectrum identity and hypothesis-generation controls | Correct/absent/shuffled spectrum; METEOR or inverse-generator trace verification; candidate-source controls; failure taxonomy |
| ED5 | Entity-collapsing validation and census sensitivity | Known-compound collapsing validation; adduct/isotope/in-source rules; uncertainty propagation; thresholds; corpus-wise entity counts |
| ED6 | Fragmentation-World / program evolution | Failure localization; typed revisions; accepted/rejected revisions; coverage growth; causal replay; ablations; compute/worker cost |
| ED7 | Atlas technical quality control | Resolution/confidence by corpus, instrument and organism; recurrence definitions; per-entry record schema; dataset-independence audit |
| ED8 | Chemical-landscape robustness | Alternative structural distances; reference-set sensitivity; class composition; family definitions; near-known/remote boundary sensitivity |
| ED9 | Biological-source attribution | Complete perturbation inventory; harmonization; positive controls; permutation nulls; batch/platform models; unresolved/mixed assignments |
| ED10 | Feature-versus-family biological analysis | Frozen family definitions; all contrasts; replication statistics; threshold sensitivity; metadata permutations; leave-one-cohort-out results |
| ED11 | Complete standard-validation and unresolved-case dossiers | All selected anchors including failures; spectra; retention; candidate alternatives; discriminating measurements |

---

## Visual style

- Low-saturation palette; use colour to encode one scientific variable per panel.
- No decorative network hairballs. Structural maps must have interpretable density/cluster summaries.
- Prefer distributions, paired effects, ECDFs and uncertainty intervals over bars.
- Every fraction shows its denominator.
- Every biological effect shows biological samples or cohort-level estimates.
- Every structural example carries its resolution level.
- Molecule drawings use a common bond length and line weight.
- Main figures should remain understandable if all implementation-specific acronyms are removed.
