#!/usr/bin/env python3
"""Render ORBIT-MS Results quantitative previews from committed figures/data CSV.

Run: python scripts/render_paper_result_previews.py --out figures/previews
Outputs SVG and PDF; never overwrites main.tex's five bound figure PDFs.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "figures" / "data"
NAVY, TEAL, GREY = "#25465D", "#397D83", "#858B90"


def read_csv(filename):
    with (DATA / filename).open(newline="", encoding="utf8") as stream:
        return list(csv.DictReader(stream))


def numeric(x):
    return float(x) if str(x).strip() else float("nan")


def configure():
    import matplotlib as mpl
    mpl.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False,
        "axes.spines.right": False, "svg.fonttype": "none",
        "pdf.fonttype": 42, "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })


def save(fig, folder, name):
    folder.mkdir(parents=True, exist_ok=True)
    for ext in ("svg", "pdf"):
        fig.savefig(folder / f"{name}.{ext}", bbox_inches="tight", pad_inches=0.2)


def trajectory(folder, csvfile, title, suffix, is_rsi=False):
    import matplotlib.pyplot as plt
    rows = read_csv(csvfile)
    x = list(range(len(rows)))
    fig, ax = plt.subplots(figsize=(9.0, 4.3), dpi=200)
    for key, label, color in (
        ("exact1_pct", "Exact@1", NAVY),
        ("exact10_pct", "Exact@10", TEAL),
        ("reach_pct", "Candidate Reach", GREY),
    ):
        ax.plot(x, [numeric(z[key]) for z in rows], "-o", lw=2, ms=4.7,
                color=color, label=label)
    if is_rsi:
        labels = [f"Gen {r['generation']}" for r in rows]
        for i, r in enumerate(rows):
            if r["promoted"] == "yes":
                ax.axvspan(i - 0.20, i + 0.20, color=TEAL, alpha=0.11, lw=0)
                ax.annotate("promoted", (i, numeric(r["exact1_pct"])),
                            xytext=(0, -26), textcoords="offset points",
                            ha="center", fontsize=8, color=TEAL)
    else:
        labels = [r["stage"] for r in rows]
    ax.set_xticks(x, labels)
    ax.tick_params(axis="x", labelrotation=22)
    ax.set_ylabel("Structure recovery (%)")
    ax.set_ylim(0, 102 if is_rsi else 27)
    ax.grid(axis="y", alpha=0.17)
    ax.legend(frameon=False, ncol=3, loc="upper left")
    ax.set_title(title, loc="left", weight="semibold", pad=12)
    fig.text(.12, .015, suffix, color="#555E64", fontsize=8)
    fig.tight_layout(rect=(0, .065, 1, 1))
    save(fig, folder, "gen_curve_rsi" if is_rsi else "gen_curve_main")
    plt.close(fig)


def bars(folder, source, category, count, name, title):
    import matplotlib.pyplot as plt
    rows = read_csv(source)
    labels = [x[category] for x in rows]
    values = [numeric(x[count]) for x in rows]
    fig, ax = plt.subplots(figsize=(7.4, max(3.0, len(rows)*.43 + 1.3)), dpi=200)
    ys = list(range(len(rows)))
    plot = ax.barh(ys, values, color=TEAL, height=.64)
    plot[0].set_color(NAVY)
    ax.set_yticks(ys, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, max(values)*1.17)
    ax.set_xlabel("Number of spectra" if name == "gems_tiers" else "Number of mass-difference edges")
    for i, val in enumerate(values):
        ax.text(val + max(values)*.018, i, f"{val:.0f}", va="center", fontsize=8)
    ax.set_title(title, loc="left", weight="semibold")
    ax.grid(axis="x", alpha=.15)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, folder, name)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "figures" / "previews")
    out = parser.parse_args().out
    configure()
    trajectory(out, "gen_curve_main.csv", "Cumulative ORBIT-MS development",
               "17,556 TEST spectra; archived grouped checkpoints. Last Reach not plotted.")
    trajectory(out, "gen_curve_rsi.csv", "RSI candidate evaluation and promotion",
               "CAL200 known-formula candidates; Gen1 accepted, others rejected.", is_rsi=True)
    bars(out, "gems_mass_deltas.csv", "formula_shift", "edges",
         "gems_mass_deltas", "GeMS candidate mass-difference relations")
    bars(out, "gems_tiers.csv", "name", "count",
         "gems_tiers", "GeMS candidate structure-support tiers")
    print(f"Saved four SVG and four PDF vector figure drafts to: {out}")


if __name__ == "__main__":
    main()
