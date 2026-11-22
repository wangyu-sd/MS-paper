"""Replay the PR95 reference Canonical Hybrid action semantics for one logged candidate."""
from collections import Counter
import json
from pathlib import Path
from types import SimpleNamespace

from rdkit import Chem
from orbit_ms.wgv import peak_ladder as pl, peak_ladder_motif as pm, peak_ladder_rings as pr

data=json.loads(Path(__file__).with_name("case_manifest.json").read_text())
candidate=data["candidates"][0]["smiles"]
info=pl.gt_info(candidate)
assert info is not None
query=data["query"]
peaks=sorted(query["peaks"],reverse=True)
target=pl.Target(Counter(info["symbols"]),sum(info["h"]),pl.carrier_of(query["adduct"]),
                 peaks,query["precursor_mz"])
mass_position=[j for j,(m,_) in enumerate(query["peaks"]) if abs(m-120.0808)<.00005][0]
h=[SimpleNamespace(peak_index=mass_position,fragment=m["motif"],prior=1.0)
   for m in data["mma"]["motifs"]]
observation=SimpleNamespace(peak_fragments=h,spectrum=SimpleNamespace(peaks=[
    SimpleNamespace(mz=m,intensity=i) for m,i in query["peaks"]]))
vocab=pr.RingVocab([])
motifs=pm.motif_templates(observation,vocab)
steps=pm.direct_trajectory(info,pm.gt_kekule(candidate),target,vocab=vocab,systems=[],motifs=motifs)
assert steps, "Reference replay failed"
result=[]
for _,state,_,_,action,_,_ in steps:
    result.append({"smiles":pl.to_smiles(state) if state.symbols else None,
                   "action":list(action),"symbols":state.symbols,"bonds":[[a,b,n] for (a,b),n in state.bonds.items()]})
assert Chem.CanonSmiles(result[-1]["smiles"],useChiral=False)==Chem.CanonSmiles(candidate,useChiral=False)
print(json.dumps({"scope":"Reference-conditioned deterministic action replay using drawn motif entries; not a historical beam rollout or a deployed checkpoint trace.",
                  "motif_templates":motifs["vocab"].keys,"steps":result},indent=2))
