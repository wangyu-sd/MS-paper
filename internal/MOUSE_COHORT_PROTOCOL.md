# Mouse Cohort Protocol

The private mouse spectra are scientifically valuable only if the manuscript preserves the distinction between **external deployment**, **blinded validation** and **ground-truth structural identification**.

## Role in the current manuscript

The cohort feeds two sections and must satisfy both:

- **§3 (atlas).** The mouse corpus is the organism-scale half of the atlas, alongside the repository corpus. Its contribution is entity count, recurrence and composition.
- **§5 (biology).** The principal biological association is drawn from it.

It is **not** the site of system validation. Calibration is established in §2 against public library growth, on chemistry independent of this cohort. Do not use mouse anchors to calibrate and then report mouse results as validated.

**Open action:** the cohort's location and provenance are unconfirmed in the current workspace. Freeze the manifest (§1 below) before Phase 4 of the execution plan.

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

Track every spectrum through the same hierarchy used throughout the manuscript, where the level is **computed from which candidates the evidence eliminates**, not assigned:

1. unresolved spectrum;
2. molecular formula;
3. chemical class / structural family;
4. bounded isomer set at the frozen elimination stringency;
5. unique putative 2D structure at that stringency;
6. orthogonally confirmed structure.

Do not merge levels 5 and 6. Levels 1–5 are statements of controlled reliability; only level 6 is an identification.

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

## 7. Where cohort results appear

Cohort results are split across two figures and must not be merged back into one deployment figure:

- **Figure 3** — the mouse corpus's contribution to entity count, recurrence and composition, reported alongside the repository corpus.
- **Figure 5** — the biological association, anchor validation dossiers with orthogonal support, and at least one explicitly unresolved isomer case.

Blinded anchor analysis (candidate recall, conditional discrimination, end-to-end resolution, false-resolution rate) is reported in **Extended Data**, not the main text, because §2 already establishes calibration on independent chemistry and the main text should not re-litigate it.

Do not use "annotation depth increased" as a biological result.

## 8. Biology

Do not manufacture a biological story from annotation output.

A biological association enters the main text only when:
- the biological comparison existed independently of ORBIT hypothesis selection;
- biological replicates, not spectra, are the statistical unit;
- multiple testing is controlled;
- the association survives reasonable annotation-confidence/risk thresholds;
- the chemistry is plausible and preferably orthogonally validated.

Otherwise Figure 5 remains a deployment and structural-discovery analysis.

## 9. Evidence-guided acquisition is out of scope

The loop `ambiguous MS2 → freeze surviving candidate set → select most discriminating MSn/CE action → acquire new measurement → quantify contraction` requires instrument time that the current budget does not include. It is **removed from the manuscript** and appears only as a stated future direction in the Discussion.

What survives from it, and must be delivered, is the *prediction* half: for every unresolved entry the atlas states the specific measurement that would resolve it. This is a computed output, costs nothing, and is what converts the atlas into a prioritized experimental agenda. Do not describe it as if the measurement had been performed.

Prioritized ambiguous mouse spectra should nonetheless be recorded in the release, so that the acquisition experiment is immediately executable by us or by others once instrument time exists.

## 10. Release plan

Before publication:
- deposit raw/processed spectra when permissions allow;
- release a de-identified manifest linking manuscript feature IDs to repository accessions;
- publish frozen candidate pools and evidence certificates;
- archive the frozen ORBIT release, calibration procedure and evaluation configuration.
