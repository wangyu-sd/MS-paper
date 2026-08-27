# Experiment Execution Plan

Ordered by **what can kill the paper earliest and cheapest**, not by manuscript order. Two experiments (E1, E2) decide whether the current framing survives; both are cheap and neither needs the GPUs currently occupied by METEOR training. Nothing downstream should be started before they return.

## Resource constraints binding every decision

- **GPU.** 8×H20 committed to METEOR training until approximately 10 September. Treat GPU as unavailable until then except for short inference jobs. Most of this plan is CPU-bound by design.
- **Wet lab.** Authentic standards only, and only commercially available compounds. No new acquisition, no targeted MSn, no perturbation experiments, no isolation or NMR.
- **Data on hand.** GeMS/DreaMS repository corpus (GeMS-A 82 GB, GeMS-B 37 GB, GeMS-C 389 GB; DreaMS Atlas over 201 M spectra with MassIVE metadata for 15,760 datasets); public library corpus (GNPS2, MassBank, MoNA, CASMI2022, NIST23); HMDB; MassSpecGym with MCES splits; public IBD cohort pipeline. **Mouse cohort location must be confirmed before Phase 4.**

---

## Phase 0 — Freeze and inventory (2 days, CPU)

**E0.1 Library snapshot construction.** Reconstruct GNPS/MassBank/MoNA at two dates: a freeze date (target: 2023-06) and an evaluation date (current). Record per-structure first-appearance dates and depositing accession. Output: `snapshots/lib_freeze.parquet`, `snapshots/lib_eval.parquet`.

**E0.2 Corpus inventory.** Per-corpus spectrum counts, adduct/instrument/collision-energy distributions, and the frozen library-search protocol that defines "dark". Output: ED1 source data.

**E0.3 Leakage audit.** Exact-structure and close-analogue (Tanimoto ≥ 0.7 or MCES < 10) overlap between every evaluation set and all pretraining corpora, including ZINC/PubChem used for METEOR and any simulator-generated training data. Output: ED1 audit table.

---

## Phase 1 — Go/no-go (1 week, CPU)

### E1 — Is the prospective set constructible? *(hours)*

Diff `lib_eval` against `lib_freeze`. Count structures deposited in the interval, then intersect with spectra present but unannotated in the repository corpus at freeze.

- **Pass:** ≥ 300 spectra dark at freeze whose structures were independently deposited later, spanning ≥ 3 chemical superclasses and ≥ 5 depositing groups.
- **Marginal:** 100–300 → widen the interval (freeze earlier), accept a weaker but still blinded assessment.
- **Fail:** < 100 → C5 cannot be the credibility spine. Fall back to a held-out-library calibration plus a scaffold-disjoint stress test, and downgrade the atlas from "resource" to "large-scale application". **Tell the team immediately if this happens; it changes the paper.**

Depositing-laboratory independence must be auditable, and any structure whose close analogue existed at freeze is excluded.

### E2 — Does elimination have a usable soundness–resolution trade-off? *(2–4 days)*

On MassSpecGym MCES-split test spectra with known answers and matched candidate pools, sweep elimination stringency. For each setting record the false-exclusion rate (true structure eliminated) and the resolution-level distribution.

- **Pass:** at a false-exclusion rate ≤ 5%, ≥ 40% of spectra resolve to unique structure, bounded isomer set, or class. That is enough for a usable atlas.
- **Marginal:** resolution collapses to "formula only" for most spectra at acceptable soundness → the atlas exists but its scientific content is thin. Consider whether entity counting and composition (C6, C7) still carry Section 3; they may, since both work at class level.
- **Fail:** no stringency gives acceptable soundness → mechanistic elimination is not reliable enough for this design. Revert to candidate-relative scoring with conformal sets and rewrite Sections 1–2.

E2 is the experiment previously discussed as the ranking-decay probe, reframed: what matters is not whether mechanism beats learned scorers on accuracy, but whether its errors are controllable.

---

## Phase 2 — Section 1 (2 weeks, CPU + short GPU)

**E3 Matched-pool discrimination benchmark (C1).** Comparators receive identical spectra and identical candidate pools: exact-mass matching, forward-spectrum similarity, CFM-ID 4.0, SIRIUS/CSI:FingerID. Difficulty strata defined without spectral scores. Report same-formula stratum separately. *Cost: CPU-heavy; CFM-ID is the bottleneck, budget several hundred core-hours.*

**E4 Spectrum-identity controls (C2).** Correct / absent / shuffled-spectrum on frozen pools, donors matched for adduct, neutral mass, acquisition and peak richness. *Reuse the existing donor-selection code.*

**E5 Trace verification (C3).** Per-step verification of METEOR traces against pLSE; accuracy of verified vs unverified at matched confidence; failure taxonomy. *Short GPU job; can run against the current checkpoint without waiting for training to finish.*

**E6 Per-peak information analysis (Fig. 1d).** Contribution of each peak to the discriminative margin against its intensity.

---

## Phase 3 — Section 2 (1 week, CPU)

**E7 Confidence model and calibration fitting.** Fit on a disjoint calibration split. Never fit on the prospective set.

**E8 Prospective evaluation (C5).** Run the frozen system on the E1 set. Report calibration error, containment at threshold, and stratification by structural distance from the frozen library.

**E9 Comparator calibration (Fig. 2d).** The identical assessment for comparators. This panel is what converts "we are calibrated" into "we are calibrated and they are not"; do not skip it.

**Freeze artifacts before E8:** model weights, rule set, calibration mapping, candidate-generation configuration, all hashed and recorded.

---

## Phase 4 — Atlas construction (1–2 weeks, GPU after 10 Sept)

**E10 Dark-subset definition.** Apply the frozen library-search protocol to mouse and repository corpora; remove accepted exact matches; retain the remainder.

**E11 Atlas run.** Estimated cost: a reverse trace is roughly 2,000 tokens; 10⁶ spectra is about 2×10⁹ tokens. With vLLM batched inference on 8 GPUs this is 1–3 days. **Compute is not the constraint; do not over-invest in scaling and under-invest in E8.**

**E12 Entity collapsing (C6).** Adduct, in-source-fragment, isotopologue and charge-state collapsing, then structural merging. Validate the collapsing rules on known compounds with known ion forms before applying to dark spectra. Report the entity count with uncertainty.

**E13 Recurrence.** Entities by number of independent datasets.

---

## Phase 5 — Composition (1 week, CPU)

**E14 Distance to known metabolite space (C7).** Freeze the reference metabolite set and the transformation vocabulary before running. Report the fraction beyond one interpretable transformation.

**E15 Chemical class composition** against reference libraries; identify classes absent from library coverage.

**E16 Uncharacterized recurrent families.** Families with no library representative, ranked by recurrence.

**E17 Rule-evolution coverage growth (C8).** Coverage by chemical class before and after evolution, and its effect on resolution rate. Retain rejected revisions. *This is one paragraph and ED6; timebox it.*

---

## Phase 6 — Biological origin (2 weeks, CPU)

**E18 Perturbation dataset assembly.** Filter MassIVE metadata (`species_resolved`, title, description, keywords) for mouse datasets containing germ-free/gnotobiotic controls, antibiotic treatment or defined dietary intervention. Manually verify every included accession; automated metadata parsing is not sufficient evidence of design.

**E19 Positive-control validation.** Metabolites of established origin must recover their known attribution before any dark family is interpreted. Include a label-permutation null.

**E20 Attribution (C9).** Presence/absence modelling across studies with batch and platform controls. Families consistent with more than one origin are left unresolved.

**E21 Structure–origin concordance.** Class composition within each origin group.

**Risk.** This phase depends entirely on public data containing enough well-designed mouse perturbation studies. Run a scoping query during Phase 0 so the risk surfaces early; if fewer than roughly 10 usable datasets exist per perturbation type, Section 4 must be replaced (candidate replacement: tissue and compartment distribution across the mouse atlas, which needs no perturbation data).

---

## Phase 7 — Biology and validation (3–4 weeks + standards lead time)

**E22 Family freezing.** Freeze family definitions and transformation graphs, with hashes, before any association testing.

**E23 Association testing (C10).** Biological replicates as the unit. Multiplicity control across preregistered endpoints. Per-feature vs family-level evidence.

**E24 Replication** in independent cohorts.

**E25 Anchor selection and purchase (C11).** Select 2–4 anchors from a frozen discovery criterion, restricted to commercially available compounds. **Order early — standards lead time is often 4–8 weeks and is the critical path for submission.**

**E26 Standard validation.** Matched MS/MS and retention/coelution. Report anchors that fail to confirm.

**E27 Unresolved case dossier.** For one representative member: surviving isomer set, eliminating evidence, and the specific measurement that would separate the survivors.

---

## Critical path

`E1 → E2 → (E3–E6 ‖ E7–E9) → E10–E13 → E14–E16 → E18–E21 → E22–E24 → E26`

with **E25 ordered as soon as E22 freezes**, because standards lead time, not compute, determines the submission date.

## Standing rules

1. Freeze before you look. Every evaluation set, family definition and calibration mapping is hashed before the analysis that consumes it.
2. Report the denominator with every fraction.
3. Retain and report negative results: rejected rule revisions, unconfirmed anchors, unresolved attributions, spectra that resolve to nothing.
4. No placeholder in `main.tex` is filled from a training log or an exploratory notebook. Only from an immutable artifact named in the claim–evidence matrix.
5. If E1 or E2 fails, stop and re-plan rather than proceeding with a weakened version of the same claim.
