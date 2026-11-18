# ORBIT-MS Figure 1 detail revision

The reference and the artwork at prior PR #18 commit `5594f4d` were reviewed alongside the [current vector revision](orbit_ms_nmi_figure1_reference_comparison.png). Panel boundaries and the 180 × 101.53 mm page match the previous vector version.

| Area | Changes |
| --- | --- |
| Flow | A shared vector arrow system uses a fixed-size spearhead and a smaller head for tight gaps. Rerouted selected bends and branches, including the MMA backbone, acquisition outputs and intervention selector. |
| Alignment | Aligned inference boxes and W/V arrows to their centerlines. Centered the acquisition headers over the weight cells, and kept the data, operation and output on each f row at the same height. Moved the chemical formula beneath the structures in e. |
| Spectra | Redrew the experimental benchmark as a centroid stick plot with a linear m/z axis, relative intensity in percent and reference ticks. Inset spectra use the same visual conventions at a compact scale. Each stick carries its original centroid and intensity metadata in the SVG. |
| Experience data | Replaced f's ring glyphs with archived RDKit structures. Added the measured MassSpecGym TRAIN pair 0000570, kept GeMS Wake as a pseudopair, and used the archived W peaks for Sleep and Hindsight. g sample IDs link the plotted examples to the illustrative acquisition rows. |

The PDF was visually checked at 180 mm and in enlarged panel crops. It has 2,667 vector drawing objects, embedded Arial and Times New Roman, and zero raster images. The verifier checks the displayed peak tables, their normalized stick heights, the canonical structures, all 102 motif containment edges, native text intersections and connector crossings.

At print scale, the compact experience structures are identifiable but fine atom labels still benefit from magnification. The mini spectra lack numeric ticks. Two benchmark sticks at 120.0808 and 120.0893 are too close to resolve visually across the full benchmark mass range; both centroids are retained in the SVG and listed separately in the evidence matrix. See the [source inventory](orbit_ms_nmi_figure1_sources/README.md) for the archived cases, calibration scope and qualitative acquisition weights.
