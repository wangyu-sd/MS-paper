"""Build the editable ORBIT-MS method figure from the case manifest and RDKit."""
from html import escape
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from rdkit import Chem, rdBase
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

HERE = Path(__file__).resolve().parent
STEM = "orbit_ms_nmi_method_overview"
ASSEMBLY = json.loads((HERE / "case_manifest.json").read_text())
A = ASSEMBLY["query"]
B = ASSEMBLY["mma_alignment"]
C = ASSEMBLY["candidates"]
S = ASSEMBLY["source_depicted_g_states"]["states"]
INK = "#30373C"
SLATE = "#435F75"
GRAY = "#5F6E79"
RULE = "#D9E1E5"
TEAL = "#4E8C89"
DEEP_TEAL = "#356D68"
PALE = "#E8F2EF"
OCHRE = "#BD8A58"
PURPLE = "#796A82"
LIGHT_PURPLE = "#F1EDF3"
SVG = []


def add(markup):
    SVG.append(markup)


def label(x, y, value, size=17, *, color=INK, weight=400, anchor="start", italic=False):
    add(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
        f'fill="{color}" text-anchor="{anchor}" font-style="{"italic" if italic else "normal"}">'
        f'{escape(value)}</text>')


def lines(x, y, values, size=16, *, line_height=20, **style):
    for i, value in enumerate(values):
        label(x, y+i*line_height, value, size, **style)


def path(d, *, color=SLATE, width=1.65, dash=None, head=None):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker = f' marker-end="url(#{head})"' if head else ""
    add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dash_attr}{marker}/>')


def rule(x1, y1, x2, y2):
    path(f"M{x1} {y1}H{x2}" if y1 == y2 else f"M{x1} {y1}V{y2}", color=RULE, width=1)


def arrow(d, color="inference", *, dash=None, width=1.8):
    path(d, color={"inference": SLATE, "learning": TEAL, "decision": PURPLE,
                   "memory": "#827589"}[color], width=width, dash=dash, head=color)


def box(x, y, w, h, fill, *, stroke="none", radius=0, dash=None):
    style = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}"{style}/>')


def dot(x, y, radius, *, fill=TEAL):
    add(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}"/>')


def panel(letter, x, y, title):
    add(f'<g id="panel-{letter}" role="group" aria-label="{escape(title)}">')
    label(x, y, letter, 27, color=SLATE, weight=700)
    label(x+28, y, title, 23, weight=700)


def end():
    add("</g>")


def slot(x, y, w, h, value):
    box(x, y, w, h, "#FFFFFF", stroke="#BFC9CF", dash="4 3")
    label(x+w/2, y+h/2+5, value, 14, color=GRAY, anchor="middle", italic=True)


def draw_mol(name, smiles, x, y, w, h, *, highlight=(), colour=(.77, .88, .84),
             bond_length=14):
    """Save the component SVG and insert editable RDKit paths in figure space."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(smiles)
    Chem.RemoveStereochemistry(mol)
    rdDepictor.Compute2DCoords(mol)
    scale = 4
    drawer = rdMolDraw2D.MolDraw2DSVG(w*scale, h*scale)
    opt = drawer.drawOptions()
    opt.clearBackground = False
    opt.padding = .065
    opt.fixedBondLength = bond_length*scale
    opt.minFontSize = 34
    opt.maxFontSize = 58
    opt.bondLineWidth = 4.8
    opt.highlightBondWidthMultiplier = 4
    opt.updateAtomPalette({6: (.19, .22, .24), 7: (.16, .32, .46), 8: (.63, .32, .23)})
    highlights = list(highlight)
    bonds = [b.GetIdx() for b in mol.GetBonds()
             if b.GetBeginAtomIdx() in highlights and b.GetEndAtomIdx() in highlights]
    rdMolDraw2D.PrepareAndDrawMolecule(
        drawer, mol, highlightAtoms=highlights, highlightBonds=bonds,
        highlightAtomColors={i: colour for i in highlights},
        highlightBondColors={i: colour for i in bonds},
        highlightAtomRadii={i: .20 for i in highlights},
    )
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    (HERE / "assets" / f"{name}.svg").write_text(svg)
    body = re.search(r"<svg\b[^>]*>(.*)</svg>", svg, re.S).group(1)
    add(f'<g transform="translate({x} {y}) scale(0.25)" aria-label="{name}">{body}</g>')
    return [(x+drawer.GetDrawCoords(i).x/scale, y+drawer.GetDrawCoords(i).y/scale)
            for i in range(mol.GetNumAtoms())]


def side_chain(smiles, branched):
    mol = Chem.MolFromSmiles(smiles)
    pattern = Chem.MolFromSmarts(
        "[CH3][CH]([CH3])[CH;R][#7]" if branched else "[CH3][CH2][CH2][CH;R][#7]"
    )
    match = mol.GetSubstructMatch(pattern)
    if not match:
        raise ValueError("No side-chain match")
    return match[:4]


def spectrum(x, y, w, h):
    selected = (72.0816, 90.9773, 120.0808)
    fx = lambda mz: x+w*(mz-66)/(125-66)
    path(f"M{x} {y-h}V{y}H{x+w}", color=GRAY, width=1)
    label(x-8, y-h+4, "1", 13, color=GRAY, anchor="end")
    label(x-8, y+4, "0", 13, color=GRAY, anchor="end")
    for mz, intensity in A["peaks"]:
        px = fx(mz)
        path(f"M{px:.3f} {y}V{y-intensity*h:.3f}",
             color=OCHRE if mz in selected else SLATE, width=2.0 if mz in selected else 1)
    for mz in (70, 80, 90, 100, 110, 120):
        px = fx(mz)
        path(f"M{px:.3f} {y}v4", color=GRAY, width=1)
        label(round(px), y+17, str(mz), 13, color=GRAY, anchor="middle")
    label(x+w+8, y+17, "m/z", 14, color=GRAY, italic=True)
    for mz, intensity in A["peaks"]:
        if mz in selected:
            label(round(fx(mz))-4, round(y-intensity*h-5), f"{mz:.4f}", 14,
                  color="#865726", anchor="end" if mz == 120.0808 else "middle")
    label(x+5, y-h+4, "Relative intensity", 13, color=GRAY)


def panel_a():
    panel("a", 43, 39, "Molecular structure elucidation from MS/MS")
    start = len(SVG)
    add('<g id="measured-spectrum">')
    spectrum(63, 117, 392, 56)
    end()
    body = "\n".join(SVG[start:])
    (HERE / "assets" / "measured_spectrum.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="42 46 453 94" '
        'font-family="Arial, Helvetica, sans-serif">\n' + body + "\n</svg>\n"
    )
    label(504, 65, "MassSpecGym 0002114", 17, weight=700)
    label(504, 87, "Measured MS/MS · benchmark", 15, color=GRAY)
    label(504, 110, "493.2804 m/z  [M+H]⁺", 17, color=SLATE)
    rule(753, 55, 753, 132)
    label(735, 132, "Same formula", 14, color=GRAY, anchor="end")
    ochre = (.92, .83, .72)
    for i, (x, key, title) in enumerate([(773, "M1", "M1 · G candidate"),
                                          (1077, "M2", "M2 · refinement")]):
        info = C[key]
        draw_mol(key, info["smiles"], x, 48, 130, 92,
                 highlight=side_chain(info["smiles"], i == 1), colour=ochre)
        label(x+134, 82, title, 16, weight=700)
        label(x+134, 104, ("n-Propyl side chain", "Isopropyl side chain")[i], 15, color=GRAY)
        label(x+134, 124, "C₂₈H₃₆N₄O₄", 15, color=GRAY)
    end()


def panel_b():
    panel("b", 43, 182, "Mass-matched substructure alignment (MMA)")
    label(71, 204, "Observed ions → reusable fragment graphs", 16, color=DEEP_TEAL)
    rule(43, 214, 633, 214)
    label(45, 239, "Fragment resource", 17, weight=700)
    label(45, 262, "TRAIN structures + frozen W", 15, color=GRAY)
    arrow("M257 251H275")
    slot(282, 232, 130, 31, "Mined motif record")
    arrow("M415 251H431")
    lines(439, 239, ["Adduct, ion formula, motif", "Support by source group"], 15,
          color=SLATE, line_height=21)
    label(45, 279, "Own-group support excluded during TRAIN retrieval", 14, color=GRAY)
    rule(43, 289, 633, 289)

    label(45, 314, "Peak p₃", 17, weight=700)
    label(45, 337, "120.0808", 17, color="#865726")
    arrow("M132 327H158")
    label(171, 313, "Compatible ion", 16, weight=700)
    label(171, 337, "C₈H₁₀N⁺", 20, color=SLATE)
    arrow("M285 327H311")
    label(323, 310, "Top-K fragment graphs", 16, weight=700)
    draw_mol("phenethylamine_motif", B["motif"]["smiles"], 324, 315, 124, 37, bond_length=13)
    label(455, 332, "Source-depicted motif", 15, color=DEEP_TEAL)
    label(455, 350, "Other motifs / priors pending", 13, color=GRAY, italic=True)
    label(45, 358, "Mass tolerance · precursor inventory · support prior", 14, color=GRAY)
    rule(43, 369, 633, 369)

    label(45, 395, "Motif-to-partial-graph correspondence", 17, weight=700)
    label(630, 395, "Code replay", 14, color=GRAY, anchor="end", italic=True)
    pairs = B["alignment"]
    match = [i for i, _, _ in pairs]
    mcoords = draw_mol("alignment_motif", B["motif"]["smiles"], 47, 412, 135, 80,
                       highlight=range(len(B["motif_graph"]["z"])), bond_length=20)
    coords = draw_mol("alignment_partial", S[1]["smiles"], 231, 408, 172, 85,
                      highlight=match, bond_length=16)
    # Use paired reference indices rather than imply a trained attention weight.
    anchors = [next((i, j) for i, _, j in pairs if j == k) for k in (0, 1)]
    for index, (i, j) in enumerate(anchors, 1):
        for (x, y), dy in ((mcoords[j], -8), (coords[i], -8)):
            dot(round(x)+5, round(y)+dy, 7.5)
            label(round(x)+5, round(y)+dy+4, str(index), 10, color="#FFFFFF", anchor="middle", weight=700)
    path("M183 447H226", color=TEAL, dash="3 4", width=1.8)
    label(204, 439, "1, 2", 13, color=DEEP_TEAL, anchor="middle")
    label(109, 508, "Encoded motif", 14, color=GRAY, anchor="middle")
    label(313, 508, "Incomplete graph", 14, color=GRAY, anchor="middle")
    rule(418, 405, 418, 510)
    lines(430, 420, ["Peak ↔ motif attention", "→ spectrum memory"], 15,
          line_height=20, color=SLATE)
    lines(430, 469, ["Motif atoms ↔ state atoms", "→ G atom / graph memory"], 15,
          line_height=20, color=DEEP_TEAL)
    rule(43, 520, 633, 520)
    label(45, 545, "G", 17, color=DEEP_TEAL, weight=700)
    label(70, 545, "Atom / ring / motif actions and multi-motif starts", 16)
    label(45, 568, "V", 17, color=SLATE, weight=700)
    label(70, 568, "Optional learned motif evidence alongside W", 16, color=SLATE)
    end()


def panel_c():
    panel("c", 658, 182, "Generate, simulate and discriminate molecular hypotheses")
    label(659, 214, "G  Canonical Hybrid construction", 17, weight=700)
    label(1388, 214, "Formula / valence / bond constraints", 15, color=GRAY, anchor="end")
    frame_x = [667, 820, 996, 1192]
    widths = [104, 126, 142, 160]
    texts = ["Motif start", "Motif attachment", "Amide extension", "M2 · reference connectivity"]
    for i, state in enumerate(S):
        x, w = frame_x[i], widths[i]
        draw_mol(f"G_state_{i+1}", state["smiles"], x, 220, w, 82, bond_length=14)
        label(x+w/2, 319, texts[i], 15, color=SLATE, anchor="middle")
        if i < len(S)-1:
            arrow(f"M{x+w+5} 259H{frame_x[i+1]-6}")
    label(659, 340, "Source-depicted construction states", 14, color=GRAY, italic=True)
    rule(658, 352, 1388, 352)

    label(659, 378, "Candidate connectivities", 17, weight=700)
    label(896, 378, "W  Predict fragments", 17, weight=700)
    label(1152, 378, "V  Compare measured peaks", 17, weight=700)
    label(896, 399, "Target-spectrum blind", 14, color=GRAY)
    xs = [1212, 1272, 1332]
    measured = ["72.0816", "90.9773", "120.0808"]
    for x, mz in zip(xs, measured, strict=True):
        label(x, 409, mz, 13, color="#865726", anchor="middle")
        path(f"M{x} 414V512", color=RULE, dash="3 3", width=1.2)
    for y, key in [(421, "M1"), (480, "M2")]:
        label(661, y+25, key, 17, color=SLATE, weight=700)
        draw_mol(f"{key}_comparison", C[key]["smiles"], 699, y-9, 111, 57, bond_length=10)
        arrow(f"M812 {y+19}H878")
        slot(889, y+3, 187, 30, "Fragment receipt pending")
        arrow(f"M1085 {y+19}H1140")
        label(1154, y+24, key, 15, color=SLATE)
        path(f"M1182 {y+19}H1358", color=RULE, width=1.2)
    label(1182, 526, "Peak-match receipts pending", 14, color=GRAY, italic=True)
    arrow("M1274 532V544")
    label(1274, 566, "Ranked or bounded hypotheses", 16, color=SLATE, weight=700, anchor="middle")
    label(661, 551, "Reach", 16, color=SLATE, weight=700)
    label(719, 551, "Does the pool contain the structure?", 15, color=GRAY)
    label(661, 571, "Rank", 16, color=SLATE, weight=700)
    label(719, 571, "Where does it rank within that pool?", 15, color=GRAY)
    end()


def panel_d():
    panel("d", 43, 617, "Information-guided semi-supervised learning")
    for i, (name, source_name, model, output) in enumerate([
        ("Sleep", "Unpaired molecules", "Frozen W", "Structure–simulated spectrum"),
        ("Wake", "Unlabeled real spectra", "G + W/V", "Evidence-gated pseudo-labels"),
        ("Hindsight", "G-proposed graphs", "Frozen W", "Counterfactual pairs / hard negatives"),
    ]):
        y = 649+i*35
        label(45, y, name, 17, weight=700, color=DEEP_TEAL)
        label(139, y, source_name, 16)
        arrow(f"M309 {y-5}H343", "learning")
        label(352, y, model, 16, weight=700, color=SLATE)
        arrow(f"M434 {y-5}H461", "learning")
        label(470, y, output, 15)
        path(f"M739 {y-5}H757", color=TEAL, width=1.55)
    path("M757 644V714", color=TEAL, width=1.55)
    arrow("M757 679H775", "learning")
    box(778, 634, 66, 87, PALE)
    lines(811, 662, ["Select", "learning", "pairs"], 15, anchor="middle", color=DEEP_TEAL, line_height=18, weight=700)
    box(44, 742, 800, 27, "#F3F7F6")
    label(444, 761, "Spectral entropy · structural scarcity · scaffold diversity · evidence quality", 16,
          color=DEEP_TEAL, anchor="middle")
    label(45, 788, "Entropy threshold, scaffold cap and evidence gates", 14, color=GRAY)
    end()


def panel_e():
    panel("e", 868, 617, "Scientific Improver")
    label(1387, 617, "Controlled protocol · W fixed", 14, color=GRAY, anchor="end")
    label(873, 643, "TRAIN FIT", 16, weight=700, color=PURPLE)
    arrow("M956 638H976", "decision")
    label(985, 643, "Diagnose missing knowledge, candidate or rank", 15)
    label(873, 665, "Hypothesis", 16, weight=700, color=PURPLE)
    arrow("M960 660H985", "decision")
    label(995, 665, "Select one action", 16, weight=700, color=PURPLE)
    label(1387, 667, "Paired CAL evaluation", 16, anchor="end", weight=700)
    width = 198
    for i, (action, selected) in enumerate([
        ("EXPAND_KNOWLEDGE", False), ("IMPROVE_GENERATOR", True),
        ("IMPROVE_VERIFIER", False), ("COLLECT_EVIDENCE", False),
    ]):
        y = 689+20*i
        if selected:
            box(866, y-14, width, 19, LIGHT_PURPLE)
        label(874, y, action, 14, weight=700 if selected else 400, color=PURPLE)
    label(1069, 750, "→ d", 14, color=DEEP_TEAL)
    label(1068, 705, "Execute", 14, color=PURPLE)
    arrow("M1068 714H1141", "decision")
    lines(1152, 693, ["Newly reached structures", "Re-ranked true structures",
                       "Regressions · resource cost"], 15, line_height=20)
    arrow("M1258 743V778H860V660H868", "memory", dash="5 4", width=1.45)
    box(979, 767, 214, 23, "#FFFFFF")
    label(1086, 783, "Episode reflection / memory", 14, color=PURPLE, anchor="middle")
    end()


def connectors():
    # Keep measured data in the central gutter and away from W and the structures.
    path("M241 138V148", color=SLATE, width=1.65)
    dot(241, 148, 2.6, fill=SLATE)
    arrow("M241 148H86V161")
    arrow("M241 148H1406V397H1370")
    box(1200, 137, 170, 20, "#FFFFFF")
    label(1367, 151, "Measured peaks → V", 14, color=SLATE, anchor="end")
    arrow("M606 539H641V238H660", width=1.45)
    # Keep optional evidence local to V with a keyed input at its comparison.
    label(1152, 398, "+ MMA when enabled", 13, color=SLATE, italic=True)
    arrow("M846 678H851V586H530V573", "learning", width=1.75)
    box(559, 578, 261, 18, "#FFFFFF")
    label(689, 591, "Selected experience → MMA / G / V", 14,
          color=DEEP_TEAL, anchor="middle")
    arrow("M1343 741H1397V586H1262", "learning", width=1.75)
    box(998, 578, 260, 18, "#FFFFFF")
    label(1255, 591, "Promoted update → MMA / G / V", 14, color=DEEP_TEAL, anchor="end")


def main():
    if rdBase.rdkitVersion != ASSEMBLY["rendering"]["rdkit"]:
        raise ValueError("Use the RDKit version recorded in case_manifest.json")
    (HERE / "assets").mkdir(exist_ok=True)
    add('<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="101.25mm" '
        'viewBox="0 0 1440 810" font-family="Arial, Helvetica, sans-serif" role="img">')
    add("<title>ORBIT-MS MMA-centric method framework</title>")
    add("<desc>Measured MassSpecGym spectrum, source-depicted chemical structures, replayed "
        "MMA atom correspondence, learning pathways and schematic Scientific Improver.</desc>")
    add("<defs>")
    for name, color in [("inference", SLATE), ("learning", TEAL),
                        ("decision", PURPLE), ("memory", "#827589")]:
        add(f'<marker id="{name}" viewBox="0 0 8 8" refX="7.4" refY="4" markerWidth="6" '
            f'markerHeight="6" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="{color}"/></marker>')
    add("</defs>")
    box(0, 0, 1440, 810, "#FFFFFF")
    for segment in [(43, 157, 1388, 157), (646, 167, 646, 573), (43, 580, 1388, 580),
                    (855, 603, 855, 788)]:
        rule(*segment)
    panel_a()
    panel_b()
    panel_c()
    panel_d()
    panel_e()
    connectors()
    add("</svg>")
    master = HERE / f"{STEM}.svg"
    master.write_text("\n".join(SVG) + "\n")
    xml = ET.parse(master)
    assert not xml.findall(".//{http://www.w3.org/2000/svg}image")


if __name__ == "__main__":
    main()
