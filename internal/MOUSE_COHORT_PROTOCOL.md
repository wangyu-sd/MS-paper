# Mouse Cohort Protocol

The private mouse spectra are scientifically valuable only if the manuscript preserves the distinction between **external deployment** and **ground-truth validation**.

## 1. Freeze the cohort before ORBIT analysis

Create an immutable manifest containing:
- raw-file identities and hashes;
- biological sample IDs and replicate structure;
- acquisition metadata;
- preprocessing/QC version;
- blank/QC labels;
- feature/spectrum identifiers.

Do not select the “best-looking” spectra after seeing ORBIT outputs and then call the result a cohort-level validation.

## 2. Construct two analysis branches

### Anchor branch
Spectra with independent structure/reference support that can be hidden from ORBIT.

Purpose:
- blinded external accuracy;
- calibration;
- false-resolution rate;
- domain-shift analysis.

The hidden label must not be exposed to candidate generation, pLSE development or threshold calibration.

### Dark branch
Spectra with no accepted exact spectral-library annotation under a frozen search protocol.

Purpose:
- candidate-space contraction;
- reproducibility;
- auditable hypotheses;
- prospective prioritization.

Dark does **not** mean “molecule absent from every chemical database.” A structure may exist in PubChem while its experimental spectrum remains unannotated.

## 3. Annotation depth

Track every spectrum through a hierarchy:
1. unresolved spectrum;
2. molecular formula;
3. chemical class / structural family;
4. bounded candidate set;
5. unique high-confidence 2D structure hypothesis;
6. orthogonally confirmed structure.

Do not merge levels 5 and 6.

## 4. Case-study eligibility

A dark-spectrum case enters the main text only if it has:
- recurrent detection across independent samples or another strong reason for prioritization;
- a compact candidate set with close alternatives;
- at least one candidate-specific high-authority evidence path;
- a complete alternative-candidate dossier;
- explicit statement of what is still unresolved.

Prefer cases that illustrate different scientific outcomes: one resolved, one partially resolved/unresolved, and one orthogonally validated if available.

## 5. Orthogonal validation hierarchy

Strongest to weaker forms depend on available material, but structure-level “identification” should normally require a reference standard with matching MS/MS and retention/coelution or another comparably strong orthogonal route.

Possible supporting evidence:
- authentic/synthetic standard;
- retention time/coelution;
- targeted MSn;
- isotope/adduct consistency;
- independent curated library match revealed only after blind prediction;
- biological recurrence;
- database/literature consistency.

The latter items support a hypothesis but should not be relabelled as standard-confirmed identification.

## 6. Biology

Do not manufacture a biological story from annotation output.

A biological association is promoted to the main text only when:
- the biological comparison existed independently of ORBIT hypothesis selection;
- biological replicates, not spectra, are the statistical unit;
- multiple testing is controlled;
- the association survives reasonable annotation-confidence thresholds;
- the chemistry is plausible and, ideally, orthogonally validated.

Otherwise Fig. 6 remains a deployment/discovery figure, which is already scientifically valuable.

## 7. Release plan

Before publication:
- deposit raw/processed spectra when permissions allow;
- release a de-identified manifest linking manuscript feature IDs to repository accessions;
- publish candidate pools and evidence certificates;
- archive the frozen ORBIT release and evaluation configuration.
