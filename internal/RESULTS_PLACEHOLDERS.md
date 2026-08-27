# Results Placeholders

Every `[RESULT: ...]` and `[DATA: ...]` in `main.tex` maps to one experiment in `EXPERIMENT_EXECUTION_PLAN.md` and one artifact in `CLAIM_EVIDENCE_MATRIX.md`. A placeholder may only be replaced from that artifact.

Current count: **73** in abstract, introduction and the five Results sections.

| Section | Placeholders | Source experiments |
|---|---|---|
| Abstract + Introduction | 10 | all — fill last, after every section is frozen |
| §1 Physical fragmentation modelling | 10 | E3, E4, E5, E6 |
| §2 Calibration | 12 | E1, E2, E7, E8, E9 |
| §3 Atlas | 15 | E10, E11, E12, E13, E14, E15, E16, E17 |
| §4 Biological origin | 10 | E18, E19, E20, E21 |
| §5 Biology | 14 | E22, E23, E24, E25, E26, E27 |
| Discussion | 2 | derived from §2 and §3, no new experiment |

---

## §1 — Physical fragmentation modelling

| Placeholder | Source | Notes |
|---|---|---|
| final benchmark cohort and size | E3 | State the corpus, the split, and the leakage-audit result in the same sentence |
| final endpoint (pLSE) | E3 | Primary discrimination endpoint, preregistered |
| final comparator values | E3 | Recomputed by us on identical pools; never quoted from comparator papers |
| same-formula effect (pLSE) | E3 | The stratum that carries the claim |
| same-formula effect (similarity tied/inverted) | E3 | Report ties and inversions separately |
| ppm error (worked case) | E6 | From the Fig. 1a case |
| shuffled-spectrum effect | E4 | ED3 |
| absent-spectrum effect | E4 | ED3 |
| verified-vs-unverified accuracy effect | E5 | At matched confidence, not marginal |
| final failure taxonomy | E5 | Categories with counts |

## §2 — Calibration

| Placeholder | Source | Notes |
|---|---|---|
| library snapshot date | E0.1 | `[DATA]` |
| evaluation snapshot date | E0.1 | `[DATA]` |
| prospective set size | E1 | **Gate: ≥300.** If below, escalate before continuing |
| calibration error | E8 | With confidence interval |
| containment value and threshold | E8 | State the denominator |
| stratified calibration | E8 | By structural distance from the frozen library |
| comparator calibration | E9 | Comparators given their best available calibration |
| resolution-level fractions (×4) | E8 | Must sum to 1 including unresolved |
| soundness operating point | E2 | The false-exclusion rate the atlas was built at |

## §3 — Atlas

| Placeholder | Source | Notes |
|---|---|---|
| mouse cohort description and count | E10 | `[DATA]` — **cohort location unconfirmed; resolve before Phase 4** |
| repository spectrum count | E10 | After dark-subset filtering |
| final feature count | E12 | Before collapsing |
| final entity count | E12 | After collapsing, **with uncertainty interval** from the measured collapsing error rate |
| recurrent entity count and dataset count | E13 | Independence of datasets must be verified |
| fraction within one transformation | E14 | Reference set and transformation vocabulary frozen beforehand |
| fraction beyond one transformation | E14 | The key composition number |
| principal families | E16 | Named, with recurrence |
| class enrichment/depletion | E15 | Corrected for ionization and detectability bias |
| rule coverage before/after | E17 | ED6 |
| resolution rate before/after | E17 | The sentence that justifies rule evolution |

## §4 — Biological origin

| Placeholder | Source | Notes |
|---|---|---|
| accession list and counts | E18 | `[DATA]` — every accession manually verified against its publication |
| positive-control recovery rate | E19 | **Gate: interpret nothing until this passes** |
| permutation null result | E19 | Must abolish attribution |
| family counts by origin (×4) | E20 | Including the unresolved count, reported honestly |
| microbiota-dependent chemistry | E21 | Class enrichment |
| diet-dependent chemistry | E21 | Class enrichment |

## §5 — Biology

| Placeholder | Source | Notes |
|---|---|---|
| phenotype (section title) | E23 | Appears in the section heading; fix early |
| principal family | E22 | Frozen before testing |
| phenotype/contrast | E23 | Preregistered endpoint |
| effect size and adjusted significance | E23 | Biological replicate as unit |
| independent cohorts | E24 | Replication criterion stated in Methods |
| per-feature significance | E23 | The contrast that makes the family-level claim |
| family-level significance | E23 | |
| linked feature count | E22 | |
| transformation series count and edits | E22 | A mass difference is not a reaction |
| anchor count | E25 | Selected before purchase |
| standard-confirmed count | E26 | **Report failures too** |
| bounded-isomer anchor count | E26 | |
| unresolved isomer count | E27 | |
| discriminating experiment | E27 | The specific measurement, named |

---

## Filling rules

1. **Freeze before you look.** The artifact must be hashed before the analysis that produces the number.
2. **Denominator with every fraction.** In the sentence, not only in the figure.
3. **Uncertainty with every effect.** Point estimates alone are not fillable.
4. **Negative results are fillable results.** Rejected rule revisions, unconfirmed anchors, unresolved attributions and spectra resolving to nothing all have placeholders reserved for them.
5. **Abstract last.** Its ten placeholders are summaries of frozen section results and must not be written ahead of them.
6. **No number from a training log or notebook.** Only from the named artifact.

## Escalation triggers

Stop and re-plan rather than filling a weakened version if:

- E1 yields fewer than 100 qualifying prospective spectra;
- E2 finds no stringency with acceptable soundness;
- E19 positive controls fail to recover known origins;
- fewer than roughly 10 usable perturbation datasets exist per type;
- the mouse cohort cannot be located or its provenance cannot be frozen.
