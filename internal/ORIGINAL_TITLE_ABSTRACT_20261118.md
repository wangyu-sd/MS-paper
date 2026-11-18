# ORBIT-MS: original title and abstract preserved verbatim

Source: `main.tex` on `main` before the 2026-11-18 typography / metadata update. This is a content archive, not a replacement for the current draft. All original Results and Methods remain in `main.tex`.

## Original title (LaTeX)

```latex
\title{\textbf{ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter}}
```

## Original author placeholder

```latex
\author{Author names and affiliations to be finalized}
```

## Original abstract (exact LaTeX)

```latex
\noindent\textbf{Abstract.}
Untargeted tandem mass spectrometry detects a vast repertoire of molecular signals, yet most experimental spectra remain without a confident structural assignment. This metabolomic dark matter is difficult to elucidate because chemically distinct molecules can explain overlapping fragments, while fixed inference models cannot learn from the structural hypotheses they repeatedly fail to generate or distinguish. Here we introduce ORBIT-MS, an evidence-guided, agent-directed recursive self-improvement (RSI) system that couples a spectrum-conditioned molecular Generator, a structure-conditioned fragmentation World and an experimental-spectrum Verifier. A Scientific Improver Agent diagnoses failed inferences, selects targeted chemical-knowledge, generator or verifier updates, and retains the observed consequences as experience for subsequent decisions. In a source-audited three-study resource, 613,331 of 835,953 eligible biological MS/MS queries lacked an accepted reference-spectrum match. Existing known-formula calibration experiments show that fragment knowledge substantially improves molecular candidate reach and that W/V evidence improves ranking within the same candidate pool. We investigate \result{the population distribution of supported structural resolution among reference-unmatched spectra}, \result{new molecular structures and resolution tiers recovered across completed autonomous RSI generations}, and \result{chemically supported relationships connecting unresolved spectra to characterized molecular families}. Independent spectral evidence and, where available, orthogonal chemistry are used to assess the resulting assignments. ORBIT-MS aims to progressively extend the interpretable chemical space of the metabolomic dark matter rather than to assign an unsupported unique structure to every observation.

```
