"""Verify native PDF/SVG content and source chemistry, and render visual comparisons."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import re
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFont
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
    "a":(0,0,586,164),"b":(586,0,1670,164),
    "c":(0,164,361,649),"d":(361,164,1177,649),"e":(1177,164,1670,649),
    "f":(0,649,445,942),"g":(445,649,1008,942),"h":(1008,649,1670,942),
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
    parser.add_argument("--reference", type=Path, default=SOURCE/"revision_reference.png")
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
    locked_assets = {
        "a":("integrated-a-A","integrated-a-B"),
        "c":("integrated-source-molecule","integrated-mined-motif","atlas-retrieved-0","atlas-retrieved-1"),
        "d":(*[f"atlas-motif-{i}" for i in range(1,7)],"integrated-atom-correspondence",
             "integrated-partial-action","integrated-updated-action"),
        "e":("integrated-e-A","integrated-e-B","integrated-w-fragment-0","integrated-w-fragment-1"),
    }
    for panel,required in locked_assets.items():
        group=root.find(f'.//s:g[@id="panel-{panel}"]',NS)
        panel_ids={item.get("id") for item in group.iter()}
        assert set(required)<=panel_ids,(panel,set(required)-panel_ids)
    counts = Counter(e.tag.rsplit("}", 1)[-1] for e in all_elements)
    assert counts["text"] > 85 and counts["path"] > 500 and counts["circle"] >= 91

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
    assert abs(page.rect.width/page.rect.height - 1670/942) < 0.000001

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

    paired = json.loads((SOURCE/"data/paired_training_example.json").read_text())
    assert paired["fold"]=="train" and len(paired["peaks"])==20
    spectrum_sources = {
        "a-measured":case["query"], "e-measured":case["query"],
        "f-atlas-paired":paired, "f-atlas-sleep":case["experience"]["sleep"],
        "f-atlas-wake":case["experience"]["wake"],
        "f-atlas-hindsight":case["experience"]["hindsight"],
    }
    for name,record in spectrum_sources.items():
        plot=root.find(f'.//s:g[@id="spectrum-{name}"]',NS)
        assert plot is not None,name
        sticks=plot.findall("s:line",NS)
        observed=[(float(stick.get("data-mz")),float(stick.get("data-intensity"))) for stick in sticks]
        expected=sorted(map(tuple,record["peaks"]))
        assert observed==expected,name
        heights=[float(stick.get("y1"))-float(stick.get("y2")) for stick in sticks]
        peak_max=max(intensity for _,intensity in expected)
        for height,(_,intensity) in zip(heights,expected):
            assert abs(height/max(heights)-intensity/peak_max)<.0001,name

    drawing_specs = json.loads((SOURCE/'data/reference_drawing_specs.json').read_text())
    for spec in drawing_specs:
        assert Chem.MolFromSmiles(spec['canonical_smiles']) is not None
        art = ET.parse(SOURCE/'assets'/spec['asset']).getroot()
        assert not art.findall('.//s:image',NS)
        if spec["source"].startswith("experience:"):
            assert any("bond-" in item.get("class","") for item in art.iter()),spec["asset"]
            key=spec["source"].split(":")[1]
            record=paired if key=="paired" else case["experience"][key]
            expected=Chem.MolToSmiles(Chem.MolFromSmiles(record["smiles"]))
        elif spec["source"].startswith("w_fragment:"):
            _,candidate,index=spec["source"].split(":")
            entry=next(item for item in case["candidates"] if item["label"]==candidate)
            expected=Chem.MolToSmiles(Chem.MolFromSmiles(entry["shown_fragments"][int(index)]["skeleton"]))
        elif spec['source'].startswith('case_manifest'):
            index = int(spec['source'].split('[')[1].split(']')[0])
            expected = Chem.MolToSmiles(Chem.MolFromSmiles(case['mma']['motifs'][index]['motif']))
        else:
            node_id = spec['source'].split('[')[1].split(']')[0]
            expected = Chem.MolToSmiles(nodes[node_id])
        assert spec['canonical_smiles'] == expected
    display = json.loads((SOURCE/'data/reference_graph_layout.json').read_text())
    assert set(display['node_positions_px']) == set(nodes)

    bounds = json.loads((VERIFY/"text-bounds.json").read_text())
    clipped = [v["text"] for v in bounds if v["left"] < -.5 or v["right"] > 1670.5 or
               v["top"] < -.5 or v["bottom"] > 942.5]
    overlaps = []
    for i, left in enumerate(bounds):
        for right in bounds[i+1:]:
            dx = min(left["right"], right["right"]) - max(left["left"], right["left"])
            dy = min(left["bottom"], right["bottom"]) - max(left["top"], right["top"])
            if dx > 3 and dy > 2:
                overlaps.append([left["text"], right["text"]])
    panel_overflow = []
    for item in bounds:
        if not item["panel"]:
            continue
        x0,y0,x1,y1=PANELS[item["panel"][-1]]
        if item["left"]<x0 or item["right"]>x1 or item["top"]<y0 or item["bottom"]>y1:
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
    run_poppler(args.poppler_dir, "pdftoppm", "-png", "-singlefile", "-scale-to-x", "1670",
                "-scale-to-y", "942", pdf_path, VERIFY/"render-reference-size")
    source = Image.open(args.reference).convert("RGB")
    rendered = Image.open(VERIFY/"render-reference-size.png").convert("RGB")
    assert source.size == rendered.size == (1670, 942)
    source_arr, rendered_arr = np.asarray(source, dtype=np.int16), np.asarray(rendered, dtype=np.int16)
    error = abs(source_arr-rendered_arr)
    pixel_error = np.any(error != 0, axis=2)
    Image.blend(source, rendered, .5).save(VERIFY/"overlay.png")
    diff = ImageEnhance.Contrast(ImageChops.difference(source, rendered)).enhance(3)
    diff.save(VERIFY/"difference-x3.png")
    rendered.resize((709, 400), Image.Resampling.LANCZOS).save(VERIFY/"review-180mm-100dpi.png")
    # Side-by-side crop sheets retain original pixel coordinates, with both sides at the same scale.
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
    for letter, xy in PANELS.items():
        old, new = source.crop(xy), rendered.crop(xy)
        sheet = Image.new("RGB", (old.width*2+24, old.height+32), "white")
        draw = ImageDraw.Draw(sheet)
        draw.text((0,2), f"{letter} · selected PNG", fill="#29363D", font=font)
        draw.text((old.width+24,2), f"{letter} · native vector render", fill="#29363D", font=font)
        sheet.paste(old,(0,32)); sheet.paste(new,(old.width+24,32))
        sheet.save(VERIFY/f"panel-{letter}-comparison.png")

    previous_path = VERIFY/"previous-iteration-render.png"
    if not previous_path.exists():
        previous_path = VERIFY/"previous-vector-render.png"
    revision = {}
    if previous_path.exists():
        previous = Image.open(previous_path).convert("RGB")
        assert previous.size == source.size
        for letter, xy in PANELS.items():
            crops = [im.crop(xy) for im in (source, previous, rendered)]
            width,height = crops[0].size
            sheet = Image.new("RGB",(3*width+48,height+32),"white")
            draw = ImageDraw.Draw(sheet)
            for i,(im,caption) in enumerate(zip(crops,("Reference","Previous vector","Refined vector"))):
                xx = i*(width+24)
                sheet.paste(im,(xx,32))
                draw.text((xx,2),caption,fill="#101214",font=font)
            sheet.save(VERIFY/f"three-way-{letter}.png")
            reference_array = np.asarray(crops[0],dtype=np.int16)
            revision[letter] = {
                "previous_mae":float(abs(reference_array-np.asarray(crops[1],dtype=np.int16)).mean()),
                "refined_mae":float(abs(reference_array-np.asarray(crops[2],dtype=np.int16)).mean()),
            }
        (VERIFY/"revision-comparison.json").write_text(json.dumps(revision,indent=2)+"\n")

    spans = [span for b in page.get_text("dict")["blocks"] if b["type"] == 0
             for line in b["lines"] for span in line["spans"]]
    statistics = {
        "label_words": len(re.findall(r"[A-Za-z]+(?:[-–][A-Za-z]+)*",text)),
        "pdf_pages": len(document), "page_points": list(page.rect), "page_mm": [page.rect.width*25.4/72,page.rect.height*25.4/72],
        "pdf_image_count": 0, "pdf_path_objects": len(page.get_drawings()), "pdf_text_characters": len(text),
        "font_families": families, "embedded_font_records": len(page.get_fonts(full=True)),
        "svg_objects": dict(counts), "source_png": str(args.reference), "source_sha256":digest(args.reference),
        "reference_pixels": list(source.size), "changed_pixel_fraction": float(pixel_error.mean()),
        "mean_absolute_channel_error_0_255": float(error.mean()), "max_channel_error": int(error.max()),
        "native_text_clipped": clipped, "native_text_overlaps": overlaps,
        "connector_text_crossings":connector_crossings,
        "minimum_pdf_type_points": min(s["size"] for s in spans),
        "body_13_svg_pixels_in_pdf_points": 13*180*72/25.4/1670,
        "kg_nodes": len(nodes), "verified_kg_edges": len(edges),
        "pdf_sha256": digest(pdf_path), "svg_sha256":digest(svg_path),
        "note": "Differences include scientific replacements of malformed generated molecules and native font/rasterization differences; pixel equality is not expected."
    }
    (VERIFY/"statistics.json").write_text(json.dumps(statistics, indent=2)+"\n")
    index_path = SOURCE/"source_index.json"
    index = json.loads(index_path.read_text())
    index["comparison_reference_png"] = args.reference.name
    index["comparison_reference_sha256"] = digest(args.reference)
    index['assets'] = [{'file':str(path.relative_to(SOURCE)),'sha256':digest(path),
                        'representation':'native SVG paths and/or text'}
                       for path in sorted((SOURCE/'assets').glob('*.svg'))]
    index_path.write_text(json.dumps(index,indent=2)+"\n")
    print(json.dumps(statistics,indent=2))


if __name__ == "__main__":
    main()
