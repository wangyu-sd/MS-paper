# ORBIT-MS manuscript: formatting and preserved content

## Current revision

The 18 November 2026 revision continues PR #22 from the restored manuscript after PR #21 was reverted. It rewrites the abstract, Introduction and Results under the author's latest instructions, aligns Discussion, and retains the existing five-result experimental design.

The title is **ORBIT-MS: Recursive chemical learning for molecular structure elucidation from tandem mass spectra** in both the main manuscript and Supplementary Information. The abstract is an unreferenced 145-word paragraph. Introduction has no heading; the five scientific result themes now sit under a conventional Results heading.

## Content retained and updated

- All existing Results measurements retain their values and evaluation settings, including the MMA and fixed-pool ablations, trajectory feasibility, near-isomer comparison, external evaluations, conditional Macro-Core result, source census and knowledge-resource growth.
- The complete five main-figure definitions, captions and panel specifications remain unchanged.
- All pre-existing Methods content is retained. The long action-selection display is split across aligned lines, and a paragraph describes the additional benchmark snapshot and aggregation settings.
- The latest coherent PR95 partial-core development results have been added, along with additional external Top-10, reach and formula-recall measurements. Their source versions are recorded in `internal/EDITORIAL_REVISION_20261118.md`.
- Supplementary Information changes only its title. All supplementary result tables and `references.bib` remain unchanged.
- Earlier manuscript wording remains recoverable in git at commit `b8357a9a12477bb1b5b9853424f7753735ae8598`. The original title/abstract and author-provenance notes remain in `internal/`.

Pending outcomes are complete result sentences with `x` in place of unavailable values or chemical identifiers. A single draft note outside the abstract explains this convention. The `\pending{metric-id}` macro prints `x`, and the editorial record maps its locators to the experiments. Shared abstract/body outcomes use the same identifiers.

## Typography and build

`orbit-nmi.sty` retains the single-column article layout, NewTX text/math, restrained headings, simple running header and rule-delimited abstract. It is an authoring layout. Figure source specifications remain visible until their corresponding empirical PDF assets are added.

Build with a TeX Live installation containing NewTX, binhex, titling, titlesec, fancyhdr, natbib and the other packages listed in the preamble:

```bash
latexmk -pdf -halt-on-error -interaction=nonstopmode -file-line-error main.tex
```

To enable double spacing and continuous reviewer line numbers, put `\orbitreviewtrue` after `\usepackage{orbit-nmi}` and immediately before `\orbittypeset` in `main.tex`.

The Results heading begins with its first subsection on a new page. The RSI action set is broken into aligned lines to fit the text width. These layout fixes preserve the scientific content.

## Full-manuscript verification

The complete manuscript compiled successfully with `latexmk -pdf -halt-on-error -interaction=nonstopmode -file-line-error main.tex`: 23 pages, zero undefined citations, zero unresolved references, zero LaTeX warnings and zero overfull boxes. This is a full-manuscript build, not a representative title-page sample.

The title/abstract page, Results opening, benchmark paragraphs, aligned intervention equation and final figure page were rendered and visually inspected. The Results heading remains with its first subsection, and the action-selection equation fits within the text width.

Verified `main.tex` SHA-256: `6e2d5f8308af55c1cc1d36decd734e500e09fe12c290d0a04608ad1550b3b453`.

## Author information

The existing provisional author and affiliation block is retained. `internal/AUTHOR_METADATA_RECOVERY_20261118.md` records its provenance and the outstanding author metadata; this editorial revision makes no further authorship changes.
