# Claim–Evidence Matrix

This file is the internal truth contract for the manuscript. `main.tex` is intentionally written in target-final form, but no central claim is submission-ready until its evidence cell is bound to an immutable artifact.

The manuscript is now centred on **adaptive candidate-specific fragmentation evidence**, not on LLM reasoning or agent architecture.

| ID | Target manuscript claim | Primary display | Required experiment | Statistical unit | Minimum controls | Final artifact |
|---|---|---|---|---|---|---|
| **C1** | Static spectral evidence loses discriminative power as molecular alternatives become harder, across candidate generators and evidence systems. | Fig. 1 | Cross-generator, cross-evidence-system hardness audit with matched candidate-set size/formula/mass constraints. | molecule group | ≥2 independent candidate sources; ≥2 frozen evidence systems; leakage audit; matched pool size | `TBD:C1_evidence_bottleneck` |
| **C2** | Candidate-specific atom-traceable fragmentation evidence outperforms mass-only and non-candidate-specific fragmentation/simulation evidence on hard same-formula alternatives. | Fig. 2 | Hard-decoy benchmark with external fragmentation/forward comparators and mechanistic ablations. | molecule group | exact mass; opportunity-normalized; forward-spectrum; CFM-ID/SIRIUS-derived or other executable comparator; generic-cut; pLSE ablations | `TBD:C2_candidate_specific_evidence` |
| **C3** | The decisive evidence depends on the experimental spectrum rather than chemical prior alone. | Fig. 3 | Correct / no-spectrum / mass-adduct-matched shuffled-spectrum evaluation on frozen candidate pools. | molecule group | distinct shuffled donor; same adduct; neutral-mass matching; frozen chemical prior | `TBD:C3_spectral_identity_lift` |
| **C4** | Reciprocal adaptation improves the final held-out endpoint beyond adapting either hypothesis or evidence alone. | Fig. 4 | Factorial endpoint evaluation of `(H0,E0)`, `(HT,E0)`, `(H0,ET)`, `(HT,ET)` plus interaction effect. | molecule group | identical final cases/pools; frozen snapshots; fixed-side controls | `TBD:C4_factorial_adaptation` |
| **C5** | Gated reciprocal adaptation is more stable than ungated/blind alternation and exhibits post-freeze challenge–recovery dynamics. | Fig. 4 / ED7 | Gated vs ungated control + complete cross-generation matrix computed after snapshot freeze. | molecule group / run | frozen anchor; non-target; success bank; replicate runs; rejected moves retained | `TBD:C5_gated_challenge_recovery` |
| **C6** | Adapted pLSE transfers to candidate distributions produced outside ORBIT. | Fig. 4 | External-generator/retrieval candidate benchmark. | molecule group | no pLSE-guided generation/reranking; identical standardization; same-formula/near-isomer strata | `TBD:C6_external_transfer` |
| **C7** | Structural uncertainty can be represented by risk-controlled candidate sets, while generator recall and conditional discrimination remain separately measurable. | Fig. 4 | Independent calibration + final held-out prediction-set evaluation. | molecule group | disjoint calibration split; candidate recall reported separately; ambiguous-isomer controls | `TBD:C7_risk_controlled_resolution` |
| **C8** | The mouse cohort validates deployment on real unlabelled spectra without lowering structural-identification standards. | Fig. 5 | Blinded anchor evaluation + frozen dark-spectrum analysis. | anchor molecule group; biological replicate for recurrence | hidden anchor labels; blanks/QC; frozen library-hit exclusion | `TBD:C8_mouse_deployment` |
| **C9** | Selected dark mouse hypotheses are supported by orthogonal evidence or are explicitly retained as unresolved candidate sets. | Fig. 5 / ED10 | Authentic standard, coelution/RT, targeted MSn, blinded reveal, NMR or other preregistered orthogonal validation. | molecular hypothesis | full alternative-candidate dossier; evidence-level reporting | `TBD:C9_mouse_validation` |
| **C10 (Nature-extension)** | Evidence-guided acquisition prospectively selects a new MS measurement that reduces residual molecular ambiguity. | Future main/ED only if completed | Ambiguous MS2 → preregistered experiment selection → prospective MSn/CE acquisition → candidate-space contraction. | molecular case | fixed candidate set before acquisition; baseline acquisition policy; blinded outcome where feasible | `TBD:C10_active_acquisition` |

## Submission gates

### Minimum strong methods paper gate
C1–C8 must be complete, with C9 containing at least several strong validation cases if the mouse dark-spectrum application is a major conclusion.

### Nature-main-track gate
C1–C9 should be exceptionally strong. C10 is the preferred additional result because it converts adaptive evidence interpretation into true sequential hypothesis–experiment co-design.

## Supporting, non-central claim

The structured CoT six-arm experiment is retained as an implementation-level causal control in Extended Data. It is **not** a central Nature claim and is not required to define the scientific novelty of ORBIT-MS.

## Claim-boundary rules

1. **Peak matching is not mechanism validation.** A reaction-level claim requires the corresponding atom-/bond-/charge-level trace.
2. **Mechanism plausibility is not candidate discrimination.** Figure 2 must evaluate the same spectrum against matched competing structures.
3. **Global spectrum similarity is not candidate-specific evidence.** Simulation may be a comparator but cannot substitute for GT–decoy selectivity.
4. **Chemical prior is not experimental evidence.** Figure 3 requires no-spectrum and shuffled-spectrum controls.
5. **Repeated spectra are not independent samples.** Population inference occurs after molecule-group aggregation.
6. **Training improvement is not scientific improvement.** Loss, token accuracy and pLSE reward cannot substitute for held-out molecular endpoints.
7. **Cross-generation heatmaps do not by themselves prove co-evolution.** The factorial endpoint comparison is the principal causal control.
8. **Generator failure is not evidence failure.** Candidate recall, conditional discrimination and end-to-end resolution must be reported separately.
9. **Dark-spectrum predictions are not identifications.** Mouse claims require explicit confidence terminology and orthogonal validation for structure-level identification.
10. **Experimental evidence does not literally evolve unless a new measurement is acquired.** Until C10 is complete, manuscript language should refer to adaptive evidence interpretation/modeling rather than co-evolving experimental evidence.
