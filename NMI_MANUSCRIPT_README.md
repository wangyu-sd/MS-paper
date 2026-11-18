# ORBIT-MS — Nature Machine Intelligence manuscript authoring

This branch prepares an editable **Article** manuscript for *Nature Machine Intelligence* using Springer Nature's \`sn-jnl\` family with the \`sn-nature\` citation style. The journal's initial-submission requirements are flexible; the goal of this branch is scientific substance and traceability, **not shortening the draft to a word limit**.

## Scope of the manuscript edit

- **Abstract and unheaded Introduction:** restored from the original \`main\`-branch \`main.tex\` without rewriting the scientific text. The old abstract text is enclosed in \`\abstract{...}\` solely because the Springer Nature template requires that markup.
- **Results:** reorganized around five complementary scientific questions: molecular recovery/chemical generalization; MMA/transferable chemical knowledge; Sleep/Wake/Hindsight recursive learning; adaptive Scientific Improver decisions; dark-metabolome structure hypotheses and independent evidence.
- **Methods:** original study, chemistry and system details retained, with new explicit evaluation-partition/prior-access and experience-source experiments.
- **Historical data:** existing PR93/PR95 observations, CAL known-formula comparisons, Gen series, PR94 source counts, and published supplementary material retained. The manuscript does **not** overwrite old experimental results. Differing candidate-supply or multi-energy protocols remain separately identified.
- **Figure source locations:** five editorial slots in \`figures/fig1_chemical_generalization.pdf\`, \`figures/fig2_mma_transferable_knowledge.pdf\`, \`figures/fig3_recursive_chemical_learning.pdf\`, \`figures/fig4_scientific_improver.pdf\`, and \`figures/fig5_dark_metabolome.pdf\`. Until verified figures are available, the manuscript displays clearly labelled text figure specifications rather than pretending graphs exist.
- **Unfinished experiments:** marked \`[PENDING RESULT]\` or \`[PENDING METHOD]\`; they are not presented as measured positive findings.

## Authoring files

\`main.tex\` — primary manuscript; \`references.bib\` — existing references; \`sn-jnl.cls\` and \`sn-nature.bst\` — Springer Nature authoring class and numerical bibliography style; \`supplementary/\` — existing supplementary results.

## Local build

From the repository root, with a complete TeX Live installation:

\`\`\`bash
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
\`\`\`

If building without latexmk, run pdflatex, bibtex and pdflatex twice. The project does not yet include its final PDF figures, author metadata, grant acknowledgments or frozen final evidence receipts. These remain explicit authoring tasks, not technical assumptions.

For final submission, follow the journal's actual instructions and regenerate the bibliography as part of the manuscript file if required. The locally vendored Springer Nature authoring class should be checked against the **current publisher template** before submission:
- Springer Nature author support: https://www.springernature.com/gp/authors/campaigns/latex-author-support
- NMI initial submission: https://www.nature.com/natmachintell/submission-guidelines/initial-formatting
- NMI LaTeX instructions: https://www.nature.com/natmachintell/submission-guidelines/aip-and-formatting

## Provenance and status

The branch changes \`main.tex\` without editing \`references.bib\`, legacy supplementary tables or existing experimental receipts. Do not merge a pending claim as a completed experiment. A source-pinned per-structure evidence manifest will be added alongside final figures and newly completed RSI/chemical validation studies.

This document describes an **authoring draft**; the manuscript has not been asserted to compile cleanly on a local TeX Live installation until an actual full build receipt is attached.
