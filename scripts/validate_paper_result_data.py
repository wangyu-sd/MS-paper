#!/usr/bin/env python3
"""Checks that committed plot CSVs have internally consistent population units."""
import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"figures"/"data"
def rows(name):
    with (p/name).open(newline="", encoding="utf8") as f:
        return list(csv.DictReader(f))
m=rows("gen_curve_main.csv")
r=rows("gen_curve_rsi.csv")
a=rows("ten_axis_profile.csv")
t=rows("gems_tiers.csv")
d=rows("gems_mass_deltas.csv")
assert len(m)==8 and m[0]["stage"]=="Gen 0"
assert m[-1]["reach_pct"]=="", "Final Gen reach must not silently mix conflicting snapshots"
assert len(r)==5 and [x["promoted"] for x in r]==["no","yes","no","no","no"]
assert len(set(z["axis"] for z in a))==10 and len(a)>=30
assert sum(int(z["count"]) for z in t)==1000
assert sum(int(z["edges"]) for z in d)==168
for row in m[:-1]:
    assert float(row["exact1_pct"])<=float(row["exact10_pct"])<=float(row["reach_pct"])
for row in r:
    assert float(row["exact1_pct"])<=float(row["exact10_pct"])<=float(row["reach_pct"])
print(f"OK: {len(m)} historical checkpoints, {len(r)} RSI episodes, {len(a)} generalization strata")
