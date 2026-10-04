# Revision data

Aggregated results of the evaluation campaigns run for the major revision of
COMNET-D-26-04044. The two main campaigns, `state_accounting/` and `failure_sweep/`, come from
one LEOPath build, `3efafaa`, on constellation configurations corrected against their FCC
filings: Starlink as 72 planes of 22 satellites rather than 22 of 72, mean motions that fly
the altitude each config declares, and OneWeb as 12 planes spread over 180 degrees of right
ascension the way it actually flies. The earlier results, and the configurations that
produced them, are preserved under the `pre-config-fix` tag in this repository and in LEOPath.
The focused campaigns that followed each name their own build below; every run's
`metadata.json` on the server keeps the image tag as `code_version`.

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

## `gs_multihoming/`

Superseded; kept for the record. A first multihoming sweep (LEOPath `591510e`, K = 1, 2, 4)
in which transit satellites could still minimise over all K of a station's attachments, so its
routing numbers are an optimistic any-attachment bound rather than one fixed address per
packet. `gs_address_policy/` replaces them. Its radio-assignment counts (attachments assigned,
shortfall under the exclusive policy) still stand.

## `gs_address_policy/`

Which of a multihomed station's K addresses its flows use, under one address per packet.

- Code: LEOPath `a41e5e7` (image `leopath:9d76b6c-perflow`), on `6genablers-dlt-1`,
  `~/leopath-addr-sweep-9d76b6c-perflow`. 312 runs, none failed.
- Matrix: four constellations, no failures and 5% ISL loss over seeds 1-5, link-state and
  topological routing, K = 1, 2, 4 under `sticky_nearest`, `nearest` and `per_flow_pair`.
- Every run walks fixed addresses (`fixed_address_forwarding` = 1) with no destination
  switching. Sticky K = 4 cuts ground-station renumbering by 32-45% per minute while stretch
  moves by -1% to +4%; `nearest` equals K = 1 whatever K is; only `per_flow_pair`, which goes
  beyond RINA, removes the stretch attachment addressing costs.

## `attach_robustness/`

The failure sweep repeated under attachment addressing, K = 1.

- Code: as `gs_address_policy/`; `~/leopath-attach-robustness-9d76b6c`. 1 024 runs, none
  failed.
- Matrix: four constellations, every failure condition of `failure_sweep/`, link-state with
  visibility and with attachment addressing, and the topological scheme (guard and exceptions,
  with and without the three-hop repair) under attachment addressing.
- The scheme delivers exactly what link-state delivers with the same addresses in all 64
  cells. Exception entries stay at 0.6-0.9% of link-state's table at 5% ISL loss. A cut drops
  both to 0.49-0.72, because a station's attachment satellite can sit across the partition;
  visibility addressing keeps 1.0 there.

## `derived_geometry/`

Measured against derived pivot geometry: every ISL length beyond the first hop computed from
the shell's Walker constants and the clock instead of taken from SGP4.

- Code: LEOPath `a41e5e7` plus the derived-geometry code committed in `afa14cb` (image
  `leopath:a41e5e7-derived`); `~/leopath-derived-gate-a41e5e7`. 1 536 runs, none failed; the
  256 `link_state` runs were copied in from `attach_robustness/`.
- Matrix: four constellations, every failure condition, topological routing with measured and
  derived geometry, plain and with the full scheme, under both address models.
- Deriving instead of measuring changes delivery of the full scheme by nothing and of the plain
  rule by at most 0.00044, and distance stretch by at most 0.0033. A satellite holds 7
  constants instead of one length per ISL.

## `shell_scaling/`

- `per_shell_state.csv`: 11 shells of Starlink Gen1, Kuiper and Starlink Gen2 as filed (LEOPath
  `leopath/config/shells/`), each run as its own layer with link-state, measured-geometry and
  derived-geometry topological routing, no failures, ten minutes. Code `afa14cb` (image
  `leopath:brick-dev2`), `~/leopath-shells-brickdev2`, 33 runs, none failed. Columns give the
  per-satellite FIB, link-state's LSDB, the geometry each topological variant needs a
  satellite to hold, the table cache and its build time, delivery and forwarding stretch.
- `pivot_benchmark.csv`: `scripts/benchmark_pivot_estimators.py` on all 12 shells, table build
  time, query time with and without tables, and a 200-pair agreement check (no mismatches).
  Measured on a loaded server; the timings only compare with each other.

## `brick_wall/`

Three laser terminals per satellite (LEOPath `docs/isl-topology.md`).

- Code: `afa14cb` (image `leopath:brick-dev2`), derived geometry, one hour at one-minute steps,
  every failure condition.
- `split_a/`: cross-plane links staggered, Starlink, Kuiper and OneWeb, 829 runs
  (`~/leopath-brick-sweep-a`). `split_b/`: in-plane links staggered, Starlink and Kuiper,
  512 runs (`~/leopath-brick-sweep-b`). None failed.
- Visibility link-state was dropped from the matrix partway through split a to free the
  server, so only some of its cells exist; every comparison uses `link_state_attach`.
- The scheme delivers what link-state delivers under attachment addressing and 1.0 under
  visibility addressing in every cell. The missing terminal costs exception state: 4.0-4.6% of
  link-state's table at 5% ISL loss against 0.6-0.9% on +Grid, about 21% at 20% loss.

## `celestrak/`

CelesTrak TLE snapshots of Starlink, OneWeb and Kuiper taken on 29 September 2026, with the
outputs of LEOPath's `scripts/celestrak_shell_geometry.py` (`regularity_20260929.txt`) and
`scripts/celestrak_lattice_fit.py` (`lattice_fit_20260929.txt`). Most of Starlink flies 80-90 km
below its filings in different plane counts; where shells have settled, planes are evenly
spaced and satellites sit within about 20 km of a slot lattice with empty slots.

## `end_to_end_delay/`

One-way propagation delay per delivered pair (path length over the speed of light, ground links included), its lower bound and the gap, in milliseconds. Queueing, processing and transmission delay are not modelled.

- Code: LEOPath `1a2b231` content (image `leopath:delay-dev`), `~/leopath-delay-sweep` on `6genablers-dlt-1`. 168 runs, none failed.
- Matrix: four constellations, no failures and 5% ISL loss over seeds 1-5, link-state with visibility and attachment addressing, topological with visibility addressing and the full scheme under attachment addressing, DRA, explicit-path replanned every 1 and 15 minutes.
- Without failures topological forwarding matches link-state to within 0.02 ms; DRA adds 1.4-4.0 ms and 15-minute explicit-path 7.6-10.6 ms. Attachment addressing adds 7-37 ms on average for link-state and topological alike.
- `attachment_analysis/`: outputs of LEOPath's `scripts/pass_direction_check.py` and `scripts/decompose_attachment_cost.py`, which trace that cost to the two halves of a Walker delta shell.

## `attachment_direction/`

Pass-direction-aware attachment and the `requester_aware` address policy.

- Code: LEOPath `1a2b231` (image `leopath:dir-dev`), `~/leopath-dir-sweep`. 192 runs, none failed.
- Matrix: four constellations, no failures and 5% ISL loss over seeds 1-5, link-state and topological (derived geometry, plain rule), K = 1 `nearest`, K = 1 `nearest_ascending`, K = 2 `one_per_half` with `sticky_nearest` and with `requester_aware`.
- `requester_aware` cuts the extra delay of attachment addressing by about 80% on delta shells (Starlink 36.7 to 8.2 ms mean) with fewer flow updates than K = 1. The K = 2 variants run without exceptions, so their delivery under failures is the plain rule's.

## `terminal_population/`

Ground-terminal population at the addressing level, no routing.

- `population_points.csv.gz`: North American census population points built by LEOPath's `scripts/fetch_population_points.py` from the US Census Bureau (2024 county estimates at 2024 Gazetteer points), INEGI (Censo 2020 localities) and Statistics Canada (2021 dissemination blocks at dissemination-area points). Totals match each census exactly; `SOURCES.txt` records each file's URL and SHA-256.
- `terminals_<shell>.csv`: `scripts/terminal_population.py` for five shells, 1k to 1M terminals, census-weighted and uniform, `nearest` and `stay_while_visible`, static and 250 km/h. Columns: busiest-satellite load, endpoint bits x needs, address changes per terminal-minute, directory updates per second. Run on `6genablers-dlt-1` with image `leopath:dir-dev`.

## `final_matrix/` and `brick_wall_matrix/`

Table 4 and Figure 11 of the revised manuscript, regenerated from the failure-free,
seed-1 runs of the final model with `scripts/matrix_from_sweep.py`, which links runs
written in the failure-sweep layout into the layout of LEOPath's
`state_accounting_tables` and runs it.

- `final_matrix/`: 120 runs, four constellations × ring, grid and grid_seam × ten
  variants, six hours at one-minute steps. Sources: Z (`dlt-1:~/leopath-final-matrix-*`:
  `link_state`, `link_state_dir_asc`, `explicit_r1`, `explicit_r3`,
  `topological_derived`, `topological_scheme_asc`), Z2 (`sna-13:~/sergio-dra-matrix-*`:
  `dra_scheme_asc`) and Z3, the realistic smart-directory rerun
  (`dlt-1:~/leopath-real-matrix-*`: `link_state_dir_half_req`, `dra_scheme_req`,
  `topological_scheme_req`).
- `brick_wall_matrix/`: 15 runs, three ISLs per satellite in layouts `brick_a`
  (Starlink, Kuiper, OneWeb) and `brick_b` (Starlink, Kuiper), one hour at one-minute
  steps, `link_state_dir_asc`, `topological_scheme_asc` and `topological_scheme_asc_1p`
  (`sna-12:~/sergio-brick-1p-brick_{a,b}`, `sna-13:~/sergio-brick-1p-brick_a`, image
  `leopath:final-1p`).

```
python scripts/matrix_from_sweep.py --leopath ~/phd/LEOPath \
    --sweep Z=final-matrix --sweep Z2=dra-matrix --sweep Z3=real-matrix \
    --pick Z:link_state,link_state_dir_asc,explicit_r1,explicit_r3,topological_derived,topological_scheme_asc \
    --pick Z2:dra_scheme_asc \
    --pick Z3:link_state_dir_half_req,dra_scheme_req,topological_scheme_req \
    --output revision/final_matrix
python scripts/matrix_from_sweep.py --leopath ~/phd/LEOPath --sweep B=brick --isl brick_a brick_b \
    --pick B:link_state_dir_asc,topological_scheme_asc,topological_scheme_asc_1p \
    --output revision/brick_wall_matrix
python plot_story_figures.py --final-matrix revision/final_matrix/matrix_runs.csv \
    --brick-matrix revision/brick_wall_matrix/matrix_runs.csv   # in ntn-paper-overleaf
```

Forwarding stretch, shared stretch and extra delay in Table 4 come from the sweep
summaries in `realistic_directory_runs/` (`z_final/` and the Z3 rerun) and, for the brick
wall, from `summarize_failure_sweep` over the same runs.

## `attachment_count/`

How the number of attachments per station changes reachability on Ring and the cost of
attachment addressing on +Grid. Four constellations × K = 1, 2, 3, 4, 6, 8 nearest
attachments (`gs_attachment_order: nearest`, `gs_address_policy: requester_aware`, so the
destination answers each flow request with an address the requester can reach), full
scheme with derived geometry, guard and grow exceptions; failure-free, seed 1, six hours
at one-minute steps. LEOPath `ad92b9b` (variants `topological_k{K}_req` in
`scripts/run-failure-sweep.sh`), image `leopath:final-1p`. Ring on `sna-12:~/sergio-ksweep-ring`,
+Grid on `dlt-1:~/ksweep-grid`; summaries by `summarize_failure_sweep`.
