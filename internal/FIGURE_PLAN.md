# Figure Plan

The main text uses **six** primary figures. The paper is organized around one scientific object and one adaptive mechanism:

- **scientific object:** fragment-mass fingerprints (FMFs) as structure-derived, experimentally sampled molecular evidence;
- **adaptive mechanism:** agent-driven scientific evolution of the executable FMF / fragmentation-evidence program under an immutable verification boundary.

The visual story should read:

`FMF structural code → candidate-relative evidence → evidence bottleneck → spectrum-specific evidence → agent-evolved FMF program → dark-metabolome resource → biological discovery`.

Agent architecture, Research OS/UI, LLM routing, token/runtime infrastructure and generic software diagrams do **not** belong in the main figures.

## Figure 1 — Fragment-mass fingerprints encode discriminative molecular identity

**Message:** a small subset of structure-supported fragment masses carries substantial molecular identity information, but shared fragment masses do not distinguish close alternatives.

- **a** Define the FMF for molecule $M$ under executable program $G$: $F_G(M)=\{m_i\}$, optionally retaining source/provenance and authority. Show a few supported masses rather than a dense mechanistic graph.
- **b** Intrinsic resolving-power experiment across the large structure pool: Top-1 / information bits versus number of sampled FMF masses; include isobaric-only retrieval.
- **c** Database-scaling result: precursor-only ambiguity grows with chemical-space size whereas sparse FMF matching contracts the candidate set.
- **d** Real-spectrum bridge: GT versus same-formula best-decoy FMF support, GT rank and GT-best-decoy margin on measured MS/MS.
- **e** FMF composition / depth ablation showing that more theoretical fragments are not automatically more informative; test depth-1, depth<=2 and full-lattice support.
- **f** Candidate-relative discrimination: shared masses versus GT-specific masses for one intuitive same-formula case.
- **g–h** Two deep chemical examples, including one correctly resolved case and one explicitly unresolved case.

**Critical claim:** FMF is not merely a database fingerprint. It is the structure-derived mass-support layer from which candidate-relative experimental evidence is constructed.

**Critical control:** synthetic self-retrieval and measured-spectrum evaluation must be visually and statistically separated.

## Figure 2 — Better molecular hypotheses expose an evidence bottleneck

**Message:** as incorrect candidates approach the true structure, their FMFs increasingly overlap and fixed evidence loses discriminative margin.

- **a** Conceptual regime shift from implausible alternatives to close same-formula / local-connectivity alternatives.
- **b** Candidate difficulty across independent generators and matched database candidates using structure-only metrics.
- **c** Shared FMF support rises and candidate-specific FMF support falls with candidate similarity.
- **d** Multiple frozen evidence systems on identical difficulty strata: exact mass, forward-spectrum similarity, external fragmentation-aware comparator(s), FMF support and initial pLSE/evidence snapshot.
- **e** Molecule-group candidate fidelity versus GT-best-decoy separability after matching candidate-set size and precursor constraints.
- **f** One spectrum followed across easy and hard candidate populations to show how previously discriminative masses become shared.

**Critical claim:** better candidate generation can shift metabolite elucidation from generation-limited to evidence-limited.

**Critical control:** hardness cannot be created by arbitrary negative mining; the trend must reproduce across independent candidate sources with matched candidate counts and precursor constraints.

## Figure 3 — Experimental spectra distinguish FMF evidence from chemical possibility

**Message:** structure-derived FMF support is a chemical prior; experimental evidence is the subset of measured observations that changes the relative support of competing molecular hypotheses.

- **a** Structure-derived FMF / reaction-space prior versus spectrum-conditioned evidence view.
- **b** Correct-spectrum / no-spectrum / matched shuffled-spectrum controls on identical candidates.
- **c** Spectral lift and identity lift in GT rank, GT-best-decoy margin and candidate-specific FMF evidence.
- **d** Evidence-authority decomposition: mass-supported, candidate-specific, trajectory-certified, shared, unsupported and not-evaluated/truncated.
- **e** Representative candidate set where the chemical prior is similar across alternatives but only the correct measured spectrum changes the supported hypothesis.

**Move out of main figure:** language-form CoT controls and UI/agent observability → Extended Data / Supplementary.

## Figure 4 — Agent-driven evolution improves the executable FMF evidence program

**Message:** hard molecular counterexamples can drive causal, auditable improvement of the program that generates and interprets FMF evidence, without allowing the LLM to define scientific truth.

This figure must show the **scientific evolution loop**, not a generic multi-agent architecture.

- **a** One real failure: an experimentally informative GT-specific mass is missing, or an over-broad rule creates shared accidental support. Localize the failure to a mutable FMF / CID / ERSF algorithm surface.
- **b** Typed scientific mutation contract: parent program, failure evidence, hypothesis, causal claim, exact edit, predicted gain/regression, falsification test and compute budget. The LLM proposes the edit but does not choose the scientific objective or promotion outcome.
- **c** Immutable verification boundary: atom/H/charge/electron conservation, exact-mass closure, atom lineage, no spectrum-created chemistry edges, evaluator/dataset receipts, protected-split firewall and frozen promotion authority.
- **d** Replay/ablation causal credit on one frozen evaluator receipt: associated-only → replay-supported → ablation-supported. Show that budget inflation or evaluator drift cannot receive causal credit.
- **e** Scientific memory: only replay/ablation-supported lessons from mutation-eligible screen/discovery data can seed later mutations; held-out/external/prospective evidence may support or refute a lesson but never re-enter adaptive mutation.
- **f** Evolution trajectory across generations: GT-decoy discrimination / FMF specificity versus complexity or runtime, with accepted and rejected mutations distinguished.
- **g** Ablations: no-agent/random mutation, no causal replay, no reusable scientific memory, ungated evolution and full scientific-RSI loop.
- **h** External transfer of the evolved FMF evidence program to independent molecule groups / candidate sources / datasets.

**Critical claim:** the paper is not claiming that an LLM can certify chemistry. The claim is that LLM-proposed typed program edits can yield replay-confirmed, transferable scientific improvements when deterministic scientific authority remains outside the mutable search space.

**Critical validation:** PR #43 implements this P5 substrate; PR #44 explicitly leaves the frozen replay/ablation/external-transfer scientific benchmark open. The final figure requires those benchmark results before any self-improvement claim is promoted.

**Move to Extended Data:** independent reviewer → repair actor → fresh evaluation lifecycle; full mutation operator catalogue; runtime/ledger details; complete cross-generation matrices if visually dense.

## Figure 5 — Evidence-bounded mapping of the dark metabolome

**Message:** the practical output at metabolomics scale is a high-throughput evidence-bounded molecular resource, not a forced unique SMILES for every dark spectrum.

- **a** Independent metabolomics cohort(s): all MS/MS → frozen QC → exact-library-hit removal → blinded anchors + dark spectra.
- **b** Blinded-anchor generator recall, conditional discrimination and end-to-end resolution with peer-reviewed baselines.
- **c** Resource-wide resolution landscape: unresolved → formula/class → molecular family → bounded candidate set → high-confidence putative 2D structure → orthogonally confirmed identity.
- **d** Candidate-space contraction and calibrated set-size / false-resolution distributions.
- **e** Chemical-space / molecular-family organization of dark spectra, with structural similarity and evidence level encoded separately.
- **f** Recurrence and reproducibility across biological samples / cohorts.
- **g** Parallel resolved and unresolved evidence dossiers.

**Resource deliverable:** spectrum provenance, precursor information, FMF-supported/discriminative masses, candidate set, evidence authority, unresolved alternatives, calibrated resolution, recurrence and validation status.

## Figure 6 — Dark-metabolome mapping reveals previously hidden biology

**Message:** structural organization of the dark-metabolome resource exposes one reproducible biological programme that could not be interpreted reliably from chemically anonymous features alone.

- **a** Resource-wide discovery of one coherent molecular family / transformation series / metabolite programme associated with a predefined biological context.
- **b** Replication in independent biological samples or an external cohort where available.
- **c** Structural organization of the family, including shared scaffold / repeated transformations / discriminative fragment-mass evidence.
- **d** Select 2–4 anchor metabolites or spectra from a frozen discovery criterion.
- **e** Authentic-standard validation with matched MS/MS and RT/coelution; targeted MSn or spike-in for hard isomers when necessary.
- **f** One focused biological validation only when it directly tests the resource-derived biological hypothesis.
- **g** Integrated biological model constrained to the validated structural resolution.

**Critical claim:** a large annotation resource alone is insufficient. Figure 6 must show a biological conclusion enabled by the structural organization of previously dark spectra.

## Extended Data

1. Dataset composition, split and pretraining leakage audit.
2. Full synthetic FMF resolving-power/database-scaling/robustness analyses.
3. Complete real-spectrum FMF benchmark and same-formula candidate diagnostics.
4. Candidate-difficulty matching and evidence-bottleneck sensitivity analyses.
5. FMF depth/source/lattice-size and mechanistic-authority ablations.
6. Correct/no/shuffled-spectrum and structured-reasoning controls.
7. Scientific-RSI mutation catalogue, falsification contracts, replay/ablation details and budget controls.
8. ScientificLesson memory boundary, independent review/repair/fresh-evaluation lifecycle and protected-data firewall tests.
9. Full evolution replicates, random/no-memory/no-replay/ungated controls and external transfer.
10. Dark-metabolome resource QC, blinded-anchor evaluation and recurrence.
11. Complete dark-spectrum evidence dossiers and standards/RT/MSn validation.
12. Resource-wide biological association, multiple-testing control, replication and negative controls.

## Visual principles

- White background, restrained typography, large molecular structures and spectra.
- Do not make an agent architecture diagram the centre of Figure 4; lead with one falsifying chemical counterexample and one exact program revision.
- Reuse anchor spectra across Figures 1–4 to make the scientific progression visually continuous.
- Distinguish structure-derived FMF support, measured spectral evidence, candidate specificity and mechanistic authority consistently.
- `NOT_EVALUATED`, truncation and unsupported chemistry must never be rendered as candidate contradiction.
- Figures 5–6 should visually resemble metabolomics resource/discovery figures rather than AI benchmark figures.
