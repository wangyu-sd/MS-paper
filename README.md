# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Working proposition

**The dark metabolome is not an unstructured residue of unidentified spectral features. It is a recurrent, chemically organized and biologically partitioned layer of small-molecule chemistry whose scale and structure have been obscured because spectra are counted as features rather than resolved into bounded structural entities.**

ORBIT-MS is the enabling measurement system, not the headline. It converts a tandem mass spectrum into the most specific structural statement supported by the measurement by combining candidate generation with a conservation-preserving fragmentation World and calibrated candidate elimination. The manuscript then uses those statements to answer four field-level questions:

1. **How large is the dark metabolome once redundant spectral features are collapsed onto structural entities?**
2. **How is dark chemistry organized relative to characterized metabolism?**
3. **Do recurrent dark structural families partition by biological source?**
4. **Does structural family resolution expose reproducible biology that anonymous feature-level analysis misses?**

The paper succeeds at Nature only if the answers to those questions are strong. Benchmark accuracy, calibration, World learning, agent evolution and reasoning traces are credibility/supporting evidence.

## Current title

**A structural census of the dark metabolome**

Alternative title if chemical-space organization becomes the strongest result:

**The structural organization of the dark metabolome**

Do not lead the title with ORBIT-MS, the agent, the language model or fragmentation simulation.

## Main-text architecture

The manuscript is organized as **1 credibility figure + 4 discovery figures**.

| § | Section | Figure | Scientific question |
|---|---|---|---|
| 1 | A calibrated fragmentation World turns dark spectra into bounded structural statements | Fig. 1 | Why can the census be trusted? |
| 2 | The dark metabolome contains far fewer recurrent chemical entities than spectral features imply | Fig. 2 | How large is it? |
| 3 | Dark chemistry forms a structured landscape beyond known metabolism | Fig. 3 | How is it chemically organized? |
| 4 | Biological sources partition dark chemical space | Fig. 4 | Where does it come from? |
| 5 | Structural families reveal biological programmes hidden at feature level | Fig. 5 | What biology becomes visible? |

The chain is:

`dark spectra → bounded structural statements → structural entities → recurrent chemical families → biological source → reproducible biological programme`.

Prospective library-growth calibration is no longer a standalone main figure. It is the credibility spine of Fig. 1 and receives complete treatment in Extended Data.

## Headline numbers

Three numbers determine whether the paper has a Nature-scale result:

1. **Census contraction**
   `N dark features → N recurrent structural entities`, with uncertainty from validated entity collapsing.
2. **Chemical novelty**
   the fraction of recurrent entities/families that lie outside the predefined neighbourhood of characterized metabolism.
3. **Biological organization**
   the fraction of recurrent structural families that show reproducible source or phenotype organization, and the gain in cross-cohort reproducibility obtained by structural-family analysis relative to anonymous features.

These are not targets to optimize after looking at the data. Definitions, denominators and analysis thresholds are frozen before confirmatory analysis.

## Scientific object

For candidate `M` and observed peak `p`, distinguish:

1. **support** — an atom/electron/charge-consistent fragmentation trajectory of `M` can produce `p`;
2. **specificity** — that support distinguishes `M` from competing structures;
3. **elimination** — under a calibrated operating point, the evidence is sufficient to exclude `M`.

The output is not forced to be a single structure. Each spectrum receives the most specific bounded statement supported by the evidence:

`unique putative structure → bounded isomer set → shared substructure / chemical class → formula only → unresolved`.

Only orthogonal reference-standard validation is called an identification.

## Credibility hierarchy

The main text asks readers to believe an atlas built from model-derived structural statements. Therefore:

- exact and analogue leakage audits are mandatory;
- generator recall, conditional discrimination and end-to-end resolution are reported separately;
- elimination soundness is measured, not assumed;
- the complete system and calibration mapping are frozen before prospective library-growth evaluation;
- prospective outcomes are stratified by structural distance from the frozen library;
- comparator methods receive the same candidate pools and their own fair calibration;
- entity collapsing is validated on known compounds before dark-entity counts are reported;
- family definitions are frozen before origin or phenotype testing;
- biological samples, not spectra, are the unit of biological inference.

## Result distribution

Main-text space belongs to statements about the world.

**Main text**
- bounded structural measurement and prospective credibility;
- census size and recurrence;
- chemical-space organization;
- source partition;
- global family-level biological gain plus one deeply characterized example.

**Extended Data / Supplementary**
- full comparator benchmark;
- spectrum-shuffle and trace-verification controls;
- World/action-space ablations;
- rule/program evolution;
- structured-CoT controls;
- complete calibration stratifications;
- entity-collapsing sensitivity;
- complete origin/association models;
- all standard-validation dossiers.

## Cost constraints

- No new discovery-scale MS acquisition is assumed.
- Public perturbation data are used for source attribution.
- Authentic standards are reserved for a small set of frozen anchors.
- Evidence-guided acquisition remains a future direction; the released atlas may state the measurement predicted to resolve an ambiguous entry, but must not imply that measurement was performed.

## Draft conventions

`main.tex` is target-final prose. Missing evidence remains explicit:

- `[RESULT: ...]` — numerical/statistical result from a frozen artifact;
- `[DATA: ...]` — cohort or dataset information still to be bound;
- `[METHOD: ...]` — protocol detail that must be frozen.

No placeholder is filled from memory, a transient training log or an exploratory notebook.

## Files

- `main.tex` — target Nature Article.
- `internal/FIGURE_PLAN.md` — panel-level design for Figs. 1–5 and Extended Data.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — claim → experiment → unit → controls → artifact.
- `internal/EXPERIMENT_EXECUTION_PLAN.md` — kill-risk-first execution order.
- `internal/RESULTS_PLACEHOLDERS.md` — result-to-artifact checklist.
- `internal/LITERATURE_POSITIONING.md` — competitive and claim-boundary logic.
- `internal/MOUSE_COHORT_PROTOCOL.md` — cohort freezing and biological-inference rules.
- `supplementary/Supplementary_Information.tex` — supporting analyses and reproducibility details.

## Standing claim boundaries

1. Dark spectra are not synonymous with molecules absent from chemical databases.
2. Spectral features are not molecular entities.
3. Recurrence across spectra is not recurrence across independent biological datasets.
4. A structural relationship is not evidence of an enzymatic reaction.
5. Source attribution establishes perturbation dependence, not biosynthetic origin in the mechanistic sense.
6. A model-derived unique structure is not a reference-standard identification.
7. Mechanistic completeness is empirical; missing trajectories cannot be treated as absolute impossibility without calibration.
8. Training loss, selector accuracy and agent progress are not scientific endpoints.
