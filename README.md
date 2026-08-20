# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Working proposition

**A plausible molecular structure is not an elucidated molecular structure. As molecular hypotheses become increasingly realistic, structure elucidation can shift from a generation-limited to an evidence-limited regime in which the central challenge is identifying which experimental observations distinguish one plausible structure from its alternatives.**

ORBIT-MS addresses this regime with adaptive, candidate-specific fragmentation evidence.

The manuscript is written as a **target final paper**, not a progress report. Missing results remain explicitly marked in `main.tex` as:

- `[RESULT: ...]` — a numerical/statistical result that must come from a frozen experiment;
- `[DATA: ...]` — cohort/dataset information still to be bound;
- `[METHOD: ...]` — a protocol detail that must be frozen before submission.

No placeholder should be filled from memory, a transient training log or an exploratory notebook. Every replacement should map to an immutable artifact in the claim–evidence matrix.

## Current title

**An evidence bottleneck in molecular structure elucidation**

The manuscript is intentionally framed around a scientific phenomenon rather than a model architecture. The central conceptual distinction is:

**spectral reproduction ≠ chemical support ≠ structural discrimination.**

## Files

- `main.tex` — complete target manuscript with Introduction, **five** Results, Discussion, Methods, main-figure legends and Extended Data legends.
- `references.bib` — core peer-reviewed literature used by the central argument.
- `supplementary/Supplementary_Information.tex` — detailed benchmark, chemistry, adaptation, calibration and mouse reporting shell.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — claim → experiment → statistical unit → control → artifact contract.
- `internal/EXPERIMENT_EXECUTION_PLAN.md` — step-by-step execution plan from dataset/snapshot freezing through Figures 1–5, mouse validation and the prospective MSn/CE extension.
- `internal/RESULTS_PLACEHOLDERS.md` — canonical checklist of results needed to remove manuscript placeholders.
- `internal/FIGURE_PLAN.md` — panel-level plan for Figures 1–5 and Extended Data.
- `internal/MOUSE_COHORT_PROTOCOL.md` — rules for using the private unlabelled mouse spectra without inflating annotation confidence.
- `internal/LITERATURE_POSITIONING.md` — peer-reviewed competitive positioning and claim boundaries.

## Manuscript architecture

1. **Better molecular hypotheses create an evidence bottleneck.**
2. **Discriminative fragments resolve close molecular alternatives.**
3. **Experimental spectra distinguish evidence from chemical plausibility.**
4. **Evidence must adapt as molecular hypotheses become harder.**
5. **From dark spectra to testable molecular hypotheses.**

The five sections form one scientific chain:

`better hypotheses → weaker fixed discrimination → discriminative evidence → spectrum-specific evidence → adaptive evidence → evidence-bounded real-world hypotheses`.

Structured CoT is not a central manuscript claim; its six-arm causal analysis is supporting Extended Data.

## Scientific object

The core pLSE object is not global peak coverage. For candidate `M_j` and peak `p`, the manuscript distinguishes:

1. **candidate support** — whether `M_j` has a trace-valid, mass-compatible fragmentation trajectory supporting `p`;
2. **candidate specificity** — whether that support exceeds the best support available to the competing candidates;
3. **candidate score** — the aggregation of positive candidate-specific evidence with explicit accidental-match opportunity control.

Because the deterministic reaction basis is incomplete, failure to explain a peak is not automatically negative evidence.

## Narrative hierarchy

Only three concepts should dominate the main text:

- **evidence bottleneck** — the field-level phenomenon;
- **discriminative fragmentation evidence** — the scientific object;
- **adaptive evidence** — the solution principle.

Implementation terms such as METEOR, pLSE, Chemical-World/Spectral-Reality, reciprocal runtime, conformal calibration and agent governance remain subordinate to these three concepts.

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

The system should return calibrated or risk-controlled structural candidate sets rather than force one answer from every spectrum. A dark-spectrum prediction is **not** called an identified metabolite without the corresponding orthogonal evidence level.

## Nature-main-track extension

The preferred additional experiment is evidence-guided acquisition:

`ambiguous MS2 → select most discriminating MSn/CE measurement → acquire new spectrum → quantify candidate-space contraction`.

If completed prospectively, this would extend the paper from adaptive evidence interpretation to sequential hypothesis–experiment co-design.

## Citation policy

The central argument is grounded in peer-reviewed work. Preprints can be acknowledged as frontier context but should not carry essential scientific claims. The comparator landscape should include mature fragmentation/spectrum methods such as SIRIUS/CSI:FingerID, CFM-ID and FIORA in addition to modern inverse/generative methods where executable and technically comparable.