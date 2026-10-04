#!/usr/bin/env python3
"""Generate story-focused evaluation figures for the NTN paper.

Every plotted value is read from the evaluation summaries written by
``leopath.experiments.state_accounting_tables``, so the figures and the tables
cannot drift apart. Point ``--summaries`` at the directory holding the
``headline`` and ``explicit_strict_r3`` summaries.

    python plot_story_figures.py --summaries ../rerun-3efafaa-summaries
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
FIGURE_DIR = ROOT / "figures"

COLORS = {
    # Okabe-Ito palette: colorblind-safe and distinct in print.
    "link_state": "#0072B2",
    "topological": "#009E73",
    "explicit": "#CC79A7",
    "sensitivity_cached": "#009E73",
    "sensitivity_repair": "#E69F00",
    "sensitivity_failure": "#D55E00",
    "sensitivity_metric": "#0072B2",
    "sensitivity_baseline": "#000000",
    "compact": "#CC79A7",
    "srv6": "#CC79A7",
}

CONSTELLATIONS = ["Starlink", "Kuiper", "OneWeb", "Telesat"]
ALGORITHMS = ["Link-state", "Topological", "Explicit-path"]
CONFIG_OF = {name: name.lower() for name in CONSTELLATIONS}
ALGORITHM_OF = {
    "Link-state": "shortest_path_link_state",
    "Topological": "topological_routing",
    "Explicit-path": "explicit_path_routing",
}
ISL_OF = {"Ring": "ring", "+Grid": "grid"}
# Final-model runs (revision): the variant each family is shown with in the
# data-plane footprint. Link-state and topological use the same northbound
# station addresses, so the comparison isolates forwarding.
FINAL_VARIANT_OF = {
    "Link-state": "link_state_dir_asc",
    "Topological": "topological_scheme_asc",
    "Explicit-path": "explicit_r3",
}
DEFAULT_SUMMARIES = ROOT.parent / "rerun-3efafaa-summaries"


def load_matrix(summaries: Path, campaign: str) -> dict:
    with (summaries / campaign / "matrix_runs.csv").open() as handle:
        return {(r["constellation"], r["algorithm"], r["isl"]): r for r in csv.DictReader(handle)}


def value(matrix: dict, constellation: str, algorithm: str, isl: str, column: str) -> float:
    return float(matrix[(CONFIG_OF[constellation], ALGORITHM_OF[algorithm], ISL_OF[isl])][column])


def load_final_matrix(csv_path: Path) -> dict:
    """Final-model matrix written by ntn-paper-eval-data/scripts/matrix_from_sweep.py,
    re-keyed by the family names the plots use."""
    variant_family = {variant: ALGORITHM_OF[family] for family, variant in FINAL_VARIANT_OF.items()}
    with csv_path.open() as handle:
        return {
            (r["constellation"], variant_family[r["algorithm"]], r["isl"]): r
            for r in csv.DictReader(handle)
            if r["algorithm"] in variant_family
        }


def mean(values) -> float:
    return sum(values) / len(values)


def by_isl(matrix: dict, column: str) -> dict:
    return {
        isl: {
            algorithm: [value(matrix, c, algorithm, isl, column) for c in CONSTELLATIONS]
            for algorithm in ALGORITHMS
        }
        for isl in ISL_OF
    }


def apply_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 300,
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlepad": 8,
        }
    )


def annotate_bars(ax, bars, fmt: str = "{:.3g}", dy: float = 1.05) -> None:
    for bar in bars:
        value = bar.get_height()
        if value <= 0:
            continue
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value * dy,
            fmt.format(value),
            ha="center",
            va="bottom",
            fontsize=9,
        )


def annotate_hbars(ax, bars, fmt: str = "{:.3g}", dx: float = 1.06) -> None:
    for bar in bars:
        value = bar.get_width()
        if value <= 0:
            continue
        ax.text(
            value * dx,
            bar.get_y() + bar.get_height() / 2,
            fmt.format(value),
            ha="left",
            va="center",
            fontsize=9,
        )


def plot_resource_footprint(fstate_by_isl: dict, updates_by_isl: dict) -> None:
    labels = ["Link-state", "Topological", "Explicit-path (R=3)"]
    colors = [COLORS["link_state"], COLORS["topological"], COLORS["explicit"]]

    # +Grid means across Starlink, Kuiper, OneWeb, and Telesat.
    forwarding_state = [mean(fstate_by_isl["+Grid"][a]) for a in ALGORITHMS]
    satellite_updates = [mean(updates_by_isl["+Grid"][a]) for a in ALGORITHMS]

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.1))
    for ax, values, title, ylabel in [
        (
            axes[0],
            forwarding_state,
            "(a) Forwarding state (+Grid)",
            "Mean units per satellite",
        ),
        (
            axes[1],
            satellite_updates,
            "(b) Routing table updates (+Grid)",
            "Mean updates per satellite per snapshot",
        ),
    ]:
        y = np.arange(len(labels))
        bars = ax.barh(y, values, color=colors, height=0.58)
        ax.set_xscale("log")
        ax.set_title(title)
        ax.set_xlabel(ylabel)
        ax.set_yticks(y)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.grid(True, axis="x", alpha=0.22)
        annotate_hbars(ax, bars)

    axes[0].set_xlim(3, 1600)
    axes[1].set_xlim(0.01, 40)
    fig.tight_layout(w_pad=2.4)
    fig.savefig(FIGURE_DIR / "evaluation_resource_footprint.png", bbox_inches="tight")
    plt.close(fig)


def plot_resource_footprint_with_brick(final: dict, brick_csv: Path) -> None:
    """Fig. 11 for the final model: +Grid means over the four shells and, for
    link-state and topological forwarding, brick-wall means over the shells and
    layouts that have a brick wall (Starlink and Kuiper in both, OneWeb in one)."""
    families = ["Link-state", "Topological", "Explicit-path"]
    labels = ["Link-state", "Topological", "Explicit-path (R=3)"]
    colors = [COLORS["link_state"], COLORS["topological"], COLORS["explicit"]]
    with brick_csv.open() as handle:
        brick_rows = list(csv.DictReader(handle))

    def grid_mean(family: str, column: str) -> float:
        return mean([value(final, c, family, "+Grid", column) for c in CONSTELLATIONS])

    def brick_mean(family: str, column: str) -> float | None:
        variant = FINAL_VARIANT_OF[family]
        values = [float(r[column]) for r in brick_rows if r["algorithm"] == variant]
        return mean(values) if values else None

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.6))
    for ax, column, title, xlabel, xlim in [
        (axes[0], "fstate_proxy", "(a) Forwarding state", "Mean units per satellite", (2, 2500)),
        (
            axes[1],
            "fstate_updates_per_snapshot",
            "(b) Routing table updates",
            "Mean updates per satellite per snapshot",
            (0.01, 60),
        ),
    ]:
        y = np.arange(len(families))
        height = 0.36
        grid_bars = ax.barh(
            y - height / 2, [grid_mean(f, column) for f in families], height=height, color=colors, label="+Grid"
        )
        brick_values = [brick_mean(f, column) for f in families]
        brick_y = [yy + height / 2 for yy, v in zip(y, brick_values) if v is not None]
        brick_bars = ax.barh(
            brick_y,
            [v for v in brick_values if v is not None],
            height=height,
            color=[c for c, v in zip(colors, brick_values) if v is not None],
            alpha=0.45,
            hatch="///",
            edgecolor="black",
            linewidth=0.4,
            label="Brick wall",
        )
        ax.set_xscale("log")
        ax.set_xlim(*xlim)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_yticks(y)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.grid(True, axis="x", alpha=0.22)
        for bars in (grid_bars, brick_bars):
            for bar in bars:
                width = bar.get_width()
                ax.text(
                    width * 1.06,
                    bar.get_y() + bar.get_height() / 2,
                    f"{width:,.0f}" if width >= 100 else f"{width:.3g}",
                    ha="left",
                    va="center",
                    fontsize=9,
                )
    handles = [
        plt.Rectangle((0, 0), 1, 1, color="0.45"),
        plt.Rectangle((0, 0), 1, 1, facecolor="0.45", alpha=0.45, hatch="///", edgecolor="black", linewidth=0.4),
    ]
    axes[0].legend(handles, ["+Grid", "Brick wall"], loc="lower right", frameon=False)
    fig.tight_layout(w_pad=2.4)
    fig.savefig(FIGURE_DIR / "evaluation_resource_footprint.png", bbox_inches="tight")
    plt.close(fig)


def plot_failure_exception_state(sweep_dir: Path) -> None:
    """Exception state under random failures (failure-injection simulations, grow rule,
    northbound addresses): region entries on the busiest satellite, one panel per failure
    type, against the routes link-state holds on every satellite."""
    with (sweep_dir / "failure_sweep_seeds.csv").open() as handle:
        seeds = [r for r in csv.DictReader(handle) if r["variant"] == "topological_scheme_asc"]
    shells = {"starlink": ("Starlink", 1584), "kuiper": ("Kuiper", 1156),
              "oneweb": ("OneWeb", 588), "telesat": ("Telesat", 351)}
    palette = {"starlink": "#0072B2", "kuiper": "#009E73", "oneweb": "#E69F00", "telesat": "#CC79A7"}
    panels = [
        ("isl", [0.01, 0.02, 0.05, 0.10, 0.20], "(a) Links lost", "Links down, % of time"),
        ("sat", [0.005, 0.01, 0.02, 0.05], "(b) Satellites out", "Satellites down, % of time"),
    ]

    def condition(kind: str, rate: float) -> str:
        return f"{kind}_p{rate:.3f}".rstrip("0") if kind == "sat" else f"{kind}_p{rate:.2f}"

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.8), sharey=True)
    for ax, (kind, rates, title, xlabel) in zip(axes, panels):
        x = [100 * rate for rate in rates]
        for shell, (name, routes) in shells.items():
            busiest = [
                mean([float(r["exception_region_max_per_satellite"]) for r in seeds
                      if r["constellation"] == shell and r["condition"] == condition(kind, rate)])
                for rate in rates
            ]
            ax.plot(x, busiest, "-o", color=palette[shell], markersize=4, label=name)
            ax.axhline(routes, color=palette[shell], linestyle=(0, (1.2, 1.6)), linewidth=2.4)
        ax.set_xscale("log")
        ax.set_xticks(x)
        ax.set_xticklabels([f"{v:g}" for v in x])
        ax.minorticks_off()
        ax.set_yscale("log")
        ax.set_ylim(2, 3000)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.grid(True, alpha=0.22)
    axes[0].set_ylabel("Entries on the busiest satellite")
    axes[0].text(1.0, 2200, "dotted: link-state routes on every satellite", fontsize=8.5, color="0.35")
    axes[0].legend(loc="lower right", frameon=False, fontsize=9, ncol=2, title="solid: topological",
                   title_fontsize=8.5)
    for ax, point in zip(axes, (1.0, 0.5)):
        ax.axvline(point, color="0.55", linewidth=6, alpha=0.18, zorder=0)
        ax.text(point * 1.06, 150, "realistic\nrates", fontsize=8, color="0.4", va="center")
    fig.tight_layout(w_pad=1.6)
    fig.savefig(FIGURE_DIR / "failure_exception_state.png", bbox_inches="tight")
    plt.close(fig)

def plot_constellation_robustness(fstate_by_isl: dict, updates_by_isl: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11.4, 5.8), sharex="col")
    bar_width = 0.23
    x = np.arange(len(CONSTELLATIONS))
    offsets = [-bar_width, 0.0, bar_width]
    algorithm_colors = [COLORS["link_state"], COLORS["topological"], COLORS["explicit"]]

    rows = [
        (fstate_by_isl, "Forwarding state", "Units per satellite", (1.5, 2200)),
        (
            updates_by_isl,
            "Routing table updates",
            "Updates per satellite per snapshot",
            (0.015, 60),
        ),
    ]
    for row_idx, (data_by_isl, metric_title, ylabel, ylim) in enumerate(rows):
        for col_idx, isl in enumerate(["Ring", "+Grid"]):
            ax = axes[row_idx, col_idx]
            for algorithm, offset, color in zip(ALGORITHMS, offsets, algorithm_colors):
                ax.bar(
                    x + offset,
                    data_by_isl[isl][algorithm],
                    bar_width,
                    color=color,
                    label=algorithm,
                )
            ax.set_yscale("log")
            ax.set_ylim(*ylim)
            ax.set_title(f"{metric_title}: {isl}")
            ax.set_xticks(x)
            ax.set_xticklabels(CONSTELLATIONS, rotation=18, ha="right")
            ax.grid(True, axis="y", alpha=0.22)
            if col_idx == 0:
                ax.set_ylabel(ylabel)

    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(
        handles, labels, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.02), ncol=3
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94), h_pad=2.0, w_pad=2.2)
    fig.savefig(FIGURE_DIR / "evaluation_constellation_robustness.png", bbox_inches="tight")
    plt.close(fig)


def plot_explicit_sensitivity(headline: dict, strict: dict) -> None:
    """Strict against dynamic final-egress repair, pooled over the four +Grid shells.

    Every deliverable pair either rides its cached egress, gets rescued by
    dynamic repair, or is lost, so the three shares sum to one. These rates count
    pairs rather than failover events: explicit_failover_count equals the
    deliverable pairs.
    """
    variants = ["R=3\nstrict", "R=3\ndynamic"]
    x = np.arange(len(variants))

    shares, stretches = [], []
    for matrix in (strict, headline):
        delivered = mean(
            [value(matrix, c, "Explicit-path", "+Grid", "delivery_rate") for c in CONSTELLATIONS]
        )
        repaired = mean(
            [
                value(
                    matrix,
                    c,
                    "Explicit-path",
                    "+Grid",
                    "explicit_failover_dynamic_egress_repair_rate",
                )
                for c in CONSTELLATIONS
            ]
        )
        shares.append((delivered - repaired, repaired, 1.0 - delivered))
        stretches.append(
            mean(
                [
                    value(matrix, c, "Explicit-path", "+Grid", "stretch_dist_shared")
                    for c in CONSTELLATIONS
                ]
            )
        )
    delivered_cached = np.array([share[0] for share in shares])
    dynamic_repair = np.array([share[1] for share in shares])
    failure = np.array([share[2] for share in shares])
    stretch = np.array(stretches)
    stretch_excess_percent = (stretch - 1.0) * 100.0

    fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.2))

    axes[0].bar(
        x,
        delivered_cached,
        color=COLORS["sensitivity_cached"],
        width=0.62,
        label="Delivered via cached egress",
    )
    axes[0].bar(
        x,
        dynamic_repair,
        bottom=delivered_cached,
        color=COLORS["sensitivity_repair"],
        width=0.62,
        label="Delivered via final-egress repair",
    )
    axes[0].bar(
        x,
        failure,
        bottom=delivered_cached + dynamic_repair,
        color=COLORS["sensitivity_failure"],
        width=0.62,
        label="Failed stale egress",
    )
    axes[0].set_ylim(0, 1.08)
    axes[0].set_title("(a) Delivery")
    axes[0].set_ylabel("Fraction of pairs")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(variants)
    axes[0].grid(True, axis="y", alpha=0.22)
    handles, legend_labels = axes[0].get_legend_handles_labels()

    bars = axes[1].bar(x, stretch_excess_percent, color=COLORS["sensitivity_metric"], width=0.62)
    axes[1].set_title("(b) Delivered-path detour")
    axes[1].set_ylabel("Mean distance-stretch excess (%)")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(variants)
    # Follow the data: the excess moved from hundredths of a percent under R=1
    # refresh to a couple of percent once paths are actually reused.
    axes[1].set_ylim(0, max(stretch_excess_percent) * 1.3)
    axes[1].grid(True, axis="y", alpha=0.22)
    annotate_bars(axes[1], bars, fmt="{:.3f}", dy=1.08)

    fig.legend(
        handles,
        legend_labels,
        frameon=False,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.02),
        ncol=3,
    )
    fig.tight_layout(rect=(0, 0.12, 1, 1), w_pad=2.0)
    fig.savefig(FIGURE_DIR / "explicit_path_sensitivity.png", bbox_inches="tight")
    plt.close(fig)


def plot_packet_forwarding_information(headline: dict) -> None:
    labels = [
        "Link-state header\n(IPv6 dst addr.)",
        "Topological header\n(6G-RUPA locator)",
        "Explicit-path header\n(SRv6 SRH, IPv6 SIDs)",
    ]
    # Link-state shown with an IPv6 destination address. The topological locator
    # is the current 23-bit 6G-RUPA tuple encoding rounded up to full bytes.
    # SRv6 SRH bytes are 8 + 16k for k carried segment identifiers, excluding
    # the IPv6 base header.
    srv6_bytes = mean(
        [
            value(headline, c, "Explicit-path", "+Grid", "srv6_srh_bytes_mean")
            for c in CONSTELLATIONS
        ]
    )
    values = [16.0, 3.0, srv6_bytes]
    colors = [COLORS["link_state"], COLORS["topological"], COLORS["srv6"]]

    fig, ax = plt.subplots(figsize=(5.8, 2.4))
    y = np.arange(len(labels))
    bars = ax.barh(y, values, color=colors, height=0.56)
    ax.set_title("Packet-Carried Forwarding Information (+Grid)")
    ax.set_xlabel("Mean carried bytes per active GS->GS packet")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 180)
    ax.grid(True, axis="x", alpha=0.22)
    annotate_hbars(ax, bars, fmt="{:.1f}", dx=1.02)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "packet_forwarding_information.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate the paper figures")
    parser.add_argument(
        "--summaries",
        type=Path,
        default=DEFAULT_SUMMARIES,
        help="directory holding the per-campaign summary folders",
    )
    parser.add_argument(
        "--final-matrix",
        type=Path,
        default=None,
        help="final-model matrix_runs.csv; when given, the data-plane footprint is drawn from it",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="where to write the figures (default: figures/ next to this script)",
    )
    parser.add_argument(
        "--failure-sweep",
        type=Path,
        default=None,
        help="failure-injection summary directory (failure_sweep_summary.csv and _seeds.csv)",
    )
    parser.add_argument(
        "--brick-matrix",
        type=Path,
        default=None,
        help="brick-wall matrix_runs.csv, added to the footprint next to +Grid",
    )
    args = parser.parse_args()
    global FIGURE_DIR
    if args.output_dir is not None:
        FIGURE_DIR = args.output_dir

    headline = load_matrix(args.summaries, "headline")
    strict = load_matrix(args.summaries, "explicit_strict_r3")
    fstate_by_isl = by_isl(headline, "fstate_proxy")
    updates_by_isl = by_isl(headline, "fstate_updates_per_snapshot")

    FIGURE_DIR.mkdir(exist_ok=True)
    apply_style()
    if args.final_matrix is not None:
        final = load_final_matrix(args.final_matrix)
        if args.brick_matrix is not None:
            plot_resource_footprint_with_brick(final, args.brick_matrix)
        else:
            plot_resource_footprint(by_isl(final, "fstate_proxy"), by_isl(final, "fstate_updates_per_snapshot"))
    else:
        plot_resource_footprint(fstate_by_isl, updates_by_isl)
    plot_constellation_robustness(fstate_by_isl, updates_by_isl)
    if args.failure_sweep is not None:
        plot_failure_exception_state(args.failure_sweep)
    plot_explicit_sensitivity(headline, strict)
    plot_packet_forwarding_information(headline)
    print(f"figures written to {FIGURE_DIR} from {args.summaries}")


if __name__ == "__main__":
    main()
