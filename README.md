# NTN LEO Satellite Routing Evaluation Data

This repository contains the raw evaluation data supporting the research paper on topological routing for LEO satellite networks (6G-RUPA).

## Overview

This dataset contains performance metrics for the three routing families compared in the paper, evaluated across four LEO satellite constellation configurations under dynamic orbital evolution. The evaluation was conducted using the [LEOPath](https://github.com/Fundacio-i2CAT/LEOPath) simulation framework: six-hour windows sampled at one-minute intervals (360 topology snapshots per run), with 24 ground stations at major population centers (`ground_stations_dense` configuration) and all 552 ordered ground-station pairs as traffic endpoints.

## Constellations

Each is a single shell, parameterised from its operator's filing rather than imported from a
TLE catalogue. Mean motions are set so SGP4 flies the altitude each configuration declares,
since that altitude also fixes the ground-link range and the maximum ISL length.

| | planes × satellites | total | altitude | inclination | layout from |
|---|---|---|---|---|---|
| **Starlink** | 72 × 22 | 1,584 | 550 km | 53° | FCC 21-48 ¶4 |
| **Kuiper** | 34 × 34 | 1,156 | 630 km | 51.9° | FCC 20-102 |
| **OneWeb** | 12 × 49 | 588 | 1,200 km | 87.9° | FCC DA 23-362 ¶6 |
| **Telesat** | 27 × 13 | 351 | 1,015 km | 98.98° | Hypatia `telesat_1015` |

Starlink, Kuiper and Telesat spread their ascending nodes over a full circle, a Walker delta.
OneWeb flies as a Walker star, its 12 planes covering about 180 degrees, which is what live
orbital elements show. That distinction decides whether the +Grid wrap exists: see below.

An earlier version of this dataset modelled Starlink as 22 planes of 72, OneWeb as 18 planes of
36 over a full circle, and mean motions that missed their stated altitudes by 42 to 100 km.
Those results remain available under the `pre-config-fix` tag.

## Routing Algorithms

1. **Topological Routing** (proposed): low-state greedy forwarding on topological addresses, using the pivot-weighted discrete-torus distance (`torus_weighted_pivot`)
2. **Link-State Shortest Path** (`shortest_path_link_state`): destination-oriented shortest-path forwarding from full snapshot topology knowledge
3. **Explicit-Path Routing** (`explicit_path_routing`): source-selected paths reused across R snapshots with dynamic final-egress repair

## ISL Scenarios

- **Ring**: 2 ISLs per satellite (intra-plane only)
- **+Grid**: 4 ISLs per satellite (intra-plane + inter-plane)
- **+Grid (seam/cylinder)**: +Grid with the wrap between the last and first plane removed, yielding a cylinder rather than a torus

Whether that wrap is physical depends on the shell. In a Walker delta the last and first planes
travel the same way and the wrap is an ordinary neighbour link, so the cylinder is a stress test
for losing it. In a Walker star they counter-rotate, and the wrap would join satellites up to half
an orbit apart, so it cannot be built: OneWeb's `grid` runs are the cylinder, and its `grid` and
`grid_seam` results are identical. Each run records which case applied as `isl_seam_wrap`.

## Sampling-Interval Sensitivity

The `sampling_sensitivity/` subtree re-runs the +Grid topological-forwarding (pivot)
and link-state matrices over the same 6h horizon at three sampling intervals — 10s
(`interval_10s`), 1min (`interval_1min`), and 5min (`interval_5min`) — to confirm
the main-matrix results are not artifacts of the 1-min sampling choice. Runs are
distinguished by `time_step_minutes` in `summary_sampling_sensitivity.csv` (aggregated
separately so the main `summary.csv` is unaffected). Forwarding-state size and
delivered-path stretch are sampling-invariant; the link-state per-hour update rate
grows as sampling tightens while the topological rate stays negligible. All twelve
constellation and algorithm pairs were run at every interval, including the three
heaviest 10s cases that an earlier version of this dataset left out.

## Metrics

Each evaluation run produces:
- `timestep_metrics.csv`: Per-timestep metrics (forwarding state size, stretch, compute time)
- `delta_metrics.csv`: Changes between consecutive timesteps, including installed forwarding-state updates (`sat_fstate_updates_*`) and route-instability companion metrics
- `metadata.json`: Configuration and run parameters

`summary.csv` at the repository root aggregates all runs (generated with `python -m leopath.experiments.aggregate_eval`).

### Key Metrics

| Metric | Description |
|--------|-------------|
| Forwarding State | Number of forwarding-state units per satellite |
| Routing Table Updates | Installed satellite-local state mutations per snapshot (`sat_fstate_updates_total_mean`) |
| Churn | Rate of next-hop changes between timesteps |
| Stretch | Ratio of delivered path length to shortest path length in the same snapshot |
| Compute Time | Wall-clock time to process each snapshot |

## Citation

If you use this data in your research, please cite:

```
@software{leopath_eval_data,
  author = {Sergio Giménez-Antón and Eduard Grasa and Jordi Perelló},
  title = {NTN LEO Satellite Routing Evaluation Data},
  year = {2026},
  url = {https://github.com/PhD-Sergio/data-ntn-topological-evaluation}
}
```

## Related Repositories

- [LEOPath](https://github.com/Fundacio-i2CAT/LEOPath) - LEO satellite routing simulation framework

## License

CC BY 4.0 - Creative Commons Attribution 4.0 International
