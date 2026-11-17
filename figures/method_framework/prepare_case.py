"""Extract the illustrated case from a pinned MassSpecGym release and PR95 tree."""
import argparse
import ast
from collections import Counter
import csv
from dataclasses import asdict
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import networkx as nx
from rdkit import Chem, rdBase
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

HERE = Path(__file__).resolve().parent
CASE = "MassSpecGymID0002114"
PR95 = "97444cc648f318e0eb2e0fbbce5fecc3cbc6e43d"
PR96 = "c63c32ce24b29d959164c2b081e511b25641a1c4"
PR13 = "b53a2b9351597312e41f773df2459df194441aa8"
DATA = "https://huggingface.co/datasets/roman-bushuiev/MassSpecGym/resolve/1b6d1ec/data/MassSpecGym.tsv"
DATA_SHA = "0c9cc50450def3f0d4fe2dc09dea1105fc15e635db8c6656bc3e3be37a3bcd95"
PRIOR = "src/orbit_ms/wgv/peak_fragment_prior.py"
TRACE = "scripts/plot_pr93_paper_figures.py"
CANDIDATES = "scripts/plot_pr93_gen7_reasoning_trajectories.py"
PR95_FILES = [
    PRIOR, TRACE, CANDIDATES,
    "src/orbit_ms/wgv/cocograph_v4_peak_msa.py",
    "src/orbit_ms/wgv/peak_ladder_motif.py",
    "src/orbit_ms/wgv/peak_ladder_scaffold.py",
    "src/orbit_ms/wgv/v_set_mma.py",
    "scripts/build_pr93_unlabeled_gems_rsi_cycle.py",
    "scripts/run_pr93_autonomous_rsi.py",
]
PR96_FILES = [
    "src/orbit_ms/agents/scientific_improver.py",
    "scripts/run_pr93_scientific_improver.py",
    "docs/results/PR96_SCIENTIFIC_RSI_CLUSTER_REPRO.md",
]


def source(repo, commit, path):
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{commit}:{path}"])


def literal_case(code):
    for node in ast.walk(ast.parse(code)):
        if not isinstance(node, ast.Dict):
            continue
        try:
            value = ast.literal_eval(node)
        except (ValueError, TypeError):
            continue
        if value.get("cid") == CASE:
            return value, node.lineno
    raise LookupError(CASE)


def molecule(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    return mol


def descriptor(smiles):
    mol = molecule(smiles)
    return {
        "smiles": smiles, "formula": CalcMolFormula(mol),
        "inchikey14": Chem.MolToInchiKey(mol).split("-")[0],
    }


def compute_mma(code, motif, partial, ion_formula, index):
    """Evaluate graph encoding and structural correspondence, not learned scores."""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "peak_fragment_prior.py"
        path.write_bytes(code)
        spec = spec_from_file_location("peak_fragment_prior", path)
        mma = module_from_spec(spec)
        sys.modules[spec.name] = mma
        spec.loader.exec_module(mma)

    precursor = Chem.Mol(molecule(partial))
    Chem.Kekulize(precursor, clearAromaticFlags=True)
    graph = nx.MultiGraph()
    for atom in precursor.GetAtoms():
        graph.add_node(atom.GetIdx(), label=atom.GetSymbol())
    for bond in precursor.GetBonds():
        for _ in range(int(bond.GetBondTypeAsDouble())):
            graph.add_edge(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx())
    nodes = list(graph.nodes)
    units = [(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), 0) for bond in precursor.GetBonds()]
    # Unit weights isolate the structural match. They are not library support or priors.
    hypothesis = mma.PeakFragmentHypothesis(index, 0, motif, ion_formula, 1, 1.0, 1.0)
    features = mma.template_features(graph, nodes, units, [hypothesis], {index: 0})
    if not features["sanitized"] or not features["alignment"].size:
        raise ValueError("The source motif must match the source partial graph.")
    return {
        "ion_exact_mz": mma._ion_mass(ion_formula),
        "motif_graph": {key: value.tolist() for key, value in mma.motif_graph(motif).items()},
        "alignment": features["alignment"].tolist(),
        "bond_units": [list(unit[:2]) for unit in units],
        "matched_internal_bonds": [i for i, row in enumerate(features["unit"]) if row[0]],
        "matched_boundary_bonds": [i for i, row in enumerate(features["unit"]) if row[1]],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("massspecgym", type=Path)
    parser.add_argument("orbit_ms_checkout", type=Path)
    args = parser.parse_args()
    with args.massspecgym.open("rb") as stream:
        if sha256_iter(stream) != DATA_SHA:
            raise ValueError("Unexpected MassSpecGym TSV digest")
        stream.seek(0)
        lines = io.TextIOWrapper(stream, encoding="utf-8", newline="")
        header = next(lines)
        row_text = next(line for line in lines if line.startswith(CASE + "\t"))
    row = next(csv.DictReader([header, row_text], delimiter="\t"))
    peaks = list(zip(map(float, row["mzs"].split(",")), map(float, row["intensities"].split(",")), strict=True))
    sources = {
        path: (commit, source(args.orbit_ms_checkout, commit, path))
        for commit, paths in [(PR95, PR95_FILES), (PR96, PR96_FILES)]
        for path in paths
    }
    trace, trace_line = literal_case(sources[TRACE][1])
    candidates, candidate_line = literal_case(sources[CANDIDATES][1])
    structures = {key: descriptor(candidates[f"{key}_smi"]) for key in ("c1", "c3")}
    assert structures["c1"]["formula"] == structures["c3"]["formula"] == row["formula"]
    assert structures["c1"]["inchikey14"] != structures["c3"]["inchikey14"] == row["inchikey"]
    states = [
        {**descriptor(smiles), "source_label": label, "source_highlight_smiles": highlight}
        for label, smiles, highlight in trace["steps"]
    ]
    motif = states[0]["smiles"]
    peak_index = [m for m, _ in peaks].index(120.0808)
    ion_formula = "C8H10N"
    mma = compute_mma(sources[PRIOR][1], motif, states[1]["smiles"], ion_formula, peak_index)
    delta = peaks[peak_index][0] - mma["ion_exact_mz"]
    assert abs(delta) < .005
    manifest = {
        "design_pr": {"url": "https://github.com/wangyu-sd/MS-paper/pull/13", "head": PR13},
        "code_pr_heads": {"95": PR95, "96": PR96},
        "code_sources": {
            p: {"url": f"https://github.com/wangyu-sd/orbit-ms/blob/{commit}/{p}",
                "sha256": sha256(content).hexdigest()}
            for p, (commit, content) in sources.items()
        },
        "query": {
            "id": CASE, "dataset": "MassSpecGym", "split": row["fold"],
            "dataset_url": DATA, "dataset_sha256": DATA_SHA,
            "tsv_row_sha256": sha256(row_text.encode()).hexdigest(),
            "instrument_type": row["instrument_type"], "collision_energy_as_reported": row["collision_energy"],
            "adduct": row["adduct"], "precursor_mz": float(row["precursor_mz"]),
            "reference_formula": row["formula"], "reference_smiles": row["smiles"],
            "reference_inchikey14": row["inchikey"], "peaks": peaks,
        },
        "candidates": {
            "source": CANDIDATES, "source_line": candidate_line,
            "M1": {**structures["c1"], "role": "source-depicted first-round G candidate"},
            "M2": {**structures["c3"], "role": "source-depicted second-round local refinement; reference connectivity"},
            "scope": "Same-formula structures from a historical refinement example. This pair is not a logged fixed candidate pool or a direct G versus W/V rerank.",
        },
        "source_depicted_g_states": {
            "source": TRACE, "source_line": trace_line, "states": states,
            "scope": "RDKit structures transcribed from the upstream Fig. 9 drawing script. This is a documented construction illustration, not a saved checkpoint rollout or a trace for M1. No checkpoint hash or raw per-step action receipt was available.",
        },
        "mma_alignment": {
            "status": "Code replay of motif_graph/template_features on the published motif/partial-graph pair. Correspondence indices are real; no learned activations, retrieval scores, or execution claims.",
            "peak_index": peak_index, "observed_mz": peaks[peak_index][0], "mass_error_da": delta,
            "ion_formula": ion_formula + "+", "motif": descriptor(motif),
            "mass_scope": "Calculated composition compatible with the measured peak. The neutral motif SMILES is the source-depicted graph and its formula differs from the ion formula. The source does not provide this query's peak-to-motif retrieval receipt.",
            "support_prior": None, "alternate_motifs": None, **mma,
        },
        "unset_assets": {
            "b1": "TRAIN/W mined precursor-fragment linkage, supporting source groups.",
            "b2": "Actual top-K candidate list and per-candidate support, prior and peak weight.",
            "c": "Original checkpoint rollout and same-query candidate-wise W structural-ion receipts, V per-peak matches and fixed-pool score/rank receipts. Earlier drawing-script peak annotations that are absent from the pinned measured row were discarded.",
            "e": "No completed controlled PR96 episode receipt was found. The controller is shown schematically.",
        },
        "rendering": {"rdkit": rdBase.rdkitVersion, "stereochemistry": "Connectivity diagrams, not stereochemical assignment."},
    }
    (HERE / "case_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def sha256_iter(stream):
    digest = sha256()
    for block in iter(lambda: stream.read(1 << 20), b""):
        digest.update(block)
    return digest.hexdigest()


if __name__ == "__main__":
    main()
