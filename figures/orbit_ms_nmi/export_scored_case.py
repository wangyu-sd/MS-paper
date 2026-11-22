"""Export frozen W fragments and V posterior for selected logged candidates."""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys

def report(message):
    print(message, file=sys.stderr, flush=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", type=Path, required=True)
    parser.add_argument("--ranking", type=Path, required=True)
    parser.add_argument("--submission", type=Path, required=True)
    parser.add_argument("--w", type=Path, required=True)
    parser.add_argument("--v", type=Path, required=True)
    parser.add_argument("--case", default="MassSpecGymID0002114")
    parser.add_argument("--key", action="append", required=True)
    args = parser.parse_args()
    report("Loading torch")
    import torch
    torch.set_num_threads(1)
    report("Loading W/V scorer")
    from scripts.score_pr87_frozen_wv_graph_edit import FrozenWVGraphScorer
    qline = next(l for l in args.query.open() if args.case in l)
    rline = next(l for l in args.ranking.open() if args.case in l)
    query, ranking = map(json.loads, (qline,rline))
    assert query["case_id"] == ranking["case_id"] == args.case
    submission = json.loads(args.submission.read_text())
    report("Loading frozen W/V checkpoints")
    scorer = FrozenWVGraphScorer(args.w, args.v, device="cpu")
    assert scorer.hashes["w_checkpoint"] == submission["input_sha256"]["w"]
    assert scorer.hashes["v_checkpoint"] == submission["input_sha256"]["v"]
    selected = []
    for key in args.key:
        rank, candidate = next((i,c) for i,c in enumerate(ranking["generated"],1) if c["key14"] == key)
        report(f"Scoring rank {rank}")
        score, details = scorer.score(candidate["smiles"], query, include_fragment_details=True)
        selected.append({
            "rank":rank, "raw_G_pool":key in ranking["raw_candidate_keys"],
            "candidate":candidate, "score":asdict(score), "details":details,
            "v_sigma_da":scorer.v.config.sigma_da,
        })
    print(json.dumps({
        "query":query, "query_row_sha256": hashlib.sha256(qline.encode()).hexdigest(),
        "rank_row_sha256":hashlib.sha256(rline.encode()).hexdigest(), "hashes":scorer.hashes,
        "submission":submission["input_sha256"], "submission_source_sha":submission["source_sha"],
        "query_path":str(args.query), "ranking_path":str(args.ranking),
        "w_path":str(args.w),"v_path":str(args.v), "candidates":selected,
    }))

if __name__ == "__main__":
    main()
