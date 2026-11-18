# ORBIT-MS Figure 1 chemical atlas redesign

The baseline is the vector figure at PR #18 commit `23fa6e8`. The [before/after preview](orbit_ms_nmi_figure1_atlas_before_after.png) shows both PDF renders at equal width.

| Area | Editorial change |
| --- | --- |
| a–b | The spectrum, molecular formula and A/B pointer explain ambiguity. Complete candidate structures appear once, in e. The inference band separates G/W/V flow from the measured-spectrum connection into V. |
| c–e | d occupies about 50% of the middle band. The archived graph, highlighted neighborhood and RDKit structures are the main visual sequence. The atom correspondence, alignment, backbone and constrained replay replace separate model cards. c and e use matching label hierarchy and short panel references for retrieved motifs and candidates. |
| f–g | Four actual records replace repeated input/output graphics. Row numbers connect the experiences to a quieter, illustrative sampling matrix. The brief output strip gives the three distinct learning routes. |
| h | Decision and controlled evaluation occupy separate rows. The pipeline distinguishes promotion and retention. A short dashed connector points episode memory to the next hypothesis. |

The canvas uses neutral separators, fixed arrowhead sizes, recurring alignment lines and the requested charcoal, slate, teal, copper and violet palette. Compared with the baseline, extracted English words fell from 334 to 210, and editable rectangles fell from 184 to 49. The counts describe layout density and include structural and technical labels.

At 180 mm page width, panel letters are approximately 12.5 pt, titles 9.3 pt and mechanism headings 8.1 pt. Main labels are generally 6.5–7.3 pt. Some compact metadata and numeric ticks are about 6.1–6.4 pt, and chemical subscripts and atom glyphs are smaller. The page was reviewed at 180 mm and at 2× raster scale, checking d's molecular bounds and atom mapping, e's evidence symbols, f/g's alignment and h's gate and memory connections. The final motif depictions have extra internal padding to clear terminal atoms and ring vertices. Automated checks found no label overlap, panel overflow or sampled connector/label crossings.

The editable SVG and PDF contain no raster images. The PDF has 1,541 vector drawing objects and embedded, searchable Arial and Times New Roman. The verifier checks the spectra against their recorded centroids and normalized intensities. It also checks the chemical source records, atom mapping and all 102 displayed containment edges.

## Material for the figure caption

- The benchmark trace and evidence matrix are for MassSpecGym 0002114. The precursor is [M+H]+ at m/z 493.2804. The close 120.0808/120.0893 observed sticks remain separate in the SVG and are listed independently in e.
- The overview is a 91-node archived sample. The containment network is independent of retrieval score; motif 2 is phenethylamine and motif 3 is N-ethylaniline. The group counts are for mined source shards. The ion lookup is also supported by paired TRAIN and W simulations.
- The atom correspondence illustrates an archived marked substructure. Motif Atom Memory is used when enabled. The before/after example is a reference-conditioned motif attachment replay. A/B in e are benchmark candidates.
- The four acquisition rows reuse the measured TRAIN record and archived Sleep, Wake and Hindsight examples. The bars illustrate weighting rather than reporting fitted weights. Evidence/scaffold filters precede sampling, and TRAIN anchors contribute to learning.
- The agent uses a TRAIN FIT diagnostic subset and a separate, matched CAL set. W is frozen. Only promotion advances the WGV generation. Episode memory informs the next hypothesis. Collecting evidence can update memory directly.

The [source inventory](orbit_ms_nmi_figure1_sources/README.md) records the underlying cases and rebuild commands.
