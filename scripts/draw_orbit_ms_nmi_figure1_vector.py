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
INK, BLUE, TEAL, COPPER, VIOLET = "#202D35", "#35566B", "#247C74", "#B9753D", "#716284"
FAINT, SECONDARY, LIGHT = "#CCD5D7", "#566972", "#EFF2F2"
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
        f'fill="{color}" font-weight="400" text-anchor="{anchor}">{"".join(spans)}</text>')


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


def title(code,x,y,text):
    group("panel-"+code)
    label(x,y,code,38,True)
    label(x+47,y-2,text,30.5,True)


def badge(x, y, value, radius=14):
    circle(x, y, radius, BLUE)
    label(x, y+7, value, 21, True, "white", "middle")


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
    for original, replacement in (("#30373B", INK), ("#2D5B87", "#284FA6"),
                                  ("#9E4433", "#B4463A")):
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
    opts.padding = .11 if name.startswith("atlas-motif-") else .065
    opts.bondLineWidth = bond_width
    opts.fixedFontSize = font_size
    opts.updateAtomPalette({6:(.13,.18,.21),7:(.16,.31,.65),8:(.70,.27,.22),16:(.52,.38,.04)})
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
            label(x-8,yy+6,str(tick),20,anchor="end")
    for mz,intensity in sorted(peaks):
        xx=x+(mz-lower)/(upper-lower)*width
        yy=base-intensity/intensity_max*height
        color = TEAL if simulated else BLUE if axes else COPPER
        if highlight and abs(mz-120.0808)<.00001:
            color = COPPER
        add(f'<line x1="{xx:.4f}" x2="{xx:.4f}" y1="{base:.4f}" y2="{yy:.4f}" '
            f'data-mz="{mz}" data-intensity="{intensity}" stroke="{color}" '
            f'stroke-width="{1.65 if axes else 1.1}" stroke-linecap="butt"/>')
    line(f"M{x} {y}V{base}H{x+width}",axis,.9 if axes else .7)
    if axes:
        for tick in (70,90,110):
            xx=x+(tick-lower)/(upper-lower)*width
            line(f"M{xx} {base}v3",axis,.85)
            label(xx,base+22,str(tick),20,anchor="middle")
        label(x+width+4,base+22,"m/z",21,math=True)
    end()
    art = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-54} {y-10} {width+70} {height+52}">' + "\n".join(PARTS[start:]) + "</svg>"
    filename = f"spectrum-{name}.svg" if name.startswith("f-") else f"{name}.svg"
    (ASSETS/filename).write_text(art)


def arrow(path, color=BLUE, secondary=False):
    line(path,color,1.55 if secondary else 2.05,"compact" if secondary else True)


def subsection(x,y,text,color=INK):
    label(x,y,text,26.5,True,color)


def panel_a():
    title("a",26,49,"Metabolomic dark matter")
    spectrum("a-measured",CASE["query"]["peaks"],91,80,228,47,axes=True,highlight=True,domain=(65,125))
    label(91,76,"Intensity (%)",21.5,color=SECONDARY)
    label(315,75,"120.0808",20,color=COPPER,anchor="end",math=True)
    for record,x in zip(CASE["candidates"],(356,471)):
        badge(x+5,78,record["label"],12)
        asset("candidate_"+record["label"],x+13,63,92,72,"integrated-a-"+record["label"])
    formula(470,152,"C28H36N4O4",22,anchor="middle")
    end()


def panel_b():
    title("b",604,49,"ORBIT-MS inference")
    generation(1020,48,size=22,color=BLUE)
    label(1641,48,"World–Generator–Verifier",21,color=SECONDARY,anchor="end")
    stages=((616,166,"MS/MS"),(826,150,"G  Generator"),(1023,154,"Candidates"),
            (1224,119,"W  World"),(1377,120,"V  Verifier"))
    for i,(x,w,text) in enumerate(stages):
        if i in (1,3,4):
            rectangle(x,75,w,47,"white","#B1C1C7",5,1.15)
        label(x+w/2,107,text,24,True,BLUE,"middle")
        if i>0:
            old_x,old_w,_=stages[i-1]
            arrow(f"M{old_x+old_w+3} 98.5H{x-4}")
    label(1582,96,"Structural",22,True,BLUE,"middle")
    label(1582,120,"hypotheses",22,True,BLUE,"middle")
    arrow("M1500 98.5H1517")
    arrow("M699 116V145H1437V126",COPPER,True)
    label(898,139,"MMA cues from c/d",21.5,color=TEAL,anchor="middle")
    label(1153,139,"Measured spectrum",21.5,color=COPPER,anchor="middle")
    end()


def panel_c():
    title("c",26,212,"Motif knowledge")
    subsection(27,251,"Offline motif mining",TEAL)
    asset("library_parent",27,260,316,105,"integrated-source-molecule")
    arrow("M119 365V403H183",TEAL,True)
    label(26,431,"Canonicalize",20.5,True,TEAL)
    motif_reference("integrated-mined-motif",0,193,366,143,59)
    line("M26 439H347",FAINT,1)
    subsection(26,468,"Mass-matched retrieval",TEAL)
    label(26,500,"120.0808",24,True,COPPER,math=True)
    arrow("M137 494H172",TEAL,True)
    formula(184,500,"C8H10N+",25)
    motifs=((29,0),(190,1))
    for x,index in motifs:
        motif_reference(f"atlas-retrieved-{index}",index,x,515,138,55)
        support=CASE["mma"]["motifs"][index]["support"]
        label(x+9,590,f"{index+2} · {support} groups",21,True,TEAL)
    label(26,626,"TRAIN + W index",20,color=SECONDARY)
    label(346,626,"2 / 3 → d",21.5,True,TEAL,"end")
    end()


def atlas_overview():
    subsection(378,252,"Motif Knowledge Graph",TEAL)
    focus={"1":(613,272),"2":(635,304),"3":(709,267),
           "4":(600,325),"5":(711,310),"6":(671,337)}
    positions=dict(focus)
    for node in KG["nodes"]:
        if node["id"] not in focus:
            x,y=node["xy"]
            positions[node["id"]]=(379+x*.239,259+y*.188)
    DISPLAY_POSITIONS.update(positions)
    rectangle(590,258,137,91,"#EFF7F5","none",6)
    for edge in KG["overview_edges"]:
        u,v=edge["larger"],edge["included"]
        a,b=positions[u]
        c,d=positions[v]
        active=u in focus and v in focus
        group(f"kg-edge-{u}-{v}")
        line(f"M{a:.2f} {b:.2f}L{c:.2f} {d:.2f}",TEAL if active else "#C6D2D4",1.8 if active else .8)
        end()
    for id_,(x,y) in positions.items():
        group(f"kg-node-{id_}")
        circle(x,y,5 if id_ in focus else 2.25,TEAL if id_ in focus else "#AAB6BB")
        end()
    label(378,363,"Archived sample",21.5,color=SECONDARY)
    line("M605 352L561 366M716 352L729 366",TEAL,1.2,dash="4 4")


def panel_d():
    title("d",377,212,"MMA-guided construction")
    label(1164,209,"Mass-matched substructure alignment",21,color=SECONDARY,anchor="end")
    atlas_overview()
    subsection(378,391,"Substructure containment",TEAL)
    positions={"1":(378,416,114,60),"2":(508,416,112,60),"3":(636,416,112,60),
               "4":(380,509,111,60),"5":(634,509,112,60),"6":(535,563,65,53)}
    paths={("1","2"):"M493 445H505",("1","4"):"M430 479V506",
           ("2","6"):"M563 480V558",("4","6"):"M492 550L533 574",
           ("3","5"):"M691 479V506",("5","6"):"M633 550L602 574"}
    for edge in KG["zoom_edges"]:
        arrow(paths[tuple(edge)],TEAL,True)
    nodes={node["id"]:node for node in KG["nodes"]}
    for id_,(x,y,w,h) in positions.items():
        if id_ in {"2","3"}:
            rectangle(x,y,w,h,"#E8F3F0","none",5)
        svg_id=f"atlas-motif-{id_}"
        art=oriented_motif(svg_id,nodes[id_]["canonical_smiles"],w,h,rotate=0,
                           source=f"motif-topology.json:node[{id_}]",font_size=16,bond_width=1.7)
        inline_svg(svg_id,art,x,y,w,h)
        if id_ in {"2","3"}:
            circle(x+12,y+2,11,TEAL)
            label(x+12,y+9,id_,19,True,"white","middle")
    line("M759 241V625",FAINT,.9)
    subsection(776,251,"Peak-to-Motif Alignment",TEAL)
    # A real measured peak and the two compatible motif inputs meet at attention.
    line("M778 284H824",SECONDARY,.9)
    line("M801 284V261",COPPER,2.3)
    label(832,282,"120.0808",21,color=COPPER,math=True)
    arrow("M918 275H1090V296",COPPER,True)
    for x,value in ((791,"2"),(825,"3")):
        circle(x,314,12,TEAL)
        label(x,321,value,19,True,"white","middle")
    arrow("M843 314H859",TEAL,True)
    label(868,321,"Motif encoder",21.5,True,BLUE)
    arrow("M1014 314H1030",BLUE,True)
    label(1038,321,"Attention",21.5,True,BLUE)
    label(1155,344,"Peak memory",21,color=SECONDARY,anchor="end")
    subsection(776,375,"Motif-to-Graph Alignment",TEAL)
    inline_svg("integrated-atom-correspondence",(ASSETS/"atom-level-alignment.svg").read_text(),776,382,386,68)
    circle(790,461,11,TEAL)
    label(790,468,"2",18,True,"white","middle")
    label(808,468,"Motif Atom Memory",21.5,True,TEAL)
    label(1161,468,"Partial graph",21.5,color=SECONDARY,anchor="end")
    arrow("M1161 337H1169V478H945V484",BLUE,True)
    arrow("M802 472V484",TEAL,True)
    label(778,505,"Shared graph state",21.5,True,BLUE)
    arrow("M981 498H991",BLUE,True)
    label(998,505,"Hybrid policy",21.5,True,BLUE)
    label(778,530,"Atom / ring / motif",21.5)
    label(1159,530,"Mass + valence",21.5,color=SECONDARY,anchor="end")
    asset("growth_2",778,540,144,57,"integrated-partial-action")
    arrow("M928 568H973",TEAL)
    asset("growth_3",981,538,184,61,"integrated-updated-action")
    label(950,607,"mattach",20,True,TEAL,"middle")
    label(778,634,"Reference-conditioned replay",21,color=SECONDARY)
    label(1160,634,"→ e",21.5,True,BLUE,"end")
    end()


def panel_e():
    title("e",1192,212,"Fragment evidence")
    label(1194,246,"G candidates",21.5,True,BLUE)
    label(1642,246,"MassSpecGym 0002114",21,color=SECONDARY,anchor="end")
    for item,x in zip(CASE["candidates"],(1211,1435)):
        badge(x+10,273,item["label"])
        asset("candidate_"+item["label"],x+27,250,145,92,"integrated-e-"+item["label"])
    line("M1307 343V350H1531V343",BLUE,1.55)
    arrow("M1419 350V357",BLUE,True)
    subsection(1194,381,"W   Predicted fragments",BLUE)
    for index,fragment in enumerate(CASE["candidates"][0]["shown_fragments"]):
        x=(1202,1434)[index]
        asset_name=f"integrated-w-fragment-{index}"
        art=oriented_motif(asset_name,fragment["skeleton"],143,49,rotate=180,
                           source=f"w_fragment:A:{index}",font_size=13,bond_width=1.6)
        inline_svg(asset_name,art,x+28,390,143,49)
        label(x,459,f'{fragment["mass"]:.4f}',22,True,COPPER,math=True)
        label(x+90,459,("Shared A/B","A only · weak")[index],21)
    line("M1194 478H1642",FAINT,.9)
    label(1194,511,"V   Match observed MS/MS",23.5,True,BLUE)
    spectrum("e-measured",CASE["query"]["peaks"],1495,490,143,24,highlight=True,domain=(65,125))
    xs=(1273,1382,1491,1600)
    label(1197,543,"m/z",21,math=True)
    for value,x in zip(CASE["evidence"]["peaks"],xs):
        label(x,543,f"{value:.4f}",21,anchor="middle",math=True)
    for i,item in enumerate(CASE["candidates"]):
        y=566+i*30
        line(f"M1194 {y-15}H1642",FAINT,.9)
        label(1200,y+7,item["label"],22,True,BLUE)
        for j,(cell,x) in enumerate(zip(item["evidence"],xs)):
            present=cell["density"]>0
            color=COPPER if j==3 else BLUE
            circle(x,y,6.6,color if present else "white",color,1.4)
    circle(1202,626,5.1,BLUE)
    label(1214,633,"Supported",21,color=SECONDARY)
    circle(1340,626,5.1,"white",BLUE,1.25)
    label(1352,633,"Unexplained",21,color=SECONDARY)
    label(1642,633,"A/B hypotheses",21,True,BLUE,"end")
    end()


def experience_molecule(key,instance,x,y,w,h):
    record=PAIRED_TRAIN if key=="paired" else CASE["experience"][key]
    art=oriented_motif(instance,record["smiles"],w,h,rotate=0,source=f"experience:{key}",
                      font_size=7 if key=="wake" else 9,bond_width=1.2)
    inline_svg(instance,art,x,y,w,h)


def panel_f():
    title("f",26,699,"Molecular experience")
    rows=(("paired","Paired","Measured TRAIN"),
          ("sleep","Structure-only","Sleep · frozen W"),
          ("wake","Spectrum-only","Wake · pseudo-pair"),
          ("hindsight","Model-generated","Hindsight · frozen W"))
    for i,(key,name,route) in enumerate(rows):
        y=740+i*52
        label(28,y,name,22,True)
        label(28,y+25,route,21.5,color=SECONDARY)
        record=PAIRED_TRAIN if key=="paired" else CASE["experience"][key]
        if key=="wake":
            spectrum("f-atlas-wake",record["peaks"],218,y-23,79,34)
            arrow(f"M302 {y-3}H318",BLUE,True)
            experience_molecule(key,"atlas-f-"+key,321,y-25,90,42)
        else:
            experience_molecule(key,"atlas-f-"+key,209,y-25,90,42)
            if key=="paired":
                label(303,y+3,"+",20,color=SECONDARY)
            else:
                arrow(f"M300 {y-3}H319",TEAL,True)
            spectrum("f-atlas-"+key,record["peaks"],323,y-23,88,34,simulated=key!="paired")
        label(424,y+6,str(i+1),21,True,TEAL)
        if i<3:
            line(f"M27 {y+33}H436",FAINT,.9)
    end()


def panel_g():
    title("g",455,699,"Information-guided learning")
    columns=((529,("Spectral","entropy")),(629,("TRAIN","C/N/O")),(729,("Ring","scarcity")),
             (829,("Wake /","Hindsight")),(929,("Sampling","weight")))
    for x,words in columns:
        for i,word in enumerate(words):
            label(x,734+i*23,word,21,anchor="middle")
    weights=((.4,.65,.5,.25,.47),(.7,.35,.8,.8,.75),(.3,.85,.6,.8,.82),(.6,.45,.25,.35,.4))
    for i,row in enumerate(weights):
        y=772+i*23
        label(461,y+12,str(i+1),21,True,TEAL)
        for j,(value,(x,_)) in enumerate(zip(row,columns)):
            group(f"acquisition-cell-{i}-{j}")
            rectangle(x-37,y,74,13,"#E7F0ED","none",2)
            rectangle(x-37,y,74*value,13,TEAL if j==4 else "#77A99F","none",2)
            end()
    label(456,883,"Weighted sampling without replacement",21.5,True)
    label(992,883,"Illustrative",21.5,color=SECONDARY,anchor="end")
    line("M456 895H993",FAINT,1)
    label(456,922,"Expand MMA",21,True,TEAL)
    label(648,922,"Train G",21,True,TEAL)
    label(813,922,"Train V",21,True,TEAL)
    end()


def panel_h():
    title("h",1022,699,"Scientific Improver")
    robot(1606,677)
    label(1027,739,"TRAIN FIT failures",23,True,VIOLET)
    label(1027,764,"Absent / misranked",21)
    label(1027,787,"Motif gaps",21)
    arrow("M1230 731H1247",VIOLET,True)
    label(1255,739,"Hypothesis",23,True,VIOLET)
    arrow("M1378 731H1390",VIOLET,True)
    label(1397,739,"Bounded intervention",23,True,VIOLET)
    label(1397,764,"Expand MMA · improve G/V",20.5)
    label(1397,787,"Collect evidence → memory",20.5)
    line("M1027 800H1642",FAINT,1)
    label(1028,849,"Trial · g",22,True,TEAL)
    label(1028,876,"W frozen",20.5,color=SECONDARY)
    arrow("M1108 842H1123",TEAL,True)
    rectangle(1129,811,235,72,"#EFF2F2","none",4)
    label(1246,835,"Paired CAL",22,True,BLUE,"middle")
    line("M1142 843H1352M1246 848V875",FAINT,1)
    label(1187,869,"Baseline",21.5,anchor="middle")
    label(1306,869,"Trial",21.5,anchor="middle")
    arrow("M1368 845H1388",BLUE,True)
    rectangle(1393,820,104,55,"white",VIOLET,4,1)
    label(1445,843,"Promotion",20,True,VIOLET,"middle")
    label(1445,866,"gate",20,True,VIOLET,"middle")
    line("M1497 845H1511V825",VIOLET,1.6)
    arrow("M1511 825H1527",TEAL,True)
    generation(1572,832,True,23,TEAL)
    label(1618,831,"→ b",20,True,TEAL)
    arrow("M1511 845V867H1527",VIOLET,True)
    label(1536,874,"Retain",21,True,VIOLET)
    arrow("M1445 878V914H1408",VIOLET,True)
    rectangle(1173,895,231,37,"#F2EFF4","none",4)
    label(1288,920,"Episode Memory",22,True,VIOLET,"middle")
    line("M1170 914H1015V709H1307V715",VIOLET,1.45,"compact","4 4")
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
        for size,length,height in (("main",10,8),("compact",7,5.6)):
            add(f'<marker id="head-{color[1:]}-{size}" viewBox="0 0 10 8" refX="10" refY="4" '
                f'markerUnits="userSpaceOnUse" markerWidth="{length}" markerHeight="{height}" orient="auto">'
                f'<path d="M0 0L10 4L0 8L2.4 4Z" fill="{color}"/></marker>')
    add("</defs>")
    rectangle(0,0,W,H,"white","none",0)
    for separator in ("M25 164H1644", "M25 649H1644", "M586 17V148",
                      "M361 181V628", "M1177 181V628", "M445 674V923",
                      "M1008 674V923"):
        line(separator,FAINT,1)
    panel_a();panel_b();panel_c();panel_d();panel_e();panel_f();panel_g();panel_h()
    add("</svg>")
    result=re.sub(r"[ \t]+$", "", "\n".join(PARTS),flags=re.M)+"\n"
    target=FIG/"orbit_ms_nmi_figure1_vector.svg"
    target.write_text(result)
    (SOURCE/'data/reference_drawing_specs.json').write_text(json.dumps(DRAWING_SPECS,indent=2)+'\n')
    (SOURCE/'data/reference_graph_layout.json').write_text(json.dumps({
        'canvas_px':[W,H],'node_positions_px':DISPLAY_POSITIONS,
        'highlight_bounds_px':[590,258,137,91],
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
