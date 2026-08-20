# Mouse Cohort Protocol

The private mouse spectra are scientifically valuable only if the manuscript preserves the distinction between **external deployment**, **blinded validation** and **ground-truth structural identification**.

## 1. Freeze the cohort before ORBIT analysis

Create an immutable manifest containing:
- raw-file identities and hashes;
- biological sample IDs and replicate structure;
- acquisition metadata;
- preprocessing/QC version;
- blank/QC labels;
- feature/spectrum identifiers;
- the exact library-search protocol used to define the dark subset.

Do not select the “best-looking” spectra after seeing ORBIT outputs and then call the result a cohort-level validation.

## 2. Construct two analysis branches

### Anchor branch
Spectra with independent structure/reference support that can be hidden from ORBIT.

Purpose:
- blinded external candidate recall;
- conditional discrimination given the reference is in the candidate set;
- risk-controlled end-to-end resolution;
- false-resolution rate;
- domain-shift analysis.

The hidden reference must not be exposed to candidate generation, pLSE development or structural-set calibration.

### Dark branch
Spectra with no accepted exact spectral-library annotation under the frozen search protocol.

Purpose:
- candidate-space contraction;
- risk-controlled structural sets;
- reproducibility across biological samples;
- auditable molecular hypotheses;
- prioritization for orthogonal validation or targeted follow-up.

Dark does **not** mean “molecule absent from every chemical database.” A structure may exist in PubChem/HMDB while its experimental spectrum remains unannotated.

## 3. Annotation depth

Track every spectrum through a hierarchy:
1. unresolved spectrum;
2. molecular formula;
3. chemical class / structural family;
4. risk-controlled bounded candidate set;
5. unique putative 2D structure at the frozen structural-risk threshold;
6. orthogonally confirmed structure.

Do not merge levels 5 and 6.

## 4. Separate generator and evidence failures

For every blinded anchor analysis report:
- whether the reference structure is present in the generated candidate set;
- the rank/set result conditional on reference presence;
- the end-to-end resolution result.

Do not describe a missing reference candidate as a pLSE/evidence-ranking error.

## 5. Case-study eligibility

A dark-spectrum case enters the main text only if it has:
- recurrent detection across independent samples or another preregistered reason for prioritization;
- a compact but non-trivial candidate set containing close alternatives;
- at least one candidate-specific high-authority evidence path, or a scientifically important unresolved outcome;
- a complete alternative-candidate dossier;
- explicit statement of what remains unresolved.

Prefer cases illustrating distinct outcomes: one strongly narrowed/resolved, one deliberately unresolved and one orthogonally validated if available.

## 6. Orthogonal validation hierarchy

Structure-level “identification” should normally require a reference standard with matching MS/MS and retention/coelution or another comparably strong orthogonal route.

Possible evidence includes:
- authentic/synthetic standard;
- retention time/coelution;
- targeted MSn;
- isotope/adduct consistency;
- independent curated reference revealed only after blind prediction;
- NMR where material permits;
- biological recurrence;
- database/literature consistency.

The latter evidence types can support a hypothesis but must not be relabelled as standard-confirmed identification.

## 7. Main Figure 5 reporting

Figure 5 should contain:
- cohort design and blinded anchor/dark split;
- anchor candidate recall, conditional discrimination and risk-controlled end-to-end resolution;
- candidate-space contraction in the dark subset;
- recurrence across samples;
- at least one complete evidence dossier with orthogonal support;
- at least one unresolved isomer case.

Do not use “annotation depth increased” as the sole biological result.

## 8. Biology

Do not manufacture a biological story from annotation output.

A biological association enters the main text only when:
- the biological comparison existed independently of ORBIT hypothesis selection;
- biological replicates, not spectra, are the statistical unit;
- multiple testing is controlled;
- the association survives reasonable annotation-confidence/risk thresholds;
- the chemistry is plausible and preferably orthogonally validated.

Otherwise Figure 5 remains a deployment and structural-discovery analysis.

## 9. Nature-main-track extension

If follow-up material is available, prioritized ambiguous mouse spectra are strong candidates for evidence-guided acquisition:

`ambiguous MS2 → freeze surviving candidate set → select most discriminating MSn/CE action → acquire new measurement → quantify candidate-space contraction`.

This is the preferred route for converting adaptive evidence interpretation into a prospective experimental-discovery result.

## 10. Release plan

Before publication:
- deposit raw/processed spectra when permissions allow;
- release a de-identified manifest linking manuscript feature IDs to repository accessions;
- publish frozen candidate pools and evidence certificates;
- archive the frozen ORBIT release, calibration procedure and evaluation configuration.
