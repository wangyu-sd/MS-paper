# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Working proposition

**Molecular structure elucidation improves when increasingly difficult molecular hypotheses are coupled to candidate-specific, experimentally grounded fragmentation evidence that can itself improve.**

The paper is deliberately written as a **target final manuscript**, not a progress report. Missing quantitative results are marked in `main.tex` as:

- `[RESULT: ...]` — numerical/statistical result to be filled from a frozen experiment;
- `[DATA: ...]` — dataset/cohort metadata still to be bound;
- `[METHOD: ...]` — protocol detail that must be frozen before submission.

No placeholder should be replaced from memory or a transient training log. Every replacement should point to an immutable result artifact in the claim–evidence matrix.

## Files

- `main.tex` — complete Nature-style target manuscript with Introduction, six Results, Discussion, Methods, main figure legends and Extended Data legends.
- `references.bib` — core peer-reviewed literature. Preprints are intentionally excluded from the central argument.
- `supplementary/Supplementary_Information.tex` — planned supplementary analyses/tables and detailed reporting shell.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — claim → experiment → statistical unit → artifact contract.
- `internal/RESULTS_PLACEHOLDERS.md` — canonical checklist of results required to remove manuscript placeholders.
- `internal/FIGURE_PLAN.md` — panel-level plan for Figures 1–6 and Extended Data.
- `internal/MOUSE_COHORT_PROTOCOL.md` — rules for using the private unlabelled mouse spectra without inflating annotation confidence.

## Overleaf

Upload/clone the repository into Overleaf and set `main.tex` as the main document.

The draft uses only standard LaTeX packages and numeric superscript citations. Nature accepts flexible formatting at initial submission; if accepted, all textual material can later be flattened into one `.tex` file and the draft-only placeholder macros removed.

## Manuscript architecture

1. Better molecular hypotheses create harder structural alternatives.
2. Candidate-specific fragmentation evidence distinguishes close alternatives.
3. Experimental spectra contribute information beyond chemical plausibility.
4. Reciprocal challenge produces measurable hypothesis–evidence co-evolution.
5. Adaptive evidence transfers across generators and calibrates non-resolution.
6. ORBIT-MS converts mouse dark spectra into auditable structural hypotheses.

## Evidence policy

The manuscript must distinguish:

- chemical plausibility from experimentally supported evidence;
- peak coverage from candidate discrimination;
- generated fragments from atom-traceable mechanism evidence;
- benchmark structure accuracy from dark-spectrum hypotheses;
- unique structure resolution from calibrated unresolved candidate sets;
- repeated spectra from independent molecule groups.

For the mouse cohort, an ORBIT prediction is **not** called an identified metabolite without the corresponding orthogonal evidence level.

## Citation policy

The central literature argument prioritizes peer-reviewed work in Nature, Nature Methods, Nature Biotechnology, Nature Machine Intelligence, Nature Communications, PNAS, NeurIPS and ICML proceedings. Preprints may be added later only to acknowledge frontier developments and should not carry essential scientific claims.
