"""Reconstruct the approved 1670 x 942 Figure 1 using native SVG objects.

The reference controls placement. Chemistry and spectra come from the committed
source manifests and RDKit SVG assets. No raster artwork or tracing is used.
"""
from html import escape
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
SOURCE = FIG / "orbit_ms_nmi_figure1_sources"
ASSETS = SOURCE / "assets"
CASE = json.loads((SOURCE / "data/case_manifest.json").read_text())
PAIRED_TRAIN = json.loads((SOURCE / "data/paired_training_example.json").read_text())
KG = json.loads((SOURCE / "data/motif-topology.json").read_text())
MOLECULE_BOUNDS = json.loads((ASSETS / "molecule_bounds.json").read_text())
W, H = 1670, 942
INK, BLUE, TEAL, COPPER, VIOLET = "#101214", "#008BC0", "#00A77C", "#BD4B00", "#7934D7"
FAINT, SECONDARY, LIGHT = "#D7DEE0", "#677680", "#F2F5F4"
PARTS = []
DRAWING_SPECS = []
DISPLAY_POSITIONS = {}
FONT_DIR = Path('/System/Library/Fonts/Supplemental')


def add(markup):
    PARTS.append(markup)


def group(name):
    add(f'<g id="{name}"><title>{escape(name.replace("-", " "))}</title>')


def end():
    add("</g>")


def label(x, y, value, size=13, bold=False, color=INK, anchor="start", math=False, width=None, italic=False):
    family = "Times New Roman" if math else "Arial"
    if width and not math:
        font_name = "Arial Bold.ttf" if bold else "Arial.ttf"
        natural = ImageFont.truetype(str(FONT_DIR/font_name),round(size*10)).getlength(value)/10
        width = min(width,natural)
    fit = f' textLength="{width}" lengthAdjust="spacingAndGlyphs"' if width else ''
    style = ' font-style="italic"' if italic else ''
    add(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" '
        f'font-weight="{700 if bold else 400}" text-anchor="{anchor}"{fit}{style}>{escape(value)}</text>')


def formula(x, y, value, size=15, color=INK, anchor="start"):
    # Input uses ordinary chemistry notation. Digits become real subscript spans.
    tokens = re.findall(r"\d+|\+|[^\d+]+", value)
    spans = []
    for token in tokens:
        baseline = "sub" if token.isdigit() else "super" if token == "+" else "baseline"
        size_attr = ' font-size="72%"' if baseline != "baseline" else ""
        spans.append(f'<tspan baseline-shift="{baseline}"{size_attr}>{escape(token)}</tspan>')
    add(f'<text x="{x}" y="{y}" font-family="Times New Roman" font-size="{size}" '
        f'fill="{color}" font-weight="700" font-style="italic" text-anchor="{anchor}">{"".join(spans)}</text>')


def generation(x, y, next_=False, size=14, color=INK, anchor="middle"):
    sub = "t+1" if next_ else "t"
    add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" '
        f'font-size="{size}" font-family="Times New Roman" font-style="italic">'
        f'WGV<tspan baseline-shift="sub" font-size="72%">{sub}</tspan></text>')


def line(points, color=BLUE, width=1.3, arrow=False, dash=None):
    if arrow:
        width = max(width,1.45)
    cap = "butt" if arrow else "round"
    marker_size = "compact" if arrow == "compact" else "main"
    marker = f' marker-end="url(#head-{color[1:]}-{marker_size})"' if arrow else ""
    role = ' data-role="connector"' if arrow else ''
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{points}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="{cap}" stroke-linejoin="round"{marker}{dashed}{role}/>')


def circle(x, y, radius, fill, stroke="none", width=1):
    add(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')


def rectangle(x, y, w, h, fill="white", stroke=FAINT, radius=4, width=.8, dash=None):
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{dashed}/>')


def box(x, y, w, h, values, size=13, stroke="#BCD0DA", fill="#F1F4F5", bold=False, color=INK):
    rectangle(x, y, w, h, fill, stroke, min(9,h/3), 1)
    values = [values] if isinstance(values, str) else values
    spacing = size * 1.12
    baseline = y + h/2 - (len(values)-1)*spacing/2 + size*.34
    for i, value in enumerate(values):
        font_name = "Arial Bold.ttf" if bold else "Arial.ttf"
        natural = ImageFont.truetype(str(FONT_DIR/font_name),round(size*10)).getlength(value)/10
        label(x+w/2, baseline+i*spacing, value, size, bold, color, "middle",width=min(natural,w-8))


def title(code, x, y, values, size=21):
    group("panel-"+code)
    label(x, y, code, 23, True)
    for i, value in enumerate([values] if isinstance(values, str) else values):
        target_widths={"a":[281],"b":[574],"c":[301,143],"d":[448],"e":[435],
                       "f":[306],"g":[418],"h":[260]}
        label(x+34, y+i*23, value, max(size,22), True,width=target_widths[code][i])


def band(x, y, w, value):
    rectangle(x, y, w, 19, LIGHT, "none", 7)
    label(x+12, y+14, value, 16, True)


def badge(x, y, value, radius=14):
    circle(x, y, radius, BLUE)
    label(x, y+5, value, 18, True, "white", "middle")


def inline_svg(key, artwork, x, y, w, h):
    root = ET.fromstring(artwork)
    view = root.attrib.get("viewBox")
    if not view:
        view = f'0 0 {root.attrib["width"].replace("px","")} {root.attrib["height"].replace("px","")}'
    inner = re.search(r"<svg\b[^>]*>(.*)</svg>", artwork, re.S).group(1)
    inner = re.sub(r"<metadata>.*?</metadata>", "", inner, flags=re.S)
    for old in sorted(set(re.findall(r'\bid="([^"]+)"', inner)), key=len, reverse=True):
        inner = inner.replace(f'id="{old}"', f'id="{key}-{old}"')
        inner = inner.replace(f'#{old}"', f'#{key}-{old}"').replace(f'#{old})', f'#{key}-{old})')
    add(f'<svg id="{key}" x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{view}" '
        f'preserveAspectRatio="xMidYMid meet"><title>{escape(key)}</title>{inner}</svg>')


def asset(name, x, y, w, h, instance=None):
    artwork = (ASSETS/(name+".svg")).read_text()
    # Match the reference's conventional black-bond / blue-N / red-O drawing style.
    # Atom and bond geometry remains the archived RDKit vector geometry.
    for original, replacement in (("#30373B", "#000000"), ("#2D5B87", "#0000FF"),
                                  ("#9E4433", "#FF0000")):
        artwork = artwork.replace(original, replacement)
    if name+".svg" in MOLECULE_BOUNDS:
        left, top, width, height = MOLECULE_BOUNDS[name+".svg"]
        crop = f"{left-6} {top-6} {width+12} {height+12}"
        artwork = re.sub(r"""viewBox=['"][^'"]+['"]""", f'viewBox="{crop}"', artwork, count=1)
    inline_svg(instance or name, artwork, x, y, w, h)


def new_molecule(name, smiles, rotate=0):
    path = ASSETS / (name+".svg")
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(smiles)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DSVG(540, 300)
    opts = drawer.drawOptions()
    opts.clearBackground = False
    opts.padding = .09
    opts.fixedBondLength = 60
    opts.bondLineWidth = 5.0
    opts.minFontSize = 36
    opts.maxFontSize = 48
    opts.rotate = rotate
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    path.write_text(re.sub(r"[ \t]+$", "", drawer.GetDrawingText(), flags=re.M))


def oriented_motif(name, smiles, width, height, rotate=180, source=None, font_size=14, bond_width=1.5):
    """Draw the same canonical motif in the reference orientation at its final size."""
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DSVG(width,height)
    opts = drawer.drawOptions()
    opts.clearBackground = False
    opts.padding = .03
    opts.bondLineWidth = bond_width
    opts.fixedFontSize = font_size
    opts.updateAtomPalette({16:(.52,.38,.04)})
    opts.rotate = rotate
    rdMolDraw2D.PrepareAndDrawMolecule(drawer,mol)
    drawer.FinishDrawing()
    artwork = drawer.GetDrawingText()
    (ASSETS/(name+'.svg')).write_text(artwork)
    DRAWING_SPECS.append({'asset':name+'.svg','canonical_smiles':Chem.MolToSmiles(mol),
                          'width_px':width,'height_px':height,'rotation_degrees':rotate,
                          'atom_font_px':font_size,'source':source})
    return artwork


def motif_reference(name, index, x,y,w,h):
    art = oriented_motif(name, CASE['mma']['motifs'][index]['motif'], w,h,
                        source=f'case_manifest.json:mma.motifs[{index}]')
    inline_svg(name, art, x,y,w,h)


def atom_alignment():
    """Render the archived atom mapping in its own editable vector coordinate system."""
    motif = Chem.MolFromSmiles(CASE["mma"]["motifs"][0]["motif"])
    partial = Chem.MolFromSmiles(CASE["construction"]["states"][1])
    correspondence = CASE["mma"]["alignment"]
    pieces, coordinates = [], []
    for i, mol in enumerate((motif, partial)):
        rdDepictor.Compute2DCoords(mol)
        drawer = rdMolDraw2D.MolDraw2DSVG(450, 185)
        opts = drawer.drawOptions()
        opts.clearBackground = False
        opts.bondLineWidth = 3
        opts.padding = .06
        opts.maxFontSize = 29
        atoms = [m if i == 0 else g for g, m in correspondence]
        rdMolDraw2D.PrepareAndDrawMolecule(
            drawer, mol, highlightAtoms=atoms,
            highlightAtomColors={j:(.72,.86,.82) for j in atoms},
        )
        drawer.FinishDrawing()
        content = re.search(r"<svg\b[^>]*>(.*)</svg>", drawer.GetDrawingText(), re.S).group(1)
        pieces.append(f'<g transform="translate({i*450} 0)">{content}</g>')
        coordinates.append([(drawer.GetDrawCoords(j).x+i*450,drawer.GetDrawCoords(j).y) for j in range(mol.GetNumAtoms())])
    connections = []
    for g,m in (correspondence[4],correspondence[6]):
        a,b=coordinates[0][m]; c,d=coordinates[1][g]
        connections.append(f'<path d="M{a:.2f} {b:.2f}C430 {b:.2f} 460 {d:.2f} {c:.2f} {d:.2f}" '
                           f'fill="none" stroke="{TEAL}" stroke-width="2.4" stroke-dasharray="8 8"/>')
    art = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 185">'+"".join(connections+pieces)+"</svg>"
    (ASSETS/"atom-level-alignment.svg").write_text(art)


def spectrum(name, peaks, x, y, width, height, *, axes=False, highlight=False, simulated=False, domain=None):
    """Draw centroid sticks from archived peaks. Normalize to the base peak."""
    start = len(PARTS)
    group("spectrum-"+name)
    intensity_max = max(intensity for _,intensity in peaks)
    mz_min = min(mz for mz,_ in peaks)
    mz_max = max(mz for mz,_ in peaks)
    pad = max((mz_max-mz_min)*.045,2)
    lower,upper = domain or (mz_min-pad,mz_max+pad)
    base = y+height
    axis = "#65747C"
    if axes:
        for tick in (0,50,100):
            yy=base-tick*height/100
            if tick:
                line(f"M{x} {yy}H{x+width}","#E4EAEC",.65)
            line(f"M{x-4} {yy}H{x}",axis,.85)
            label(x-8,yy+4,str(tick),12.5,anchor="end")
    for mz,intensity in sorted(peaks):
        xx=x+(mz-lower)/(upper-lower)*width
        yy=base-intensity/intensity_max*height
        color = TEAL if simulated else COPPER
        if highlight and abs(mz-120.0808)<.00001:
            color = "#A84B09"
        add(f'<line x1="{xx:.4f}" x2="{xx:.4f}" y1="{base:.4f}" y2="{yy:.4f}" '
            f'data-mz="{mz}" data-intensity="{intensity}" stroke="{color}" '
            f'stroke-width="{1.65 if axes else 1.1}" stroke-linecap="butt"/>')
    line(f"M{x} {y}V{base}H{x+width}",axis,.9 if axes else .7)
    if axes:
        for tick in range(70,121,10):
            xx=x+(tick-lower)/(upper-lower)*width
            line(f"M{xx} {base}v3",axis,.85)
            label(xx,base+16,str(tick),13,anchor="middle")
        label(x+width+3,base+16,"m/z",13,math=True)
        add(f'<text transform="translate({x-42} {y+height/2}) rotate(-90)" text-anchor="middle" '
            f'font-family="Arial" font-size="12.5" fill="{INK}">Rel. intensity (%)</text>')
    end()
    art = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-54} {y-10} {width+70} {height+52}">' + "\n".join(PARTS[start:]) + "</svg>"
    filename = f"spectrum-{name}.svg" if name.startswith("f-") else f"{name}.svg"
    (ASSETS/filename).write_text(art)


def panel_a():
    title("a",21,25,"Metabolomic dark matter",22)
    label(70,46,"Tandem mass spectrometry (MS/MS)",14)
    label(363,18,"Benchmark illustration",15)
    spectrum("a-measured",CASE["query"]["peaks"],83,58,243,59,axes=True,highlight=True,domain=(65,125))
    label(303,69,"120.0808",16,color=COPPER,anchor="end",math=True)
    label(48,161,"MassSpecGym 0002114",13.5,True)
    add(f'<text x="222" y="160" font-size="14" font-weight="700" font-family="Times New Roman" fill="{INK}">'
        '[M+H]<tspan baseline-shift="super" font-size="72%">+</tspan> 493.2804</text>')
    for c,x in zip(CASE["candidates"],(365,537)):
        badge(x+2,44,c["label"])
        asset("candidate_"+c["label"],x+8,22,130,112,"a-candidate-"+c["label"])
        formula(x+66,151,"C28H36N4O4",23,anchor="middle")
    end()


def panel_b():
    title("b",700,25,"ORBIT-MS molecular inference at generation t",21)
    label(745,48,"World–Generator–Verifier (WGV)",18)
    label(1068,47,"Within-spectrum molecular inference",13,color=SECONDARY)
    box(704,72,130,48,["Experimental","MS/MS"],16,stroke="#A7CEC5",fill="#F7FBF9")
    box(885,72,173,48,[],16,stroke="#AFBFC8")
    label(971,88,"MMA-conditioned",17,anchor="middle")
    label(971,110,"G",17,True,anchor="middle",math=True,italic=True)
    box(1101,72,108,48,["Molecular","candidates"],17)
    box(1257,72,106,48,[],18,stroke="#AFBFC8")
    label(1310,101,"W",22,True,anchor="middle",math=True,italic=True)
    box(1410,72,94,48,[],18,stroke="#AFBFC8")
    label(1457,101,"V",22,True,anchor="middle",math=True,italic=True)
    box(1540,72,114,48,["Structural","hypotheses"],17)
    for x1,x2 in ((835,883),(1059,1099),(1210,1255),(1364,1408),(1505,1538)):
        line(f"M{x1} 96H{x2}",arrow=True)
    box(708,143,108,23,"Next WGV",16,stroke="#8DBFB3",fill="#F7FBF9",bold=True,color=TEAL)
    line("M817 154H841V131H863V109H882",TEAL,1,True)
    label(1392,29,"Measured MS/MS",17,color=COPPER)
    line("M1458 39V69",COPPER,1.5,True)
    line("M917 122V143",SECONDARY,.8,False,"2 3")
    line("M1025 122V143",SECONDARY,.8,False,"2 3")
    label(864,161,"c  MMA retrieval",14,True)
    label(1009,161,"d  Molecular Generator (G)",14)
    line("M1277 121V133H1491V121",SECONDARY,.7)
    label(1282,155,"e  Fragmentation World (W) /",14)
    label(1310,170,"Spectral Verifier (V)",14)
    end()


def panel_c():
    title("c",19,209,["Motif knowledge construction","and retrieval"],20)
    band(15,249,357,"Offline structure-only")
    asset("library_parent",19,270,337,127)
    line("M99 399V447",TEAL,1.1,True)
    motif_reference("c-extracted-reference",0,23,453,130,44)
    box(171,408,118,40,["Substructure","mining"],18)
    line("M230 450V460",BLUE,1.1,True)
    box(171,463,119,47,["Canonicalize /","deduplicate"],17)
    line("M155 477H168",TEAL,1.1,True)
    box(308,463,63,42,["Mined","motifs"],17)
    line("M291 485H305",TEAL,1.1,True)
    line("M372 484H391V322H411",BLUE,1,True)
    band(15,537,357,"Online mass-matched retrieval")
    spectrum("c-query",[(CASE['mma']['observed_mz'],1)],22,615,56,27,highlight=True)
    label(11,611,"120.0808",18,color=COPPER,math=True)
    box(86,595,81,57,[],12)
    label(126,612,"Mass /",15,anchor="middle")
    label(126,629,"composition",14,anchor="middle",width=74)
    line("M79 624H84",BLUE,1.45,"compact")
    formula(126,648,"C8H10N+",17,anchor="middle")
    line("M168 623H180V585H190",TEAL,1.5,True)
    line("M180 623V654H190",TEAL,1.5,True)
    motif_reference("c-online-motif-2-reference",0,193,566,108,31)
    motif_reference("c-online-motif-3-reference",1,195,636,104,34)
    label(191,611,"2  Phenethylamine",15)
    label(213,627,"427 groups",14.5)
    label(189,688,"3  N-ethylaniline",15)
    label(214,704,"107 groups",14.5)
    box(27,670,116,36,["Paired TRAIN /","W simulations"],15)
    box(306,663,72,42,["Retrieved","motifs 2, 3"],14,stroke="#9BC7BF",fill="#F2FAF5")
    line("M298 681H304",TEAL,1.45,"compact")
    end()


def graph_overview():
    label(409,254,"Motif containment overview",17,True)
    label(449,395,"Archived motif sample",13,color=SECONDARY)
    nodes = {node["id"]:node for node in KG["nodes"]}
    focus = set(KG["focus_ids"])
    def xy(id_):
        selected_positions={"1":(963,261),"2":(930,296),"3":(1065,281),
                            "4":(976,326),"5":(1068,320),"6":(993,361)}
        if id_ in selected_positions:
            DISPLAY_POSITIONS[id_]=list(selected_positions[id_])
            return selected_positions[id_]
        x,y=nodes[id_]["xy"]
        result = [407+x*0.52,253+y*.275]
        DISPLAY_POSITIONS[id_] = result
        return result
    rectangle(913,242,184,136,"#F8FBFA",TEAL,12,1,dash="4 3")
    for edge in KG["overview_edges"]:
        u,v=edge["larger"],edge["included"]
        a,b=xy(u);c,d=xy(v)
        selected=u in focus and v in focus
        group("kg-edge-"+u+"-"+v)
        line(f"M{a:.2f} {b:.2f}L{c:.2f} {d:.2f}",
             TEAL if selected else "#CCD8DA",1.5 if selected else .65)
        end()
    for id_ in nodes:
        x,y=xy(id_)
        group("kg-node-"+id_)
        circle(x,y,6.8 if id_ in focus else 2.5,"#168C70" if id_ in focus else "#6E8B98")
        if id_ in focus:
            label(x+10,y+5,id_,15,True)
        end()
    line("M913 377L721 412M1094 376L1122 412",TEAL,.8)


def panel_d():
    title("d",399,209,"Knowledge graph to molecular construction",20)
    label(435,231,"Mass-matched substructure alignment (MMA)",16,True)
    group("knowledge-graph-overview")
    graph_overview()
    end()
    label(399,436,"Selected molecular neighborhood",18,True)
    group("zoomed-motif-neighborhood")
    positions={"1":(397,449,117,59),"2":(521,487,114,51),"3":(644,452,106,55),
               "4":(414,589,93,50),"5":(675,594,73,50),"6":(557,623,53,51)}
    captions={"1":(454,523),"2":(575,552),"3":(694,523),
              "4":(459,659),"5":(708,659),"6":(584,684)}
    names={"1":"Phenylalanine","2":"Phenethylamine","3":"N-ethylaniline","4":"Ethylbenzene","5":"Aniline","6":"Benzene"}
    for u,v in KG["zoom_edges"]:
        paths={("1","2"):"M500 494L514 505",("1","4"):"M446 541V586",
               ("2","6"):"M583 565V620",("4","6"):"M510 631L551 649",
               ("3","5"):"M686 529H643V579H678L692 591",("5","6"):"M665 632L617 651"}
        line(paths[u,v],TEAL,1.25,True)
    for id_,(x,y,w,h) in positions.items():
        node = next(n for n in KG['nodes'] if n['id']==id_)
        art=oriented_motif('zoom-display-'+id_,node['canonical_smiles'],w,h,rotate=0,
                          source=f'motif-topology.json:node[{id_}]')
        inline_svg('zoom-display-'+id_,art,x,y,w,h)
        cx,cy=captions[id_]
        caption_width={'1':126,'2':126,'3':114,'4':118,'5':80,'6':80}[id_]
        label(cx,cy,id_+" "+names[id_],15,anchor="middle",width=caption_width)
    label(435,705,"Substructure containment",17,True)
    end()
    line("M756 421V710",FAINT,.8)
    label(777,436,"MMA alignment and construction",18,True)
    motif_reference("encoder-motif-reference",0,769,459,93,43)
    box(658,539,93,36,["Retrieved","motifs 2, 3"],13,stroke="#8DBFB3",fill="#F7FBF9")
    line("M752 557H772Q775 557 775 554V522Q775 519 778 519H851Q854 519 854 516V500Q854 496 858 496H869",TEAL,1.45,True)
    box(872,463,61,53,["Motif","graph","encoder"],15)
    box(955,445,79,49,["Peak","attention","+ prior"],14)
    box(1063,449,66,32,["Peak","memory"],14)
    box(955,493,80,43,["Motif atom","memory","(optional)"],13.5)
    box(1055,498,57,34,["Graph","state"],15)
    line("M863 482H870",BLUE,1.45,"compact")
    line("M934 489.5H943V469.5H953",BLUE,1.2,True)
    line("M943 489.5V515H953",BLUE,1.2,True)
    line("M1035 465H1061",BLUE,1.2,True)
    line("M1036 515H1053",BLUE,1.2,True)
    box(833,540,231,22,"Shared spectrum/graph backbone",14.5)
    line("M1130 465H1139V551H1067",BLUE,1.45,True)
    line("M1113 515H1139",BLUE,1.2)
    line("M832 551H802V572",BLUE,1.2,True)
    box(766,575,132,50,[],12)
    label(832,596,"Hybrid policy",15.5,True,anchor="middle")
    label(832,615,"Atom / ring / motif",14.5,anchor="middle")
    box(920,575,81,50,["Mass /","valence","constraint"],15)
    box(1019,579,70,42,["Graph","transition"],15)
    box(1096,579,52,42,["A/B","candidates"],13.5)
    line("M899 600H918",BLUE,1.2,True)
    line("M1002 600H1017",BLUE,1.2,True)
    line("M1090 600H1094",BLUE,1.45,"compact")
    # The selected atoms are represented separately from the parent-preserving action replay.
    rectangle(767,633,372,78,"white",FAINT,8)
    label(775,651,"Reference-conditioned action replay",16.5,True,width=331)
    asset("growth_2",778,657,145,48,"replay-before")
    asset("growth_3",968,657,164,48,"replay-after")
    line("M927 680H961",BLUE,1.2,True)
    end()


def panel_e():
    title("e",1172,209,"Fragmentation evidence and verification",19)
    label(1221,231,"MassSpecGym 0002114 · benchmark",15,italic=True)
    for c,y in zip(CASE["candidates"],(250,324)):
        badge(1182,y+13,c["label"],13)
        asset("candidate_"+c["label"],1195,y-5,76,68,"e-input-"+c["label"])
    box(1280,285,60,40,["A/B","candidates"],15,bold=True)
    line("M1265 275H1270V348H1265",BLUE,1.15)
    line("M1270 305H1278",BLUE,1.15,True)
    box(1357,280,68,50,["W","fragments"],16,bold=True)
    line("M1341 305H1355",BLUE,1,True)
    box(1439,279,142,24,"120.0808 · shared",15)
    box(1439,312,142,24,"120.0889 · A only",15)
    label(1435,272,"Predicted m/z",16)
    line("M1426 291H1437",BLUE,1,True)
    line("M1426 324H1437",BLUE,1,True)
    box(1596,297,55,35,"V",18,bold=True)
    line("M1582 291H1588V314.5H1594",BLUE,1.45,"compact")
    line("M1582 324H1588V314.5",BLUE,1)
    spectrum("e-measured",CASE["query"]["peaks"],1554,250,93,25,domain=(65,125),highlight=True)
    label(1529,242,"Measured MS/MS",16)
    line("M1623.5 277V294",BLUE,1,True)
    box(1170,389,87,53,["Candidates","from","G output"],14)
    rectangle(1261,410,373,49,"white","#B5CAD6",4)
    for x in (1305,1392,1471,1550):
        line(f"M{x} 410V459","#B5CAD6",.6)
    line("M1261 435H1634","#B5CAD6",.6)
    label(1282,404,"m/z",15,anchor="middle",math=True)
    for j,mz in enumerate((72.0816,90.9773,120.0808,120.0893)):
        xx=(1352,1428,1509,1590)[j]
        label(xx,404,f"{mz:.4f}",16,anchor="middle",math=True)
    for i,c in enumerate(CASE["candidates"]):
        yy=425+i*23
        label(1282,yy+4,c["label"],16,True,anchor="middle")
        for j,cell in enumerate(c["evidence"]):
            xx=(1352,1428,1509,1590)[j]
            present=cell["density"]>0
            fill=COPPER if j==3 and present else "#789099" if present else "white"
            circle(xx,yy,6.5,fill,"#78939E" if not present else "none",1.1)
    circle(1284,473,4.3,"#789099")
    label(1295,478,"Supported",14.5)
    circle(1400,473,4.3,"white","#78939E",1.1)
    label(1411,478,"Unexplained",14.5)
    label(1198,504,"Structural hypotheses",20,True)
    for c,x in zip(CASE["candidates"],(1241,1448)):
        badge(x,534,c["label"])
        asset("candidate_"+c["label"],x+7,511,134,81,"e-output-"+c["label"])
    formula(1310,614,"C28H36N4O4",19,anchor="middle")
    label(1478,614,"(MassSpecGym 0002114)",15,True,anchor="middle")
    label(1275,648,"Separate TRAIN FIT audit",21,True)
    end()


def experience_molecule(key, instance, x, center_y, width, height=33):
    record = PAIRED_TRAIN if key == "paired" else CASE["experience"][key]
    # Use the archived structure itself, including stereochemistry where recorded.
    atom_font = 6 if key == "wake" else 8
    art = oriented_motif(instance,record["smiles"],width,height,rotate=0,
                         source=f"experience:{key}",font_size=atom_font,bond_width=1.0)
    inline_svg(instance,art,x,center_y-height/2,width,height)


def panel_f():
    title("f",20,750,"Molecular experience sources",21)
    rectangle(16,761,425,19,LIGHT,"none",7)
    label(182,776,"Available data",15,True,anchor="middle")
    label(390,776,"Learning pair",15,True,anchor="middle")
    rows = (
        ("paired",800,["Paired","molecule–spectrum"]),
        ("sleep",838,["Structure-only"]),
        ("wake",875,["Spectrum-only"]),
        ("hindsight",916,["Model-generated"]),
    )
    for key,y,words in rows:
        box(16,y-14,115,28,words,14.2)
        record = PAIRED_TRAIN if key == "paired" else CASE["experience"][key]
        peaks = record["peaks"]
        if key != "wake":
            # Paired and counterfactual rows retain the same structure on both sides.
            experience_molecule(key,"f-"+key+"-input",139,y,48 if key=="paired" else 83)
        if key in {"paired","wake"}:
            spectrum("f-"+key+"-input",peaks,190 if key=="paired" else 156,y-12,
                     39 if key=="paired" else 67,24)
        if key == "paired":
            line(f"M234 {y}H339",BLUE,1.5,True)
        elif key == "sleep":
            box(248,811,81,17,"Motif mining",13,stroke="#A7CEC5",fill="#F2FAF5")
            line("M229 838H239V819.5H246",TEAL,1.5,True)
            line("M239 838H246",TEAL,1.5,True)
            box(248,y-10,81,25,["Sleep","Frozen W"],12.5)
            line(f"M331 {y}H339",BLUE,1.5,True)
        else:
            operation = ["Wake","G/W/V filter"] if key == "wake" else ["Hindsight","Frozen W"]
            box(248,y-14,81,28,operation,12.5)
            line(f"M229 {y}H246",BLUE,1.5,True)
            line(f"M331 {y}H339",BLUE,1.5,True)
        experience_molecule(key,"f-"+key+"-pair",342,y,55)
        spectrum("f-"+key+"-pair",peaks,401,y-11,39,22,simulated=key in {"sleep","hindsight"})
        if key=="wake":
            label(440,900,"Pseudo-pair",12.5,italic=True,anchor="end",width=57)
    end()


def panel_g():
    title("g",463,750,"Information-guided experience acquisition",21)
    band(484,762,260,"Evidence / scaffold guards")
    headers=[(539,[("Entropy",803)]),(593,[("TRAIN",794),("C/N/O",810)]),
             (648,[("Ring",794),("scarcity",810)]),
             (702,[("Wake /",790),("Hindsight",805),("priority",820)]),
             (751,[("Weight",819)])]
    for x,words in headers:
        for word,y in words:
            label(x,y,word,13.5,anchor="middle",width=54)
    examples = (PAIRED_TRAIN,CASE["experience"]["sleep"],CASE["experience"]["wake"],CASE["experience"]["hindsight"])
    # Qualitative acquisition diagram; these are not measured sample probabilities.
    weights=[[.4,.65,.5,.25,.47],[.7,.35,.8,.8,.75],[.3,.85,.6,.8,.82],[.6,.45,.25,.35,.4]]
    palette=["#DAF2E6","#C8ECDA","#AFE4CA","#93DDBA","#72D3A8","#42C694","#15B986"]
    for i,values in enumerate(weights):
        yy=829+i*18
        label(474,yy+4,str(i+1),12,anchor="middle",color=SECONDARY)
        spectrum(f"g-spectrum-{i}",examples[i]["peaks"],486,yy-10,30,15,simulated=i in (1,3))
        for j,value in enumerate(values):
            x=[521,575,630,684,733][j]
            group(f"acquisition-cell-{i}-{j}")
            for k in range(6):
                idx=round(max(0,min(6,value*5+(k-2)*.3)))
                color="#216B8A" if j==4 and k==0 else palette[idx]
                rectangle(x+k*6,yy-6,6,12,color,"none",0)
            end()
    for i,word in enumerate(["Weighted","sampling","without","replacement"]):
        label(801,833+i*15,word,14.5,anchor="middle",width=62)
    for word,y in [("Selected",776),("pairs",791)]:
        label(850,y,word,14.5,anchor="middle")
    for i,yy in enumerate((802,843,883)):
        # Show the qualitative selection as row IDs paired with the source spectra.
        selected = (0,1,3)[i]
        label(850,yy+4,str(selected+1),13,anchor="middle",color=SECONDARY)
        spectrum(f"g-selected-{i}",examples[selected]["peaks"],863,yy-12,33,22,
                 simulated=selected in (1,3))
    line("M901 802V883",TEAL,1.45)
    for i,(caption,code) in enumerate([(["Knowledge","expansion"],"c"),(["Generator","learning"],"d"),(["Verifier","learning"],"e")]):
        yy=[784,825,865][i]
        box(914,yy,80,37,caption,16,stroke="#A6C8C1",fill="#F2FAF5")
        line(f"M901 {yy+18}H912",TEAL,1.5,True)
        circle(1010,yy+18,12.5,TEAL)
        label(1010,yy+24,code,19,True,"white","middle")
    label(543,917,"Paired TRAIN anchors",16)
    line("M743 912H769",BLUE,1.6,True)
    box(772,901,126,25,"Tool resources",16,stroke="#A6C8C1",fill="#F2FAF5")
    end()


def robot(x,y):
    group("scientific-agent-vector-icon")
    rectangle(x,y,30,21,"white",VIOLET,6,1.4)
    circle(x+9,y+8,2,VIOLET);circle(x+22,y+8,2,VIOLET)
    line(f"M{x+11} {y+15}h8",VIOLET,1.2)
    line(f"M{x+15} {y}v-6",VIOLET,1.1)
    circle(x+15,y-8,2,"white",VIOLET,1.2)
    line(f"M{x-3} {y+7}v9M{x+33} {y+7}v9",VIOLET,1.2)
    end()


def panel_h():
    title("h",1046,750,"Scientific Improver Agent",21)
    robot(1072,767)
    rectangle(1059,788,111,100,"white",FAINT,4)
    label(1066,802,"TRAIN FIT ·",15,True)
    label(1066,817,"diagnostic subset",14)
    for i,s in enumerate(["Absent","Misranked","Motif gaps"]):
        y=839+i*16
        label(1067,y,"• "+s,14.5)
    box(1180,825,63,27,"Hypothesis",14,stroke="#C7BDCF")
    line("M1171 838.5H1178",VIOLET,1.45,"compact")
    label(1217,791,"Select ONE",16,color=VIOLET)
    box(1256,800,118,42,["Expand","MMA knowledge"],15,stroke="#C7BDCF",fill="#F9F4FD")
    box(1256,845,118,20,"Improve G",15,stroke="#C7BDCF",fill="#F9F4FD")
    box(1256,868,118,20,"Improve V",15,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1244 838.5H1247",VIOLET,1.45)
    line("M1247 838.5V821H1254M1247 838.5V855H1254M1247 855V878H1254",VIOLET,1.45,"compact")
    box(1237,891,138,20,"Tool selection → g",15,stroke="#C7BDCF",fill="#F9F4FD")
    box(1378,750,114,22,"Trial from g",15,bold=True,stroke="#AFBFC8")
    line("M1435 773V783",BLUE,1.1,True)
    label(1390,798,"Paired CAL ·",16,True)
    label(1379,811,"Independent split",14)
    rectangle(1380,816,117,51,"white",FAINT,4)
    line("M1438 816V867",FAINT,.6)
    label(1408,830,"Baseline",14,anchor="middle",width=52)
    label(1408,844,"WGV",13,anchor="middle")
    label(1466,830,"Trial",14,anchor="middle")
    label(1466,844,"WGV",13,anchor="middle")
    label(1466,860,"(W frozen)",12,True,anchor="middle",width=51,italic=True)
    box(1505,815,63,43,["Promotion","gate"],14,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1498 837H1503",BLUE,1.45,"compact")
    box(1590,792,71,30,"",12,stroke="#94BEAF",fill="#F7FBF9")
    generation(1625,811,True,18)
    label(1589,787,"Pass",14,italic=True)
    line("M1569 829H1577V807H1588",TEAL,1.2,True)
    box(1590,846,71,30,"Retain",15)
    label(1575,842,"Fail",14)
    line("M1569 850H1577V861H1588",SECONDARY,1.1,True)
    box(1237,915,138,20,"Collect evidence",15,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1211.5 854V921Q1211.5 925 1215.5 925H1235",VIOLET,1,True)
    box(1405,902,95,34,["Episode","Memory"],15,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1376 925H1403",VIOLET,1,True)
    line("M1538 859V879H1452V900",VIOLET,1,True,"3 3")
    line("M1501 919H1533",VIOLET,1.35,True,"3 3")
    label(1540,925,"Next hypothesis",15,color=VIOLET,italic=True)
    end()


def main():
    for node in KG["nodes"]:
        if node["id"] in KG["focus_ids"]:
            new_molecule("zoom_motif_"+node["id"],node["canonical_smiles"])
    atom_alignment()
    add(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="180mm" height="{180*H/W:.10f}mm" viewBox="0 0 {W} {H}" font-family="Arial">')
    add("<title>ORBIT-MS molecular structure elucidation and scientific improvement</title>")
    add("<defs>")
    for color in (INK,BLUE,TEAL,COPPER,VIOLET,SECONDARY):
        for size,length,height in (("main",8,6.4),("compact",5.2,4.1)):
            add(f'<marker id="head-{color[1:]}-{size}" viewBox="0 0 10 8" refX="10" refY="4" '
                f'markerUnits="userSpaceOnUse" markerWidth="{length}" markerHeight="{height}" orient="auto">'
                f'<path d="M0 0L10 4L0 8L2.4 4Z" fill="{color}"/></marker>')
    add("</defs>")
    rectangle(0,0,W,H,"white","none",0)
    for d in ("M20 174H1658","M20 720H1658","M687 5V168","M383 185V710","M1153 185V710",
              "M453 735V935","M1034 735V935"):
        line(d,FAINT,.8)
    label(27,725,"Across-generation scientific learning",14,color=SECONDARY)
    panel_a();panel_b();panel_c();panel_d();panel_e();panel_f();panel_g();panel_h()
    add("</svg>")
    result=re.sub(r"[ \t]+$", "", "\n".join(PARTS),flags=re.M)+"\n"
    target=FIG/"orbit_ms_nmi_figure1_vector.svg"
    target.write_text(result)
    (SOURCE/'data/reference_drawing_specs.json').write_text(json.dumps(DRAWING_SPECS,indent=2)+'\n')
    (SOURCE/'data/reference_graph_layout.json').write_text(json.dumps({
        'canvas_px':[W,H],'node_positions_px':DISPLAY_POSITIONS,
        'highlight_bounds_px':[913,242,184,136],
        'edges_source':'motif-topology.json:overview_edges'},indent=2)+'\n')
    root=ET.fromstring(result)
    assert not root.findall(".//{http://www.w3.org/2000/svg}image")


if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["--normalize-pdf-page"]:
        from pypdf import PdfReader, PdfWriter
        from pypdf.generic import RectangleObject
        from decimal import Decimal
        pdf_path = FIG / "orbit_ms_nmi_figure1_vector.pdf"
        writer = PdfWriter()
        writer.clone_document_from_reader(PdfReader(pdf_path))
        width = Decimal(180) * Decimal(72) / Decimal("25.4")
        height = width * H / W
        writer.pages[0].mediabox = RectangleObject([0,0,float(width),float(height)])
        writer.pages[0].cropbox = RectangleObject([0,0,float(width),float(height)])
        tmp = pdf_path.with_suffix(".tmp.pdf")
        writer.write(tmp)
        tmp.replace(pdf_path)
    else:
        main()
