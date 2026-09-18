# Revision data

Aggregated results of the two evaluation campaigns run for the major revision of
COMNET-D-26-04044. Raw per-run outputs (`timestep_metrics.csv`, `delta_metrics.csv`,
`metadata.json`) are kept on the evaluation server and are not copied here yet.

Rates are pooled over each run's snapshots (delivered pairs over deliverable pairs)
and stretch is weighted by the pairs it was measured over.

## `state_accounting/`

Re-run of the evaluation matrix with state accounting.

- Code: LEOPath `9ac211f` (state counters by category, link-state database counters).
- Matrix: Telesat, OneWeb, Kuiper, Starlink × topological (pivot), DRA, explicit path,
  link-state × Ring, +Grid, +Grid open seam. Six hours at one-minute steps, 24 ground
  stations (`ground_stations_dense`), 552 ordered pairs.
- `summary.csv`: `python -m leopath.experiments.aggregate_eval`, same format as the
  dataset's root `summary.csv`.
- `matrix_runs.csv`, `matrix_tables.md`: `python -m leopath.experiments.state_accounting_tables`.

## `failure_sweep/`

Robustness sweep with injected failures, on +Grid for one hour at one-minute steps with the
same 24 ground stations.

Conditions: no failures; ISL loss at stationary rates of 1, 2, 5, 10 and 20% (mean outage
10 min); satellite outage at 0.5, 1, 2 and 5% (mean outage 60 min); contiguous voids of 2×2,
4×4 and 8×8 satellites; a two-boundary plane cut; polar deactivation of inter-plane links
above 75° and 60°. Random conditions use seeds 1 to 5 and deterministic ones use seed 1.

The failure pattern depends only on the seed and the failure parameters, so every variant
of a given seed routes over exactly the same failures, even though the variants were run
from four different LEOPath builds:

| variant | routing | build |
|---|---|---|
| `link_state` | shortest-path link-state | `ba2f20f` |
| `explicit_r1`, `explicit_r15` | explicit paths refreshed every 1 or 15 snapshots, with backup adjacencies | `ba2f20f` |
| `dra` | DRA hop-only forwarding | `ba2f20f` |
| `topological_nominal` | pivot geometry from the failure-free graph, no guard | `ba2f20f` |
| `topological_observed` | pivot geometry from the graph with failures | `ba2f20f` |
| `topological_nominal_progress`, `topological_observed_progress` | the two above plus the progress guard | `f1dd6d5` |
| `topological_nominal_progress_repair` | nominal geometry, guard, three-hop local repair | `3b927e7` |
| `topological_nominal_progress_exceptions` | nominal geometry, guard, exception entries | `2aea3c8` |
| `topological_nominal_progress_repair_exceptions` | nominal geometry, guard, local repair and exception entries | `2aea3c8` |

The later builds didn't touch the failure injection or how delivery and stretch are measured;
they added routing options and new counters. Runs from `f1dd6d5` on record their Docker image
tag as `code_version` in `metadata.json`.

`failure_sweep_seeds.csv` has one row per run, pooled over its snapshots.
`failure_sweep_summary.csv` combines the seeds of each constellation, condition and variant
into a mean and a 95% confidence half-width, and `failure_sweep_tables.md` renders it per
constellation: delivery, the delivery gap to link-state paired by seed, stretch, the dominant
failure cause, loops, and exception entries with their share of link-state's table. All three
come from `python -m leopath.experiments.summarize_failure_sweep --input <sweep> --output-dir <out>`;
the version that reads the exception counters is on LEOPath branch `feat/failure-injection`
after `2aea3c8`.

Some columns need a note:

- `live_minima_per_snapshot` counts local minima of the progress guard at satellites that still
  have a live link. Runs from `f1dd6d5` and `3b927e7` predate the fix that set dead satellites
  apart, so the script subtracts one decision per ground station per dead satellite for them.
  Every snapshot in this sweep had full ground visibility, and that makes the subtraction exact.
- `exception_entries_per_snapshot` is what the grow placement installs; entries go only where a
  walk breaks. `exception_entries_one_pass_per_snapshot` is its upper bound, one entry for every
  satellite whose rule-based walk fails.
- `exception_share_of_link_state` divides the installed entries by link-state's table size, one
  entry per satellite per ground station.
- `exception_hops_to_failure_mean` weights each entry's hop distance to the nearest satellite
  that lost a link.
- `failure_events_per_snapshot` counts failures that appeared or cleared since the previous
  snapshot, with the first snapshot counting every failure present. Only the `2aea3c8` runs
  report it, but since the pattern is shared, it holds for every variant of the same seed.
