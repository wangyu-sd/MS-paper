# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Working proposition

**What blocks the use of unidentified spectra is not that structure predictions are imperfect, but that their output form carries no reliable information about its own limits. Simulating the physical fragmentation process changes the output form: candidates are eliminated by peaks they cannot produce, what survives is a statement rather than a rank, and the reliability of that statement can be calibrated against chemistry the system has never seen.**

The manuscript delivers two inseparable contributions:

1. **the system** — an executable fragmentation model (pLSE) plus a verifiable reasoning model (METEOR) that together return the most specific structural statement a spectrum supports, with calibrated confidence;
2. **the atlas** — the resource produced by applying that system to mouse and repository-scale dark spectra, and the biology it makes visible.

Neither stands alone. Calibration is the hinge: without it the system is one more scorer, and without the system the atlas is a pile of guesses. This is the argument that must survive review.

## Current title

**Simulating molecular fragmentation resolves the structural composition of the dark metabolome**

First clause is the system, second clause is the finding. Do not restore a title that leads with the agent — automated rule evolution is an enabling method (Section 3 paragraph 4 and ED6), not the headline.

## Result distribution

Nature research Articles in this area run roughly **1 part method to 4 parts finding**. Gentry 2024 devotes Fig. 1 to the method and Figs. 2–5 to findings about the world; the same holds for DeepMet. The previous draft of this manuscript was 4 parts method to 2 parts finding, which is a methods paper with a discovery appendix.

The current structure is **1 system : 1 resource : 3 findings**. Preserve this ratio. Benchmark ablations, hard-decoy analyses, shuffled-spectrum controls and the agent's challenge–recovery dynamics live in Methods and Extended Data. Main-text space belongs to statements about the world.

## Manuscript architecture

| § | Section | Figure | Role |
|---|---|---|---|
| 1 | Physical fragmentation modelling resolves spectra that spectral similarity cannot | Fig. 1 | system |
| 2 | Structural confidence calibrated against prospective library growth | Fig. 2 | hinge |
| 3 | A structural atlas of the mouse and repository-scale dark metabolome | Fig. 3 | resource + finding |
| 4 | Dark structural families partition by biological origin | Fig. 4 | finding |
| 5 | A structurally defined metabolite family associated with a phenotype | Fig. 5 | finding |

The chain: `mechanistic elimination → computed resolution level → calibrated confidence → usable atlas → composition of the dark metabolome → origin → biology`.

## Draft conventions

`main.tex` is written in target-final form. Missing results stay marked as:

- `[RESULT: ...]` — a number that must come from a frozen experiment;
- `[DATA: ...]` — cohort/dataset information still to be bound;
- `[METHOD: ...]` — a protocol detail that must be frozen before submission.

No placeholder may be filled from memory, a transient training log or an exploratory notebook. Every replacement maps to an immutable artifact in the claim–evidence matrix.

## Files

- `main.tex` — target manuscript: Introduction, five Results sections, Discussion, Methods, Extended Data legends.
- `references.bib` — peer-reviewed literature carrying the central argument.
- `supplementary/Supplementary_Information.tex` — supporting experiments, in the order they must be executed.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — claim → experiment → statistical unit → controls → artifact contract.
- `internal/EXPERIMENT_EXECUTION_PLAN.md` — execution order, cost and dependency for every experiment.
- `internal/FIGURE_PLAN.md` — panel-level plan for Figures 1–5 and ED1–11.
- `internal/RESULTS_PLACEHOLDERS.md` — checklist mapping every placeholder to its source experiment.
- `internal/MOUSE_COHORT_PROTOCOL.md` — rules for the private mouse spectra.
- `internal/LITERATURE_POSITIONING.md` — competitive positioning and claim boundaries.

## Scientific object

For candidate `M` and peak `p`, the manuscript distinguishes three things and must never conflate them:

1. **support** — `M` has an atom-balanced, mass-compatible fragmentation trajectory reaching `p`;
2. **specificity** — that support exceeds the best support available to competing candidates;
3. **elimination** — no trajectory of `M` reaches `p`, so `M` is excluded.

Elimination is the operation that makes the output a statement rather than a rank, because eliminations compose across peaks and are machine-checkable. It is also the operation that can be wrong: the deterministic reaction basis is incomplete, so failure to explain a peak is only negative evidence to the extent that the model covers the relevant chemistry. This is why elimination stringency is calibrated to a measured rate of excluding true structures rather than assumed sound.

## Resolution policy

Every spectrum receives the **most specific true statement** its surviving candidate set admits:

`unique structure` → `bounded isomer set` → `substructure or chemical class` → `formula only` → `unresolved`

The level is **computed from the evidence**, not assigned by convention. This is the operational contribution against the established human-assigned confidence-level scheme, and it must be stated that way rather than as a new confidence score.

Generator recall and evidence discrimination are always reported separately: `P(GT ∈ C_K)`, conditional discrimination given GT present, and end-to-end resolution. A dark-spectrum prediction is never called an identified metabolite without the corresponding orthogonal evidence.

## Cost constraints binding this design

- **No new MS acquisition.** No targeted MSn campaigns, no new biological sampling, no perturbation experiments performed here.
- **Authentic standards only**, and only for structures that are commercially available.
- Consequences: biological origin attribution mines public perturbation datasets that others already acquired (§4); prospective validation uses public library growth rather than new measurements (§2); the evidence-guided acquisition loop is removed from the manuscript and retained only as a stated future direction.

## Citation policy

The central argument is grounded in peer-reviewed work. Preprints may provide frontier context but must not carry essential claims. The comparator set must include mature fragmentation and spectrum methods (SIRIUS/CSI:FingerID, CFM-ID) alongside modern generative methods, and must acknowledge that mechanistic fragmentation models are reported as *less* accurate than learned models under in-distribution evaluation. The claim of this paper is not that mechanism is more accurate; it is that mechanism yields eliminations that can be calibrated, which is what a resource requires.
