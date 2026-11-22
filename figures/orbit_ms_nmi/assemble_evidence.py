"""Build the figure manifest from public measured data and source run extracts."""
import argparse
import ast
from hashlib import sha256
import json
import math
from pathlib import Path
import subprocess

from rdkit import Chem, RDLogger
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

CASE = "MassSpecGymID0002114"
PR95 = "44bf931fc2510fc7b86c02024c719ee34f4ee144"
PR95_AUDITED_HEAD = "efce3e5452f124b6971336a74ddb5c9d5031e516"
PR96 = "c63c32ce24b29d959164c2b081e511b25641a1c4"
PR12 = "91045d0d3966ed66058a3c1cdb7176f2fbba28ad"
PR13 = "b53a2b9351597312e41f773df2459df194441aa8"
TRACE = "scripts/plot_pr93_paper_figures.py"
KEYS = ("OWKLJRMFTXDULF", "JBGBHQCAWKJFMS")
MOTIFS = ("NCCc1ccccc1", "CCNc1ccccc1")


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def obj(path):
    return json.loads(path.read_text())


def rd_mol(smiles):
    value = Chem.MolFromSmiles(smiles)
    if value is None:
        raise ValueError(smiles)
    return value


def lineage(smiles, mask):
    bits = int(mask, 16)
    parent = rd_mol(smiles)
    atoms = [i for i in range(parent.GetNumAtoms()) if (bits >> i) & 1]
    assert len(atoms) == bits.bit_count()
    # This is a display skeleton. The ion mass belongs to the W atom mask and ion channel.
    small = Chem.MolFragmentToSmiles(parent, atomsToUse=atoms, isomericSmiles=False)
    return atoms, small if Chem.MolFromSmiles(small) else None


def evidence(candidates, query):
    """Project the whole-spectrum V posterior with its exact per-peak mass kernel."""
    peaks = [mz for mz, _ in query["peaks"]]
    selected = []
    for row in candidates:
        info = row["details"]
        v = info["v_structural_candidates"]
        sigma = row["v_sigma_da"]
        assert 0 < sigma < 0.1
        assert abs(sum(z["v_posterior"] for z in v) - 1) < 1e-4
        plotted = []
        for peak in peaks:
            weighted = [(z["v_posterior"]*math.exp(-.5*((z["calculated_mz"]-peak)/sigma)**2),z)
                        for z in v if abs(z["calculated_mz"]-peak) <= 3*sigma]
            val = sum(k for k,_ in weighted)
            example = max(weighted, default=(0,None), key=lambda r:r[0])[1]
            plotted.append({"density":val,"best":example})
        selected.append(plotted)
    best = max((out["density"] for r in selected for out in r), default=0)
    for i, row in enumerate(selected):
        for j, cell in enumerate(row):
            own,peer=cell["density"],selected[1-i][j]["density"]
            cell["stronger"]=own>0 and (peer == 0 or own/peer>=4)
            cell["radius"]=round(4+13*math.sqrt(own/best),2) if best and own else 0
    return {"peaks":peaks,"metric":"V-posterior projection through V's Gaussian mass kernel (within 3 sigma). Radius scales with sqrt projected support. Teal marks at least 4-fold support or support only in one candidate. Neither radius nor color is a calibrated correctness probability.",
            "candidates":selected}


def source_states(repo):
    p=subprocess.check_output(["git","-C",str(repo),"show",f"{PR95}:{TRACE}"])
    for node in ast.walk(ast.parse(p)):
        if not isinstance(node,ast.Dict):
            continue
        try:
            data=ast.literal_eval(node)
        except (ValueError,TypeError):
            continue
        if data.get("cid")==CASE:
            steps=[s for _,s,_ in data["steps"]]
            assert all(rd_mol(b).HasSubstructMatch(rd_mol(a)) for a,b in zip(steps,steps[1:]))
            return {"states":steps,"sha256":sha256(p).hexdigest(),"source_line":node.lineno,
                    "source":f"https://github.com/wangyu-sd/orbit-ms/blob/{PR95}/{TRACE}",
                    "scope":"Upstream illustration states, separately annotated; an original beam parent chain was not retained in the case ranking file."}
    raise ValueError("No source illustration states")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs",type=Path)
    parser.add_argument("orbit_git",type=Path)
    parser.add_argument("--out",type=Path,default=Path(__file__).with_name("case_manifest.json"))
    args=parser.parse_args()
    RDLogger.DisableLog("rdApp.error")
    p=args.inputs
    raw=[json.loads(s) for s in (p/"case_probe.jsonl").read_text().splitlines()]
    source=raw[2]
    run=source["row"]
    assert run["case_id"] == CASE
    query=raw[0]["row"]["query"]
    candidates=[]
    wv_path=p/"nmi_wv_export.json"
    wv=obj(wv_path) if wv_path.stat().st_size else None
    picked=[z for key in KEYS for z in wv["candidates"] if z["candidate"]["key14"]==key] if wv else []
    ev=evidence(picked,query) if len(picked)==2 else {"peaks":[mz for mz,_ in query["peaks"]],
                                                     "candidates":[[None]*len(query["peaks"])]*2}
    for i,(label,key) in enumerate(zip("AB",KEYS)):
        rank,original=next((j,x) for j,x in enumerate(run["generated"],1) if x["key14"]==key)
        canonical=picked[i]["details"]["smiles"] if picked else original["smiles"]
        c={"label":label,"smiles":canonical,"record":original,"rank":rank,"key":key,
           "in_raw_G_pool":key in run["raw_candidate_keys"],"evidence":ev["candidates"][i]}
        assert CalcMolFormula(rd_mol(canonical))==original["formula"]
        if picked:
            v=picked[i]
            for score,replay in [("w_score","world_score"),("v_score","matched_v_score")]:
                assert abs(original[score]-v["score"][replay]) < 0.01
            # Prefer a mass-compatible example that can be shown as a clean standalone skeleton.
            alternatives=sorted((x["best"] for x in ev["candidates"][i] if x["best"]),
                                key=lambda z:-z["v_posterior"])
            if not alternatives:
                alternatives=sorted(v["details"]["v_structural_candidates"],key=lambda z:-z["v_posterior"])
            for obj0 in alternatives:
                indices,skeleton=lineage(canonical,obj0["mask_hex"])
                if skeleton or obj0 == alternatives[-1]:
                    c["illustration"]={"atoms":indices,"skeleton":skeleton,
                                       "mass":obj0["calculated_mz"],"object":obj0}
                    break
            sections=[]
            for j,cell in enumerate(ev["candidates"][i]):
                if cell["best"] and (j == 2 or cell["stronger"]):
                    ion=cell["best"]
                    atoms,skel=lineage(canonical,ion["mask_hex"])
                    sections.append({"atoms":atoms,"skeleton":skel,"mass":ion["calculated_mz"],
                                     "peak_index":j,"object":ion})
            c["shown_fragments"]=sections
            c["projection_sigma_da"]=v["v_sigma_da"]
            c["w_emitted_peaks"]=v["details"]["w_emitted_peaks"]
            c["replayed_WV"]=v["score"]
        candidates.append(c)

    assert candidates[0]["record"]["formula"]==candidates[1]["record"]["formula"]
    states=source_states(args.orbit_git)
    motif_index=obj(p/"nmi_mma_entries.json")
    motifs=[next(x for x in motif_index["entries"] if x["motif"]==m and x["ion"]=="C8H10N1") for m in MOTIFS]
    assert all(x["support"]>0 for x in motifs)
    matched=rd_mol(states["states"][1]).GetSubstructMatch(rd_mol(MOTIFS[0]))
    assert len(matched)==rd_mol(MOTIFS[0]).GetNumAtoms()
    alignment=[[i,j] for j,i in enumerate(matched)]
    experience={}
    hindsight_input=None
    for line in (p/"nmi_experience.jsonl").read_text().splitlines():
        item=json.loads(line)
        row=item["row"]
        if item["role"] == "hindsight_input":
            hindsight_input=item
            continue
        context={"case_id":row["case_id"],"peaks":row["query"]["peaks"],"source":item["path"],
                 "evidence_mode":row["query"].get("metadata",{}).get("query_evidence_mode"),
                 "row_sha256":sha256(json.dumps(row,sort_keys=True).encode()).hexdigest(),
                 "smiles":row.get("gt_smiles")}
        if item["role"]=="sleep" and "ABDWINSTWUZFIV" in row["case_id"]:
            experience["fragment_knowledge"]={**context,
                "motif_match":list(rd_mol(row["gt_smiles"]).GetSubstructMatch(rd_mol(MOTIFS[0])))}
        elif item["role"] == "sleep" and "ALISTFINEQANJP" in row["case_id"]:
            experience["sleep"]=context
        elif item["role"]!="sleep":
            experience[item["role"]]=context
    if hindsight_input:
        assert Chem.CanonSmiles(hindsight_input["row"]["smiles"]) == Chem.CanonSmiles(experience["hindsight"]["smiles"])
        experience["hindsight"]["generated_input"]=hindsight_input
    replay_path=p/"nmi_g_replay.json"
    if replay_path.exists() and replay_path.stat().st_size:
        g=obj(replay_path)
        indices=[1,2,3,len(g["steps"])-1]
        states["shown_replay_states"]=[g["steps"][i] for i in indices]
        states["reference_replay_scope"]=g["scope"]
        states["reference_replay_hash"]=sha(replay_path)
        states["reference_replay_steps"]=g["steps"]
        states["reference_replay_motifs"]=g["motif_templates"]
    manifest={
        "design_and_source": {
            "paper_PR12":PR12,"paper_PR13":PR13,"orbit_PR95":PR95,
            "orbit_PR95_audited_head":PR95_AUDITED_HEAD,"orbit_PR96":PR96,
            "score_source":f"https://github.com/wangyu-sd/orbit-ms/blob/{PR95}/scripts/score_pr87_frozen_wv_graph_edit.py",
            "agent_source":f"https://github.com/wangyu-sd/orbit-ms/blob/{PR96}/src/orbit_ms/agents/scientific_improver.py"},
        "query":query,"query_source":raw[0]["path"],
        "raw_run": {"ranking":source["path"],"source_sha":source["receipt"]["source_sha"],
                    "runtime_seconds":run["runtime_seconds"],"input_sha256":source["receipt"]["input_sha256"],
                    "formula_top":run["formula_top"],"authority":source["receipt"]["authority"]},
        "candidates":candidates,"evidence":{k:v for k,v in ev.items() if k!="candidates"},
        "mma":{"ion":"C8H10N+","observed_mz":120.0808,"motifs":motifs,"alignment":alignment,
               "source":motif_index["source"],"source_shards":motif_index["shards"],
               "scope":"Two selected drawable neutral skeletal motifs indexed under the ion-formula key in the four mined HMDB source shards. Counts are exact unique-group counts within those shards, not post-merge retrieval weights. Formula and mass labels belong to the ion key, not the neutral RDKit drawings."},
        "construction":states,"experience":experience,
        "inputs_sha256":{name:sha(p/name) for name in ["case_probe.jsonl","nmi_mma_entries.json","nmi_experience.jsonl","nmi_wv_export.json"]},
        "limitations":[
            "Reported ranks are from the same archived scored candidate pool. No claim that the exact W/V comparison was sufficient to establish the structure.",
            "MMA graph alignment uses the source motif and depicted partial graph. Attention operations are schematic; no trained attention weights are shown.",
            "One measured case anchors the upper figure. The lower data-stream examples are independent records.",
            "The bounded controller depicts implemented decision and evaluation logic. No measured autonomous performance is shown.",
        ],
    }
    if wv:
        manifest["replay"]={"checkpoint_hashes":wv["hashes"],"rank_row_sha256":wv["rank_row_sha256"],
                            "query_row_sha256":wv["query_row_sha256"],"W":wv["w_path"],"V":wv["v_path"]}
    else:
        manifest["limitations"].append("Frozen W/V structural replay unavailable; peak-level evidence has not been populated.")
    args.out.write_text(json.dumps(manifest,indent=2)+"\n")


if __name__=="__main__":
    main()
