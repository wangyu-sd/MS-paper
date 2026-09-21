# Literature Positioning

This manuscript should not be positioned as another spectrum-to-structure predictor or another metabolomics atlas.

Its methodological proposition is:

> **A tandem mass spectrum is a partial observation of a latent gas-phase fragmentation world. Molecular structure inference should therefore proceed through a learned chemical world rather than by a direct spectrum-to-structure shortcut.**

Its scientific consequence is:

> **World-based inference yields graded structural evidence strong enough to resolve dark chemistry at scale and reveal its structural and biological organization.**

---

## 1. Direct prediction versus inference through a world

Most scalable MS methods learn one of several direct mappings:

- structure → spectrum;
- spectrum → fingerprint/class;
- spectrum → candidate rank;
- spectrum → molecular structure.

These mappings can be highly predictive, but they usually do not represent the latent reaction process as the common causal object shared by forward and inverse inference.

ORBIT-MS instead introduces:

[
M,c ightarrow mathcal W(M,c) ightarrow S_{m obs}
]

where (mathcal W) is a latent probabilistic reaction world and the observed spectrum is incomplete evidence about it.

The key novelty is not “we also simulate fragmentation”. It is that **prediction, explanation and inverse inference are queries to the same learned world**.

---

## 2. Why the partial-observation formulation matters

An experimental spectrum does not enumerate every chemically possible fragmentation state.

A generated state may be absent because of:
- low occupancy;
- competing branches;
- ionization microstate;
- collision condition;
- instrument response;
- censoring/detection threshold.

Therefore:
[
	ext{unobserved} 
eq 	ext{chemically false}.
]

This distinguishes the World formulation from objectives that treat every unobserved predicted peak as a conventional false positive.

The manuscript should be careful: this does not imply every unobserved World state is correct. It means negativity must be mediated by an observation model or empirical calibration rather than assumed from absence.

---

## 3. WGV is one world, not three independent models

The three modes are:

[
egin{aligned}
	ext{Free:}&quad p(mathcal T,Smid M,c),\
	ext{Guided:}&quad p(mathcal Tmid M,S_{m obs},c),\
	ext{Inverse:}&quad p(M,mathcal Tmid S_{m obs},c).
end{aligned}
]

This is the conceptual advantage over separately training:
- one spectrum simulator;
- one explanation model;
- one de novo generator;
- one unrelated reranker.

The scientific test is whether shared World semantics improve or stabilize these tasks under matched evaluation, not whether a diagram contains shared weights.

---

## 4. Why RL/GFlowNet is scientifically motivated

The fragmentation world is combinatorial and multi-modal.

The task is not always:
[
argmax_	au R(	au).
]

Free fragmentation requires multiple plausible paths and probability flow.
Inverse inference requires multiple plausible molecular structures.
Guided explanation requires long-horizon compute allocation toward evidence-bearing branches.

This motivates:
- GFlowNet/SubTB for many valid trajectories;
- Guided IQL/DAgger for spectrum-conditioned long-horizon value;
- SMC/GFlowNet for diverse inverse posterior hypotheses;
- search/planning for finite compute allocation.

Do not sell the paper as “RL improves the score”. Sell it as:

> **RL allocates finite computation over a large constrained chemical world.**

---

## 5. Chemistry is not the reward

A central credibility distinction is:

> **Chemistry defines legality; learning defines preference.**

Atom, electron, charge, H, mass, formula and valence constraints are executable constraints.

This differs from approaches where chemically impossible outputs are merely discouraged by a loss term.

The paper must not overclaim that hard constraints guarantee correct mechanisms. They guarantee bookkeeping/legal consistency, while event propensity and mechanistic likelihood remain learned/empirical.

---

## 6. Fragmentation models and mechanistic precedent

Mechanistic and semi-mechanistic fragmentation methods are well established. The manuscript must not claim to invent:
- fragmentation trees;
- reaction-rule fragmentation;
- electron-flow representations;
- mechanistic peak explanation.

The novel combination is:
1. a shared learned probabilistic World;
2. multi-branch latent network rather than one route;
3. partial-observation semantics;
4. bidirectional use for inverse structure inference;
5. RL-based adaptive compute allocation;
6. evidence hierarchy derived from forward/backward consistency.

Do not claim mechanism is universally more accurate than neural spectrum prediction.

---

## 7. De novo generation is not the whole problem

Modern de novo structure generators map spectra to molecular candidates, increasingly with formula or graph constraints.

ORBIT-MS should not compete only on Top-1.

Its distinctive question is:

> **Can a generated molecule survive replay through the same chemical world that defines forward fragmentation?**

Therefore the important comparison includes:
- Recall@K;
- structural diversity;
- chemical validity;
- forward World consistency;
- candidate-specific mechanistic evidence;
- calibrated bounded output.

The posterior set is more important than a single rank-1 guess for ambiguous spectra.

---

## 8. Evidence hierarchy as the bridge to dark metabolomics

The World paradigm matters scientifically only if stronger evidence levels correspond to stronger structural reliability.

The paper therefore builds:

[
	ext{formula}
ightarrow
	ext{World reachability}
ightarrow
	ext{executable support}
ightarrow
	ext{candidate-specific evidence}
ightarrow
	ext{bidirectional consistency}
ightarrow
	ext{calibrated structural statement}
ightarrow
	ext{standard confirmation}.
]

This is the bridge from AI methodology to repository-scale science.

The manuscript should report both:
- reliability conditional on evidence level;
- coverage/fraction of dark spectra reaching each level.

---

## 9. Relationship to DeepMet and reverse metabolomics

DeepMet demonstrates that known metabolite structure space contains learnable regularities that can anticipate unobserved metabolites.

Reverse metabolomics demonstrates that starting from molecular structures and searching public metabolomes can connect chemistry to human biology.

Our distinct proposition is:

> **learn the fragmentation world linking molecules to observations, invert that world to obtain high-evidence structures from dark spectra, then study the resulting chemical population.**

The dark-metabolome analysis must reveal a global property, not merely several additional molecules.

---

## 10. Relationship to DreaMS and large-scale spectral organization

Large-scale representation learning shows that hundreds of millions of spectra contain organization in spectral space.

Our question is complementary:

> **What molecular structures and reaction-consistent relationships underlie recurrent dark spectral organization?**

Do not claim that large-scale spectral clustering or recurrence is novel.

The manuscript contribution is moving from:
[
	ext{spectral organization}
]
to:
[
	ext{graded structural evidence and molecular organization}.
]

---

## 11. Why dark-metabolome analysis must follow evidence, not precede it

A dark-metabolome atlas built from weak rank-1 predictions is vulnerable to compounding false structure.

Therefore the paper first validates the evidence hierarchy, then freezes it, then runs the dark corpus.

This ordering is scientifically important:
- no phenotype labels influence structural inference;
- no dark-corpus success tunes evidence thresholds;
- no “interesting” family changes the World after the fact.

The atlas is a consequence of the inference paradigm, not a training dataset for it.

---

## 12. Nature-level proposition

The Nature-level story is strongest if all three statements hold:

### Paradigm
**Molecular fragmentation can be represented as a learnable probabilistic world that supports forward, conditional and inverse inference.**

### Evidence
**Inference through this world produces stronger, auditable and calibrated structural evidence than direct ranking alone.**

### Discovery
**At repository scale, this evidence reveals recurrent dark molecular families and biological organization hidden from feature-level metabolomics.**

Any one statement alone is smaller:
- paradigm only → methods paper;
- evidence only → annotation paper;
- discovery only → atlas/resource paper.

The combined chain is the manuscript.

---

## 13. Claims not to make

Do not claim:
- every World trajectory is a validated physical mechanism;
- every unobserved state is real;
- mechanistic models universally beat neural predictors;
- RL discovers chemistry without priors/constraints;
- WGV uniquely identifies every molecule;
- a structural family is a metabolic pathway;
- microbiota dependence proves microbial biosynthesis;
- a model-resolved unique structure equals authentic-standard identification.

---

## Editorial test

An editor should be able to extract the paper in one sentence:

> **The authors learn a probabilistic molecular fragmentation world, use it for forward, explanatory and inverse inference, and thereby obtain sufficiently strong structural evidence to reveal the organization of previously dark metabolomic chemistry.**

If the abstract instead reads like a list of ORBIT-MS modules or an atlas inventory, the hierarchy has drifted.
