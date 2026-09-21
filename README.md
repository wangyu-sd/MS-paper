# MS-paper

Nature-level manuscript workspace for ORBIT-MS.

## Central proposition

**A tandem mass spectrum is a partial observation of a latent gas-phase molecular fragmentation world. Rather than learning a direct spectrum-to-structure shortcut, ORBIT-MS learns this world and performs prediction, explanation and inverse structure inference inside the same conservation-preserving chemical process.**

The manuscript has two inseparable layers.

### 1. A new inference paradigm

ORBIT-MS learns a probabilistic **molecular fragmentation world**:

`molecule + ionization + collision conditions → latent multi-branch reaction world → partial spectral observation`.

The same world supports three conditional inference modes:

- **World / Free:** what fragmentation networks can this molecule produce?
- **Verifier / Guided:** which reaction paths best explain the observed spectrum under a fixed computational budget?
- **Generator / Inverse:** which molecular structures can generate this observation and remain consistent when replayed through the same World?

This is the WGV-RL contribution. It is not three independent models. It is **one chemical world, three modes of inference**.

### 2. A new scientific object

The WGV system converts dark spectra into structural statements supported by progressively stronger evidence:

`mass/formula compatibility → World reachability → executable path support → candidate-specific evidence → bidirectional spectrum–structure consistency → calibrated structural statement → authentic-standard confirmation`.

This evidence hierarchy makes it possible to resolve dark chemistry at repository scale without pretending that every spectrum identifies one unique molecule. The resulting high-evidence structural population is then used to ask what the dark metabolome contains, how it is organized and what biology it encodes.

## Current title

**A molecular fragmentation world reveals the organization of the dark metabolome**

Alternative if the World results become the dominant contribution:

**Learning a molecular fragmentation world for mass-spectral inference**

Alternative if the biological organization becomes overwhelmingly strong:

**A molecular fragmentation world reveals the dark metabolome**

The preferred title retains both the methodological paradigm and the scientific consequence.

## Scientific model

The core generative picture is:

[
M,c ightarrow mathcal{W}(M,c) ightarrow S_{mathrm{obs}}
]

where:
- (M) is molecular structure;
- (c) is ionization/collision/instrument condition;
- (mathcal{W}) is the latent probabilistic fragmentation reaction world;
- (S_{mathrm{obs}}) is an incomplete experimental observation of that world.

Therefore:

[
S_{mathrm{obs}} 
eq mathcal{W}
]

and:

[
	ext{unobserved fragmentation} 
eq 	ext{false fragmentation}.
]

This distinction is fundamental to the paper.

## WGV as conditional inference over one world

[
egin{aligned}
	ext{Free:} &quad p(mathcal{T},Smid M,c) \
	ext{Guided:} &quad p(mathcal{T}mid M,S_{mathrm{obs}},c) \
	ext{Inverse:} &quad p(M,mathcal{T}mid S_{mathrm{obs}},c)
end{aligned}
]

where (mathcal{T}) denotes fragmentation trajectories/networks.

### Free / World
Learns a multi-branch probabilistic reaction network rather than a single predicted spectrum or one preferred mechanism.

### Guided / Verifier
Uses the observed spectrum to allocate computation toward reaction branches with the greatest explanatory/discriminative value. Chemical probability and evidential value are intentionally separated.

### Inverse / Generator
Maintains multiple molecular hypotheses rather than collapsing immediately to Top-1. Completed candidates must be replayed through the same World and evaluated for forward consistency.

## Why RL is necessary

The latent fragmentation world is combinatorial. Exhaustive expansion is impossible.

RL therefore solves a scientific resource-allocation problem:

> **Where should limited computation be spent in a large chemical reaction world?**

- SubTB/GFlowNet distributes flow across multiple plausible Free trajectories.
- Guided IQL/DAgger learns long-horizon value under spectrum conditioning.
- Inverse GFlowNet/SMC maintains diverse posterior molecular hypotheses.
- Frontier planning allocates compute without redefining chemistry.

This is not “RL to raise a score”. It is adaptive inference over a constrained chemical world.

## Chemistry and learning have different roles

**Chemistry defines legality; learning defines preference.**

Hard constraints include:
- atom/element conservation;
- electron conservation;
- formal charge;
- explicit H identity and transfer;
- exact mass;
- valence;
- formula/inventory closure;
- typed transition materializability.

These are not reward penalties that the policy may trade away. Invalid actions are removed from the executable action space.

Learning estimates:
- event propensity;
- branch probability;
- long-horizon explanatory value;
- posterior molecular probability;
- compute allocation.

## Evidence hierarchy

The paper should never collapse every result into “annotation accuracy”.

Every dark-spectrum result is assigned the strongest evidence level it actually reaches:

1. precursor mass / formula compatible;
2. structurally valid candidate;
3. reachable in the learned World;
4. observed peaks supported by executable trajectories;
5. candidate-specific discriminative evidence;
6. spectrum → molecule → World → spectrum consistency;
7. calibrated bounded structural statement;
8. authentic-standard confirmation.

Main figures must report how much dark chemistry reaches each level.

## Main-text architecture

The manuscript is organized as **2 method-capability figures + 3 discovery figures**.

| § | Section | Figure | Role |
|---|---|---|---|
| 1 | A molecular fragmentation world unifies prediction, explanation and inverse inference | Fig. 1 | paradigm |
| 2 | World-based inference establishes graded structural evidence | Fig. 2 | capability / credibility |
| 3 | High-evidence inference resolves the dark metabolome at scale | Fig. 3 | large-scale discovery |
| 4 | Resolved dark chemistry reveals structural and biological organization | Fig. 4 | chemical/source discovery |
| 5 | Dark molecular families reveal biology hidden from feature-level metabolomics | Fig. 5 | biological discovery |

The chain is:

`partial spectral observation → fragmentation World → W/G/V inference → graded structural evidence → high-evidence dark structures → chemical families → biological organization`.

## Figure-level questions

1. **What is the hidden object behind a spectrum?**  
   A latent probabilistic fragmentation world.

2. **What new inference capabilities does one shared World provide?**  
   Forward prediction, spectrum-guided explanation, inverse structure inference and bidirectional verification.

3. **How much dark chemistry can be resolved, and at what evidence level?**  
   Repository-scale evidence hierarchy and entity/family census.

4. **How is resolved dark chemistry organized?**  
   Near-known versus remote structural families plus microbiota/diet/host dependence.

5. **Does structure change biological inference?**  
   Frozen structural families versus anonymous feature-level analysis, followed by one deeply validated programme.

## Agent role

The LLM/MS-agent remains outside online WGV inference.

[
	ext{systematic failure}
ightarrow
	ext{hypothesis}
ightarrow
	ext{program/state/action/algorithm revision}
ightarrow
	ext{typed compiler + held-out gates}
ightarrow
	ext{new World}
]

The agent evolves the scientific program; it does not replace the reproducible chemical state, policy or transition model.

## Nature-level success criteria

The paper should demonstrate all three layers:

### Paradigm
A shared learned fragmentation World supports Free, Guided and Inverse inference better than disconnected/direct alternatives.

### Evidence
World-based bidirectional inference produces more reliable, auditable and calibrated structural conclusions than similarity/rank alone.

### Discovery
Applying this evidence hierarchy at scale reveals reproducible dark structural families and biological organization not visible at feature level.

If the paper only shows a better W/G/V benchmark, it becomes a methods paper. If it only shows an atlas, it underuses the methodological novelty. The Nature story requires both.

## Draft conventions

`main.tex` is target-final prose. Missing evidence remains explicit:

- `[RESULT: ...]` — numerical/statistical result from a frozen artifact;
- `[DATA: ...]` — cohort or dataset information still to be bound;
- `[METHOD: ...]` — protocol detail that must be frozen.

No placeholder is filled from memory, transient logs or exploratory notebooks.

## Standing claim boundaries

1. A spectrum is a partial observation of the fragmentation world, not a complete negative label over all unobserved states.
2. W/G/V share one chemical world but optimize different conditional objectives.
3. Chemical legality is hard-constrained; RL learns preference and compute allocation.
4. Candidate recall, evidence discrimination and end-to-end recovery are separate endpoints.
5. Dark-spectrum predictions are not automatically identifications.
6. Structural relationships are not biosynthetic mechanisms.
7. Source attribution establishes dependence, not synthesis.
8. Training loss and agent progress are not scientific endpoints.
