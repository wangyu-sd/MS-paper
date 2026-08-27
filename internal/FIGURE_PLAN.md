# Figure Plan

Five main figures. The ratio is fixed at **1 system : 1 hinge : 3 findings**; do not add a sixth main figure for the agent, the benchmark ablations or the representation analysis.

Every main panel must be readable by a non-specialist in under ten seconds and must state a fact about the world or about reliability, never about an implementation.

---

## Figure 1 | Mechanistic elimination discriminates where spectral similarity cannot

**a. The operation.** One spectrum, two same-formula candidates. Peaks shared by both are greyed out; the one peak reachable only by the true candidate is highlighted, with its atom-balanced trajectory drawn beneath (bonds broken, H transfers, ppm error). This panel must make "eliminated by a peak it cannot produce" visually obvious. It carries the whole paper.

**b. Output form.** The same spectrum's candidate set before and after elimination, and the resulting statement: unique structure / bounded isomer set / substructure / class. Show a second spectrum that terminates at the isomer-set level, so the reader learns immediately that the system reports partial answers.

**c. Benchmark.** Discrimination endpoint vs comparators (exact mass, forward-spectrum similarity, CFM-ID, SIRIUS/CSI:FingerID) on identical spectra and pools. Grouped by difficulty stratum. Same-formula stratum highlighted.

**d. Where the information lives.** Per-peak contribution to the discriminative margin against peak intensity, showing that abundant peaks are typically shared and low-intensity peaks carry the identity. Log x-axis.

**e. Trace verification.** Structural accuracy of verified vs unverified METEOR traces at matched confidence, with the failure taxonomy as a small stacked bar.

*Source claims:* C1, C2 (control in ED3), C3.

---

## Figure 2 | Confidence calibrated against prospective library growth

**a. Freeze design.** Timeline: library snapshot at freeze, system frozen with artifact hashes, spectra dark at freeze, structures independently deposited by other laboratories during the interval, evaluation snapshot. Must communicate that the answers did not exist when predictions were made.

**b. Calibration curve.** Reported confidence vs observed containment on the prospective set, with the diagonal, confidence band, and calibration error stated numerically. Held-out-library calibration overlaid in a paler tone to show the optimism gap.

**c. Calibration under distribution shift.** Calibration error stratified by structural distance from the frozen library. The claim is that accuracy falls but confidence falls with it.

**d. Comparators.** The same calibration assessment for comparator methods on the identical prospective set. This is where "mechanism is calibratable, similarity is not" is demonstrated rather than asserted.

**e. Soundness–resolution trade-off.** Rate of excluding the true structure against fraction resolved at each level, as elimination stringency is swept. Mark the operating point used for the atlas.

**f. Resolution-level distribution** at the operating point, as a stacked bar. This sets reader expectations for Figure 3.

*Source claims:* C4, C5.

---

## Figure 3 | The structural composition of the dark metabolome

**a. Atlas scale.** Sankey from raw spectra → dark subset → resolved statements → distinct molecular entities after collapsing. The width contraction from features to entities is itself a headline result.

**b. How big is the dark metabolome.** Entity count with uncertainty, against the feature count it was derived from, with the collapsing operations broken out (adducts, in-source fragments, isotopologues, charge states, redundant acquisition). Include the validation on known compounds as an inset.

**c. Recurrence.** Entities by number of independent datasets in which they recur, separating reproducible chemistry from single-study artefacts.

**d. Distance to known metabolite space.** Distribution of resolved entities by transformation distance to the nearest characterized metabolite. The fraction beyond one interpretable transformation is the key number.

**e. Chemical composition** against reference libraries, showing which classes are enriched and which are absent from library coverage.

**f. Uncharacterized recurrent families.** The top families with no library representative, with a representative structural statement for each and the number of entities and datasets involved.

*Source claims:* C6, C7. Rule-evolution coverage growth (C8) is one sentence in the text and lives in ED6, not here.

---

## Figure 4 | Dark structural families partition by biological origin

**a. Design.** The public perturbation datasets used, by type (germ-free/gnotobiotic, antibiotic, dietary intervention), with sample counts and platforms.

**b. Positive controls.** Metabolites of established origin recovering their known attribution, plus the label-permutation null. This panel earns the right to interpret panel c.

**c. Attribution.** Resolved families partitioned into microbiota-dependent, diet-dependent, host-associated and unresolved, with the unresolved fraction shown honestly.

**d. Structure–origin concordance.** Chemical class composition within each origin group, showing that attribution corresponds to chemistry rather than to abundance or detectability.

**e. Worked example.** One family with its members, their presence/absence pattern across perturbations, and its structural statement.

*Source claim:* C9.

---

## Figure 5 | A structurally defined family associated with a phenotype

**a. Association.** Family-level effect across the biological contrast, with biological replicates as points, effect size and adjusted significance.

**b. Family beats feature.** Per-feature significance vs family-level significance, showing that structural grouping aggregates evidence that feature-level analysis disperses.

**c. Replication** in independent cohorts.

**d. The family.** Structural statements for all members, drawn as a transformation series where members differ by interpretable edits, with resolution level and confidence annotated per member.

**e. Anchor validation.** For standard-confirmed anchors: overlaid MS/MS of sample and authentic standard, retention/coelution.

**f. An unresolved case.** The surviving isomer set for one member, the evidence that eliminated everything else, and the specific measurement that would separate the survivors. This panel is required, not optional; it is the paper's honesty made visible.

*Source claims:* C10, C11.

---

## Extended Data

| # | Title | Contents |
|---|---|---|
| ED1 | Corpora, leakage audit and dark-subset construction | Composition of every corpus; structure standardization; exact and analogue leakage audits against all pretraining data; frozen library-search protocol; mouse cohort QC |
| ED2 | Complete fragmentation-model benchmark | Full comparator matrix; same-formula and near-isomer strata; candidate-count controls; per-peak analysis; runtime and enumeration cost; intrinsic support-set properties |
| ED3 | Spectrum-identity and reasoning-verification controls | Correct/absent/shuffled-spectrum experiments with full matching; per-step trace verification; failure taxonomy; structured-CoT causal control |
| ED4 | Elimination stringency and robustness | False-exclusion rate vs stringency; sensitivity to mass tolerance, intensity threshold, noise peaks, collision energy, instrument |
| ED5 | Complete calibration and prospective validation | All calibration curves; stratifications; comparator calibration; depositing-laboratory independence audit; freeze artifact hashes |
| ED6 | Fragmentation-rule evolution | Failure localization; typed revision contracts; acceptance gates (fresh evaluation, replay, ablation, transfer); rejected revisions; coverage growth; factorial adaptation endpoint; worker cost |
| ED7 | Atlas quality control and entity collapsing | Collapsing validation; merging rules; recurrence; resolution and confidence distributions by corpus, instrument, organism; per-entry record schema |
| ED8 | Chemical composition of the dark metabolome | Distance distributions; class composition; uncharacterized families; transformation-series construction and its boundary against inferred enzymology |
| ED9 | Biological origin attribution | Dataset inventory and harmonization; presence/absence models; batch and platform controls; positive controls; permutation nulls; unresolved attributions |
| ED10 | Biological association, replication and sensitivity | Frozen family definitions; association statistics; replication; per-feature vs family evidence; threshold sensitivity; metadata permutation |
| ED11 | Complete anchor validation dossiers | Per anchor: peak table, candidate set, eliminating peaks, atom-level trajectories, standard comparison, complete alternative-candidate dossier, unresolved isomers and their discriminating measurements |

## Style

Low-saturation palette, no chartjunk, DejaVu Sans or the journal equivalent. Every axis labelled with units. Confidence intervals on every effect. Where a fraction is reported, the denominator appears in the panel. Molecule renderings use a fixed bond length across all panels so structures are visually comparable.
