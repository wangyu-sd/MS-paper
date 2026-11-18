# NMI manuscript revision — additive, content-preserving

This branch improves the typesetting and the **title, abstract and Methods only**. It was started from the restored main branch after PR #21 was reverted. It does **not** rework the existing Results, Discussion, figure captions, figure definitions, Extended Data legends or Supplementary.

## Files
- `main.tex`: existing full scientific manuscript plus revised title/abstract, provisional author contact block, five new Methods subsections and a minimal preamble change to include `orbit-nmi.sty`.
- `orbit-nmi.sty`: lightweight single-column manuscript typography (NewTX text/math, restrained headings, simple running header, understated abstract rules); does not replace the article class with `sn-jnl`.
- `internal/ORIGINAL_TITLE_ABSTRACT_20261118.md`: word-for-word original title and abstract archived before the revision.
- `internal/AUTHOR_METADATA_RECOVERY_20261118.md`: provenance note about the previously recovered names, which belong to *MolSpecFlow* and **have not been verified for ORBIT-MS**.

## Preservation contract and verification

The revised `main.tex` was constructed with exact-content comparisons against pre-edit main:

1. The entire existing **Results and Discussion byte string remains identical**.
2. All 15 original Methods text blocks remain intact, with **five additive** subsections.
3. All five original main-figure definitions, captions and fallback specifications remain present.
4. The original title and abstract are preserved verbatim in the archive above.
5. The existing `references.bib`, supplementary, and any earlier manuscript histories were not modified.

The resulting `main.tex` grew from 60,147 to more than 69,000 characters; no historical experiment content was intentionally shortened.

## Author information

Historical `MS-paper/main.tex` and Overleaf copies only contained generic author placeholders. A historical eleven-person author block was recovered from a separate *MolSpecFlow* manuscript. It is recorded as a **cross-project reference only**, and is **not silently treated as the ORBIT-MS coauthor list**. Yu Wang and a provisional institution block are visible on the draft, with full author roster, superscripts, contribution notes and correspondence explicitly pending confirmation. Do not submit the temporary block as finalized metadata.

## Typography and build

This is a professional authoring/readability layout, **not an official Nature Machine Intelligence production template**. Submission formatting can be adjusted later without affecting the scientific content.

With standard TeX Live fonts and packages installed:

```bash
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
```

To switch from the polished reading copy to a double-spaced, line-numbered review copy, insert `\\orbitreviewtrue` after `\\usepackage{orbit-nmi}` in `main.tex` and before `\\orbittypeset`. The original `\\doublespacing` and `\\linenumbers` commands are preserved in that mode.

A **representative first-page sample** with the new typography and actual current title/abstract compiled successfully with pdflatex/latexmk on TeX Live (three-page example). The **complete manuscript has not yet been independently built end-to-end** from the GitHub-connected files. No claim is made that a full-manuscript build passed.

## Scientific editing notes

The updated abstract preserves only sourced results and retains explicit `[RESULT: ...]` placeholders for unmatched agent-vs-fixed and independent dark-metabolomics chemical validation. The additional Methods detail the novelty/prior-access evaluation, MMA mass-matched motif construction, Sleep/Wake/Hindsight experiences, typed Scientific Improver decisions, and same-cohort reporting protocol. Existing claims and uncompleted experimental placeholders remain as originally authored.
