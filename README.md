# NTN LEO Satellite Routing Evaluation Data

This repository contains the raw evaluation data supporting the research paper on topological routing for LEO satellite networks (6G-RUPA).

## Overview

This dataset contains performance metrics for the three routing families compared in the paper, evaluated across four LEO satellite constellation configurations under dynamic orbital evolution. The evaluation was conducted using the [LEOPath](https://github.com/Fundacio-i2CAT/LEOPath) simulation framework: six-hour windows sampled at one-minute intervals (360 topology snapshots per run), with 24 ground stations at major population centers (`ground_stations_dense` configuration) and all 552 ordered ground-station pairs as traffic endpoints.

## Constellations

- **Starlink**: 22 planes × 72 satellites = 1,584 satellites
- **Kuiper**: 34 planes × 34 satellites = 1,156 satellites
- **OneWeb**: 18 planes × 36 satellites = 648 satellites
- **Telesat**: 27 planes × 13 satellites = 351 satellites

## Routing Algorithms

1. **Topological Routing** (proposed): low-state greedy forwarding on topological addresses, using the pivot-weighted discrete-torus distance (`torus_weighted_pivot`)
2. **Link-State Shortest Path** (`shortest_path_link_state`): destination-oriented shortest-path forwarding from full snapshot topology knowledge
3. **Explicit-Path Routing** (`explicit_path_routing`): source-selected paths reused across R snapshots with dynamic final-egress repair

## ISL Scenarios

- **Ring**: 2 ISLs per satellite (intra-plane only)
- **+Grid**: 4 ISLs per satellite (intra-plane + inter-plane)
- **+Grid (seam/cylinder)**: +Grid with the cross-seam inter-plane wrap removed (counter-rotating planes), yielding a cylinder rather than a torus

## Sampling-Interval Sensitivity

The `sampling_sensitivity/` subtree re-runs the +Grid topological-forwarding (pivot)
and link-state matrices over the same 6h horizon at three sampling intervals — 10s
(`interval_10s`), 1min (`interval_1min`), and 5min (`interval_5min`) — to confirm
the main-matrix results are not artifacts of the 1-min sampling choice. Runs are
distinguished by `time_step_minutes` in `summary_sampling_sensitivity.csv` (aggregated
separately so the main `summary.csv` is unaffected). Forwarding-state size and
delivered-path stretch are sampling-invariant; the link-state per-hour update rate
grows as sampling tightens while the topological rate stays negligible. The two
largest 10s link-state cases (Kuiper, Starlink) and Starlink-10s topological were
not run for compute reasons; the trend is already monotone.

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
  url = {https://github.com/PhD-Sergio/ntn-paper-eval-data}
}
```

## Related Repositories

- [LEOPath](https://github.com/Fundacio-i2CAT/LEOPath) - LEO satellite routing simulation framework

## License

CC BY 4.0 - Creative Commons Attribution 4.0 International
