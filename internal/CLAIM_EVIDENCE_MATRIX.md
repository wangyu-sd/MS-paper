# Claim–Evidence Matrix

This file is the internal truth contract for the manuscript. The prose in `main.tex` is written in target-final form, but a claim becomes submission-ready only when every required evidence cell below is bound to an immutable artifact.

| ID | Target manuscript claim | Primary display | Required experiment | Statistical unit | Minimum controls | Final artifact |
|---|---|---|---|---|---|---|
| C1 | Better molecular hypotheses become harder to distinguish with static spectral evidence. | Fig. 1 | Cross-frontier hardness audit over frozen candidate generations. | molecule group | identical spectra; fixed evidence model; structural leakage audit | `TBD:C1_cross_frontier_hardness` |
| C2 | Atom-traceable CID evidence improves GT–decoy discrimination beyond mass-only or generic structural matching. | Fig. 2 | Same-formula/near-isomer hard-decoy benchmark with mechanistic ablations. | molecule group | mass-only; opportunity-normalized; generic cut; reaction-centre; charge/H; full pLSE | `TBD:C2_plse_discrimination` |
| C3 | The decisive signal is experimental-spectrum-specific rather than chemical prior alone. | Fig. 3 | Correct / no-spectrum / mass-adduct-matched shuffled-spectrum paired evaluation. | molecule group | fixed candidate pools; distinct shuffled donor; no spectrum | `TBD:C3_spectral_lift` |
| C4 | Explicit fragmentation reasoning contributes causally to the molecular decision. | Fig. 3 | Parent/pilot × normal/no-CoT/shuffled-CoT six-arm experiment. | molecule group | frozen prompts and cases; FWER control; non-target gates | `TBD:C4_cot_causal` |
| C5 | Hypothesis and evidence frontiers exhibit reciprocal challenge–recovery rather than blind alternation. | Fig. 4 | Complete cross-generation matrix evaluated after snapshots freeze. | molecule group | frozen anchor; non-target; success bank; rejected moves retained | `TBD:C5_cross_generation` |
| C6 | Adapted pLSE transfers to candidates generated outside ORBIT. | Fig. 5 | External-generator candidate benchmark. | molecule group | no pLSE-guided generation/reranking; identical standardization | `TBD:C6_external_transfer` |
| C7 | ORBIT knows when MS/MS evidence is insufficient for unique 2D structure resolution. | Fig. 5 | Calibration + selective prediction on held-out data. | molecule group | independent calibration split; ambiguous-isomer cases | `TBD:C7_abstention` |
| C8 | The mouse cohort validates deployment on real unlabelled spectra without lowering identification standards. | Fig. 6 | Blinded anchor evaluation + dark-spectrum deployment. | independent feature/molecule group; biological replicate for recurrence | hidden anchor labels; library-hit exclusion; blanks/QC | `TBD:C8_mouse_deployment` |
| C9 | Selected mouse hypotheses are experimentally/orthogonally supported. | Fig. 6 / ED10 | Standard, RT, MSn, blinded reveal or other preregistered orthogonal validation. | molecular hypothesis | alternative-candidate dossier | `TBD:C9_mouse_validation` |
| C10 | Any reported biological association is reproducible and not a post hoc annotation story. | Fig. 6 only if supported | Predefined phenotype/tissue analysis in independent biological samples. | biological replicate | multiple-testing control; annotation confidence stratification | `TBD:C10_mouse_biology` |

## Submission gate

A Nature-level submission should not proceed unless **C1–C8 are complete**. C9 should contain multiple strong cases if the dark-spectrum application is a major conclusion. C10 is optional: omit biological storytelling if the private mouse cohort does not contain a reproducible biological contrast.

## Claim-boundary rules

1. **Peak matching is not mechanism validation.** A mechanism claim requires the corresponding atom-/bond-/charge-level trace.
2. **Mechanism plausibility is not candidate discrimination.** Fig. 2 must show GT–decoy selectivity.
3. **Chemical prior is not spectrum evidence.** Fig. 3 must include no-spectrum and shuffled-spectrum controls.
4. **Repeated spectra are not independent samples.** Inference is performed after molecule-group aggregation.
5. **Training improvement is not scientific improvement.** Loss, token accuracy and pLSE reward cannot substitute for held-out molecular endpoints.
6. **Dark-spectrum predictions are not identifications.** Mouse claims must use an explicit confidence hierarchy and orthogonal validation where structure-level identification is asserted.
7. **Cross-generation results are post-freeze analyses.** Do not tune intermediate frontiers on the matrix intended to demonstrate co-evolution.
