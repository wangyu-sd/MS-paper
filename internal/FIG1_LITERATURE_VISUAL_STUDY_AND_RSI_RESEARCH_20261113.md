# ORBIT-MS Figure 1 redesign: scientific figure references and actionable Agentic RSI research

**Date:** 2026-11-13  
**Purpose:** Evidence-based visual design and a limited-compute proposal to improve the *existing* Scientific Improver.  
**Status:** Literature-backed **design decisions and future implementation proposals**. This document does not claim an implemented new agent policy, completed additional model training, autonomous performance gain, or a validated chemical discovery.

## A. What strong scientific framework figures actually do

The main methodological Figure 1 should be **chemistry-led and example-led**, not four equal columns named G/W/V/Agent. It must communicate (i) why measured MS/MS is structurally ambiguous; (ii) what new chemical information MMA represents; (iii) how graph construction and forward fragmentation use that information; (iv) which errors are discriminated or deliberately left ambiguous; and (v) how one **measured** training failure selects the next scientific learning intervention.

| Reference, publication and original link | Observed figure grammar | What to borrow for ORBIT-MS | What NOT to copy |
| --- | --- | --- | --- |
| **DreaMS**, Bushuiev et al., *Nature Biotechnology* (2025), [Fig. 1](https://www.nature.com/articles/s41587-025-02663-3), also attached locally as \`s41587-025-02663-3.pdf\` (p. 3) | (a) experimental sample → spectrum/annotation deficit; (b) measured space vs annotated reference-molecule space; (c) data/learning/applications | Scientific bottleneck stated first, clear observed-spectra versus structure-information separation; few visual grammars per zone | Do not turn Figure 1 into a global dataset census or UMAP |
| **BUDDY**, Xing et al., *Nature Methods* (2023), [Fig. 1](https://www.nature.com/articles/s41592-023-01850-x) | Direct visual contrast of top-down and bottom-up MS/MS formula reasoning; measured spectral peaks and formula candidates are the scientific objects | Use the actual mapping from peak to ionic formula and candidate chemical fragments for MMA; visualize why the inverse problem is ambiguous | Do not represent a predicted fragment graph as experimentally identified |
| **MADGEN**, Wang et al., *ICLR* (2025), [Fig. 1](https://openreview.net/pdf?id=z5uVAKwmjf), locally \`2501.01950v4.pdf\` (p. 4) | Compact two-stage overview PLUS source-based molecular drawings at steps 0, 10, 20, 30, 40 | Use a single authentic precursor spectrum and **actual partial-graph sequence** for MMA/Canonical Hybrid G; show different complete isomer candidates | Do not use a schematic "trajectory" with arbitrarily assembled chemical structures |
| **ChemCrow**, Bran et al., *Nature Machine Intelligence* (2024), [Fig. 1](https://www.nature.com/articles/s42256-024-00832-8) | Real chemistry task + thought/action/tool observation; one substantive scientific example explains tool use | Use a single evidence-backed failure → hypothesis → intervention → experimental outcome record for the Agent; clear inputs and outputs | Do not use generic agent/tool icons or imply an LLM computes fragment chemistry itself |
| **Robin**, Ghareeb et al., *Nature* (2026), [Fig. 1](https://www.nature.com/articles/s41586-026-10652-y) | Scientific hypothesis → experiment → analysis → next hypothesis, with agent architecture subordinate to experimental feedback | Show **two distinct RSI loops**: WGV chemical capability update and evidence-memory update of Agent decisions | Robin's actual laboratory experiments should not be invented for ORBIT-MS: our first loop is computational training/evaluation |
| **Saturn**, *Nature Machine Intelligence* (2026), [Fig. 1–2](https://www.nature.com/articles/s42256-026-01200-4) | Generator / expensive-oracle evaluation / cached rewards / replay, depicted as repeated closed-loop measurement | Reinforce that expensive computation must be tied to measured outcome and reusable experience, not repeated blind generation | Do not transplant RL training, SMILES replay or an oracle budget module into our method figure |
| **AI Scientist**, *Nature* (2026), [Fig. 1](https://www.nature.com/articles/s41586-026-10265-5) | Experimental-tree search and staged empirical selection, not only a circular arrow | Use traceable before/after experimental receipts and a specific update decision | We do not need open-ended code editing or tree search to make the chemical discovery scientifically meaningful |
| **Agentic AI systems for scientific discovery**, *Nature Reviews Methods Primers* (2026), [Fig. 1–2](https://www.nature.com/articles/s43586-026-00534-y) | Distinguishes scientific-cycle overview from actual architecture/tool interfaces | Figure 1 can show the chemistry inference and scientific learning cycle; leave training-log implementation to Extended Data | Do not merge all agent components, sources, evaluation and paper results into one giant product-flow chart |

**Design synthesis:** BUDDY provides **chemical evidence grammar**, MADGEN provides **one-molecule trace grammar**, DreaMS provides **problem-to-method hierarchy**, ChemCrow/Robin provide **grounded scientific decision grammar**. Keep the figure uniquely ORBIT-MS: an experimentally observed peak is connected to alternative structural motifs, those motifs inform legal graph construction, chemically represented fragmentation tests complete candidates, and an Agent chooses the next chemistry capability to improve.

## B. The final Figure 1 should have one dominant chemical trace and five labelled panels

**Proposed visual hierarchy, 16:9 landscape, white background, no marketing-style cards:**

- **Upper ribbon (a; ~13–15% height):** A real measured MS/MS and a compact same-formula ambiguous connectivity pair. One short problem statement: "Mass agreement does not uniquely specify molecular connectivity." No global corpus statistics.
- **Main body left (b; ~30% width): MMA — peak → structural motifs.** One *measured* fragment peak branches into 2–3 **compatible** ionic compositions or 2–3 **alternative graph-based fragment hypotheses**, each with an explicit support/proposal prior. Show an **atom–bond alignment** from a fragment candidate to an existing partial molecular graph. A small Exact / H-shift / restricted Edit tier legend is meaningful only when source-output examples exist.
- **Main body centre (c; ~30% width): G — construct complete structures.** Three real canonical growth snapshots: motif/ring initial state → legal atom/ring/motif attachment → two source-generated competing precursor graphs with same allowed composition. Keep partial graphs fully drawn and graph-valid, not abstract icons.
- **Main body right (d; ~40% width): W predicts / V compares.** Two candidate graphs produce **different structurally represented fragment hypotheses** in W, which receives **no measured product-ion peaks**. Separately route the *same real measured MS/MS* directly to V. The lower portion of d shows a **candidate × measured-peak evidence matrix**, common vs discriminative support and actual score/rank or a bounded set. Explicitly label proposed ion structures as model hypotheses, not experimentally observed intermediates.
- **Lower ribbon (e; ~26–30% height): RSI — scientific diagnosis to measured capability change.** Show one actual TRAIN FIT failure case/failure cluster and a scientific decision record; one of four pre-existing typed actions executed; before/after structural recovery and persistent memory. One teal return line updates MMA/G/V and one thin gray line returns a tested lesson to future Agent decisions. Until agent episodes finish, this panel is marked **schematic / protocol**, not a plot of fabricated learning gains.

**Real continuity matters:** All molecule/fragment examples in b–d must be from the **same experimental query** and real versioned G/W/V output. A known-formula example must say "known-formula conditional illustration". Use RDKit SVG with consistent scale and actual stick spectrum from the same source. Candidate sets without source scores/peak assignments are not sufficient.

**Scientific message visible without caption:**
1. Hypothesis generation can fail before evidence ranking begins.
2. MMA introduces *structured peak-conditioned chemical knowledge*, not just a motif embedding.
3. W/V distinguishes competing *complete molecules* using proposed fragmentation linked to actual measured ions.
4. Failure in either stage tells the Agent what kind of chemical experience to collect next.

## C. Agentic RSI: current code reality, not the story we would like it to tell

Source: [orbit-ms PR96](https://github.com/wangyu-sd/orbit-ms/pull/96), especially \`src/orbit_ms/agents/scientific_improver.py\` and \`scripts/run_pr93_scientific_improver.py\`. PR96 is open/draft at the time of this note.

- \`observation()\` classifies TRAIN FIT cases into \`solved\`, \`ranking\` and combined \`generator_or_knowledge\`, sends at most 12 failed case evidence packets, top-three candidates per case, a few numerical G/W/V fields and an optional aggregate failure analysis. It does **not** expose a structured per-peak chemical explanation of why a motif, ring or candidate-specific fragment was missing.
- \`choose()\` lets the LLM select a **single** closed action from \`EXPAND_KNOWLEDGE\`, \`IMPROVE_GENERATOR\`, \`IMPROVE_VERIFIER\`, \`COLLECT_EVIDENCE\`. The decision must include textual diagnosis/hypothesis, case IDs, expected endpoint and confidence, but **does not currently select a chemical target subset or intervention parameters**.
- \`observation()\` passes \`history[-3:]\`; the runner derives condensed previous episodes. Memory is thus **recent chronological context**, not outcome-conditioned or applicability-matched chemical experience retrieval.
- \`args_action()\` currently maps each chosen action to an existing bounded training/analysis recipe. This is good reuse and should be maintained, but it is not fine-grained targeted scientific curriculum selection.
- \`compare()\` performs paired CAL evaluation to decide update acceptance. Actual multi-generation Autonomous Agent gains and GPU cost records have **not** been established through this GitHub audit. PR95 Gen1–10 are human/scripted development milestones, not an autonomous RSI experiment.
- The crucial weakness: if the Agent receives only Reach/Exact@1 and chooses "G for missed reach, V for wrong rank", a simple scripted router is a strong alternative explanation. To claim scientific reasoning, the Agent must exploit **nontrivial chemical context and cross-episode experience** that a scalar failure rule does not use.

## D. Literature-grounded, low-cost improvements worth implementing

| Research source | Useful mechanism | ORBIT-MS adaptation | Implementation priority |
| --- | --- | --- | --- |
| **Reflexion**, NeurIPS 2023, [paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | Store linguistic reflections from trial outcomes, retrieve on later attempts without LLM weight tuning | Keep real **hypothesis → action → observed chemical outcome → failure/success lesson**, not generic self-praise | P1 |
| **ExpeL**, AAAI 2024, [paper](https://ojs.aaai.org/index.php/AAAI/article/view/29936) | Extract and reuse transferable rules across experiences | Store a short applicability signature: adduct, formula/size/ring/motif profile, failure type, intervention, observed effect and negative outcomes | P1 |
| **GEPA**, ICLR 2026, [paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html) | Rich natural-language failure traces + measured optimization rather than only scalar rewards | Agent hypotheses should cite concrete **peak–motif–graph evidence** and a falsifiable Reach or ranking prediction | P0 |
| **AFlow**, ICLR 2025, [paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5492ecbce4439401798dcd2c90be94cd-Abstract-Conference.html) | Test decisions through actual executions and preserve useful search experience | Evaluate each selected chemistry intervention with the existing deterministic WGV tools | P0 (existing base) |
| **Darwin Gödel Machine**, 2025/2026, [paper](https://arxiv.org/abs/2505.22954) | Archive productive variants and avoid one fragile linear trajectory | Optional **tiny checkpoint archive** of champion/specialist states only if the one-path controller stalls; do not adopt code self-rewriting | P3 optional |
| **AlphaEvolve**, Google DeepMind 2025, [report](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | LLM proposes interventions; executable evaluator determines truth | Prioritize real structural recovery and measured cost over LLM's verbal confidence | P0 (principle) |
| **Self-Improvements in Modern Agentic Systems**, 2026, [survey](https://arxiv.org/abs/2607.13104) | Distinguishes foundation-model updates from memory/tool/scaffold improvement | Describe our chemistry-model updates separately from memory-mediated decision improvement; do not claim LLM weight RSI | P0 (terminology) |

### P0: Chemistry-specific failure packets (small code change, highest leverage)

**Existing:** \`scientific_improver.observation\` returns aggregate reach/rank and a few top-candidate scores.

**Proposed:** produce an *observable chemical failure signature* with existing records, such as:
- input precursor \(m/z\), adduct, measured peak subset and predicted formula success/failure **only when available**;
- TRAIN-only graph features describing the case (ring count, candidate graph size, heteroatom distribution) and **which legal G action/motif transition first failed** when actual traced rollout exists;
- MMA per-peak motif coverage / candidate availability / exact-H-shift-edit tier and whether a plausible fragment motif is represented by the current partial graph;
- W candidate-specific structural fragment support and V matched-peak contrast between same-formula competing structures, plus unexplained observed peak intensity;
- observed outcome and the relevant evidence or trace IDs.

This information can be assembled from \`PeakFragmentLibrary.hypotheses\`, \`template_features\`, \`mma_on_the_fly.on_the_fly_hypotheses\`, the existing ladder failure analyzer and the same-case frozen W/V scorer, without training a new model. Do not fabricate chemistry from the LLM; all fragments and scores originate from existing computational outputs. Reference structures/GT diagnostics are allowed **only for TRAIN FIT**, and independent unknown queries never receive their GT.

### P1: Choose **what chemistry to learn**, not only which of four action names

Keep the four bounded actions. Extend the Agent decision with a compact, **typed scientific target specification**:
\`\`\`text
{
  action: EXPAND_KNOWLEDGE | IMPROVE_GENERATOR | IMPROVE_VERIFIER | COLLECT_EVIDENCE,
  target_cluster: one existing TRAIN FIT failure cluster ID,
  chemical_hypothesis: falsifiable statement grounded in peak/motif/candidate evidence,
  predicted_endpoint: new_reach | corrected_rank | selective_resolution,
  expected_direction: increase | no_change,
  budget_hint: permitted bounded budget class,
  evidence_case_ids: existing diagnostic records
}
\`\`\`
**Important:** A new JSON field is not a new scientific capability by itself. The existing \`args_action\` runner must **actually restrict source experiences and training examples by target_cluster** or explicitly declare that scope-specific training was not carried out. For missing motif families, choose which *existing permitted structure sources or formula/ring clusters* to mine; for G misses, target valid growth trajectories of that signature; for V misrankings, mine same-formula hard decoys. One action remains selected per episode. Use existing PR95 machinery and no new G/V backbone.

### P1: Outcome-conditioned chemical experience memory

Instead of passing only the last three chronological episodes, persist and retrieve a bounded set of **chemically relevant** prior outcomes:
\`\`\`text
(signature, source_evidence, hypothesis, action, target_cluster,
 observed_delta_reach, observed_delta_exact1, observed_regressions,
 cost_gpu_hours_if_measured, applicable_scope, failure_or_success)
\`\`\`
Retrieve same/similar failure signatures, and return both successful and unsuccessful precedents. Compress repeated observations into **testable reusable rules** only when supported by more than anecdotal one-case gains. LLM weights stay frozen. The experimental question is whether experience-aware selection outperforms a no-memory Agent on held-out chemical failure clusters.

### P2: Compute-aware intervention selection (simple, not a new Bayesian model)

When several actions are credible, prefer the hypothesis with the best **supported expected newly recovered molecules per incremental GPU-hour**, while accounting for lost previous successes. Until there are enough real episodes, use source-calibrated simple priors or descriptive score/rank of actions, not a fabricated predictive model. \`COLLECT_EVIDENCE\` is preferred when uncertainty about the failure type is high and a new diagnostic execution is cheaper than model retraining. Maintain explicit measured wall-time/GPU-time receipts; the current \`--max-gpu-hours\` planning input should not be called real billed resource usage.

### P3: Checkpoint diversity only if necessary

A small champion/specialist archive could preserve (i) broadly successful G/MMA and (ii) a hard-isomer-specialized V or targeted chemical competence if one linear path loses useful structures. Combine only after actual benefit is demonstrated. **Do not** implement open-ended model/code self-edits, a new RL framework, MCTS or large-scale parallel agent tournaments as the first optimization: they cost more and move the paper away from chemistry.

## E. Scientific tests that make RSI nontrivial but affordable

**Baseline state:** reuse one common Gen0 W/G/V/MMA checkpoint and the existing PR96 runner. Keep W frozen for the initial comparison.

**A minimal experiment with meaningful controls:**
1. Run a frozen TRAIN FIT diagnostic pass with rich chemical signatures. Predefine at least three chemical failure groups (unreachable graphs, reachable misranked same-formula candidates, insufficient motif/fragment coverage), and make true unseen molecule groups the evaluation unit.
2. In 3 consecutive actual update generations, compare **Agent using chemistry + outcome memory** against the **best fixed intervention** and a **simple Reach-vs-ranking scripted router** with matched model/data/compute budgets. Track transfers to different molecules rather than only the exemplars used for diagnosis.
3. **Diagnostic-ablation replay**: on the *same* frozen state, compare action choice with/without detailed peak/motif evidence (still execute an intervention for a matched subset of states). This tests whether chemical understanding changes scientific decisions.
4. **Memory ablation**: retain the current LLM but suppress semantically retrieved past episode lessons. Decision-only agreement is diagnostic, not a substitute for measured downstream structural improvement.
5. Primary chemical endpoints: (i) correct graph newly enters candidate pool; (ii) correct graph was present but becomes top-ranked; (iii) prior successes lost; (iv) structural-resolution level on unseen real dark spectra improves under *independently calibrated* evidence rules. Secondary cost endpoint: measured incremental GPU hours / newly recovered true connectivity group.
6. Do **not** use CAL/official TEST labels for Agent training/action selection; keep a group-disjoint frozen evaluation and predeclare promotion and final held-out tests. Historical PR95 CAL200 and other development results are background only.

The user’s resource constraint is a maximum of **8 GPUs**. Start with **no new foundation model, no W retraining, no new physical experiment**, and reuse all PR95 chemistry data/tools. Any projected performance improvements remain **targets**, not reported scientific results.

## F. What is suitable to depict in the next Figure 1 versus a future Figure 3

**Figure 1 can show now (implementation-backed or conceptual):**
- chemically precise MMA peak→fragment-graph retrieval and partial-graph atom/bond alignment;
- G atom/ring/motif trajectory; W target-spectrum-blind forward fragmentation; V measured peak comparison;
- current Agent action set, measured-outcome evaluation, memory-mediated decision feedback and **explicitly schematic** RSI loop;
- the *scientific design objective*: extending recoverable molecular structures after selected chemistry learning.

**Figure 1 must NOT show as completed:**
- a real Agent selecting \`target_cluster\` or cost-optimal action before these fields are implemented and executed;
- an empirically improved 3-generation RSI curve or an LLM changed by weight-space finetuning;
- hallucinated structures/fragments/reaction mechanisms or dark-metabolite discovery counts.

**Figure 3 after implementation/tests:** use actual per-generation recovered and lost molecule IDs, chemical action/target cluster, successful vs unsuccessful memory-conditioned decisions, equal-budget fixed/rule/agent baselines, and real source-linked spectral/candidate illustrations. That is where the RSI mechanism becomes evidence rather than a cartoon.

## G. Implementation staging for future orbit-ms PR96 work

1. **First PR96 change (P0):** \`observation()\` chemistry evidence packet + unit tests checking source lineage, threshold semantics, case IDs and missing optional fields. No new training required.
2. **Second PR96 change (P1):** typed \`target_cluster\` + scoped existing-data training and semantic outcome retrieval with actual case filtering; preserve fixed action compatibility.
3. **Third PR96 change (P2):** predeclared matched action cost/benefit and actual episode-level model promotion receipts; 3-generation execution.
4. **Only after a measured gap:** consider optional archive/alternative branch or broader intervention grammar.

Do not silently transplant any of these planned changes into the currently implemented paper Methods as though they were experimentally validated.
