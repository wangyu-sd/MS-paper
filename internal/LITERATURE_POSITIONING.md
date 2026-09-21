# Literature Positioning

This document defines the manuscript's scientific lane and the claims that must not drift during writing.

## The field-level gap

Untargeted metabolomics has repeatedly established that most detected tandem spectra remain unidentified. What the field still cannot state is:

- how many distinct chemical entities those dark features represent;
- how many are recurrent across independent datasets;
- whether they are mostly near-neighbours of characterized metabolism or occupy recurrent remote structural families;
- whether those structural families partition by biological source;
- whether resolving anonymous features into structural families improves biological inference.

This is the paper's scientific gap.

The manuscript therefore does **not** lead with “we built a better structure-elucidation model”. It leads with:

> **The dark metabolome is a measurable, recurrent and biologically organized chemical layer rather than an unstructured residue of unidentified spectral features.**

ORBIT-MS is the enabling measurement system.

---

## Nature precedents: what made them broad-interest papers

### Reverse metabolomics
The important contribution was not merely the number of newly observed compounds. The work established a general discovery strategy that connected designed chemistry, public metabolomics and human biology.

**Lesson:** a scalable discovery operation becomes Nature-scale when it changes what biological questions can be asked.

### DeepMet
The central claim was not benchmark rank. It was that metabolite chemical space contains learnable regularities that can anticipate future metabolites, with newly observed molecules serving as evidence for that principle.

**Lesson:** the headline should be a statement about chemical space, not about model architecture.

### Implication for this manuscript
The corresponding field-level statement is not “mechanistic elimination works”. It is:

> **Once dark spectra are converted into bounded structural entities, their global scale, chemical organization and biological partition become measurable.**

Figures 2–5 must carry that statement.

---

## Why “a structural census” is distinct from annotation-rate papers

Repository-scale annotation and molecular networking are established capabilities. GNPS/MASST/ReDU, suspect-library propagation, COSMIC, SIRIUS/CSI:FingerID, MetDNA-like reaction propagation and modern learned models all expand the fraction of spectra connected to known chemistry.

That literature does not make a validated claim that:

`N spectral features = N distinct molecules`.

It also generally cannot state how uncertainty in structural annotation propagates into a molecule-level census.

The manuscript's census contribution therefore requires three things simultaneously:

1. bounded structural outputs rather than forced unique identities;
2. validated feature/adduct/isotope/in-source collapsing;
3. uncertainty on the entity count.

If those are not credible, “census” is not a defensible word.

---

## De novo generation is not the competitive axis

Modern de novo MS structure generation is advancing rapidly, but reported accuracies are highly split- and leakage-dependent. The manuscript should not enter a headline Top-1 race.

METEOR / inverse generation is a candidate-supply component. The scientific endpoints remain:

- candidate recall;
- conditional structural discrimination;
- bounded structural resolution;
- downstream census/organization/biology.

A stronger generator improves coverage but does not change the paper's central proposition.

---

## Mechanistic fragmentation: the dangerous claim boundary

The literature does not support a general claim that mechanistic fragmentation is more accurate than black-box learned spectral models in distribution.

Therefore do not write:
- “physics is more accurate”;
- “mechanistic simulation outperforms neural spectrum prediction in general”;
- “absence of a simulated fragment proves impossibility”.

The defensible role of the fragmentation World is narrower and more useful:

- it provides explicit atom/electron/charge/H-conserving trajectories;
- candidate-specific evidence is auditable;
- eliminations can be assigned an empirical false-exclusion rate;
- uncertainty can be propagated into a bounded structural statement.

The paper wins only if this credibility is sufficient to support Figures 2–5.

---

## Analogue propagation and the “near-known halo”

Similarity to characterized metabolites is one of the most productive discovery priors in metabolomics. Suspect libraries, molecular networking, reaction-network propagation, reverse metabolomics and learned metabolite priors all exploit this fact.

Do not frame this as a weakness.

Instead, Figure 3 asks an empirical question:

> **What fraction of recurrent dark chemistry lies inside the neighbourhood that existing analogue-based strategies are designed to reach, and what fraction forms recurrent structural families outside it?**

The “near-known halo” and “remote recurrent families” are measurements, not rhetorical categories. Their definitions must be frozen before the fraction is calculated.

---

## DreaMS / representation learning

Large-scale self-supervised spectral representations demonstrate that unannotated spectra have learnable organization and make repository-scale analysis tractable.

Our distinction is not that spectral organization did not exist. It is:

> spectral similarity organizes observations; structural resolution attempts to identify the chemical entities and relations underlying those observations.

Figure 2 must therefore avoid claiming that recurrence or clustering itself is novel. Figure 3's contribution is the structural interpretation of recurrent dark chemistry.

---

## Biological-source literature

Microbiome, diet and host metabolism already produce strong perturbation signatures in metabolomics. The paper does not claim to invent source attribution.

The new question is whether **previously anonymous recurrent structural families** partition under these perturbations in a chemically coherent way.

Required language:
- microbiota-dependent;
- diet-dependent;
- host-associated;
- mixed/unresolved.

Avoid:
- microbially synthesized;
- host biosynthetic product;
- pathway intermediate;

unless direct biosynthetic experiments support those terms.

---

## Biological association: case study is not enough

Many metabolomics papers can associate an unidentified feature with a phenotype. A single significant dark family is therefore not a Nature-level endpoint.

Figure 5 must first test a general principle:

> **Does replacing anonymous features with frozen structural-family objects systematically improve cross-cohort reproducibility or association coherence?**

Only after that global paired test is frozen should one principal family be used as a mechanistic/chemical case study.

This is the key upgrade from the previous manuscript design.

---

## Prospective library growth

Historical library growth remains the strongest credibility experiment because it approximates a prospective test without new acquisition:

- freeze the system and available chemistry at time T0;
- identify spectra that are dark under T0;
- evaluate against structures deposited later by independent groups.

This is not the scientific headline. It is the reason readers may trust the subsequent atlas.

If the prospective cohort is small or heavily biased, report that limitation and reduce its visual weight rather than overclaiming prospectivity.

---

## What is genuinely new if the experiments succeed

1. **A validated feature-to-entity structural census of the dark metabolome.**
2. **A quantitative decomposition of recurrent dark chemistry into near-known and remote structural regimes.**
3. **Identification of recurrent structural families poorly represented by current libraries.**
4. **A global link between dark chemical structure and perturbation-defined biological source.**
5. **Evidence that structural-family analysis changes biological inference relative to anonymous-feature analysis.**
6. **A bounded, prospectively calibrated structural reporting scheme that makes the above analyses defensible.**

The order matters. Items 1–5 are discoveries about the chemical world; item 6 is enabling methodology.

---

## What is not new

Do not claim novelty for:
- public repository mining;
- molecular networking;
- library search;
- fragmentation modelling itself;
- de novo structure generation itself;
- self-supervised spectral embeddings;
- confidence sets as a statistical concept;
- the observation that MS/MS cannot distinguish all isomers;
- host/microbiome/diet perturbation metabolomics;
- association testing of unknown features.

Novelty must come from the combination that creates a new measurable object: the recurrent structurally bounded dark metabolome.

---

## Editorial test

Before submission, the first five figure titles should answer five questions an editor can understand without knowing ORBIT-MS:

1. Can these structural statements be trusted?
2. How large is the dark metabolome?
3. How is dark chemistry organized?
4. Where is that chemistry biologically dependent?
5. Does structural resolution reveal biology that feature-level analysis misses?

If a figure title instead contains an implementation term, the hierarchy has probably drifted back toward a methods paper.

---

## Citation policy

- Peer-reviewed literature carries essential claims.
- Current/preprint work may define frontier context but cannot carry a load-bearing historical claim.
- Comparator values used in main figures are recomputed on the manuscript's own frozen cohorts whenever possible.
- Do not quote incompatible benchmark numbers side by side as if they were comparable.
- Literature that contradicts a convenient framing is cited explicitly rather than omitted.
