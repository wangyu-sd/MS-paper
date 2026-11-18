"""Assemble the 16:9 ORBIT-MS editorial figure as native SVG.

Chemistry and spectra come from the committed
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
W, H = 1600, 900
INK, BLUE, TEAL, COPPER, VIOLET = "#29363D", "#456477", "#44857F", "#BA8150", "#776A86"
FAINT, SECONDARY, LIGHT = "#D7DEE0", "#677680", "#F2F5F4"
PARTS = []
DRAWING_SPECS = []
DISPLAY_POSITIONS = {}


def add(markup):
    PARTS.append(markup)


def group(name):
    add(f'<g id="{name}"><title>{escape(name.replace("-", " "))}</title>')


def end():
    add("</g>")


def label(x, y, value, size=16, bold=False, color=INK, anchor="start", math=False):
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
        f'fill="{color}" font-weight="400" text-anchor="{anchor}">{"".join(spans)}</text>')


def generation(x, y, next_=False, size=14, color=INK, anchor="middle"):
    sub = "t+1" if next_ else "t"
    add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" '
        f'font-size="{size}" font-family="Times New Roman" font-style="italic">'
        f'WGV<tspan baseline-shift="sub" font-size="72%">{sub}</tspan></text>')


def line(points, color=BLUE, width=1.3, arrow=False, dash=None):
    if arrow and color in (BLUE,TEAL,VIOLET):
        width = max(width,1.6)
    marker = f' marker-end="url(#head-{color[1:]})"' if arrow else ""
    role = ' data-role="connector"' if arrow else ''
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{points}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{marker}{dashed}{role}/>')


def circle(x, y, radius, fill, stroke="none", width=1):
    add(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')


def rectangle(x, y, w, h, fill="white", stroke=FAINT, radius=4, width=.8, dash=None):
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{dashed}/>')


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
    # Keep distinct conventional nitrogen and oxygen colors.
    # Atom and bond geometry remains the archived RDKit vector geometry.
    for original, replacement in (("#30373B", INK), ("#2D5B87", "#2450A8"),
                                  ("#9E4433", "#AF4339")):
        artwork = artwork.replace(original, replacement)
    if name+".svg" in MOLECULE_BOUNDS:
        left, top, width, height = MOLECULE_BOUNDS[name+".svg"]
        crop = f"{left-6} {top-6} {width+12} {height+12}"
        artwork = re.sub(r"""viewBox=['"][^'"]+['"]""", f'viewBox="{crop}"', artwork, count=1)
    inline_svg(instance or name, artwork, x, y, w, h)


def oriented_motif(name, smiles, width, height, rotate=180, source=None):
    """Draw the same canonical motif in the reference orientation at its final size."""
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DSVG(width,height)
    opts = drawer.drawOptions()
    opts.clearBackground = False
    opts.padding = .09
    opts.bondLineWidth = 1.5
    opts.fixedFontSize = 17
    opts.rotate = rotate
    rdMolDraw2D.PrepareAndDrawMolecule(drawer,mol)
    drawer.FinishDrawing()
    artwork = drawer.GetDrawingText()
    (ASSETS/(name+'.svg')).write_text(artwork)
    DRAWING_SPECS.append({'asset':name+'.svg','canonical_smiles':Chem.MolToSmiles(mol),
                          'width_px':width,'height_px':height,'rotation_degrees':rotate,
                          'atom_font_px':17,'source':source})
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


def spectrum(name, peaks, x, y, width, height, axes=False, highlight=False, simulated=False):
    """Native SVG spectrum generated from the original m/z and intensity pairs."""
    start = len(PARTS)
    group("spectrum-"+name)
    norm = max(p[1] for p in peaks)
    lower, upper = (65,125) if axes else (min(p[0] for p in peaks)-2,max(p[0] for p in peaks)+2)
    base = y+height
    baseline_color = SECONDARY if axes else TEAL if simulated else COPPER
    line(f"M{x} {base}H{x+width}", baseline_color, .8)
    if axes:
        line(f"M{x} {y}V{base}", SECONDARY, .7)
    ordered = sorted(peaks,key=lambda p:bool(highlight and abs(p[0]-120.0808)<.00001))
    for mz,intensity in ordered:
        xx=x+(mz-lower)/(upper-lower)*width
        color=TEAL if simulated else BLUE if axes else COPPER
        is_base = highlight and abs(mz-120.0808)<.00001
        if is_base:
            color=COPPER
        stick_width = (4.5 if is_base else 6) if axes else (2.5 if is_base else 1.25)
        line(f"M{xx:.3f} {base}V{base-intensity/norm*height:.3f}", color, stick_width)
    if axes:
        for v in (70,90,110):
            xx=x+(v-lower)/(upper-lower)*width
            line(f"M{xx} {base}v4", SECONDARY, .7)
            label(xx,base+20,str(v),16,anchor="middle",math=True)
        label(x-8,y+8,"1",16,anchor="end",math=True)
        label(x-8,base+1,"0",16,anchor="end",math=True)
        label(x+width+2,base+20,"m/z",16,math=True)
    end()
    fragment="\n".join(PARTS[start:])
    # Standalone source shares the same vector commands with the master.
    art = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-20} {y-10} {width+40} {height+50}">{fragment}</svg>'
    (ASSETS/(name+".svg")).write_text(art)


def title(code, x, y, value):
    group("panel-"+code)
    label(x,y,code,25,True)
    label(x+31,y,value,22,True)


def chip(x, y, w, value, color=BLUE, fill="white"):
    rectangle(x,y,w,32,fill,FAINT,4,1)
    label(x+w/2,y+22,value,17,True,color,"middle")


def caption(x,y,value,color=SECONDARY,anchor="start"):
    label(x,y,value,16,color=color,anchor=anchor)


def badge(x,y,value,color=BLUE):
    circle(x,y,11,"white",color,1.3)
    label(x,y+6,value,16,True,color,"middle")


def panel_a():
    title("a",25,33,"Metabolomic dark matter")
    label(25,62,"One MS/MS spectrum, multiple structures",17)
    label(219,87,"120.0808",16,color=COPPER,math=True,anchor="end")
    spectrum("editorial-a",CASE["query"]["peaks"],43,77,230,46,axes=True,highlight=True)
    for candidate,x in zip(CASE["candidates"],(348,463)):
        badge(x,78,candidate["label"])
        asset("candidate_"+candidate["label"],x+8,64,93,77,"context-candidate-"+candidate["label"])
    formula(451,151,"C28H36N4O4",18,anchor="middle")
    end()


def panel_b():
    title("b",620,33,"WGV molecular inference")
    caption(620,61,"World–Generator–Verifier")
    generation(876,61,size=17,color=BLUE)
    chip(620,83,153,"Measured MS/MS",fill=LIGHT)
    chip(786,83,146,"MMA + G")
    chip(958,83,126,"Candidates")
    chip(1110,83,103,"World W")
    chip(1302,83,112,"Verifier V")
    for a,b in ((774,783),(933,955),(1085,1107),(1214,1299),(1416,1440)):
        line(f"M{a} 99H{b}",BLUE,1.8,True)
    label(1448,105,"Hypotheses",19,True)
    line("M691 82V73H1358V81",COPPER,1.5,True)
    for x,code,words in ((858,"c–d","Motifs and graph actions"),(1262,"e","Fragment evidence")):
        caption(x,143,f"{code}  {words}",anchor="middle")
    end()


def panel_c():
    title("c",25,192,"Motif knowledge")
    label(25,226,"Offline mining",19,True,TEAL)
    caption(25,249,"Curated bioactive structures")
    asset("library_parent",29,255,310,118,"editorial-source-molecule")
    line("M60 368V385",TEAL,1.6,True)
    motif_reference("editorial-mined-motif",0,25,387,129,53)
    label(164,406,"Mine substructures",17)
    caption(164,430,"Canonicalize · deduplicate")
    line("M25 449H352",FAINT,1)
    label(25,474,"Online mass-matched retrieval",19,True,TEAL)
    label(26,503,"120.0808",18,True,COPPER,math=True)
    formula(151,503,"C8H10N+",18,anchor="middle")
    line("M103 497H117",TEAL,1.6,True)
    caption(185,503,"Mass / formula lookup")
    for i,pos in enumerate((27,195)):
        motif_reference(f"editorial-retrieved-{i}",i,pos,516,107,43)
        label(pos,580,f'{i+2}  ·  {CASE["mma"]["motifs"][i]["support"]} groups',17,True)
    end()


def overview():
    label(388,224,"Motif knowledge graph",19,True,TEAL)
    caption(776,224,"Archived sample",anchor="end")
    positions = {"1":(719,251),"2":(739,275),"3":(811,247),
                 "4":(706,287),"5":(809,275),"6":(768,301)}
    focus = set(positions)
    for node in KG["nodes"]:
        if node["id"] not in focus:
            x,y = node["xy"]
            positions[node["id"]] = (389+x*.327,241+y*.156)
    DISPLAY_POSITIONS.update(positions)
    rectangle(695,235,131,79,"#F3F8F6",TEAL,5,1.1,"4 4")
    for edge in KG["overview_edges"]:
        u,v = edge["larger"],edge["included"]
        a,b = positions[u]
        c,d = positions[v]
        selected = u in focus and v in focus
        group(f"kg-edge-{u}-{v}")
        line(f"M{a:.2f} {b:.2f}L{c:.2f} {d:.2f}",TEAL if selected else "#D2DDDF",1.5 if selected else .75)
        end()
    for id_,(x,y) in positions.items():
        group(f"kg-node-{id_}")
        circle(x,y,4.4 if id_ in focus else 2.2,TEAL if id_ in focus else "#A5B6B9")
        end()
    line("M711 314L673 330",TEAL,1.05,dash="3 4")
    label(858,224,"Motif–graph correspondence",17,True,TEAL)
    inline_svg("atom-match-example",(ASSETS/"atom-level-alignment.svg").read_text(),850,233,275,62)
    caption(905,314,"Motif",anchor="middle")
    caption(1065,314,"Partial graph",anchor="middle")


def panel_d():
    title("d",388,192,"MMA-guided molecular construction")
    caption(1128,192,"Mass-matched substructure alignment",anchor="end")
    overview()
    label(388,350,"Selected molecular neighborhood",19,True)
    label(388,375,"Substructure containment",16,color=SECONDARY)
    positions={"1":(389,385,128,53),"2":(485,450,112,50),"3":(610,385,114,53),
               "4":(394,450,88,47),"5":(626,452,93,47),"6":(515,523,66,49)}
    routes={("1","2"):"M495 430L516 449",("1","4"):"M439 439V448",
            ("2","6"):"M545 512V523",("4","6"):"M472 502L508 535",
            ("3","5"):"M668 439V449",("5","6"):"M637 507L583 537"}
    for edge in KG["zoom_edges"]:
        line(routes[tuple(edge)],TEAL,1.45,True)
    nodes = {node["id"]:node for node in KG["nodes"]}
    for id_,(x,y,w,h) in positions.items():
        if id_ in {"2","3"}:
            rectangle(x,y,w,h,"#ECF5F1","none",5)
        art=oriented_motif("editorial-neighborhood-"+id_,nodes[id_]["canonical_smiles"],w,h,0,
                           f"motif-topology.json:node[{id_}]")
        inline_svg("editorial-neighborhood-"+id_,art,x,y,w,h)
        if id_ in {"2","3"}:
            badge(x+w-4,y+9,id_,TEAL)
    label(743,350,"Peak-to-motif alignment",19,True,TEAL)
    line("M725 408H737",TEAL,1.6,True)
    rectangle(742,362,386,111,LIGHT,"none",5)
    label(753,385,"Motif graph encoder",17,True)
    line("M924 380H941",BLUE,1.6,True)
    label(947,385,"Peak attention",17,True)
    caption(947,406,"Updates peak memory")
    label(753,412,"Motif atom memory",17)
    caption(753,433,"Optional graph-state input")
    label(753,459,"Shared spectrum / graph backbone",18,True)
    line("M935 474V480",BLUE,1.6,True)
    label(753,499,"Hybrid policy",18,True)
    label(896,499,"Atom / ring / motif actions",17)
    caption(753,522,"Mass and valence constrain graph transitions")
    asset("growth_2",744,528,127,43,"editorial-before-action")
    line("M873 549H925",TEAL,1.6,True)
    asset("growth_3",930,528,197,43,"editorial-after-action")
    caption(744,589,"Motif attachment · reference-conditioned replay")
    end()


def panel_e():
    title("e",1150,192,"Fragment evidence")
    for candidate,x in zip(CASE["candidates"],(1175,1389)):
        badge(x,226,candidate["label"])
        asset("candidate_"+candidate["label"],x+18,214,136,109,"evidence-candidate-"+candidate["label"])
        line(f"M{x+86} 325V338",BLUE,1.7,True)
    label(1150,360,"W  Predicted fragments",19,True,BLUE)
    label(1150,388,"120.0808",18,True,COPPER,math=True)
    caption(1231,388,"shared")
    label(1348,388,"120.0889",18,True,COPPER,math=True)
    caption(1429,388,"A only")
    line("M1536 389V408",BLUE,1.7,True)
    label(1150,424,"V  Match measured MS/MS",19,True,BLUE)
    spectrum("editorial-e",CASE["query"]["peaks"],1404,435,161,26,highlight=True)
    xs=(1237,1331,1425,1519)
    label(1153,463,"m/z",16,math=True)
    for value,x in zip(CASE["evidence"]["peaks"],xs):
        label(x,485,f"{value:.4f}",16,anchor="middle",math=True)
    for i,candidate in enumerate(CASE["candidates"]):
        y=511+i*30
        line(f"M1150 {y-16}H1570",FAINT,1)
        badge(1174,y,candidate["label"])
        for j,(cell,x) in enumerate(zip(candidate["evidence"],xs)):
            present=cell["density"]>0
            color = COPPER if j==3 else BLUE
            circle(x,y,5.7,color if present else "white",color,1.3)
    circle(1155,569,4.2,BLUE)
    caption(1166,574,"Supported")
    circle(1269,569,4.2,"white",BLUE,1.25)
    caption(1280,574,"Unexplained")
    caption(1569,574,"A-only support",COPPER,"end")
    caption(1150,593,"MassSpecGym 0002114")
    label(1569,593,"A/B hypotheses",17,True,BLUE,"end")
    end()


def molecule_symbol(x,y,color=INK):
    line(f"M{x-9} {y}l5 -8h9l5 8l-5 8h-9Z",color,1.5)


def panel_f():
    title("f",25,639,"Molecular experience")
    for i,(name,route) in enumerate((
        ("Paired molecule–spectrum","TRAIN anchors"),
        ("Structure-only","Motif mining / Sleep"),
        ("Spectrum-only","Wake via G/W/V"),
        ("Model-generated","Hindsight via frozen W")
    )):
        y=674+i*55
        if i!=2:
            molecule_symbol(35,y-1,TEAL)
        if i in {0,2}:
            line(f"M51 {y+7}h20m-16 0v-8m5 8v-14m6 14v-5",COPPER,1.6)
        label(83,y+3,name,18,True)
        caption(83,y+24,route)
        if i<3:
            line(f"M25 {y+34}H361",FAINT,.85)
    end()


def panel_g():
    title("g",388,639,"Information-guided acquisition")
    caption(388,664,"Evidence and scaffold filters")
    caption(898,664,"Illustrative weights",anchor="end")
    columns=[(431,("Spectral","entropy")),(525,("Chemical","scarcity")),
             (619,("Ring-system","scarcity")),(713,("Wake /","Hindsight priority")),(807,("Sampling","weight"))]
    for x,words in columns:
        for i,word in enumerate(words):
            label(x,690+18*i,word,16,anchor="middle")
    weights=((.4,.65,.5,.25,.47),(.7,.35,.8,.8,.75),(.3,.85,.6,.8,.82),(.6,.45,.25,.35,.4))
    for i,row in enumerate(weights):
        for j,(value,(x,_)) in enumerate(zip(row,columns)):
            y=723+17*i
            group(f"acquisition-cell-{i}-{j}")
            rectangle(x-31,y,62,11,"#E8EFEC","none",2)
            rectangle(x-31,y,62*value,11,TEAL if j==4 else "#A0C7BD","none",2)
            end()
    label(388,810,"Weighted sampling",18,True)
    caption(565,810,"without replacement")
    line("M389 825H904",FAINT,1)
    line("M757 804H840",TEAL,1.6,True)
    caption(899,810,"Tasks",TEAL,"end")
    for x,code,words in ((389,"c",("Knowledge","expansion")),(565,"d",("Generator","learning")),(732,"e",("Verifier","learning"))):
        badge(x+10,851,code,TEAL)
        for i,word in enumerate(words):
            label(x+29,849+22*i,word,17,True,TEAL)
    end()


def panel_h():
    title("h",927,639,"Scientific improver agent")
    # Single-color robot glyph signals agent actions in this panel.
    rectangle(1516,618,34,23,"white",VIOLET,4,1.4)
    circle(1526,629,2,VIOLET)
    circle(1540,629,2,VIOLET)
    line("M1533 617V611m-5 24h10",VIOLET,1.4)
    label(935,672,"TRAIN FIT failures",18,True,VIOLET)
    caption(935,693,"Absent · misranked")
    caption(935,712,"Motif gaps")
    line("M1081 681H1090",VIOLET,1.7,True)
    label(1101,672,"Scientific",18,True,VIOLET)
    label(1101,693,"hypothesis",18,True,VIOLET)
    line("M1192 681H1222",VIOLET,1.7,True)
    label(1230,672,"Select one intervention",18,True,VIOLET)
    caption(1230,694,"Expand knowledge · Improve G / V")
    caption(1230,717,"Collect evidence → memory")
    line("M1488 689H1504",TEAL,1.7,True)
    label(1511,694,"Tools",17,True,TEAL)
    line("M927 735H1572",FAINT,1)
    label(927,766,"Trial from g",18,True,TEAL)
    caption(927,788,"W frozen")
    line("M1028 759H1042",TEAL,1.7,True)
    label(1051,766,"Paired CAL",18,True,BLUE)
    caption(1051,788,"Trial vs baseline")
    line("M1176 759H1192",BLUE,1.7,True)
    label(1200,766,"Promotion gate",18,True,VIOLET)
    line("M1338 759H1368",VIOLET,1.7,True)
    generation(1409,766,True,20,TEAL)
    caption(1458,766,"or retain current")
    line("M1264 777V818",VIOLET,1.6,True)
    line("M1145 846H921V649H1150V654",VIOLET,1.45,True,"4 4")
    rectangle(1146,818,237,52,"#F5F2F6","none",5)
    label(1160,842,"Episode memory",18,True,VIOLET)
    caption(1160,862,"Outcomes and reflection")
    caption(1406,859,"Promoted update → b",TEAL)
    end()


def main():
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
    for separator in ("M25 164H1574", "M25 605H1574", "M598 20V148",
                      "M371 176V590", "M1139 176V590", "M371 620V876", "M916 620V876"):
        line(separator,FAINT,1)
    panel_a();panel_b();panel_c();panel_d();panel_e();panel_f();panel_g();panel_h()
    add("</svg>")
    result=re.sub(r"[ \t]+$", "", "\n".join(PARTS),flags=re.M)+"\n"
    target=FIG/"orbit_ms_nmi_figure1_vector.svg"
    target.write_text(result)
    (SOURCE/'data/editorial_drawing_specs.json').write_text(json.dumps(DRAWING_SPECS,indent=2)+'\n')
    (SOURCE/'data/editorial_graph_layout.json').write_text(json.dumps({
        'canvas_px':[W,H],'node_positions_px':DISPLAY_POSITIONS,
        'highlight_bounds_px':[695,235,131,79],
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
