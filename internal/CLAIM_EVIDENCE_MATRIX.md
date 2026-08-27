# Claim–Evidence Matrix

Internal truth contract. `main.tex` is written in target-final form; no claim is submission-ready until its evidence cell is bound to an immutable artifact.

The manuscript is centred on **mechanistic elimination producing calibrated structural statements**, and on the **atlas** that becomes possible once those statements exist. It is not centred on LLM reasoning, agent architecture, or on beating de novo generators at exact-match accuracy.

## Section 1 — Physical fragmentation modelling (Fig. 1)

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C1** | Mechanistic, candidate-relative elimination discriminates close structural alternatives where spectral similarity does not. | Matched-pool benchmark against exact-mass matching, forward-spectrum similarity, CFM-ID and SIRIUS/CSI:FingerID on identical spectra and identical candidate pools. | molecule group | matched candidate-set size, formula and mass constraint; difficulty strata by MCES/Morgan/scaffold defined without spectral scores; full leakage audit | `TBD:C1_mechanistic_discrimination` |
| **C2** | The discriminative evidence is bound to the measured spectrum, not to chemical plausibility. | Correct / absent / shuffled-spectrum evaluation on frozen candidate pools. | molecule group | shuffled donor from a distinct molecule group matched for adduct, neutral mass, acquisition and peak richness; chemical prior held fixed | `TBD:C2_spectral_identity` |
| **C3** | METEOR reasoning traces are verifiable step-by-step, and verification predicts structural accuracy. | Per-step verification of trace claims against pLSE; accuracy of verified vs unverified traces at matched confidence. | trace / molecule group | matched confidence bins; failure taxonomy; held-out molecules | `TBD:C3_trace_verification` |

**Boundary rules.** Peak matching is not mechanism validation — a reaction-level claim requires the atom/bond/charge trace. Global spectrum similarity is not candidate-specific evidence. Mechanism plausibility is not candidate discrimination.

## Section 2 — Calibration (Fig. 2)

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C4** | Structural resolution level is computed from the evidence, and the soundness–resolution trade-off is controllable. | Sweep elimination stringency; measure rate of excluding the true structure against the resulting resolution-level distribution. | molecule group | mass tolerance, intensity threshold, noise-peak and acquisition-metadata sensitivity; disjoint calibration split | `TBD:C4_soundness_resolution` |
| **C5** | Reported confidence is calibrated on chemistry the frozen system never saw. | Freeze the complete system against a historical library snapshot; evaluate on spectra dark at that time whose structures were independently deposited before the evaluation snapshot. | spectrum / structure | no structure or close analogue present at freeze; depositing-laboratory independence audit; stratification by structural distance from the frozen library; comparator methods scored on the identical set | `TBD:C5_prospective_calibration` |

**C5 is the credibility spine of the manuscript.** If it fails, the atlas cannot be released as a resource and the paper reverts to a benchmark study. Execute it before committing to Sections 3–5.

## Section 3 — Atlas (Fig. 3)

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C6** | Structural resolution collapses dark features onto a far smaller number of distinct molecular entities, giving the first structure-based estimate of the size of the dark metabolome. | Adduct / in-source-fragment / isotopologue / charge-state collapsing followed by structural merging across the mouse and repository corpora. | molecular entity | collapsing validated on known compounds with known ion forms; recurrence across independent datasets; sensitivity to confidence threshold | `TBD:C6_entity_count` |
| **C7** | A substantial fraction of the dark metabolome lies outside one interpretable transformation of any characterized metabolite. | Distance-to-known-metabolite analysis over resolved entities; chemical-class composition against reference libraries. | molecular entity | reference metabolite set frozen; transformation vocabulary preregistered; class assignment restricted to entities resolved at or above class level | `TBD:C7_composition` |
| **C8** | Automated fragmentation-rule evolution extends coverage beyond the curated rule set and is what makes repository-scale resolution possible. | Coverage growth by chemical class and its effect on resolution rate, with rejected revisions retained. | rule / chemical class | fresh deterministic evaluation, causal replay, ablation and cross-family transfer required for acceptance; no regression elsewhere; low-cost workers restricted to proposal | `TBD:C8_rule_evolution` |

C8 is **supporting**, reported in one paragraph and ED6. It must not expand into a main figure.

## Section 4 — Biological origin (Fig. 4)

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C9** | Resolved dark structural families partition by biological origin using perturbation data already deposited by others. | Presence/absence modelling of family members across public germ-free/gnotobiotic, antibiotic and dietary-intervention mouse datasets. | structural family / dataset | positive-control panel of metabolites with established origin; label-permutation null; batch and platform controls; families consistent with multiple origins left unresolved | `TBD:C9_origin_attribution` |

**Boundary rule.** This establishes *dependence*, not biosynthetic route. Manuscript language must say microbiota-dependent, diet-dependent or host-associated, never "microbially synthesized", unless a biosynthetic experiment exists.

## Section 5 — Biology (Fig. 5)

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C10** | A structurally defined dark family is reproducibly associated with a biological contrast, and the association is carried by the family rather than by any single feature. | Association testing after family freezing; per-feature vs family-level evidence; replication in independent cohorts. | biological sample | families frozen before any association testing; multiplicity control across preregistered endpoints; metadata-permutation control; sensitivity to confidence and resolution-level thresholds | `TBD:C10_biological_association` |
| **C11** | Selected anchors are confirmed by authentic standards; unresolved anchors are retained as bounded isomer sets with their discriminating measurement stated. | Authentic standard MS/MS and retention/coelution matching for commercially available anchors. | molecular hypothesis | anchors selected from a frozen discovery criterion before purchase; complete alternative-candidate dossier; explicit level reporting | `TBD:C11_anchor_validation` |

**Boundary rule.** Levels 5 (unique putative structure at threshold) and 6 (orthogonally confirmed) are never merged.

## Submission gates

**Minimum gate.** C1–C7 and C10 complete, C11 with at least two standard-confirmed anchors.

**Nature-main-track gate.** C5 exceptionally strong, including comparator calibration on the identical prospective set. C6 and C7 must yield numbers the field does not currently have. C9 must survive its permutation null.

## Removed from the manuscript

- **Evidence-guided acquisition (former C10).** Requires new MS acquisition, which is out of budget. Retained only as a stated future direction in the Discussion.
- **Factorial co-evolution endpoint (former C4/C5).** The `(H0,E0)/(HT,E0)/(H0,ET)/(HT,ET)` design and gated-vs-ungated controls move to ED6 as acceptance evidence for rule evolution, not as a main claim.
- **Structured CoT six-arm causal control.** Implementation-level, Extended Data only.
- **Intrinsic FMF retrieval / information-bit scaling.** Property of a representation, not a finding about the world. Methods and ED2 only.

## Standing claim-boundary rules

1. Repeated spectra are not independent samples; population inference occurs after molecule-group aggregation.
2. Training improvement is not scientific improvement; loss and token accuracy cannot substitute for held-out molecular endpoints.
3. Generator failure is not evidence failure; candidate recall, conditional discrimination and end-to-end resolution are reported separately.
4. Dark-spectrum predictions are not identifications.
5. A mass difference alone does not establish an enzymatic reaction.
6. Mechanistic completeness is empirical, not provable; elimination stringency is calibrated to a measured false-exclusion rate and reported as such.
7. Do not claim mechanism is more accurate than learned models. Published in-distribution comparisons say the opposite. The claim is that mechanism yields calibratable eliminations.
