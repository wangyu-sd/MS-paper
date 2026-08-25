# Figure Plan

The main text uses **six** primary figures. The paper is organized around one scientific representation, one reason that static inference fails, one experimental grounding principle, one long-horizon learning mechanism and one biological payoff:

- **representation:** fragment-mass fingerprints (FMFs) provide a structure-derived mass-support space on which molecular alternatives can be compared;
- **challenge:** increasingly faithful molecular hypotheses create progressively harder evidence demands rather than monotonically simplifying identification;
- **grounding:** experimental spectra, not chemical plausibility or model prose, determine which FMF support becomes discriminative evidence;
- **long-horizon learning:** a scientific agent persists across challenge–degradation–repair–recovery–transfer cycles, revising either the executable FMF/pLSE program or the post-pretraining METEOR reasoning program while scientific authority remains immutable;
- **deployment:** evidence seeking carries each dark spectrum only to the structural resolution justified by the available experiment;
- **biological payoff:** evidence-bounded molecular families and transformation series expose biological programmes that anonymous peaks cannot support reliably.

The visual story should read:

`representation → harder challenge → experimental grounding → long-horizon learning → evidence-seeking dark-metabolome map → biological programme`.

Agent architecture, Research OS/UI, LLM routing, token/runtime infrastructure and generic software diagrams do **not** belong in the main figures.

## Figure 1 — Fragment-mass fingerprints encode molecular identity

**Scientific question:** what representation does the agent reason over?

**Message:** a small subset of structure-supported fragment masses contains substantial molecular identity information, but shared fragment masses do not distinguish close alternatives.

- **a** Define the FMF for molecule $M$ under executable program $G$: $F_G(M)=\{m_i\}$, retaining source/provenance and authority where available. Show a few supported masses rather than a dense mechanistic graph.
- **b** Intrinsic resolving-power experiment across the large structure pool: Top-1 / information bits versus number of sampled FMF masses; include isobaric-only retrieval.
- **c** Database-scaling result: precursor-only ambiguity grows with chemical-space size whereas sparse FMF matching contracts the candidate set.
- **d** Real-spectrum bridge: GT versus same-formula best-decoy FMF support, GT rank and GT-best-decoy margin on measured MS/MS.
- **e** FMF composition/depth ablation showing that more theoretical fragments are not automatically more informative; test depth-1, depth<=2 and full-lattice support.
- **f** Candidate-relative discrimination: shared masses versus GT-specific masses for one intuitive same-formula case.
- **g–h** Two deep chemical examples, including one correctly resolved case and one explicitly unresolved case.

**Critical claim:** FMF is not merely a database fingerprint. It is the structure-derived scientific representation from which candidate-relative experimental evidence is constructed.

**Critical control:** synthetic self-retrieval and measured-spectrum evaluation must be visually and statistically separated.

## Figure 2 — Improved molecular hypotheses create progressively harder evidence challenges

**Scientific question:** why is a static spectrum-to-structure model insufficient?

**Message:** as incorrect candidates approach the true structure, their FMFs increasingly overlap and fixed evidence loses discriminative margin.

- **a** Conceptual regime shift from implausible alternatives to close same-formula/local-connectivity alternatives.
- **b** Candidate difficulty across independent generators and matched database candidates using structure-only metrics.
- **c** Shared FMF support rises and candidate-specific FMF support falls with candidate similarity.
- **d** Multiple frozen evidence systems on identical difficulty strata: exact mass, forward-spectrum similarity, external fragmentation-aware comparator(s), FMF support and initial pLSE/evidence snapshot.
- **e** Molecule-group candidate fidelity versus GT-best-decoy separability after matching candidate-set size and precursor constraints.
- **f** One spectrum followed across easy and hard candidate populations to show how previously discriminative masses become shared.

**Critical claim:** better molecular hypothesis generation can create harder scientific challenges and move metabolite elucidation from generation-limited to evidence-limited.

**Critical control:** hardness cannot be created by arbitrary negative mining; the trend must reproduce across independent candidate sources with matched candidate counts and precursor constraints.

## Figure 3 — Experimental spectra ground discriminative FMF evidence

**Scientific question:** what determines whether the agent has learned the right evidence?

**Message:** structure-derived FMF support is chemical possibility; experimental evidence is the subset of measured observations that changes the relative support of competing molecular hypotheses.

- **a** Structure-derived FMF/reaction-space prior versus spectrum-conditioned evidence view.
- **b** Correct-spectrum / no-spectrum / matched shuffled-spectrum controls on identical candidates.
- **c** Spectral lift and identity lift in GT rank, GT-best-decoy margin and candidate-specific FMF evidence.
- **d** Evidence-authority decomposition: mass-supported, candidate-specific, trajectory-certified, shared, unsupported and not-evaluated/truncated.
- **e** Representative candidate set where the chemical prior is similar across alternatives but only the correct measured spectrum changes the supported hypothesis.

**Critical claim:** the scientific verifier is not another language model. Useful evidence must remain bound to the identity of the experiment and, where reaction-level authority is claimed, to executable chemistry.

**Move out of main figure:** detailed CoT language-form controls and UI/agent observability → Extended Data / Supplementary.

## Figure 4 — A long-horizon scientific agent learns through molecular challenge and recovery

**Scientific question:** how does the system improve when the scientific problem itself becomes harder?

**Message:** the long-horizon object is not a longer trajectory or monotonically increasing score, but repeated challenge → degradation → targeted repair → recovery → transfer → new challenge cycles in which harder molecular hypotheses and executable evidence falsify each other.

This figure must show the **scientific learning loop**, not a generic multi-agent architecture.

- **a** Define a durable `ChallengeSet`: one spectrum, close candidate alternatives, candidate-similarity class, FMF/pLSE evidence gap, METEOR reasoning gap and creation/resolution round. Show sources such as METEOR hard decoys, same-formula/same-scaffold alternatives, pLSE counterexamples, ERSF disagreement and unresolved spectra.
- **b** One asymmetric challenge cycle: improved METEOR candidate fidelity creates a harder local alternative set and causes a measurable fall in FMF/pLSE discrimination; failure attribution chooses the mutable side rather than round-robin mutation.
- **c** Two typed scientific programs. Evidence side: $P=(G_{chem},S_{search},E_{evidence},I_{impl})$. Hypothesis side: $M=(P_{frozen},C_{spectrum},R_{cot},T_{post},D_{decode})$, with molecular pretraining immutable. Show the CoT program as typed states (ObservedEvidence → CandidateHypotheses → MechanisticConstraints → DiscriminativePredictions → UnresolvedAmbiguities → CounterfactualPredictions → NextEvidenceRequest → FinalCandidateDistribution), not free-form prose.
- **d** Immutable verification boundary and falsification contract: exact edit, predicted gain/regression, fresh discovery evaluation, chemistry/evaluator receipts, protected-data firewall and no self-promotion.
- **e** Replay/ablation/transfer causal-credit hierarchy: associated → replay-supported → ablation-supported → transfer-supported. Scientific memory can seed later mutations only from mutation-eligible evidence.
- **f** Long-horizon challenge–recovery trajectory across rounds: candidate fidelity, candidate distinguishability, recovery rounds and recovery cost. Show repeated recovery followed by a genuinely harder challenge rather than only monotonic benchmark gain.
- **g** Causal ablations: fixed both sides, pLSE/FMF-only evolution, METEOR-only evolution, random/no-agent mutation, no replay, no reusable scientific memory and ungated/weakened verification.
- **h** Cross-generation and cross-family transfer: recovered edits must improve unseen challenge families / independent candidate sources after freeze; report reintroduced-failure rate.

**Primary long-horizon endpoints:** challenge introduction rate, recovery rate, rounds-to-recovery, cross-generation transfer, cross-family transfer, reintroduced failure rate, GT-best-decoy margin, ambiguity-set size and total compute/training cost.

**Critical claim:** ORBIT is not claimed to be intelligent because it runs for a long time or contains multiple workers. The claim is that it persists across changing molecular problems, detects when current evidence or reasoning becomes insufficient, revises the responsible executable scientific program, verifies whether the revision caused recovery, and reuses only causally supported lessons in the next challenge.

**Critical validation:** PR #45 defines the long-horizon H0–H7 architecture but is plan-only. The final main-text claim requires H5 challenge–recovery and H6 replay/ablation/transfer benchmarks to be implemented and frozen. Runtime durability alone is not scientific evidence.

**Move to Extended Data:** durable campaign/restart mechanics, worker capability ceilings, independent reviewer → repair actor → fresh evaluation lifecycle, full mutation operator catalogue and dense cross-generation matrices.

## Figure 5 — Long-horizon evidence seeking maps the dark metabolome

**Scientific question:** what does long-horizon scientific intelligence enable at metabolomics scale?

**Message:** each dark spectrum is treated as an evidence-seeking scientific campaign that can resolve, narrow or explicitly abstain; the resulting resource preserves both structural hypotheses and what evidence is still missing.

- **a** Independent metabolomics cohort(s): all MS/MS → frozen QC → exact-library-hit removal → blinded anchors + dark spectra.
- **b** DarkSpectrumCampaign: candidate proposal → FMF/pLSE evidence → posterior/ambiguity → choose next discriminating computation/evidence → belief update → stop. Valid terminal states are resolved-supported, narrowed hypotheses, unresolved-insufficient-evidence, out-of-scope and budget-exhausted.
- **c** Blinded-anchor generator recall, conditional discrimination and end-to-end resolution with peer-reviewed baselines.
- **d** Resource-wide resolution landscape: unresolved → formula/class → molecular family → bounded candidate set → high-confidence putative 2D structure → orthogonally confirmed identity; include calibrated set-size / false-resolution distributions.
- **e** Molecular-family organization of dark spectra defined from structure/FMF relationships **without biological labels**; encode evidence level separately from structural similarity.
- **f** Tissue/condition distribution and recurrence of those frozen molecular families; show whether family-level aggregation reveals coherent co-regulation that isolated peaks obscure.
- **g** Candidate structural-transformation series connecting previously anonymous features. Repeated mass/graph changes are shown as candidate relationships, not automatically labelled as enzymatic reactions.
- **h** Parallel resolved and unresolved evidence dossiers, including the remaining discriminating evidence requirement for unresolved cases.

**Campaign boundary:** an algorithmic failure discovered during a dark-spectrum or prospective campaign may create a separate discovery-phase improvement campaign, but protected/prospective evidence from the original case must not become adaptive mutation input.

**Resource deliverable:** spectrum provenance, precursor information, FMF-supported/discriminative masses, candidate set, evidence authority, unresolved alternatives, remaining evidence requirement, calibrated resolution, recurrence, family membership, biological distribution summaries and validation status.

**Biological principle:** Figure 5 changes the unit of biological analysis from isolated anonymous peaks to evidence-qualified molecular families without pretending that every spectrum has reached exact structural identity.

## Figure 6 — Structural organization of the dark metabolome reveals biological programmes

**Scientific question:** why does the long-horizon system matter for metabolomics biology?

**Message:** one coherent biological conclusion emerges because dark features have been structurally organized, not merely because more peaks received names.

The exact biological result must be data-driven. Prioritize the strongest result among three prespecified levels:

1. **tissue/compartment programme:** a molecular family is reproducibly restricted to, or enriched in, one tissue/compartment;
2. **condition programme:** a structurally coherent family or transformation series changes together across a genotype, treatment, disease or phenotype;
3. **origin/pathway programme:** dedicated perturbation or tracing resolves dietary, microbial or host contribution or places the family in a candidate metabolic pathway.

- **a** Resource-wide tissue/condition map identifying the principal evidence-qualified family or metabolite programme.
- **b** Replication across independent biological samples or an external cohort where available.
- **c** Structural/FMF organization of the family, including shared scaffold and repeated candidate transformations linking previously dark features.
- **d** Select 2–4 anchor metabolites or spectra using a frozen discovery criterion.
- **e** Authentic-standard validation with matched MS/MS and RT/coelution; targeted MSn or spike-in for hard isomers when necessary.
- **f** Source-attribution experiment when the cohort supports it: diet intervention, antibiotic/gnotobiotic microbiome perturbation, isotope tracing, genotype or pathway perturbation.
- **g** One focused functional/pathway assay only when directly motivated by the resource-derived biological hypothesis and adequately supported anchor structures.
- **h** Integrated model constrained to the experimentally supported structural and causal resolution; explicitly retain unresolved branches.

**Critical claim:** tissue restriction does not prove origin; co-abundance does not prove a pathway; repeated mass differences do not prove enzymatic reactions. Figure 6 should progress from descriptive organization → replicated association → source/causal evidence only when each layer has the appropriate experiment.

**Nature-level payoff:** the strongest version is not “ORBIT annotated N spectra” but “a long-horizon scientific agent structurally organized a previously anonymous molecular programme, enabling a reproducible biological relationship and a targeted experiment that could not be formulated from the unannotated peaks alone.”

## Extended Data

1. Dataset composition, split and pretraining leakage audit.
2. Full synthetic FMF resolving-power/database-scaling/robustness analyses.
3. Complete real-spectrum FMF benchmark and same-formula candidate diagnostics.
4. Candidate-difficulty matching and evidence-bottleneck sensitivity analyses.
5. FMF depth/source/lattice-size and mechanistic-authority ablations.
6. Correct/no/shuffled-spectrum and typed-reasoning controls.
7. Long-horizon campaign contracts, pLSE/METEOR typed mutation surfaces, falsification contracts and worker capability boundaries.
8. Replay/ablation/transfer causal receipts, ScientificLesson memory boundary, independent review/repair/fresh-evaluation lifecycle and protected-data firewall tests.
9. Full challenge–recovery replicates, fixed-side/random/no-memory/no-replay/ungated controls, recovery cost and cross-family/external transfer.
10. DarkSpectrumCampaign terminal-state audit, resource QC, blinded-anchor evaluation, recurrence and calibrated resolution.
11. Molecular-family definitions, tissue/condition maps, family-level co-variation, candidate transformation series, metadata-permutation controls and evidence-level sensitivity analyses.
12. Complete anchor standards/RT/MSn validation plus diet/microbiome/isotope/genotype/pathway evidence where available; retain negative and unresolved source-attribution results.

## Visual principles

- White background, restrained typography, large molecular structures and spectra.
- Do not make an agent architecture diagram the centre of Figure 4; lead with a real challenge, a measurable degradation and a targeted recovery.
- Reuse anchor spectra across Figures 1–4 to make the scientific progression visually continuous.
- Distinguish structure-derived FMF support, measured spectral evidence, candidate specificity and mechanistic authority consistently.
- `NOT_EVALUATED`, truncation and unsupported chemistry must never be rendered as candidate contradiction.
- Figures 5–6 should visually resemble metabolomics resource/discovery figures rather than AI benchmark figures.
- In Figure 6, use biological metadata only after structural family construction is frozen, so the visual logic itself communicates that the biology was discovered from the resource rather than used to define it.
