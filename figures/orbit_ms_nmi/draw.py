"""Render a vector methods figure from the frozen ORBIT-MS single-case evidence."""
from html import escape
from io import StringIO
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("svg")
from matplotlib import pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
DATA = json.loads((ROOT / "case_manifest.json").read_text())
W, H = 1920, 1080
INK, BLUE = "#30373C", "#435F75"
TEAL, DEEP = "#4E8C89", "#2E615E"
GOLD, PLUM = "#BD8A58", "#796A82"
FAINT, GRAY = "#D9E4E3", "#61717A"
MINT, PAPER, LILAC, CLOUD = "#E7F1EE", "#F4F6F5", "#F0ECF2", "#EDF2F5"
STROKES = {"blue": BLUE, "teal": TEAL, "violet": PLUM, "gold": GOLD}
SVG = []
matplotlib.rcParams.update({"svg.fonttype": "none", "svg.hashsalt": "orbit-ms-nmi",
                            "font.family": "DejaVu Sans"})


def add(markup):
    SVG.append(markup)


def text(x, y, label, size=21, *, fill=INK, bold=False, align="start"):
    weight = "700" if bold else "400"
    add(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{align}">{escape(label)}</text>')


def path(d, stroke=BLUE, width=1.8, dash=None, head=None):
    dash = f' stroke-dasharray="{dash}"' if dash else ""
    marker = f' marker-end="url(#{head})"' if head else ""
    add(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" '
        f'stroke-linejoin="round" stroke-linecap="round"{dash}{marker}/>')


def arrow(d, color="blue", *, width=2.0, dash=None):
    path(d, STROKES[color], width, dash, color)


def rect(x, y, w, h, fill, radius=0):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"/>')


def circle(x, y, r, fill, stroke="none", width=1):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{width}"/>')


def group(key, title):
    add(f'<g id="{key}" role="group" aria-label="{escape(title)}"><title>{escape(title)}</title>')


def end():
    add("</g>")


def panel(letter, x, y, name, color=BLUE):
    group(f"panel-{letter}", name)
    text(x, y, letter, 35, fill=color, bold=True)
    text(x+42, y, name, 29, bold=True)


def role(x, y, code, name, color=BLUE):
    circle(x+15, y-8, 15, color)
    text(x+15, y-1, code, 20, fill="#FFFFFF", bold=True, align="middle")
    text(x+41, y, name, 22, fill=color, bold=True)


def mol(key, smiles, x, y, w, h, *, atoms=(), bonds=None, scale_bond=19, color=(.70,.84,.79)):
    m = Chem.MolFromSmiles(smiles)
    if m is None:
        raise ValueError(f"Invalid molecule {key}: {smiles}")
    Chem.RemoveStereochemistry(m)
    rdDepictor.Compute2DCoords(m)
    k = 3
    drawer = rdMolDraw2D.MolDraw2DSVG(int(w*k), int(h*k))
    opt = drawer.drawOptions()
    opt.clearBackground = False
    opt.padding = .048
    opt.fixedBondLength = scale_bond*k
    opt.bondLineWidth = 4.5
    opt.highlightBondWidthMultiplier = 4
    opt.minFontSize = min(34, int(h*.43))
    opt.maxFontSize = 56
    opt.updateAtomPalette({6:(.19,.216,.235), 7:(.18,.36,.53), 8:(.62,.27,.20)})
    a = sorted(set(atoms))
    if bonds is None:
        bonds = [b.GetIdx() for b in m.GetBonds()
                 if b.GetBeginAtomIdx() in a and b.GetEndAtomIdx() in a]
    rdMolDraw2D.PrepareAndDrawMolecule(
        drawer, m, highlightAtoms=a, highlightBonds=bonds,
        highlightAtomColors={i: color for i in a},
        highlightBondColors={i: color for i in bonds},
        highlightAtomRadii={i:.19 for i in a},
    )
    drawer.FinishDrawing()
    svg = re.sub(r"[ \t]+$", "", drawer.GetDrawingText(), flags=re.M)
    (ASSETS / f"{key}.svg").write_text(svg)
    inner = re.search(r"<svg\b[^>]*>(.*)</svg>", svg, re.S).group(1).strip()
    add(f'<g id="{key}" transform="translate({x} {y}) scale({1/k:.10f})">{inner}</g>')
    return [(x+drawer.GetDrawCoords(i).x/k, y+drawer.GetDrawCoords(i).y/k)
            for i in range(m.GetNumAtoms())]


def plot(key, peaks, x, y, w, h, *, axis=False, highlight=None, color=BLUE):
    """Build a standalone plot SVG, then inline editable vector content."""
    fig = plt.figure(figsize=(w/72, h/72), facecolor="none")
    a = fig.add_axes([.12,.24,.85,.68] if axis else [.02,.12,.96,.82])
    a.set_facecolor("none")
    masses, vals = zip(*peaks)
    norm = max(vals)
    a.vlines(masses, 0, [v/norm for v in vals], color=color, lw=1.7 if axis else 1.2)
    if highlight is not None:
        i = min(range(len(masses)), key=lambda n: abs(masses[n]-highlight))
        a.vlines([masses[i]], 0, [vals[i]/norm], color=GOLD, lw=3.0)
        a.text(masses[i]-1.3,.91,f"{masses[i]:.4f}",ha="right",va="top",
               fontsize=17, color="#805425")
    a.set_ylim(0,1.1)
    if axis:
        a.set_xlim(65,125)
        a.set_xticks([70,80,90,100,110,120]);a.set_yticks([0,1])
        a.tick_params(labelsize=18,width=.75,length=4,colors=GRAY)
        a.set_xlabel("m/z", labelpad=0, fontsize=18, loc="right", color=GRAY)
    else:
        a.set_xticks([]);a.set_yticks([])
        a.spines["left"].set_visible(False)
    a.spines["top"].set_visible(False);a.spines["right"].set_visible(False)
    for s in ("bottom","left"):
        a.spines[s].set_color(GRAY);a.spines[s].set_linewidth(.8)
    stream = StringIO()
    fig.savefig(stream, format="svg", transparent=True, metadata={"Date":None})
    plt.close(fig)
    svg = re.sub(r"[ \t]+$", "", stream.getvalue(), flags=re.M)
    (ASSETS/f"{key}.svg").write_text(svg)
    inner = re.search(r"<svg\b[^>]*>(.*)</svg>", svg, re.S).group(1)
    inner = re.sub(r"<metadata>.*?</metadata>", "", inner, flags=re.S)
    # Matplotlib IDs are namespaced before merging plots.
    names = re.findall(r'\bid="([^"]+)"',inner)
    for name in sorted(set(names), key=len, reverse=True):
        inner = inner.replace(f'id="{name}"', f'id="{key}-{name}"')
        inner = inner.replace(f'#{name}"', f'#{key}-{name}"').replace(f'#{name})',f'#{key}-{name})')
    add(f'<g transform="translate({x} {y})">{inner}</g>')


def first_panel():
    q, mm, states = DATA["query"], DATA["mma"], DATA["construction"]["states"]
    panel("a", 54, 57, "Mass-matched substructure alignment (MMA)", DEEP)
    text(65, 96, "Experimental tandem spectrum", 21, bold=True)
    text(65, 121, "Cyclic tetrapeptide benchmark  ·  [M+H]⁺ 493.2804", 16, fill=GRAY)
    plot("measured_msms", q["peaks"], 62, 123, 355, 138, axis=True, highlight=120.0808)

    rec = DATA["experience"]["fragment_knowledge"]
    text(463, 96, "Fragment knowledge", 21, bold=True, fill=DEEP)
    mol("library_parent", rec["smiles"], 463, 106, 236, 110, scale_bond=15,
        atoms=rec.get("motif_match", ()))
    plot("library_simulated", rec["peaks"], 716, 134, 113, 53, color=TEAL)
    text(466, 237,"Source molecule", 17, fill=GRAY)
    text(711, 215,"W-simulated", 16, fill=GRAY)
    path("M456 107V244", FAINT, 1)
    arrow("M669 232 Q670 257 691 273", "teal")

    # The highlighted mass is the query. Ion and drawable skeletal hypotheses are distinct.
    rect(67, 276, 761, 119, PAPER, 6)
    text(85, 316,"Compatible ion",19,bold=True)
    text(85, 351,"C₈H₁₀N⁺",24,fill=DEEP,bold=True)
    text(85, 378,"m/z 120.0808",17,fill=GRAY)
    arrow("M216 336 H254","teal")
    text(275, 301,"Alternative skeletal motifs",18,bold=True,fill=DEEP)
    for i,o in enumerate(mm["motifs"]):
        x=275+256*i
        mol(f"retrieved_motif_{i+1}",o["motif"],x,305,169,63,scale_bond=18)
        text(x+168,342,f'{o["support"]} groups',17,fill=DEEP)
    text(531, 385,"Support in mined source groups",17,fill=GRAY)
    arrow("M159 260V273","gold")

    text(66, 439,"Atom-level correspondence",22,bold=True)
    text(820,439,"Local structural alignment",16,fill=DEEP,align="end")
    motif=mm["motifs"][0]["motif"]
    matches=mm["alignment"]
    a0=len(SVG)
    left=mol("aligned_motif",motif,71,454,270,119,
             atoms=range(len(matches)),scale_bond=23)
    right=mol("aligned_partial",states[1],412,451,393,124,
              atoms=[i for i,_ in matches],scale_bond=21)
    art=SVG[a0:]
    del SVG[a0:]
    # Route two mapped aromatic atom correspondences through the gap.
    for g,m in [matches[4],matches[6]]:
        x,y=left[m]; u,v=right[g]
        path(f"M{x:.1f} {y:.1f} C365 {y-12:.1f} 379 {v-12:.1f} {u:.1f} {v:.1f}",
             TEAL, 1.25,"4 5")
    SVG.extend(art)
    for g,m in [matches[4],matches[6]]:
        for x,y in (left[m],right[g]):
            circle(round(x,2),round(y,2),3.5,"#FFFFFF",TEAL,1.55)
    text(176,594,"Motif graph",18,align="middle")
    text(607,594,"Growing molecular graph",18,align="middle")
    path("M67 615 H828", FAINT, 1)
    text(66,642,"Motif graph encoder",18,bold=True,fill=DEEP)
    for i in range(6):
        rect(126+i*13,650,9,9,[MINT,MINT,TEAL,MINT,CLOUD,TEAL][i],1)
    arrow("M264 640H291","teal")
    text(302,635,"Peak-to-motif attention",17)
    text(302,665,"Atom alignment + motif memory",17)
    arrow("M529 629H565","teal");arrow("M539 659H565","teal")
    text(576,635,"Peak memory",17,bold=True,fill=DEEP)
    text(576,665,"Graph state",17,bold=True,fill=DEEP)
    path("M711 627H745V657H711",TEAL,1.6)
    arrow("M745 643H821","teal")
    circle(827,643,6,TEAL)
    text(816,625,"Graph action",16,fill=DEEP,align="end")
    text(67,690,"Mass-aware variant: mass and hydrogen-shift features",17,fill=GRAY)
    end()


def second_panel():
    panel("b", 867, 57, "World–Generator–Verifier (WGV)")
    text(1867,55,"Candidate coverage  →  spectral discrimination",18,fill=GRAY,align="end")
    steps=[r["smiles"] for r in DATA["construction"]["shown_replay_states"]]
    circle(878,96,6,TEAL)
    role(892,104,"G","Generator")
    text(1059,103,"MMA-guided graph actions within formula and valence constraints",20)
    x_list=[896,1134,1385,1627]
    for i,(x,st) in enumerate(zip(x_list,steps,strict=True)):
        m=Chem.MolFromSmiles(st)
        old=Chem.MolFromSmiles(steps[i-1]) if i else None
        existing=set(m.GetSubstructMatch(old)) if old else set()
        new=[a.GetIdx() for a in m.GetAtoms() if a.GetIdx() not in existing]
        extra_links=[b.GetIdx() for b in m.GetBonds()
                     if (b.GetBeginAtomIdx() in new) != (b.GetEndAtomIdx() in new)]
        hi=new if i==2 else []
        coat=(.69,.84,.80)
        draw=[b.GetIdx() for b in m.GetBonds()
              if b.GetBeginAtomIdx() in hi and b.GetEndAtomIdx() in hi]
        if i==2: draw+=extra_links
        mol(f"growth_{i+1}",st,x,121,198,105,atoms=hi,bonds=draw,scale_bond=17,color=coat)
        if i<3: arrow(f"M{x+202} 177H{x_list[i+1]-8}")
        text(x+99,251,["Motif start","Add an atom","Attach motif + new bond","Complete cyclic precursor"][i],
             17,fill=BLUE,align="middle")
    text(895,278,"Reference-conditioned action replay",16,fill=GRAY)
    text(1864,278,"Highlighted: one motif attachment",16,fill=DEEP,align="end")
    path("M872 294 H1866", FAINT, 1)
    role(1114,336,"W","Fragmentation World")
    role(1483,336,"V","Verifier")
    text(887,336,"Candidate structures",20,bold=True)
    text(1115,364,"Candidate graph → fragment ions",17,fill=GRAY)
    text(1484,364,"Compare with measured peaks",17,fill=GRAY)
    # The measured input is represented by a second rendering of the same acquired spectrum.
    plot("verifier_observed",DATA["query"]["peaks"],1511,379,267,52,color=GOLD)
    text(1800,413,"Observed",15,fill="#805425")
    arrow("M1644 432 V448","gold")

    candidates=DATA["candidates"]
    evidence_cols=DATA["evidence"]["peaks"]
    for i,c in enumerate(candidates):
        y=[497,593][i]
        text(881,y+5,c["label"],24,fill=BLUE,bold=True)
        mol(f"candidate_{c['label']}",c["smiles"],913,y-43,181,87,
            atoms=c["illustration"]["atoms"], scale_bond=15)
        arrow(f"M1100 {y} H1125")
        for j,f in enumerate(c["shown_fragments"]):
            x=1131+153*j
            if f["skeleton"] is None:
                mol(f"w_fragment_{c['label']}_{j}",c["smiles"],x,y-38,140,61,
                    atoms=f["atoms"],scale_bond=13)
            else:
                mol(f"w_fragment_{c['label']}_{j}",f["skeleton"],x,y-38,140,61,
                    scale_bond=15,color=(.77,.88,.84))
            text(x+70,y+33,f'{f["mass"]:.4f}',16,fill=DEEP if j else BLUE,align="middle")
        arrow(f"M1420 {y} H1443")
    rect(1456,450,407,177,CLOUD,5)
    for j,p in enumerate(evidence_cols):
        x=1510+j*100
        text(x,474,f'{p:.4f}',16,fill="#805425",align="middle")
        path(f"M{x} 484 V619",FAINT,1.15,dash="3 4")
        for i,c in enumerate(candidates):
            y=[497,593][i]
            cell=c["evidence"][j]
            if cell["density"]<=0.0:
                circle(x,y,6.4,"#FFFFFF","#9CACB2",1.2)
            else:
                color=TEAL if cell["stronger"] else "#9BACB3"
                circle(x,y,cell["radius"],color)
    path("M1468 544H1851",FAINT,1)
    text(1460,650,"Shared",16,fill=GRAY);circle(1530,644,5,"#9BACB3")
    text(1560,650,"A-only (weak)",16,fill=DEEP);circle(1674,644,5,TEAL)
    text(1703,650,"Unsupported",16,fill=GRAY);circle(1812,644,6,"#FFFFFF","#9CACB2",1.2)
    text(887,656,"Same elemental formula",18,fill=GRAY)
    text(887,679,"A: rank 1 · B: rank 3",18,fill=BLUE)
    text(1130,656,"W-predicted ion m/z",18,fill=BLUE)
    text(1130,679,"Neutral skeletons shown",16,fill=GRAY)
    text(1456,681,"Ranked hypotheses or a bounded isomer set",19,bold=True,fill=BLUE)
    end()


def learning_panel():
    panel("c",54,746,"Information-guided experience acquisition",DEEP)
    rec=DATA["experience"]
    text(187,787,"Data source",17,fill=GRAY)
    text(494,787,"Model operation",17,fill=GRAY)
    text(713,787,"Learning experience",17,fill=GRAY)
    lanes=[
        ("Sleep","Unpaired molecule","Frozen W","Simulated pair","sleep",TEAL),
        ("Wake","Unlabeled MS/MS","G + W/V gate","Gated pseudo-label","wake",GOLD),
        ("Hindsight","Generated candidate","Frozen W","Counterfactual pair","hindsight",TEAL),
    ]
    for i,(name,source,operation,out,key,color) in enumerate(lanes):
        y=837+i*55
        text(62,y,name,19,bold=True,fill=DEEP)
        record=rec.get(key)
        if key=="wake" and record:
            plot("wake_observed",record["peaks"],186,y-34,75,39,color=GOLD)
        elif record and record.get("smiles"):
            mol(f"{key}_source",record["smiles"],183,y-41,86,49,scale_bond=7)
        text(278,y,source,17)
        arrow(f"M447 {y-7}H480","teal")
        text(493,y,operation,17,bold=True,fill=BLUE)
        arrow(f"M659 {y-7}H688","teal")
        if key in ("sleep","hindsight") and record:
            plot(f"{key}_simulated",record["peaks"],700,y-32,69,37,color=color)
        elif key=="wake" and record and record["smiles"]:
            mol("wake_pseudolabel",record["smiles"],697,y-38,75,46,scale_bond=7)
        text(780,y,out,16)
        path(f"M968 {y-7}H1001",TEAL,1.6)
    path("M1001 830V940",TEAL,1.6)
    arrow("M1001 940V980","teal")
    rect(62,987,952,48,MINT,6)
    text(77,1018,"Select: entropy · scarcity · scaffold diversity · evidence quality",18,fill=DEEP)
    text(999,1018,"Keep real training anchors",17,fill=DEEP,align="end")
    end()


def agent_panel():
    panel("d",1056,746,"Scientific Improver",PLUM)
    x=1065
    text(x,793,"Failure evidence",18,bold=True,fill=PLUM)
    # The two miniature rank readouts are policy illustrations, with no fabricated values.
    for i,(yy,title) in enumerate([(826,"Correct graph absent"),(869,"Correct graph misranked")]):
        for j in range(3):
            circle(x+5+j*19,yy-6,5.1,TEAL if i==1 and j==2 else "#CAD4D9")
        text(x+65,yy,title,17)
    arrow("M1321 838H1357","violet")
    text(1372,792,"Diagnosis → hypothesis",18,bold=True,fill=PLUM)
    text(1372,822,"Choose one intervention",17,fill=INK)
    actions=[
        (1372,851,"Expand knowledge"),(1618,851,"Improve generator"),
        (1372,880,"Improve verifier"),(1618,880,"Collect evidence"),
    ]
    for x0,y,value in actions:
        text(x0,y,value,16,fill=PLUM)
    arrow("M1610 884V920","violet")
    text(1373,912,"Train selected component",16,fill=PLUM)
    arrow("M1759 875H1888","violet",dash="4 4",width=1.4)
    rect(1371,927,498,51,LILAC,5)
    text(1384,949,"Paired evaluation",18,bold=True,fill=PLUM)
    text(1384,970,"Gate promotion on recovery and regressions",16,fill=INK)
    arrow("M1867 951Q1890 951 1890 798H1852","violet",dash="4 5")
    text(1869,914,"Episode memory",16,fill=PLUM,align="end")
    arrow("M1400 979V1011H1364","teal")
    arrow("M1021 1011H1081","teal")
    rect(1088,989,268,45,MINT,5)
    text(1222,1018,"Update MMA / G / V",19,bold=True,fill=DEEP,align="middle")
    text(1866,1022,"W frozen in the controlled episode",15,fill=GRAY,align="end")
    arrow("M1342 792H1349V767H1024V974H1004","violet",dash="4 5",width=1.45)
    rect(1093,756,193,20,"#FFFFFF")
    text(1099,771,"Curriculum proposal",16,fill=PLUM)
    arrow("M1093 991 V984 H1042 V703","teal",width=1.6)
    text(1055,690,"Next model cycle",16,fill=DEEP)
    end()


def main():
    add(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="180mm" height="101.25mm" viewBox="0 0 {W} {H}" '
        'font-family="Arial, Helvetica, sans-serif">')
    add("<title>ORBIT-MS molecular structure elucidation</title>")
    add("<defs>")
    for key,color in STROKES.items():
        add(f'<marker id="{key}" viewBox="0 0 9 8" refX="8" refY="4" markerWidth="6" '
            f'markerHeight="6" orient="auto"><path d="M0 0L9 4L0 8Z" fill="{color}"/></marker>')
    add("</defs>")
    rect(0,0,W,H,"#FFFFFF")
    path("M850 42V678",FAINT,1)
    path("M52 699H1871",FAINT,1.2)
    path("M1033 724V977",FAINT,1)
    first_panel();second_panel();learning_panel();agent_panel()
    add("</svg>")
    master = re.sub(r"[ \t]+$", "", "\n".join(SVG)+"\n", flags=re.M)
    (ROOT/"orbit_ms_nmi_framework.svg").write_text(master)
    ET.parse(ROOT/"orbit_ms_nmi_framework.svg")


if __name__ == "__main__":
    main()
