"""Churn of a full link-state forwarding table on a shell's ISL graph.

A link-state satellite keyed on satellite addresses holds one route to every
satellite. A station handover changes none of them; what changes them is the
graph itself, here only the ISL lengths, since the +Grid wiring is fixed and
there are no failures. For each snapshot this builds the simulator's ISL graph
(the same _build_topologies/_compute_isls calls as eval_harness, ISL weight =
length in metres), computes the next hop from every satellite toward every
other one with Dijkstra, and counts per satellite the destinations whose next
hop differs from the previous snapshot.

Output: one CSV row per snapshot and a JSON summary.
"""

import argparse
import csv
import json
import time

import numpy as np
from astropy import units as astro_units
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

from leopath.experiments.eval_harness import load_config, select_isls
from leopath.main import calculate_link_params, setup_ground_stations, setup_tles_and_satellites
from leopath.network_state.generate_network_state import _build_topologies
from leopath.network_state.helpers import _compute_isls
from leopath.topology.topology import ConstellationData
from leopath.topology.walker_geometry import walker_shell_from_config


def next_hop_table(graph, n: int) -> np.ndarray:
    rows, cols, weights = [], [], []
    for a, b, data in graph.edges(data=True):
        if a < n and b < n:
            rows += [a, b]
            cols += [b, a]
            weights += [data["weight"], data["weight"]]
    matrix = csr_matrix((weights, (rows, cols)), shape=(n, n))
    _, predecessors = dijkstra(matrix, directed=False, return_predecessors=True)
    # predecessors[d, s] is the node before s on the shortest path from d to s,
    # which in an undirected graph is the next hop from s toward d.
    return predecessors.T.copy()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--gs-config", default=None)
    parser.add_argument("--isl", default="grid")
    parser.add_argument("--hours", type=float, default=6.0)
    parser.add_argument("--step-minutes", type=float, default=1.0)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    if args.gs_config:
        with open(args.gs_config) as handle:
            import yaml

            config["ground_stations"] = yaml.safe_load(handle)["ground_stations"]
    config["simulation"]["end_time_hours"] = args.hours
    config["simulation"]["time_step_minutes"] = args.step_minutes

    parsed_tles_data, sim_satellites = setup_tles_and_satellites(config)
    try:
        ground_stations = setup_ground_stations(config)
    except Exception:
        ground_stations = []
    max_gsl, max_isl = calculate_link_params(config)
    constellation_data = ConstellationData(
        orbits=parsed_tles_data["n_orbits"],
        sats_per_orbit=parsed_tles_data["n_sats_per_orbit"],
        epoch=parsed_tles_data["epoch"],
        max_gsl_length_m=max_gsl,
        max_isl_length_m=max_isl,
        satellites=sim_satellites,
        walker=walker_shell_from_config(config["constellation"]),
    )
    raan_spread = float(config["constellation"].get("raan_spread_degree", 360.0))
    isls = select_isls(constellation_data, args.isl, raan_spread)
    n = len(sim_satellites)
    end_ns = int(args.hours * 3600 * 1e9)
    step_ns = int(args.step_minutes * 60 * 1e9)

    previous = None
    rows = []
    started = time.time()
    for index, t_ns in enumerate(range(0, end_ns, step_ns)):
        t_abs = parsed_tles_data["epoch"] + t_ns * astro_units.ns
        topology, _ = _build_topologies(constellation_data, ground_stations)
        _compute_isls(topology, isls, t_abs)
        table = next_hop_table(topology.graph, n)
        if previous is not None:
            changed = table != previous
            np.fill_diagonal(changed, False)
            per_satellite = changed.sum(axis=1)
            rows.append(
                {
                    "step": index,
                    "minutes": t_ns / 60e9,
                    "changes_per_sat_mean": float(per_satellite.mean()),
                    "changes_per_sat_max": int(per_satellite.max()),
                    "changed_share": float(changed.sum() / (n * (n - 1))),
                }
            )
        previous = table

    with open(args.out + ".csv", "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    means = np.array([row["changes_per_sat_mean"] for row in rows])
    summary = {
        "config": config["constellation"]["name"],
        "isl": args.isl,
        "satellites": n,
        "snapshots": len(rows) + 1,
        "step_minutes": args.step_minutes,
        "changes_per_sat_per_snapshot_mean": float(means.mean()),
        "changes_per_sat_per_snapshot_p95": float(np.percentile(means, 95)),
        "changes_per_sat_per_snapshot_max_step": float(means.max()),
        "changes_per_sat_max_single": int(max(row["changes_per_sat_max"] for row in rows)),
        "changed_share_mean": float(np.mean([row["changed_share"] for row in rows])),
        "wall_seconds": time.time() - started,
    }
    with open(args.out + ".json", "w") as handle:
        json.dump(summary, handle, indent=2)
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
