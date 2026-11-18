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

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
SOURCE = FIG / "orbit_ms_nmi_figure1_sources"
ASSETS = SOURCE / "assets"
CASE = json.loads((SOURCE / "data/case_manifest.json").read_text())
KG = json.loads((SOURCE / "data/motif-topology.json").read_text())
MOLECULE_BOUNDS = json.loads((ASSETS / "molecule_bounds.json").read_text())
W, H = 1670, 942
INK, BLUE, TEAL, COPPER, VIOLET = "#101214", "#008BC0", "#00A77C", "#BD4B00", "#7934D7"
FAINT, SECONDARY, LIGHT = "#D7DEE0", "#677680", "#F2F5F4"
PARTS = []


def add(markup):
    PARTS.append(markup)


def group(name):
    add(f'<g id="{name}"><title>{escape(name.replace("-", " "))}</title>')


def end():
    add("</g>")


def label(x, y, value, size=13, bold=False, color=INK, anchor="start", math=False):
    family = "Times New Roman" if math else "Arial"
    add(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" '
        f'font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(value)}</text>')


def formula(x, y, value, size=15, color=INK, anchor="start"):
    # Input uses ordinary chemistry notation. Digits become real subscript spans.
    tokens = re.findall(r"\d+|\+|[^\d+]+", value)
    spans = []
    for token in tokens:
        baseline = "sub" if token.isdigit() else "super" if token == "+" else "baseline"
        size_attr = ' font-size="72%"' if baseline != "baseline" else ""
        spans.append(f'<tspan baseline-shift="{baseline}"{size_attr}>{escape(token)}</tspan>')
    add(f'<text x="{x}" y="{y}" font-family="Times New Roman" font-size="{size}" '
        f'fill="{color}" text-anchor="{anchor}">{"".join(spans)}</text>')


def generation(x, y, next_=False, size=14, color=INK, anchor="middle"):
    sub = "t+1" if next_ else "t"
    add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" '
        f'font-size="{size}" font-family="Times New Roman" font-style="italic">'
        f'WGV<tspan baseline-shift="sub" font-size="72%">{sub}</tspan></text>')


def line(points, color=BLUE, width=1.3, arrow=False, dash=None):
    marker = f' marker-end="url(#head-{color[1:]})"' if arrow else ""
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{points}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{marker}{dashed}/>')


def circle(x, y, radius, fill, stroke="none", width=1):
    add(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')


def rectangle(x, y, w, h, fill="white", stroke=FAINT, radius=4, width=.8, dash=None):
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{dashed}/>')


def box(x, y, w, h, values, size=13, stroke="#BCD0DA", fill="#F6F8F8", bold=False, color=INK):
    rectangle(x, y, w, h, fill, stroke)
    values = [values] if isinstance(values, str) else values
    spacing = size * 1.12
    baseline = y + h/2 - (len(values)-1)*spacing/2 + size*.34
    for i, value in enumerate(values):
        label(x+w/2, baseline+i*spacing, value, size, bold, color, "middle")


def title(code, x, y, values, size=21):
    group("panel-"+code)
    label(x, y, code, 23, True)
    for i, value in enumerate([values] if isinstance(values, str) else values):
        label(x+34, y+i*23, value, size, True)


def band(x, y, w, value):
    rectangle(x, y, w, 19, LIGHT, "none", 7)
    label(x+12, y+14, value, 14, True)


def badge(x, y, value, radius=13):
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


def new_molecule(name, smiles):
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
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    path.write_text(re.sub(r"[ \t]+$", "", drawer.GetDrawingText(), flags=re.M))


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


def spectrum(name, peaks, x, y, width, height, axes=False, highlight=False, simulated=False):
    """Native SVG spectrum generated from the original m/z and intensity pairs."""
    start = len(PARTS)
    group("spectrum-"+name)
    norm = max(p[1] for p in peaks)
    lower, upper = (65,125) if axes else (min(p[0] for p in peaks)-2,max(p[0] for p in peaks)+2)
    base = y+height
    line(f"M{x} {base}H{x+width}", SECONDARY, .7)
    if axes:
        line(f"M{x} {y}V{base}", SECONDARY, .7)
    for i,(mz,intensity) in enumerate(peaks):
        xx=x+(mz-lower)/(upper-lower)*width
        color=TEAL if simulated else BLUE
        is_base = highlight and abs(mz-120.0808)<.00001
        if is_base:
            color=COPPER
        stick_width = (4.5 if is_base else 6) if axes else (1.8 if is_base else 1.25)
        line(f"M{xx:.3f} {base}V{base-intensity/norm*height:.3f}", color, stick_width)
    if axes:
        for v in (70,80,90,100,110,120):
            xx=x+(v-lower)/(upper-lower)*width
            line(f"M{xx} {base}v4", SECONDARY, .7)
            label(xx,base+17,str(v),13,anchor="middle")
        label(x-8,y+4,"1",13,anchor="end")
        label(x-8,base+4,"0",13,anchor="end")
        label(x+width,base+33,"m/z",15,anchor="end",math=True)
    if highlight:
        label(x+width-4,y+8,"120.0808",16,color=COPPER,anchor="end",math=True)
    end()
    fragment="\n".join(PARTS[start:])
    # Standalone source shares the same vector commands with the master.
    art = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-20} {y-10} {width+40} {height+50}">{fragment}</svg>'
    (ASSETS/(name+".svg")).write_text(art)


def mini_pair(name, smiles, peaks, x, y, simulated=False):
    asset(name, x, y-12, 45, 27, instance=f"{name}-{x}-{y}")
    spectrum(f"pair-{name}-{x}", peaks, x+49, y-5, 38, 20, simulated=simulated)


def panel_a():
    title("a",21,25,"Metabolomic dark matter",22)
    label(70,46,"Tandem mass spectrometry (MS/MS)",14)
    label(363,18,"Benchmark illustration",15)
    spectrum("a-measured",CASE["query"]["peaks"],65,56,264,62,True,True)
    label(52,160,"MassSpecGym 0002114",13)
    add(f'<text x="207" y="160" font-size="13" font-family="Times New Roman" fill="{INK}">'
        '[M+H]<tspan baseline-shift="super" font-size="72%">+</tspan> 493.2804</text>')
    for c,x in zip(CASE["candidates"],(365,537)):
        badge(x+2,44,c["label"])
        asset("candidate_"+c["label"],x+8,22,130,112,"a-candidate-"+c["label"])
        formula(x+66,151,"C28H36N4O4",17,anchor="middle")
    end()


def panel_b():
    title("b",700,25,"ORBIT-MS molecular inference at generation t",21)
    label(745,48,"World–Generator–Verifier (WGV)",18)
    label(1068,47,"Within-spectrum molecular inference",13,color=SECONDARY)
    box(704,71,130,50,["Experimental","MS/MS"],16,stroke="#A7CEC5",fill="#F7FBF9")
    box(885,84,173,48,["MMA-conditioned","G"],16,stroke="#AFBFC8")
    box(1101,85,108,47,["Molecular","candidates"],15)
    box(1257,85,106,47,"W",18,stroke="#AFBFC8")
    box(1410,85,94,47,"V",18,stroke="#AFBFC8")
    box(1540,84,114,48,["Structural","hypotheses"],15)
    for x1,x2 in ((835,883),(1059,1099),(1210,1255),(1364,1408),(1505,1538)):
        line(f"M{x1} 107H{x2}",arrow=True)
    box(909,54,99,25,"Next WGV",14,stroke="#8DBFB3",fill="#F7FBF9")
    line("M958 79V83",TEAL,1,True)
    spectrum("b-measured",CASE["query"]["peaks"],1375,28,90,25,highlight=False)
    label(1392,20,"Measured MS/MS",15,color=COPPER)
    line("M1458 55V79",COPPER,1.2,True)
    line("M917 133V149",SECONDARY,.8,False,"2 3")
    line("M1025 133V149",SECONDARY,.8,False,"2 3")
    label(853,166,"c  MMA retrieval",14,True)
    label(1008,166,"d  Molecular Generator (G)",14)
    line("M1277 134V140H1491V134",SECONDARY,.7)
    label(1282,155,"e  Fragmentation World (W) /",14)
    label(1310,170,"Spectral Verifier (V)",14)
    end()


def panel_c():
    title("c",19,209,["Motif knowledge construction","and retrieval"],20)
    band(15,249,357,"Offline structure-only")
    asset("library_parent",19,270,337,127)
    line("M99 401V442",TEAL,1.1,True)
    asset("retrieved_motif_1",14,444,140,57,"c-extracted")
    box(171,408,118,40,["Substructure","mining"],13)
    line("M229 448V461",BLUE,1.1,True)
    box(171,463,119,47,["Canonicalize /","deduplicate"],13)
    line("M154 480H168",TEAL,1.1,True)
    box(308,463,63,42,["Mined","motifs"],13)
    line("M291 484H305",TEAL,1.1,True)
    line("M371 484H389V322H410",BLUE,1,True)
    band(15,537,357,"Online mass-matched retrieval")
    spectrum("c-query",CASE["query"]["peaks"],22,614,58,33,highlight=True)
    box(86,595,86,66,[],12)
    label(129,613,"Precursor",12,anchor="middle")
    label(129,627,"mass/formula",12,anchor="middle")
    line("M80 638H84",BLUE,1,True)
    formula(128,650,"C8H10N+",14,anchor="middle")
    line("M170 621H180V583H192",TEAL,1,True)
    line("M180 621V664H192",TEAL,1,True)
    asset("retrieved_motif_1",192,563,108,37,"c-query-motif-2")
    asset("retrieved_motif_2",193,642,108,38,"c-query-motif-3")
    label(192,612,"2 · Phenethylamine",12.3)
    label(213,627,"427 mined groups",12.3)
    label(190,688,"3 · N-ethylaniline",12.3)
    label(214,703,"107 mined groups",12.3)
    box(23,674,112,29,["Paired TRAIN /","W simulations"],11.7)
    box(309,663,69,42,["Retrieved","motifs 2, 3"],12,stroke="#9BC7BF",fill="#F7FBF9")
    line("M298 682H307",TEAL,1,True)
    end()


def graph_overview():
    label(409,254,"Motif containment overview",17,True)
    label(449,274,"Archived motif sample",13)
    nodes = {node["id"]:node for node in KG["nodes"]}
    focus = set(KG["focus_ids"])
    def xy(id_):
        selected_positions={"1":(963,261),"2":(930,296),"3":(1065,281),
                            "4":(976,326),"5":(1068,320),"6":(993,361)}
        if id_ in selected_positions:
            return selected_positions[id_]
        x,y=nodes[id_]["xy"]
        return 407+x*0.49,253+y*.32
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
    positions={"1":(398,450,115,63),"2":(520,494,108,48),"3":(645,454,105,59),
               "4":(414,589,93,50),"5":(675,591,73,51),"6":(553,621,61,52)}
    captions={"1":(454,526),"2":(575,560),"3":(699,526),
              "4":(459,660),"5":(708,660),"6":(584,687)}
    names={"1":"Phenylalanine","2":"Phenethylamine","3":"N-ethylaniline","4":"Ethylbenzene","5":"Aniline","6":"Benzene"}
    for u,v in KG["zoom_edges"]:
        paths={("1","2"):"M512 494L534 510",("1","4"):"M446 541V586",
               ("2","6"):"M583 570V620",("4","6"):"M510 631L551 649",
               ("3","5"):"M703 577V587",("5","6"):"M665 632L617 651"}
        line(paths[u,v],TEAL,1.25,True)
    for id_,(x,y,w,h) in positions.items():
        asset("zoom_motif_"+id_,x,y,w,h)
        cx,cy=captions[id_]
        label(cx,cy,id_+" "+names[id_],14,anchor="middle")
    label(435,705,"Substructure containment",17,True)
    end()
    line("M756 421V710",FAINT,.8)
    label(777,436,"MMA alignment and construction",18,True)
    asset("retrieved_motif_1",774,461,90,44,"encoder-motif")
    box(658,539,93,36,["Retrieved","motifs 2, 3"],13,stroke="#8DBFB3",fill="#F7FBF9")
    line("M751 558H772V519H854V496H870",TEAL,1.45,True)
    box(872,463,61,53,["Motif","graph","encoder"],14)
    box(955,445,79,49,["Peak","attention","+ prior"],14)
    box(1063,449,66,32,["Peak","memory"],12)
    box(955,493,80,43,["Motif atom","memory","(optional)"],12)
    box(1055,498,57,34,["Graph","state"],13)
    line("M864 483H870",BLUE,1.2,True)
    line("M934 481H943V464H953",BLUE,1.2,True)
    line("M943 481V515H953",BLUE,1.2,True)
    line("M1035 464H1060",BLUE,1.2,True)
    line("M1036 515H1053",BLUE,1.2,True)
    box(833,540,231,22,"Shared spectrum/graph backbone",13)
    line("M1130 466H1138V551H1065",BLUE,1.2)
    line("M1113 515H1138",BLUE,1.2)
    line("M834 551H802V573",BLUE,1.2,True)
    box(766,575,132,50,[],12)
    label(795,589,"Hybrid",14,anchor="middle")
    label(796,604,"atom/ring/",14,anchor="middle")
    label(796,619,"motif",14,anchor="middle")
    for j in range(3):
        line(f"M840 {588+j*13}h50",TEAL,.6)
        for k,height in enumerate([3,5,2,6,4]):
            line(f"M{845+k*8} {588+j*13}v{-height}",TEAL,1)
    box(920,575,81,50,["Mass /","valence","constraint"],13)
    box(1019,579,70,42,["Graph","transition"],13)
    box(1096,579,52,42,["A/B","candidates"],11.5)
    line("M899 600H918",BLUE,1.2,True)
    line("M1002 600H1017",BLUE,1.2,True)
    line("M1090 600H1094",BLUE,1.2,True)
    # The selected atoms are represented separately from the parent-preserving action replay.
    rectangle(767,633,372,78,"white",FAINT,8)
    label(775,651,"Reference-conditioned action replay",14,True)
    asset("growth_2",778,657,145,48,"replay-before")
    asset("growth_3",968,657,164,48,"replay-after")
    line("M927 680H961",BLUE,1.2,True)
    end()


def panel_e():
    title("e",1172,209,"Fragmentation evidence and verification",19)
    label(1221,231,"MassSpecGym 0002114 · benchmark",14)
    for c,y in zip(CASE["candidates"],(250,324)):
        badge(1182,y+13,c["label"],12)
        asset("candidate_"+c["label"],1195,y-5,76,68,"e-input-"+c["label"])
    box(1275,285,62,39,["A/B","candidates"],13,bold=True)
    line("M1265 299H1273",BLUE,1,True)
    box(1352,278,73,49,["W","fragments"],14,bold=True)
    line("M1338 303H1350",BLUE,1,True)
    box(1439,279,142,24,"120.0808 · shared",13)
    box(1439,312,142,24,"120.0889 · A only",13)
    label(1435,272,"Predicted m/z",15)
    line("M1426 292H1437",BLUE,1,True)
    line("M1426 319H1437",BLUE,1,True)
    box(1596,297,55,35,"V",16)
    line("M1582 290H1589V313H1594",BLUE,1,True)
    line("M1582 324H1589V313",BLUE,1)
    spectrum("e-measured",CASE["query"]["peaks"],1564,254,83,25)
    label(1551,242,"Measured MS/MS",14)
    line("M1617 280V294",BLUE,1,True)
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
    label(1198,490,"Structural hypotheses",20,True)
    for c,x in zip(CASE["candidates"],(1241,1448)):
        badge(x,521,c["label"])
        asset("candidate_"+c["label"],x+10,505,145,92,"e-output-"+c["label"])
    formula(1310,601,"C28H36N4O4",19,anchor="middle")
    label(1478,601,"(MassSpecGym 0002114)",15,True,anchor="middle")
    label(1275,638,"Separate TRAIN FIT audit",21,True)
    end()


def panel_f():
    title("f",20,754,"Molecular experience sources",19)
    rectangle(15,772,420,19,LIGHT,"none",7)
    label(58,786,"Available data",14,True)
    label(324,786,"Learning pair",14,True)
    names=[["Paired","molecule–spectrum"],["Structure-only"],["Spectrum-only"],["Model-generated"]]
    yy=[811,849,883,918]
    for i,(y,n) in enumerate(zip(yy,names)):
        box(17,y-17,112,30,n,12)
        # Native modality tokens use valid source miniatures without assigning a test compound to TRAIN.
        if i in (0,1,3):
            graph_icon(158,y-3,10,TEAL if i==3 else INK)
        if i in (0,2):
            spectrum(f"f-input-{i}",CASE["experience"]["wake"]["peaks"],181 if i==0 else 148,y-8,35,17)
        if i==0:
            line("M217 809H309",BLUE,1,True)
            graph_icon(332,y-3,9,INK)
            spectrum("f-paired",CASE["experience"]["wake"]["peaks"],355,y-9,38,18)
        elif i==1:
            line("M174 846H190V824H221",TEAL,1,True)
            box(224,805,105,19,["Motif mining"],12,stroke="#A7CEC5",fill="#F2FAF5")
            line("M190 846H221",TEAL,1,True)
            box(224,832,105,31,["Forward Sleep","frozen W"],12.5)
            line("M330 847H340",BLUE,1,True)
            graph_icon(354,y-3,9,INK)
            spectrum("f-sleep",CASE["experience"]["sleep"]["peaks"],376,y-9,35,18,simulated=True)
        elif i==2:
            line("M185 881H218",BLUE,1,True)
            box(223,867,106,31,["Wake / G,W,V","filter"],12.5)
            line("M330 881H340",BLUE,1,True)
            graph_icon(354,y-3,9,INK)
            spectrum("f-wake",CASE["experience"]["wake"]["peaks"],376,y-9,35,18)
            label(365,y+15,"Pseudo-pair",10.5)
        else:
            line("M173 915H218",BLUE,1,True)
            box(223,901,106,31,["Hindsight","frozen W"],12.5)
            line("M330 916H340",BLUE,1,True)
            graph_icon(354,y-3,9,INK)
            spectrum("f-hindsight",CASE["experience"]["hindsight"]["peaks"],376,y-9,35,18,simulated=True)
    end()


def graph_icon(x,y,r,color):
    import math
    vertices=[(x+r*math.cos(i*math.pi/3),y+r*math.sin(i*math.pi/3)) for i in range(6)]
    line("M"+"L".join(f"{a:.2f} {b:.2f}" for a,b in vertices)+"Z",color,.9)


def panel_g():
    title("g",463,754,"Information-guided experience acquisition",19)
    band(483,770,343,"Evidence / scaffold guards")
    label(486,823,"Illustrative signals",8.5,color=SECONDARY)
    for x,lines in [(540,["Entropy"]),(596,["TRAIN","composition"]),(658,["Ring","scarcity"]),(713,["Wake /","Hindsight","priority"]),(772,["Weight"])]:
        for j,s in enumerate(lines):
            label(x,803+j*11,s,10.5,anchor="middle")
    peaks=[CASE["experience"][k]["peaks"] for k in ("wake","sleep","hindsight","wake")]
    weights=[[.4,.65,.5,.25,.47],[.7,.35,.8,.8,.75],[.3,.85,.6,.8,.82],[.6,.45,.25,.35,.4]]
    for i,values in enumerate(weights):
        yy=835+i*16
        graph_icon(482,yy,6,INK)
        spectrum(f"g-spectrum-{i}",peaks[i],496,yy-7,20,11,simulated=i in (1,2))
        for j,value in enumerate(values):
            x=529+j*54
            rectangle(x,yy-6,39,8,"#E1F5EA","none",0)
            rectangle(x,yy-6,39*value,8,"#23BD90" if j==4 else "#86D6B3","none",0)
    for i,s in enumerate(["Weighted","sampling","without","replacement"]):
        label(815,840+i*13,s,11,anchor="middle")
    line("M792 876H838",BLUE,1,True)
    label(877,796,"Selected",12,anchor="middle")
    label(877,810,"experience",12,anchor="middle")
    for i in range(3):
        graph_icon(854,833+i*28,7,INK)
        spectrum(f"g-selected-{i}",peaks[i],868,826+i*28,24,16,simulated=i>0)
    for i,(caption,code) in enumerate([(["Knowledge","expansion"],"c"),(["Generator","learning"],"d"),(["Verifier","learning"],"e")]):
        yy=799+i*47
        box(918,yy,80,37,caption,13,stroke="#A6C8C1",fill="#F2FAF5")
        line(f"M898 {yy+18}H915",TEAL,1,True)
        circle(1013,yy+18,11,TEAL)
        label(1013,yy+22,code,15,True,"white","middle")
    label(555,924,"Paired TRAIN anchors",13)
    line("M707 920H768",BLUE,1,True)
    box(772,907,126,23,"Tool resources",13,stroke="#A6C8C1")
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
    title("h",1046,754,"Scientific Improver Agent",20)
    robot(1072,767)
    rectangle(1059,788,136,92,"white",FAINT,4)
    label(1066,802,"TRAIN FIT",14,True)
    label(1066,817,"training diagnostic subset",10.5)
    for i,s in enumerate(["Absent","Misranked","Motif gaps"]):
        y=839+i*16
        label(1067,y,s,12)
        for j in range(5):
            line(f"M{1152+j*6} {y-1}v{-((j+i)%3+1)*2}",VIOLET,.8)
    box(1201,829,51,27,"Hypothesis",11,stroke="#C7BDCF")
    line("M1192 842H1199",VIOLET,1,True)
    label(1249,796,"Select ONE",14,color=VIOLET)
    box(1256,800,118,42,["Expand knowledge","for retrieval /","score implementation"],11.5,stroke="#C7BDCF",fill="#F9F4FD")
    box(1256,845,118,20,"Improve G",13,stroke="#C7BDCF",fill="#F9F4FD")
    box(1256,868,118,20,"Improve V",13,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1252 842H1254",VIOLET,1,True)
    line("M1247 842V821H1254M1247 842V857H1254M1247 857V883H1254",VIOLET,1,True)
    box(1237,891,138,20,"Tool selection → g",13,stroke="#C7BDCF",fill="#F9F4FD")
    box(1378,750,114,22,"Trial from g",13,bold=True,stroke="#AFBFC8")
    line("M1433 773V783",BLUE,1.1,True)
    label(1390,798,"Paired CAL",15,True)
    label(1378,811,"independent calibration set",10)
    rectangle(1380,816,117,51,"white",FAINT,4)
    line("M1438 816V867",FAINT,.6)
    label(1408,830,"Baseline",12,anchor="middle")
    label(1408,844,"WGV",12,anchor="middle")
    label(1466,830,"Trial",12,anchor="middle")
    label(1466,844,"WGV",12,anchor="middle")
    label(1466,860,"(W frozen)",10,anchor="middle")
    box(1505,815,63,43,["Promotion","gate"],12,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1498 839H1503",BLUE,1,True)
    box(1590,792,71,30,"",12,stroke="#94BEAF",fill="#F7FBF9")
    generation(1625,811,True,15)
    label(1589,787,"Pass",12)
    line("M1569 830H1578V807H1588",TEAL,1.2,True)
    box(1590,846,71,30,"Retain",13)
    label(1575,842,"Fail",12)
    line("M1569 850H1580V860H1588",SECONDARY,1.1,True)
    box(1237,915,138,20,"Collect evidence",13,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1241 858H1229V925H1235",VIOLET,1,True)
    box(1405,902,95,34,["Episode","Memory"],13,stroke="#C7BDCF",fill="#F9F4FD")
    line("M1376 925H1403",VIOLET,1,True)
    line("M1538 859V879H1452V900",VIOLET,1,True,"3 3")
    label(1480,893,"Next hypothesis",13,color=VIOLET)
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
    for c in (INK,BLUE,TEAL,COPPER,VIOLET,SECONDARY):
        add(f'<marker id="head-{c[1:]}" viewBox="0 0 8 6" refX="7" refY="3" markerWidth="5" markerHeight="5" orient="auto">'
            f'<path d="M0 0L8 3L0 6Z" fill="{c}"/></marker>')
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
