# Mouse Cohort Protocol

The private mouse spectra support the Nature story only if the manuscript preserves a strict separation between **census construction**, **external structural validation** and **biological inference**.

## Role in the manuscript

The mouse cohort supports the **discovery half** of the WGV paper after the World/evidence hierarchy is frozen.

- **Figure 3 — high-evidence dark resolution.** Mouse dark spectra contribute to the repository-scale evidence funnel, entity collapse and recurrence analysis.
- **Figure 4 — structural and biological organization.** Where perturbation metadata permit, mouse datasets contribute to microbiota/diet/host dependence over frozen structural families.
- **Figure 5 — biological value.** The same biological samples are analysed as anonymous features and as frozen structural families to test whether structure improves reproducibility; the principal programme may be drawn from this cohort if it satisfies the preregistered criteria.

The cohort is **not** used to define World chemistry, tune evidence thresholds or calibrate prospective reliability. Those are established before dark-corpus deployment.

---
---

## 1. Freeze the cohort before atlas analysis

Create an immutable manifest containing:
- raw-file identities and hashes;
- biological sample IDs;
- biological replicate structure;
- experimental groups/phenotypes;
- acquisition metadata;
- preprocessing/QC version;
- blank/QC labels;
- feature/spectrum identifiers;
- the frozen library-search protocol defining the dark subset.

No structural family, phenotype subgroup or “representative” case is selected before the manifest is frozen.

---

## 2. Separate three branches

### A. Known-anchor branch
Spectra with independent structure/reference support hidden from ORBIT.

Use only for:
- external domain-shift diagnostics;
- candidate recall;
- conditional evidence performance;
- false-resolution audit.

These results belong in Extended Data because Figure 1 already carries the primary credibility claim.

### B. Dark-census branch
Spectra lacking an accepted spectral-library match under the frozen search protocol.

Use for:
- feature-to-entity collapse;
- structural resolution distribution;
- recurrence;
- structural-family construction.

Dark means “unannotated under the frozen spectral-library protocol”, not “absent from PubChem/HMDB”.

### C. Biological-analysis branch
The subset of biological samples with a predefined contrast/phenotype and sufficient replication.

Use for:
- anonymous feature-level analysis;
- frozen structural-family analysis;
- paired comparison of biological reproducibility.

The same samples, covariates and preprocessing must be used in both analysis arms.

---

## 3. Structural resolution hierarchy

Track every entity through:

1. unresolved;
2. formula only;
3. chemical class / shared substructure;
4. bounded isomer set;
5. unique putative 2D structure under the frozen operating point;
6. reference-standard-confirmed structure.

Levels 5 and 6 are never merged.

For Figure 2 census, report counts at every level so the entity total is not misread as a number of unique identifications.

---

## 4. Entity collapsing

Mouse data are especially vulnerable to feature inflation from:
- adducts;
- isotopologues;
- charge states;
- in-source fragments;
- multiple collision-energy acquisitions;
- technical replicates.

The collapsing rules are validated on known compounds before use on the dark branch. The measured over-/under-merging error contributes directly to uncertainty in the Figure 2 entity count.

Structural merging must never use phenotype labels.

---

## 5. Family freezing before biology

A structural family is defined using chemistry only:
- bounded structural core / graph relation;
- frozen structural-distance rule;
- confidence/resolution threshold;
- recurrence rule.

Hash family membership before any phenotype/source association is tested.

Do not:
- merge features because they co-vary biologically;
- split a family because one subgroup gives a stronger P value;
- tune structural thresholds to maximize biological significance.

---

## 6. Figure 5 paired analysis

The primary question is no longer “can we find one significant family?”

It is:

> **Does replacing anonymous dark features with frozen structural families systematically improve reproducibility of biological inference?**

Run the same cohort twice:

### Feature arm
Each dark feature is an independent analyte.

### Structural-family arm
Features are aggregated or jointly modelled under frozen structural-family membership.

Pre-register one primary global endpoint, preferably:
- cross-cohort replication rate; or
- effect-sign concordance across independent cohorts.

Secondary endpoints may include:
- multiplicity-controlled association yield;
- effect-size stability;
- variance explained/predictive stability where statistically appropriate.

The principal family case is selected only after this global comparison is frozen.

---

## 7. Biological inference rules

- Biological samples are the unit of inference.
- Technical spectra never inflate n.
- Multiplicity is controlled over the preregistered family/endpoint universe.
- Covariates and exclusion rules are fixed before association testing.
- Leave-one-cohort-out and metadata-permutation controls are required for the main family claim.
- An association surviving only under permissive structural-confidence thresholds is reported as threshold-sensitive.

If structural-family analysis does not systematically improve on feature analysis, Figure 5 must be reframed rather than replaced by one cherry-picked positive family.

---

## 8. Case-study eligibility

A principal dark family enters Figure 5 only if it has:
- frozen family definition;
- recurrence across independent biological samples/datasets;
- acceptable structural resolution/confidence;
- multiplicity-controlled biological association;
- independent replication or leave-one-cohort-out stability;
- a complete alternative-structure dossier.

Prefer a family that connects multiple previously anonymous features into one coherent programme.

---

## 9. Orthogonal validation

Structure-level “identification” normally requires:
- authentic/synthetic standard;
- matched MS/MS;
- retention/coelution or comparably strong orthogonal evidence.

Anchor selection criteria are frozen before purchase.

Report:
- successful anchors;
- failed anchors;
- ambiguous anchors;
- alternatives that remain.

A failed standard is a result, not a reason to remove the case from the denominator.

---

## 10. Source attribution

If mouse perturbation data are used for Figure 4:
- germ-free/gnotobiotic, antibiotic and dietary datasets are harmonized separately;
- positive-control metabolites must recover expected dependence;
- label permutation must destroy attribution;
- batch/platform/study effects are modelled;
- mixed and unresolved families remain explicit.

Use “microbiota-dependent”, “diet-dependent” and “host-associated”. Do not infer a biosynthetic route from dependence alone.

---

## 11. Evidence-guided acquisition

No new targeted acquisition is assumed.

For unresolved entities, the released atlas may contain:
- surviving alternatives;
- discriminating peak/path evidence;
- the additional MSn/CE/orthogonal measurement predicted to separate them.

This is a **predicted experimental agenda**, not a performed validation.

---

## 12. Release plan

Before publication:
- deposit raw/processed spectra when permissions permit;
- release de-identified sample/feature manifests;
- release structural-entity and family membership tables;
- release per-entry resolution/confidence/evidence records;
- archive frozen candidate pools and evaluation configuration;
- publish the exact feature-versus-family biological-analysis code.
