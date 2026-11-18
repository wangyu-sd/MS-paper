# Integrated Figure 1 scientific object inventory

The selected reference PNG establishes the scientific content and visual density. The editable source and archived records determine molecular identities, graph edges and plotted peaks.

| Panel | Locked scientific assets | Source |
| --- | --- | --- |
| a | Experimental spectrum, both real A/B candidates and their shared formula | MassSpecGym 0002114 and archived candidates in `data/case_manifest.json` |
| b | Measured spectrum to G and V, candidate graphs to W, W evidence to V | ORBIT-MS WGV path |
| c | Marked source molecule, extracted phenethylamine, canonical motif index, measured peak and both retrieved motifs | Archived structure and motif match, MMA ion key, source-group counts |
| d | Graph overview, six-node chemical neighborhood, measured peak and two retrieved motif inputs, marked atom correspondence, hybrid policy and motif attachment | `data/motif-topology.json`, archived atom mapping and reference-conditioned replay in the case manifest |
| e | A/B candidates, shared and A-only W fragment skeletons, observed peaks and candidate evidence matrix | Candidate fragment objects with calculated masses, masks and scores in the case manifest |
| f–g | Real training pair, structure-only Sleep, spectrum-only Wake and generated Hindsight; entropy, composition, ring rarity and source-priority weighting | `data/paired_training_example.json` and archived experience records; schematic sampling weights |
| h | FIT failures, scientific hypothesis, bounded choice, baseline/trial CAL comparison, gate, episode memory | PR96 control protocol |

The W fragment structures depict archived neutral graph skeletons. Their annotated values are the predicted ion m/z, not the exact mass of an uncharged depiction. The shared 120.0808 and weak A-only 120.0889 cases are illustrative selected objects. The two candidates in e are the benchmark comparison, separate from the deterministic reference-conditioned attachment in d.
