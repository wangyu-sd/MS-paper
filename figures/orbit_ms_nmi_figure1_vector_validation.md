# ORBIT-MS Figure 1 native vector validation

The previous `orbit_ms_nmi_figure1.pdf` consisted of one 1670 × 942 image, with no PDF font objects. Its `pdfinfo`, `pdfimages -list` and `pdffonts` outputs are preserved under [verification](orbit_ms_nmi_figure1_sources/verification).

The new editable [SVG](orbit_ms_nmi_figure1_vector.svg) and [PDF](orbit_ms_nmi_figure1_vector.pdf) are assembled from semantic vector objects. The reconstruction uses the selected second PNG as its layout reference.

## Native vector checks

- One page, 180 × 101.53294 mm, matching the selected 1670:942 aspect ratio.
- Zero embedded image objects in the PDF and zero `image`/`foreignObject` elements in the SVG.
- 2,363 PDF drawing objects, with searchable text. Arial/Arial Bold and Times New Roman/Times New Roman Italic are embedded. Scientific subscripts and superscripts use real text spans.
- The SVG contains separate molecule assets, 91 individually named motif nodes, individually named containment edges, native spectrum sticks, independent model boxes/connectors and the path-based scientific-agent icon.
- Chemical bonds and atom labels come from RDKit SVGs. No pixel tracing, OCR, full-figure bitmap, or image-generation output is embedded in the master.
- Text-bound checks found no off-canvas labels or overlapping native labels. Chemical glyphs remain scalable vector outlines.
- The PDF was also opened with PyMuPDF for `get_images()`, `get_drawings()`, `get_text()` and font inspection. Full machine-readable results are in [statistics.json](orbit_ms_nmi_figure1_sources/verification/statistics.json).

## Visual comparison

[Same-size render](orbit_ms_nmi_figure1_sources/verification/render-reference-size.png), [overlay](orbit_ms_nmi_figure1_sources/verification/overlay.png), [difference](orbit_ms_nmi_figure1_sources/verification/difference-x3.png), and [180 mm review](orbit_ms_nmi_figure1_sources/verification/review-180mm-100dpi.png) are included. Side-by-side crops for all eight panels retain the selected reference's original pixel coordinates.

Panel boundaries, title rows and scientific object regions follow the reference. Native typesetting and molecular layout differ locally. Scientific replacements correct the malformed generated A/B candidates, the missing aniline nitrogen label and malformed action structures. The containment overview uses recorded nodes/edges rather than copying or tracing the raster network.

Pixel equality is not a target of this native reconstruction. At 1670 × 942, the mean absolute channel error is approximately 27.4/255; the raw changed-pixel fraction is approximately 91.2%, including background and anti-aliasing differences. These values do not establish layout equality. The panel comparisons document the actual visual differences.

The 180 mm review preserves the source figure's dense layout. Most body labels are around 4 pt at that size, and subordinate labels are smaller. The molecular and network glyphs remain clean vector artwork at high zoom. A final author decision on print-width typography is still required; native vectors do not make the source's dense labels larger.

## Source completeness and remaining limits

All depicted candidate identities, source parent, local motifs, measured spectral values, displayed W fragments and replay states are traceable. Both candidates have formula C28H36N4O4 with different connectivity. The six local containment nodes exactly match the highlighted overview identities, and every rendered containment edge passes RDKit matching.

The original full production graph topology, original G beam parent chain and complete sample-specific acquisition weights were unavailable. The overview is a deterministic source-based display sample, the action is labeled reference-conditioned replay, and acquisition bars are explicitly illustrative. These objects are reconstructable; they do not establish missing runtime measurements.

No key scientific object has been substituted with an invented molecule or measured spectrum. Generic modality tokens and acquisition schematics are diagrammatic explanations. [Source inventory and rebuild instructions](orbit_ms_nmi_figure1_sources/README.md) record the implementation boundaries, source hashes and scripts. The selected PNG is preserved as a reference asset. Manuscript files are outside this change.
