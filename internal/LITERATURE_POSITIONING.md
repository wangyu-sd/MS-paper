# Peer-reviewed literature positioning

This document defines the competitive landscape used to write the manuscript. The central argument is grounded primarily in peer-reviewed work; preprints can be acknowledged as frontier context but must not carry the manuscript's essential scientific claims.

| Work | Venue | What it established | What ORBIT-MS must not re-claim | ORBIT-MS distinction |
|---|---|---|---|---|
| CSI:FingerID (Dührkop et al., 2015) | PNAS | spectrum/fragmentation-tree to molecular fingerprint for database search | fingerprint-based retrieval | candidate-specific evidence evaluated directly against hard alternatives |
| SIRIUS 4 (Dührkop et al., 2019) | Nature Methods | integrated formula/structure inference using fragmentation trees and CSI:FingerID | generic “turn MS/MS into structure information” | asks how discriminative evidence changes when alternatives become harder |
| CFM-ID 4.0 (Wang et al., 2021) | Analytical Chemistry | rule/probability-based ESI-MS/MS prediction and compound identification | fragmentation-aware candidate scoring | atom-traceable, competitor-relative evidence rather than spectrum fit alone |
| CANOPUS (Dührkop et al., 2021) | Nature Biotechnology | compound-class annotation of unknown spectra and biological deployment | class-level interpretation of unknown metabolomes | attempts structure-level contraction with calibrated fallback to lower resolution |
| COSMIC (Hoffmann et al., 2022) | Nature Biotechnology | confidence-aware structural annotation beyond spectral libraries | confidence scoring alone | risk control is tied to candidate-specific chemical evidence and candidate recall |
| MSNovelist (Stravs et al., 2022) | Nature Methods | de novo structure reconstruction from predicted fingerprints | fingerprint-to-SMILES generation | focuses on the evidence needed to adjudicate generated alternatives |
| BUDDY (Xing et al., 2023) | Nature Methods | bottom-up MS/MS formula discovery and FDR-aware formula inference | formula-space contraction | discrimination within same-formula structural candidate sets |
| MIST (Goldman et al., 2023) | Nature Machine Intelligence | domain-inspired spectrum transformer with formula/neutral-loss inductive bias | domain-aware spectrum encoding | separates chemical prior from experimental identity evidence and adapts the evidence model |
| MassFormer (Young et al., 2024) | Nature Machine Intelligence | strong forward-spectrum prediction with graph transformers | forward simulation | explicitly separates simulation from candidate discrimination |
| MassSpecGym (Bushuiev et al., 2024) | NeurIPS Datasets & Benchmarks | standardized leakage-resistant de novo/retrieval/simulation benchmark | benchmark construction | uses hard candidate strata to expose candidate/evidence co-difficulty |
| DiffMS (Bohde et al., 2025) | ICML | formula-constrained graph diffusion and structure-only decoder pretraining | formula-constrained de novo generation | provides an external candidate distribution for testing adaptive evidence |
| Coverage bias (Kretschmer et al., 2025) | Nature Communications | structural coverage can dominate apparent small-molecule ML performance | generic split criticism | motivates explicit pretraining leakage audit and matched candidate-difficulty analysis |
| FIORA (Nowatzky et al., 2025) | Nature Communications | bond-local fragmentation-event modeling improves forward MS/MS prediction | explainable forward fragmentation | evaluates atom-traceable fragmentation for GT–decoy specificity, not only spectral similarity |
| DreaMS (Bushuiev et al., 2026) | Nature Biotechnology | repository-scale self-supervised spectrum representation and 201M-spectrum atlas | foundation-model scale or spectral embedding novelty | uses unlabelled spectra as deployment data while focusing on evidence and structural falsification |
| MetGenX (Wang et al., 2026) | Nature Communications | structure-informed de novo generation and mouse-liver unknown-metabolite discovery | “we generated unknown mouse metabolites” as sufficient novelty | mouse deployment must show blinded calibration, alternative rejection and orthogonal validation |
| Reverse metabolomics (Gentry et al., 2024) | Nature | chemically grounded discovery linking synthesized structures, repository data and phenotypes | broad discovery claim without validation | sets the evidentiary bar for any biological/novel-structure claim |

## Editorial positioning

The Nature-level proposition is **not**:
- a larger mass-spectrometry language model;
- an agent workflow;
- a new forward-spectrum simulator;
- another de novo generator;
- another benchmark leaderboard gain;
- a set of unvalidated mouse structures;
- “CoT works for chemistry”.

The working proposition is:

> As molecular alternatives become more faithful, fixed spectral evidence loses discriminative power. Molecular structure elucidation therefore benefits from adaptive, candidate-specific fragmentation evidence that is evaluated relative to the alternatives actually under consideration.

This language is deliberately narrower than “co-evolving experimental evidence”. The experimental spectrum itself remains fixed unless a new measurement is physically acquired.

## Four distinctions to defend throughout the paper

### 1. Simulation ≠ explanation
A forward model can reproduce an observed spectrum without identifying a unique causal fragmentation trajectory.

### 2. Explanation ≠ discrimination
A chemically plausible fragment can be shared by the ground truth and every hard decoy. Figure 2 therefore evaluates evidence on matched competing structures.

### 3. Discrimination ≠ end-to-end identification
Even a perfect evidence model cannot recover a ground truth absent from the generated candidate set. Candidate recall, conditional discrimination and end-to-end resolution must be reported separately.

### 4. Prediction ≠ identification
A unique generated SMILES for a dark mouse spectrum remains a hypothesis until the evidence level supports unique resolution and, where identification is claimed, orthogonal validation is obtained.

## Comparator priority

The hard-decoy evidence benchmark should include mature peer-reviewed comparator families wherever technically executable:

- exact-mass / formula-only scoring;
- forward-spectrum similarity;
- CFM-ID;
- SIRIUS/fragmentation-tree-derived evidence where a reproducible interface is available;
- FIORA or another peer-reviewed fragment-event model where suitable;
- the frozen initial pLSE and its internal ablations.

Emerging methods that overlap strongly with fragmentation-aware ranking should be monitored, but an unreviewed preprint should not be used to support a central manuscript claim.

## Preprint policy

Preprints may be added to a final related-work paragraph only when they materially define the contemporary frontier. They should be described as emerging approaches and should not establish benchmark validity, the central evidence-bottleneck premise or biological conclusions.

## Nature-main-track extension

The strongest conceptual extension is prospective evidence-guided acquisition:

> residual candidate ambiguity → select the measurement expected to maximally separate survivors → acquire MSn/CE evidence → quantify candidate-space contraction.

Only after this loop is demonstrated should the manuscript claim literal co-evolution of hypotheses and experimental evidence or sequential hypothesis–experiment co-design.
