"""Regenerate the first weekly scientific visual from the unchanged Gate 1 CSV."""
from pathlib import Path
import csv
import json
import hashlib
import statistics
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "01-computer-architecture/evidence-gate-01-memory-locality/results/full-20260911-165240.csv"
OUT = Path(__file__).resolve().parent
EXPECTED = "2d2d28ea5bf03970718c65c0e102954b15d2212e18e2dd3a3ad2d08ab0052861"
EXPECTED_LF = "e2f7fd2528cdeb6bf6a4e5b3319db7d557313602c6ee2adbfe0b13ce252c8f50"
source_bytes = SOURCE.read_bytes()
lf_bytes = source_bytes.replace(b"\r\n", b"\n")
assert hashlib.sha256(lf_bytes).hexdigest() == EXPECTED_LF
assert hashlib.sha256(lf_bytes.replace(b"\n", b"\r\n")).hexdigest() == EXPECTED
with SOURCE.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 468 and all(r["checksum_pass"].lower() == "true" for r in rows)
conditions = ["A_DIRECT", "B_SEQ_INDEX", "C_RANDOM_INDEX", "D_POINTER_CHASE"]
sizes = sorted({int(r["size_bytes"]) for r in rows})
assert len(sizes) == 13
summary = []
for size in sizes:
    for condition in conditions:
        selected = [r for r in rows if int(r["size_bytes"]) == size and r["condition"] == condition]
        assert len(selected) == 9 and {int(r["trial"]) for r in selected} == set(range(1, 10))
        values = sorted(float(r["ns_per_access"]) for r in selected)
        q1, _, q3 = statistics.quantiles(values, n=4, method="inclusive")
        summary.append(dict(size_bytes=size, condition=condition, observations=9,
                            median_ns=statistics.median(values), q1_ns=q1, q3_ns=q3))
with (OUT / "locality-summary.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(summary[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(summary)

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "text.color": "#102326", "axes.labelcolor": "#102326",
                     "xtick.color": "#526468", "ytick.color": "#526468", "svg.fonttype": "none",
                     "svg.hashsalt": "ACE-EG01-MEMORY-001"})
fig, axes = plt.subplots(1, 2, figsize=(13, 6.6), facecolor="#f7f6f2")
colours = ["#526468", "#01696f", "#d99b42", "#102326"]
styles = ["--", "-", "-.", ":"]
labels = ["A · Direct", "B · Sequential index", "C · Random index", "D · Pointer chase"]
x = [s / 1048576 for s in sizes]
for ax in axes:
    ax.set_facecolor("#f7f6f2")
    ax.set_xscale("log", base=2)
    ax.grid(True, alpha=.18, color="#526468")
    ax.set_xlabel("Nominal data size (MiB; log scale)")
    ax.set_xticks([.015625, .0625, 1, 4, 16, 64, 256], labels=["1/64", "1/16", "1", "4", "16", "64", "256"])
for condition, colour, style, label in zip(conditions, colours, styles, labels):
    s = [r for r in summary if r["condition"] == condition]
    axes[0].plot(x, [r["median_ns"] for r in s], color=colour, linestyle=style, marker="o", markersize=3, label=label)
    axes[0].fill_between(x, [r["q1_ns"] for r in s], [r["q3_ns"] for r in s], color=colour, alpha=.11)
axes[0].set_yscale("log")
axes[0].set_ylabel("Median ns/access (log scale)")
axes[0].set_title("Access order and dependency", loc="left", fontweight="bold")
axes[0].legend(frameon=False, fontsize=9, loc="upper left")
lookup = {(r["size_bytes"], r["condition"]): r["median_ns"] for r in summary}
ratios = [lookup[s, "C_RANDOM_INDEX"] / lookup[s, "B_SEQ_INDEX"] for s in sizes]
axes[1].plot(x, ratios, color="#01696f", marker="o", linewidth=2)
axes[1].axhline(1, color="#526468", linestyle=":", label="Parity")
axes[1].axhline(1.10, color="#d99b42", linestyle="--", label="Registered H1 threshold")
axes[1].scatter(x[-3:], ratios[-3:], color="#d99b42", s=65, zorder=3)
axes[1].set_ylabel("C/B ratio of medians")
axes[1].set_title("Random versus sequential indexed access", loc="left", fontweight="bold")
axes[1].legend(frameon=False, fontsize=9, loc="upper left")
for xx, yy in zip(x[-3:], ratios[-3:]):
    axes[1].annotate(f"{yy:.2f}×", (xx, yy), xytext=(-28, 10), textcoords="offset points", fontsize=9)
fig.suptitle("Same work. Different paths through memory.", fontsize=21, fontweight="bold", x=.07, ha="left", y=.98)
fig.text(.07, .92, "ACE Gate 1 · measured 11 September 2026 · 9 observations per condition/size", color="#526468", fontsize=11)
fig.subplots_adjust(left=.07, right=.98, top=.82, bottom=.24, wspace=.28)
fig.text(.07, .12, "Left: medians with interquartile ranges, not confidence intervals. Right: ratios of medians, without inferential error bars.", fontsize=9, color="#526468")
fig.text(.07, .085, "Indexed conditions also use index storage. Pointer-chase ns/access is not a standalone DRAM-latency measurement.", fontsize=9, color="#526468")
fig.text(.07, .05, "Amber points are the three registered H1 decision sizes. This graph does not identify exact cache capacities.", fontsize=9, color="#526468")
svg_path = OUT / "memory-locality.svg"
fig.savefig(svg_path, facecolor=fig.get_facecolor(), metadata={"Date": None, "Creator": "ACE scientific publication"})
svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
fig.savefig(OUT / "memory-locality.png", dpi=150, facecolor=fig.get_facecolor())
(OUT / "visual-provenance.json").write_text(json.dumps({
    "source_csv": str(SOURCE.relative_to(ROOT)), "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "original_windows_crlf_sha256": EXPECTED, "repository_lf_sha256": EXPECTED_LF,
    "line_ending_note": "Git normalizes CSV line endings; both serializations verified. Source file unchanged.",
    "experiment_git_head": rows[0]["git_head"], "experiment_timestamp_utc": rows[0]["timestamp_utc"],
    "observations": 468, "observations_per_condition_size": 9,
    "summary": "median and inclusive quartiles; ratio of medians",
    "iqr_is_confidence_interval": False, "new_experiment": False,
    "plotting_library": f"matplotlib {matplotlib.__version__}",
    "claim_boundary": "This machine and implementation; no exact cache/DRAM/general hardware inference"
}, indent=2) + "\n", encoding="utf-8")
print("PASS: source hash, 468 checksums, 52 groups, nine trials/group; scientific SVG/PNG/summary generated.")
