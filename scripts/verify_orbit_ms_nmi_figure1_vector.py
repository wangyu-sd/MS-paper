"""Verify native PDF/SVG content and source chemistry, and render visual comparisons."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

import re
from PIL import Image, ImageDraw, ImageFont
import pymupdf
from rdkit import Chem
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
SOURCE = FIG / "orbit_ms_nmi_figure1_sources"
VERIFY = SOURCE / "verification"
STEM = FIG / "orbit_ms_nmi_figure1_vector"
NS = {"s": "http://www.w3.org/2000/svg"}
PANELS = {
    "a": (0, 0, 598, 164), "b": (598, 0, 1600, 164),
    "c": (0, 164, 371, 605), "d": (371, 164, 1139, 605), "e": (1139, 164, 1600, 605),
    "f": (0, 605, 371, 900), "g": (371, 605, 916, 900), "h": (916, 605, 1600, 900),
}


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def run_poppler(binary_dir, name, *args):
    tool = str(Path(binary_dir) / name) if binary_dir else name
    result = subprocess.run([tool, *map(str, args)], check=True, capture_output=True, text=True)
    (VERIFY / (name+".txt")).write_text(result.stdout)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--poppler-dir")
    parser.add_argument("--before-pdf", type=Path, help="Previous Figure 1 PDF for a same-width comparison")
    args = parser.parse_args()
    VERIFY.mkdir(exist_ok=True)
    svg_path = STEM.with_suffix(".svg")
    pdf_path = STEM.with_suffix(".pdf")
    tree = ET.parse(svg_path)
    root = tree.getroot()
    assert not root.findall(".//s:image", NS)
    assert not root.findall(".//s:foreignObject", NS)
    all_elements = list(root.iter())
    ids = [e.attrib["id"] for e in all_elements if "id" in e.attrib]
    assert len(ids) == len(set(ids))
    for letter in PANELS:
        assert "panel-"+letter in ids
    counts = Counter(e.tag.rsplit("}", 1)[-1] for e in all_elements)
    assert counts["text"] > 75 and counts["path"] > 500 and counts["circle"] >= 91

    document = pymupdf.open(pdf_path)
    assert len(document) == 1
    page = document[0]
    assert not page.get_images(full=True)
    assert len(page.get_drawings()) > 1000
    text = page.get_text()
    for needle in ("Metabolomic dark matter", "Promotion", "MMA", "Substructure", "TRAIN"):
        assert needle in text, needle
    families = sorted({span["font"] for b in page.get_text("dict")["blocks"] if b["type"] == 0
                       for line in b["lines"] for span in line["spans"]})
    assert all("Arial" in family or "TimesNewRoman" in family for family in families), families
    assert abs(page.rect.width/page.rect.height - 16/9) < 0.000001

    case = json.loads((SOURCE / "data/case_manifest.json").read_text())
    a, b = [Chem.MolFromSmiles(c["smiles"]) for c in case["candidates"]]
    assert CalcMolFormula(a) == CalcMolFormula(b) == "C28H36N4O4"
    assert Chem.MolToSmiles(a) != Chem.MolToSmiles(b)
    assert case["evidence"]["peaks"] == [72.0816, 90.9773, 120.0808, 120.0893]
    assert case["candidates"][0]["evidence"][3]["density"] > 0
    assert case["candidates"][1]["evidence"][3]["density"] == 0
    assert all(c["evidence"][1]["density"] == 0 for c in case["candidates"])
    for candidate in case["candidates"]:
        for f in candidate["shown_fragments"]:
            assert Chem.MolFromSmiles(f["skeleton"]) is not None
    mol = Chem.MolFromSmiles(case["mma"]["motifs"][0]["motif"])
    partial = Chem.MolFromSmiles(case["construction"]["states"][1])
    matches = case["mma"]["alignment"]
    for graph_atom, motif_atom in matches:
        assert partial.GetAtomWithIdx(graph_atom).GetAtomicNum() == mol.GetAtomWithIdx(motif_atom).GetAtomicNum()
    for bond in mol.GetBonds():
        mapping = {motif_atom: graph_atom for graph_atom, motif_atom in matches}
        corresponding = partial.GetBondBetweenAtoms(mapping[bond.GetBeginAtomIdx()], mapping[bond.GetEndAtomIdx()])
        assert corresponding and corresponding.GetBondType() == bond.GetBondType()
    before, after = [Chem.MolFromSmiles(state["smiles"]) for state in case["construction"]["shown_replay_states"][1:3]]
    assert after.HasSubstructMatch(before)
    assert after.GetNumHeavyAtoms()-before.GetNumHeavyAtoms() == 9

    kg = json.loads((SOURCE / "data/motif-topology.json").read_text())
    nodes = {n["id"]: Chem.MolFromSmiles(n["canonical_smiles"]) for n in kg["nodes"]}
    assert all(nodes.values())
    edges = {(e["larger"], e["included"]) for e in kg["overview_edges"]}
    assert set(map(tuple, kg["zoom_edges"])) <= edges
    for u, v in edges:
        assert nodes[u].GetNumAtoms() > nodes[v].GetNumAtoms()
        assert nodes[u].HasSubstructMatch(nodes[v])
    assert set(kg["focus_ids"]) == set("123456")
    assert nodes["3"].HasSubstructMatch(nodes["5"])
    assert nodes["5"].HasSubstructMatch(nodes["6"])

    drawing_specs = json.loads((SOURCE/'data/editorial_drawing_specs.json').read_text())
    for spec in drawing_specs:
        assert Chem.MolFromSmiles(spec['canonical_smiles']) is not None
        art = ET.parse(SOURCE/'assets'/spec['asset']).getroot()
        assert not art.findall('.//s:image',NS)
        if spec['source'].startswith('case_manifest'):
            index = int(spec['source'].split('[')[1].split(']')[0])
            expected = Chem.MolToSmiles(Chem.MolFromSmiles(case['mma']['motifs'][index]['motif']))
        else:
            node_id = spec['source'].split('[')[1].split(']')[0]
            expected = Chem.MolToSmiles(nodes[node_id])
        assert spec['canonical_smiles'] == expected
    display = json.loads((SOURCE/'data/editorial_graph_layout.json').read_text())
    assert set(display['node_positions_px']) == set(nodes)

    bounds = json.loads((VERIFY/"text-bounds.json").read_text())
    clipped = [v["text"] for v in bounds if v["left"] < -.5 or v["right"] > 1600.5 or
               v["top"] < -.5 or v["bottom"] > 900.5]
    overlaps = []
    for i, left in enumerate(bounds):
        for right in bounds[i+1:]:
            dx = min(left["right"], right["right"]) - max(left["left"], right["left"])
            dy = min(left["bottom"], right["bottom"]) - max(left["top"], right["top"])
            if dx > 3 and dy > 2:
                overlaps.append([left["text"], right["text"]])
    panel_overflow = []
    for item in bounds:
        x0,y0,x1,y1 = PANELS[item["panel"][-1]]
        if (item["left"] < x0 or item["right"] > x1 or
                item["top"] < y0 or item["bottom"] > y1):
            panel_overflow.append(item["text"])
    assert not panel_overflow, panel_overflow
    assert not clipped, clipped
    assert not overlaps, overlaps
    connector_crossings = json.loads((VERIFY/'connector-crossings.json').read_text())
    assert not connector_crossings, connector_crossings

    image_list = run_poppler(args.poppler_dir, "pdfimages", "-list", pdf_path)
    assert not any(line.strip().startswith("1 ") for line in image_list.splitlines())
    fonts = run_poppler(args.poppler_dir, "pdffonts", pdf_path)
    assert "Arial" in fonts and "TimesNewRoman" in fonts
    run_poppler(args.poppler_dir, "pdfinfo", pdf_path)
    preview = FIG/"orbit_ms_nmi_figure1_vector_preview"
    run_poppler(args.poppler_dir,"pdftoppm","-png","-singlefile","-scale-to-x","3200",
                "-scale-to-y","1800",pdf_path,preview)
    run_poppler(args.poppler_dir,"pdftoppm","-png","-singlefile","-r","150",
                pdf_path,VERIFY/"review-180mm-150dpi")
    if args.before_pdf:
        with pymupdf.open(args.before_pdf) as before:
            before_text = before[0].get_text()
            pix = before[0].get_pixmap(matrix=pymupdf.Matrix(3,3),alpha=False)
            image_before = Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
        image_after = Image.open(preview.with_suffix(".png")).convert("RGB")
        width = 1440
        images = [im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
                  for im in (image_before,image_after)]
        comparison = Image.new("RGB",(width, sum(im.height for im in images)+100),"#F2F5F4")
        painter = ImageDraw.Draw(comparison)
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf",25)
        y = 0
        for title,im in zip(("Before","Editorial redesign"),images):
            painter.text((24,y+10),title,fill="#29363D",font=font)
            comparison.paste(im,(0,y+50))
            y += im.height+50
        comparison.save(FIG/"orbit_ms_nmi_figure1_before_after.png")
    else:
        before_text = ""

    spans = [span for b in page.get_text("dict")["blocks"] if b["type"] == 0
             for line in b["lines"] for span in line["spans"]]
    statistics = {
        "pdf_pages": len(document), "page_points": list(page.rect), "page_mm": [page.rect.width*25.4/72,page.rect.height*25.4/72],
        "pdf_image_count": 0, "pdf_path_objects": len(page.get_drawings()), "pdf_text_characters": len(text),
        "font_families": families, "embedded_font_records": len(page.get_fonts(full=True)),
        "svg_objects": dict(counts), "panel_text_overflow": panel_overflow,
        "label_words": len(re.findall(r"[A-Za-z]+(?:[-–][A-Za-z]+)*",text)),
        "previous_label_words": len(re.findall(r"[A-Za-z]+(?:[-–][A-Za-z]+)*",before_text)) or None,
        "native_text_clipped": clipped, "native_text_overlaps": overlaps,
        "connector_text_crossings":connector_crossings,
        "minimum_pdf_type_points": min(s["size"] for s in spans),
        "standard_annotation_points": 16*180*72/25.4/1600,
        "kg_nodes": len(nodes), "verified_kg_edges": len(edges),
        "pdf_sha256": digest(pdf_path), "svg_sha256":digest(svg_path),
        "note": "Editorial redesign at 180 mm physical page width."
    }
    (VERIFY/"statistics.json").write_text(json.dumps(statistics, indent=2)+"\n")
    index_path = SOURCE/"source_index.json"
    index = json.loads(index_path.read_text())
    index['assets'] = [{'file':str(path.relative_to(SOURCE)),'sha256':digest(path),
                        'representation':'native SVG paths and/or text'}
                       for path in sorted((SOURCE/'assets').glob('*.svg'))]
    index_path.write_text(json.dumps(index,indent=2)+"\n")
    print(json.dumps(statistics,indent=2))


if __name__ == "__main__":
    main()
