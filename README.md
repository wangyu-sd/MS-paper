# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Working proposition

**Molecular structure elucidation becomes evidence-limited when increasingly realistic molecular alternatives outpace the fixed spectral evidence used to distinguish them. ORBIT-MS addresses this regime with adaptive, candidate-specific fragmentation evidence.**

The manuscript is written as a **target final paper**, not a progress report. Missing results remain explicitly marked in `main.tex` as:

- `[RESULT: ...]` — a numerical/statistical result that must come from a frozen experiment;
- `[DATA: ...]` — cohort/dataset information still to be bound;
- `[METHOD: ...]` — a protocol detail that must be frozen before submission.

No placeholder should be filled from memory, a transient training log or an exploratory notebook. Every replacement should map to an immutable artifact in the claim–evidence matrix.

## Current title

**Adaptive fragmentation evidence for molecular structure elucidation**

The title intentionally avoids claiming that experimental evidence itself co-evolves. Until prospective evidence-guided acquisition is demonstrated, the manuscript describes an **adaptive evidence model/interpretation**, not co-evolving measurements.

## Files

- `main.tex` — complete target manuscript with Introduction, **five** Results, Discussion, Methods, main-figure legends and Extended Data legends.
- `references.bib` — core peer-reviewed literature used by the central argument.
- `supplementary/Supplementary_Information.tex` — detailed benchmark, chemistry, adaptation, calibration and mouse reporting shell.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — claim → experiment → statistical unit → control → artifact contract.
- `internal/EXPERIMENT_EXECUTION_PLAN.md` — **step-by-step execution plan** from dataset/snapshot freezing through Figures 1–5, mouse validation and the prospective MSn/CE Nature extension, including inputs, controls, metrics, statistics, artifacts and go/no-go gates.
- `internal/RESULTS_PLACEHOLDERS.md` — canonical checklist of results needed to remove manuscript placeholders.
- `internal/FIGURE_PLAN.md` — panel-level plan for Figures 1–5 and Extended Data.
- `internal/MOUSE_COHORT_PROTOCOL.md` — rules for using the private unlabelled mouse spectra without inflating annotation confidence.
- `internal/LITERATURE_POSITIONING.md` — peer-reviewed competitive positioning and claim boundaries.

## Manuscript architecture

1. **Static spectral evidence loses discriminative power as molecular alternatives improve.**
2. **Candidate-specific fragmentation evidence resolves close molecular alternatives.**
3. **Experimental spectra reshape molecular evidence beyond chemical prior.**
4. **Reciprocal adaptation improves inference without opponent-specific overfitting.**
5. **Adaptive fragmentation evidence resolves previously unannotated mouse spectra.**

Structured CoT is no longer a central manuscript claim; its six-arm causal analysis is supporting Extended Data.

## Scientific object

The core pLSE object is not global peak coverage. For candidate `M_j` and peak `p`, the manuscript distinguishes:

1. **candidate support** — whether `M_j` has a trace-valid, mass-compatible fragmentation trajectory supporting `p`;
2. **candidate specificity** — whether that support exceeds the best support available to the competing candidates;
3. **candidate score** — the aggregation of positive candidate-specific evidence with explicit accidental-match opportunity control.

Because the deterministic reaction basis is incomplete, failure to explain a peak is not automatically negative evidence.

## Critical causal controls

The paper must not use a cross-generation heatmap alone to claim co-adaptation. The principal endpoint compares:

- `(H0,E0)` — initial hypothesis and evidence;
- `(HT,E0)` — adapted hypothesis only;
- `(H0,ET)` — adapted evidence only;
- `(HT,ET)` — both adapted;

plus fixed-side and ungated/blind-alternation controls. The interaction effect is the principal test of reciprocal benefit.

## Resolution policy

Generator recall and evidence discrimination are reported separately:

- `P(GT ∈ C_K)` — generator/candidate recall;
- conditional discrimination given GT is present;
- end-to-end structural resolution.

The final system should return risk-controlled structural candidate sets rather than force one answer from every spectrum. A dark-spectrum prediction is **not** called an identified metabolite without the corresponding orthogonal evidence level.

## Nature-main-track extension

The preferred additional experiment is true evidence-guided acquisition:

`ambiguous MS2 → select most discriminating MSn/CE measurement → acquire new spectrum → quantify candidate-space contraction`.

If completed prospectively, this would support the stronger proposition of sequential hypothesis–experiment co-design.

## Citation policy

The central argument is grounded in peer-reviewed work. Preprints can be acknowledged as frontier context but should not carry essential scientific claims. The comparator landscape should include mature fragmentation/spectrum methods such as SIRIUS/CSI:FingerID, CFM-ID and FIORA in addition to modern inverse/generative methods where executable and technically comparable.
