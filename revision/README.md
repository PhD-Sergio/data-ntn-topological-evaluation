# Revision data

Aggregated results of the two evaluation campaigns run for the major revision of
COMNET-D-26-04044. Every run here comes from one LEOPath build, `3efafaa`, on constellation
configurations corrected against their FCC filings: Starlink as 72 planes of 22 satellites
rather than 22 of 72, mean motions that fly the altitude each config declares, and OneWeb as
12 planes spread over 180 degrees of right ascension the way it actually flies. The earlier
results, and the configurations that produced them, are preserved under the `pre-config-fix`
tag in this repository and in LEOPath.

The state-accounting campaign's raw per-run outputs are the ones in this repository's root.
The failure sweep's 2 816 raw run directories stay on the evaluation server; only its
aggregates are here.

Rates are pooled over each run's snapshots (delivered pairs over deliverable pairs)
and stretch is weighted by the pairs it was measured over.

## `state_accounting/`

Re-run of the evaluation matrix with state accounting.

- Code: LEOPath `3efafaa`.
- Matrix: Telesat, OneWeb, Kuiper, Starlink × topological (pivot), DRA, explicit path,
  link-state × Ring, +Grid, +Grid open seam. Six hours at one-minute steps, 24 ground
  stations (`ground_stations_dense`), 552 ordered pairs.
- `summary.csv`: `python -m leopath.experiments.aggregate_eval`, same format as the
  dataset's root `summary.csv`. These are the same runs as the repository root, so the root
  `summary.csv` supersedes this copy and the two agree.
- `matrix_runs.csv`, `matrix_tables.md`: `python -m leopath.experiments.state_accounting_tables`.

## `failure_sweep/`

Robustness sweep with injected failures, on +Grid for one hour at one-minute steps with the
same 24 ground stations.

The conditions go from mild to structural. ISL loss drops single laser links at stationary
rates of 1, 2, 5, 10 and 20% (mean outage 10 min), and satellite outage takes whole satellites
down, with every link they had, at 0.5, 1, 2 and 5% (mean outage 60 min). A void kills a square
block of neighbouring satellites, 2×2, 4×4 or 8×8, for the whole hour; topological forwarding
finds it hard because the distance estimate still points through the hole. A cut removes every
inter-plane link across two opposite plane boundaries, so the grid splits into two halves that no
link joins even though every satellite keeps working. Polar deactivation switches off inter-plane
links above 75° or 60° latitude and only bites on Telesat and OneWeb, since Starlink and Kuiper
stay below 60°. Random conditions use seeds 1 to 5 and deterministic ones seed 1. LEOPath's
`docs/evaluation.md` has diagrams of the void and the cut, and the failure causes behind
`failure_share_*`.

The failure pattern depends only on the seed and the failure parameters, so every variant of a
given seed routes over exactly the same failures. The variants differ only in how they forward:

| variant | routing |
|---|---|
| `link_state` | shortest-path link-state |
| `explicit_r1`, `explicit_r15` | explicit paths refreshed every 1 or 15 snapshots, with backup adjacencies |
| `dra` | DRA hop-only forwarding |
| `topological_nominal` | pivot geometry from the failure-free graph, no guard |
| `topological_observed` | pivot geometry from the graph with failures |
| `topological_nominal_progress`, `topological_observed_progress` | the two above plus the progress guard |
| `topological_nominal_progress_repair` | nominal geometry, guard, three-hop local repair |
| `topological_nominal_progress_exceptions` | nominal geometry, guard, exception entries |
| `topological_nominal_progress_repair_exceptions` | nominal geometry, guard, local repair and exception entries |

Every run records its Docker image tag as `code_version` in `metadata.json`.

`failure_sweep_seeds.csv` has one row per run, pooled over its snapshots.
`failure_sweep_summary.csv` combines the seeds of each constellation, condition and variant
into a mean and a 95% confidence half-width, and `failure_sweep_tables.md` renders it per
constellation: delivery, the delivery gap to link-state paired by seed, stretch, the dominant
failure cause, loops, and exception entries with their share of link-state's table. All three come from
`python -m leopath.experiments.summarize_failure_sweep --input <sweep> --output-dir <out>`.

Some columns need a note:

- `live_minima_per_snapshot` counts local minima of the progress guard at satellites that still
  have a live link. Decisions at satellites with no live link are counted apart, so no correction
  is applied to these runs.
- `exception_entries_per_snapshot` is what the grow placement installs; entries go only where a
  walk breaks. `exception_entries_one_pass_per_snapshot` is its upper bound, one entry for every
  satellite whose rule-based walk fails.
- `exception_share_of_link_state` divides the installed entries by link-state's table size, one
  entry per satellite per ground station.
- `exception_hops_to_failure_mean` weights each entry's hop distance to the nearest satellite
  that lost a link.
- `failure_events_per_snapshot` counts failures that appeared or cleared since the previous
  snapshot, with the first snapshot counting every failure present.
