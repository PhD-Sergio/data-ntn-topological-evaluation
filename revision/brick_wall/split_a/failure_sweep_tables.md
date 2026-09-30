# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 100.0 | 99.5 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 92.0 ± 3.3 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 85.8 ± 1.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.1 | 70.1 ± 2.9 | 100.0 ± 0.1 | 100.0 ± 0.0 |
| isl_p0.10 | 99.7 ± 0.2 | 48.8 ± 3.4 | 99.7 ± 0.2 | 100.0 ± 0.0 |
| isl_p0.20 | 97.7 ± 1.3 | 27.9 ± 2.1 | 97.7 ± 1.3 | 100.0 ± 0.0 |
| sat_p0.005 | 100.0 ± 0.0 | 95.3 ± 2.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 93.3 ± 3.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 83.9 ± 2.3 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.1 | 69.5 ± 4.8 | 100.0 ± 0.1 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 96.1 ± 2.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 92.2 ± 5.5 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 89.2 ± 6.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 57.5 | 93.3 | 57.5 | 100.0 |
| polar_lat75 | 100.0 | 97.3 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 82.2 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.2449 | 1.0320 | 1.2845 | 1.0317 |
| isl_p0.01 | 1.2468 | 1.0313 | 1.2919 | 1.0331 |
| isl_p0.02 | 1.2496 | 1.0309 | 1.3001 | 1.0350 |
| isl_p0.05 | 1.2597 | 1.0280 | 1.3228 | 1.0378 |
| isl_p0.10 | 1.2821 | 1.0224 | 1.3583 | 1.0451 |
| isl_p0.20 | 1.3620 | 1.0104 | 1.4484 | 1.0491 |
| sat_p0.005 | 1.2459 | 1.0317 | 1.2880 | 1.0324 |
| sat_p0.01 | 1.2472 | 1.0316 | 1.2913 | 1.0325 |
| sat_p0.02 | 1.2516 | 1.0297 | 1.3004 | 1.0335 |
| sat_p0.05 | 1.2588 | 1.0270 | 1.3154 | 1.0365 |
| void_b2 | 1.2457 | 1.0317 | 1.2873 | 1.0322 |
| void_b4 | 1.2459 | 1.0304 | 1.2881 | 1.0328 |
| void_b8 | 1.2384 | 1.0306 | 1.2864 | 1.0363 |
| cut | 1.1752 | 1.0238 | 1.2059 | 1.0260 |
| polar_lat75 | 1.2696 | 1.0179 | 1.2993 | 1.0180 |
| polar_lat60 | 1.2963 | 1.0165 | 1.3447 | 1.0238 |

### Distance stretch, egress-choice factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.245 | 1.008 | 1.245 | 1.008 |
| isl_p0.01 | 1.247 | 1.008 | 1.247 | 1.009 |
| isl_p0.02 | 1.250 | 1.008 | 1.250 | 1.009 |
| isl_p0.05 | 1.260 | 1.008 | 1.260 | 1.010 |
| isl_p0.10 | 1.282 | 1.008 | 1.282 | 1.012 |
| isl_p0.20 | 1.362 | 1.005 | 1.362 | 1.012 |
| sat_p0.005 | 1.246 | 1.008 | 1.246 | 1.008 |
| sat_p0.01 | 1.247 | 1.009 | 1.247 | 1.009 |
| sat_p0.02 | 1.252 | 1.008 | 1.252 | 1.009 |
| sat_p0.05 | 1.259 | 1.008 | 1.259 | 1.010 |
| void_b2 | 1.246 | 1.008 | 1.246 | 1.008 |
| void_b4 | 1.246 | 1.008 | 1.246 | 1.009 |
| void_b8 | 1.238 | 1.008 | 1.238 | 1.009 |
| cut | 1.175 | 1.005 | 1.175 | 1.005 |
| polar_lat75 | 1.270 | 1.005 | 1.270 | 1.005 |
| polar_lat60 | 1.296 | 1.004 | 1.296 | 1.007 |

### Distance stretch, forwarding factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.000 | 1.023 | 1.034 | 1.023 |
| isl_p0.01 | 1.000 | 1.023 | 1.038 | 1.024 |
| isl_p0.02 | 1.000 | 1.022 | 1.042 | 1.026 |
| isl_p0.05 | 1.000 | 1.019 | 1.051 | 1.027 |
| isl_p0.10 | 1.000 | 1.015 | 1.061 | 1.033 |
| isl_p0.20 | 1.000 | 1.006 | 1.065 | 1.036 |
| sat_p0.005 | 1.000 | 1.023 | 1.036 | 1.024 |
| sat_p0.01 | 1.000 | 1.023 | 1.037 | 1.024 |
| sat_p0.02 | 1.000 | 1.021 | 1.041 | 1.025 |
| sat_p0.05 | 1.000 | 1.019 | 1.046 | 1.026 |
| void_b2 | 1.000 | 1.023 | 1.035 | 1.024 |
| void_b4 | 1.000 | 1.022 | 1.036 | 1.024 |
| void_b8 | 1.000 | 1.023 | 1.041 | 1.027 |
| cut | 1.000 | 1.019 | 1.027 | 1.021 |
| polar_lat75 | 1.000 | 1.012 | 1.022 | 1.012 |
| polar_lat60 | 1.000 | 1.012 | 1.033 | 1.016 |

### Ground station renumberings per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | 0.0 | 11.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 11.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 11.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 11.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 11.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 11.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 10.9 | 0.0 |
| sat_p0.01 | — | 0.0 | 10.9 | 0.0 |
| sat_p0.02 | — | 0.0 | 10.8 | 0.0 |
| sat_p0.05 | — | 0.0 | 10.6 | 0.0 |
| void_b2 | — | 0.0 | 10.9 | 0.0 |
| void_b4 | — | 0.0 | 10.8 | 0.0 |
| void_b8 | — | 0.0 | 10.3 | 0.0 |
| cut | — | 0.0 | 11.0 | 0.0 |
| polar_lat75 | — | 0.0 | 11.0 | 0.0 |
| polar_lat60 | — | 0.0 | 11.0 | 0.0 |

### Assigned ground-station links per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 24.0 | — | 24.0 | — |
| isl_p0.01 | 24.0 | — | 24.0 | — |
| isl_p0.02 | 24.0 | — | 24.0 | — |
| isl_p0.05 | 24.0 | — | 24.0 | — |
| isl_p0.10 | 24.0 | — | 24.0 | — |
| isl_p0.20 | 24.0 | — | 24.0 | — |
| sat_p0.005 | 24.0 | — | 24.0 | — |
| sat_p0.01 | 24.0 | — | 24.0 | — |
| sat_p0.02 | 24.0 | — | 24.0 | — |
| sat_p0.05 | 24.0 | — | 24.0 | — |
| void_b2 | 24.0 | — | 24.0 | — |
| void_b4 | 24.0 | — | 24.0 | — |
| void_b8 | 23.4 | — | 23.4 | — |
| cut | 24.0 | — | 24.0 | — |
| polar_lat75 | 24.0 | — | 24.0 | — |
| polar_lat60 | 24.0 | — | 24.0 | — |

### Requested attachment shortfall per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | — | 0.0 | — |
| isl_p0.01 | 0.0 | — | 0.0 | — |
| isl_p0.02 | 0.0 | — | 0.0 | — |
| isl_p0.05 | 0.0 | — | 0.0 | — |
| isl_p0.10 | 0.0 | — | 0.0 | — |
| isl_p0.20 | 0.0 | — | 0.0 | — |
| sat_p0.005 | 0.0 | — | 0.0 | — |
| sat_p0.01 | 0.0 | — | 0.0 | — |
| sat_p0.02 | 0.0 | — | 0.0 | — |
| sat_p0.05 | 0.0 | — | 0.0 | — |
| void_b2 | 0.0 | — | 0.0 | — |
| void_b4 | 0.0 | — | 0.0 | — |
| void_b8 | 0.6 | — | 0.6 | — |
| cut | 0.0 | — | 0.0 | — |
| polar_lat75 | 0.0 | — | 0.0 | — |
| polar_lat60 | 0.0 | — | 0.0 | — |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.5 | — | 1.5 | — |
| isl_p0.01 | 1.5 | — | 1.5 | — |
| isl_p0.02 | 1.5 | — | 1.5 | — |
| isl_p0.05 | 1.5 | — | 1.5 | — |
| isl_p0.10 | 1.5 | — | 1.5 | — |
| isl_p0.20 | 1.5 | — | 1.5 | — |
| sat_p0.005 | 1.5 | — | 1.5 | — |
| sat_p0.01 | 1.5 | — | 1.5 | — |
| sat_p0.02 | 1.6 | — | 1.6 | — |
| sat_p0.05 | 1.5 | — | 1.5 | — |
| void_b2 | 1.5 | — | 1.5 | — |
| void_b4 | 1.6 | — | 1.6 | — |
| void_b8 | 1.7 | — | 1.7 | — |
| cut | 1.5 | — | 1.5 | — |
| polar_lat75 | 1.5 | — | 1.5 | — |
| polar_lat60 | 1.5 | — | 1.5 | — |

### Transit egress switches, %

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 1.6 | 0.0 | 2.1 |
| isl_p0.01 | 0.0 | 2.7 | 0.0 | 6.4 |
| isl_p0.02 | 0.0 | 3.9 | 0.0 | 10.1 |
| isl_p0.05 | 0.0 | 7.2 | 0.0 | 19.6 |
| isl_p0.10 | 0.0 | 11.3 | 0.0 | 32.3 |
| isl_p0.20 | 0.0 | 13.3 | 0.0 | 48.1 |
| sat_p0.005 | 0.0 | 2.4 | 0.0 | 4.7 |
| sat_p0.01 | 0.0 | 2.8 | 0.0 | 6.2 |
| sat_p0.02 | 0.0 | 4.6 | 0.0 | 11.6 |
| sat_p0.05 | 0.0 | 6.5 | 0.0 | 19.6 |
| void_b2 | 0.0 | 2.1 | 0.0 | 4.3 |
| void_b4 | 0.0 | 2.1 | 0.0 | 6.6 |
| void_b8 | 0.0 | 2.9 | 0.0 | 9.2 |
| cut | 0.0 | 2.4 | 0.0 | 9.0 |
| polar_lat75 | 0.0 | 1.9 | 0.0 | 4.4 |
| polar_lat60 | 0.0 | 2.1 | 0.0 | 17.2 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | loop 100% | — | — |
| isl_p0.01 | — | loop 100% | — | — |
| isl_p0.02 | — | loop 100% | — | — |
| isl_p0.05 | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.10 | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.20 | dead_end 100% | loop 100% | dead_end 100% | — |
| sat_p0.005 | — | loop 100% | — | — |
| sat_p0.01 | — | loop 100% | — | — |
| sat_p0.02 | — | loop 100% | — | — |
| sat_p0.05 | dead_end 100% | loop 100% | dead_end 100% | — |
| void_b2 | — | loop 100% | — | — |
| void_b4 | — | loop 100% | — | — |
| void_b8 | — | loop 100% | — | — |
| cut | dead_end 100% | loop 100% | dead_end 100% | — |
| polar_lat75 | — | loop 100% | — | — |
| polar_lat60 | — | loop 100% | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 3.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 44.4 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 78.6 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 164.9 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 281.6 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 390.1 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 25.9 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 36.8 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 88.8 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 168.5 | 0.0 | 0.0 |
| void_b2 | 0.0 | 21.4 | 0.0 | 0.0 |
| void_b4 | 0.0 | 43.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 56.2 | 0.0 | 0.0 |
| cut | 0.0 | 23.3 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 14.6 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 98.4 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 8.4 (239) | 2.5 (33) |
| isl_p0.01 | — | — | 125.0 (1891) | 109.3 (1178) |
| isl_p0.02 | — | — | 238.3 (3281) | 207.3 (2049) |
| isl_p0.05 | — | — | 620.1 (6608) | 562.8 (4525) |
| isl_p0.10 | — | — | 1393.8 (9904) | 1289.1 (7770) |
| isl_p0.20 | — | — | 2996.9 (11988) | 2857.1 (10648) |
| sat_p0.005 | — | — | 74.3 (1202) | 62.2 (647) |
| sat_p0.01 | — | — | 108.4 (1698) | 94.8 (1003) |
| sat_p0.02 | — | — | 252.4 (3574) | 224.1 (2186) |
| sat_p0.05 | — | — | 646.7 (6408) | 597.0 (4578) |
| void_b2 | — | — | 48.6 (806) | 41.0 (468) |
| void_b4 | — | — | 93.9 (1382) | 82.7 (983) |
| void_b8 | — | — | 201.3 (1897) | 189.0 (1489) |
| cut | — | — | 3.6 (37) | 51.6 (240) |
| polar_lat75 | — | — | 197.8 (1170) | 84.0 (418) |
| polar_lat60 | — | — | 470.2 (3201) | 263.7 (1914) |

### Exception entries, % of link-state forwarding entries

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.06 | 0.02 |
| isl_p0.01 | — | — | 0.89 | 0.77 |
| isl_p0.02 | — | — | 1.69 | 1.47 |
| isl_p0.05 | — | — | 4.39 | 3.99 |
| isl_p0.10 | — | — | 9.88 | 9.13 |
| isl_p0.20 | — | — | 21.24 | 20.25 |
| sat_p0.005 | — | — | 0.53 | 0.44 |
| sat_p0.01 | — | — | 0.77 | 0.67 |
| sat_p0.02 | — | — | 1.79 | 1.59 |
| sat_p0.05 | — | — | 4.58 | 4.23 |
| void_b2 | — | — | 0.34 | 0.29 |
| void_b4 | — | — | 0.67 | 0.59 |
| void_b8 | — | — | 1.43 | 1.34 |
| cut | — | — | 0.03 | 0.37 |
| polar_lat75 | — | — | 1.40 | 0.60 |
| polar_lat60 | — | — | 3.33 | 1.87 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 94.0 ± 1.2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 87.7 ± 1.5 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 71.6 ± 2.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 99.8 ± 0.2 | 51.1 ± 1.8 | 99.8 ± 0.2 | 100.0 ± 0.0 |
| isl_p0.20 | 98.3 ± 0.5 | 25.6 ± 1.2 | 98.3 ± 0.5 | 100.0 ± 0.0 |
| sat_p0.005 | 100.0 ± 0.0 | 96.7 ± 1.3 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 95.9 ± 1.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 90.2 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 99.9 ± 0.2 | 72.3 ± 2.5 | 99.9 ± 0.2 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 99.1 ± 0.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 98.3 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 97.0 ± 1.2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 53.9 | 81.5 | 53.9 | 100.0 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.8441 | 1.0214 | 1.8916 | 1.0214 |
| isl_p0.01 | 1.8470 | 1.0223 | 1.9107 | 1.0262 |
| isl_p0.02 | 1.8503 | 1.0230 | 1.9299 | 1.0305 |
| isl_p0.05 | 1.8619 | 1.0244 | 1.9776 | 1.0415 |
| isl_p0.10 | 1.8887 | 1.0225 | 2.0422 | 1.0548 |
| isl_p0.20 | 2.0078 | 1.0128 | 2.1917 | 1.0612 |
| sat_p0.005 | 1.8450 | 1.0222 | 1.9015 | 1.0240 |
| sat_p0.01 | 1.8444 | 1.0221 | 1.9028 | 1.0241 |
| sat_p0.02 | 1.8468 | 1.0229 | 1.9199 | 1.0284 |
| sat_p0.05 | 1.8526 | 1.0239 | 1.9578 | 1.0382 |
| void_b2 | 1.8434 | 1.0214 | 1.8929 | 1.0218 |
| void_b4 | 1.8402 | 1.0214 | 1.8908 | 1.0224 |
| void_b8 | 1.8024 | 1.0216 | 1.8563 | 1.0237 |
| cut | 1.4987 | 1.0186 | 1.5354 | 1.0697 |
| polar_lat75 | 1.8441 | 1.0214 | 1.8916 | 1.0214 |
| polar_lat60 | 1.8441 | 1.0214 | 1.8916 | 1.0214 |

### Distance stretch, egress-choice factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.844 | 1.004 | 1.844 | 1.004 |
| isl_p0.01 | 1.847 | 1.004 | 1.847 | 1.005 |
| isl_p0.02 | 1.850 | 1.005 | 1.850 | 1.006 |
| isl_p0.05 | 1.862 | 1.006 | 1.862 | 1.009 |
| isl_p0.10 | 1.889 | 1.006 | 1.889 | 1.012 |
| isl_p0.20 | 2.008 | 1.005 | 2.008 | 1.015 |
| sat_p0.005 | 1.845 | 1.004 | 1.845 | 1.005 |
| sat_p0.01 | 1.844 | 1.004 | 1.844 | 1.005 |
| sat_p0.02 | 1.847 | 1.005 | 1.847 | 1.006 |
| sat_p0.05 | 1.853 | 1.005 | 1.853 | 1.008 |
| void_b2 | 1.843 | 1.004 | 1.843 | 1.004 |
| void_b4 | 1.840 | 1.004 | 1.840 | 1.004 |
| void_b8 | 1.802 | 1.004 | 1.802 | 1.004 |
| cut | 1.499 | 1.004 | 1.499 | 1.004 |
| polar_lat75 | 1.844 | 1.004 | 1.844 | 1.004 |
| polar_lat60 | 1.844 | 1.004 | 1.844 | 1.004 |

### Distance stretch, forwarding factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.000 | 1.017 | 1.029 | 1.017 |
| isl_p0.01 | 1.000 | 1.018 | 1.037 | 1.021 |
| isl_p0.02 | 1.000 | 1.018 | 1.045 | 1.024 |
| isl_p0.05 | 1.000 | 1.019 | 1.063 | 1.032 |
| isl_p0.10 | 1.000 | 1.016 | 1.081 | 1.042 |
| isl_p0.20 | 1.000 | 1.008 | 1.089 | 1.046 |
| sat_p0.005 | 1.000 | 1.018 | 1.033 | 1.019 |
| sat_p0.01 | 1.000 | 1.018 | 1.034 | 1.019 |
| sat_p0.02 | 1.000 | 1.018 | 1.041 | 1.023 |
| sat_p0.05 | 1.000 | 1.018 | 1.057 | 1.030 |
| void_b2 | 1.000 | 1.017 | 1.030 | 1.018 |
| void_b4 | 1.000 | 1.017 | 1.030 | 1.018 |
| void_b8 | 1.000 | 1.017 | 1.032 | 1.019 |
| cut | 1.000 | 1.015 | 1.026 | 1.065 |
| polar_lat75 | 1.000 | 1.017 | 1.029 | 1.017 |
| polar_lat60 | 1.000 | 1.017 | 1.029 | 1.017 |

### Ground station renumberings per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | 0.0 | 16.8 | 0.0 |
| isl_p0.01 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.02 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.05 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.10 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.20 | — | 0.0 | 16.8 | 0.0 |
| sat_p0.005 | — | 0.0 | 16.8 | 0.0 |
| sat_p0.01 | — | 0.0 | 16.7 | 0.0 |
| sat_p0.02 | — | 0.0 | 16.6 | 0.0 |
| sat_p0.05 | — | 0.0 | 16.2 | 0.0 |
| void_b2 | — | 0.0 | 16.8 | 0.0 |
| void_b4 | — | 0.0 | 16.7 | 0.0 |
| void_b8 | — | 0.0 | 16.2 | 0.0 |
| cut | — | 0.0 | 16.8 | 0.0 |
| polar_lat75 | — | 0.0 | 16.8 | 0.0 |
| polar_lat60 | — | 0.0 | 16.8 | 0.0 |

### Assigned ground-station links per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 24.0 | — | 24.0 | — |
| isl_p0.01 | 24.0 | — | 24.0 | — |
| isl_p0.02 | 24.0 | — | 24.0 | — |
| isl_p0.05 | 24.0 | — | 24.0 | — |
| isl_p0.10 | 24.0 | — | 24.0 | — |
| isl_p0.20 | 24.0 | — | 24.0 | — |
| sat_p0.005 | 24.0 | — | 24.0 | — |
| sat_p0.01 | 24.0 | — | 24.0 | — |
| sat_p0.02 | 24.0 | — | 24.0 | — |
| sat_p0.05 | 24.0 | — | 24.0 | — |
| void_b2 | 24.0 | — | 24.0 | — |
| void_b4 | 24.0 | — | 24.0 | — |
| void_b8 | 24.0 | — | 24.0 | — |
| cut | 24.0 | — | 24.0 | — |
| polar_lat75 | 24.0 | — | 24.0 | — |
| polar_lat60 | 24.0 | — | 24.0 | — |

### Requested attachment shortfall per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | — | 0.0 | — |
| isl_p0.01 | 0.0 | — | 0.0 | — |
| isl_p0.02 | 0.0 | — | 0.0 | — |
| isl_p0.05 | 0.0 | — | 0.0 | — |
| isl_p0.10 | 0.0 | — | 0.0 | — |
| isl_p0.20 | 0.0 | — | 0.0 | — |
| sat_p0.005 | 0.0 | — | 0.0 | — |
| sat_p0.01 | 0.0 | — | 0.0 | — |
| sat_p0.02 | 0.0 | — | 0.0 | — |
| sat_p0.05 | 0.0 | — | 0.0 | — |
| void_b2 | 0.0 | — | 0.0 | — |
| void_b4 | 0.0 | — | 0.0 | — |
| void_b8 | 0.0 | — | 0.0 | — |
| cut | 0.0 | — | 0.0 | — |
| polar_lat75 | 0.0 | — | 0.0 | — |
| polar_lat60 | 0.0 | — | 0.0 | — |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.4 | — | 0.4 | — |
| isl_p0.01 | 0.4 | — | 0.4 | — |
| isl_p0.02 | 0.4 | — | 0.4 | — |
| isl_p0.05 | 0.4 | — | 0.4 | — |
| isl_p0.10 | 0.4 | — | 0.4 | — |
| isl_p0.20 | 0.4 | — | 0.4 | — |
| sat_p0.005 | 0.4 | — | 0.4 | — |
| sat_p0.01 | 0.4 | — | 0.4 | — |
| sat_p0.02 | 0.4 | — | 0.4 | — |
| sat_p0.05 | 0.4 | — | 0.4 | — |
| void_b2 | 0.4 | — | 0.4 | — |
| void_b4 | 0.4 | — | 0.4 | — |
| void_b8 | 0.5 | — | 0.5 | — |
| cut | 0.4 | — | 0.4 | — |
| polar_lat75 | 0.4 | — | 0.4 | — |
| polar_lat60 | 0.4 | — | 0.4 | — |

### Transit egress switches, %

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 1.4 | 0.0 | 3.8 |
| isl_p0.02 | 0.0 | 2.8 | 0.0 | 7.5 |
| isl_p0.05 | 0.0 | 6.9 | 0.0 | 16.4 |
| isl_p0.10 | 0.0 | 10.2 | 0.0 | 26.0 |
| isl_p0.20 | 0.0 | 14.3 | 0.0 | 42.2 |
| sat_p0.005 | 0.0 | 0.8 | 0.0 | 1.9 |
| sat_p0.01 | 0.0 | 1.1 | 0.0 | 2.4 |
| sat_p0.02 | 0.0 | 2.4 | 0.0 | 5.5 |
| sat_p0.05 | 0.0 | 5.8 | 0.0 | 14.0 |
| void_b2 | 0.0 | 0.2 | 0.0 | 0.5 |
| void_b4 | 0.0 | 0.2 | 0.0 | 0.7 |
| void_b8 | 0.0 | 0.4 | 0.0 | 1.3 |
| cut | 0.0 | 2.6 | 0.0 | 20.7 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | — |
| isl_p0.02 | — | loop 100% | — | — |
| isl_p0.05 | — | loop 100% | — | — |
| isl_p0.10 | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.20 | dead_end 100% | loop 100% | dead_end 100% | — |
| sat_p0.005 | — | loop 100% | — | — |
| sat_p0.01 | — | loop 100% | — | — |
| sat_p0.02 | — | loop 100% | — | — |
| sat_p0.05 | dead_end 100% | loop 100% | dead_end 100% | — |
| void_b2 | — | loop 100% | — | — |
| void_b4 | — | loop 100% | — | — |
| void_b8 | — | loop 100% | — | — |
| cut | dead_end 100% | loop 100% | dead_end 100% | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 33.2 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 67.8 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 156.9 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 269.3 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 404.1 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 18.4 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 22.6 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 54.1 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 152.7 | 0.0 | 0.0 |
| void_b2 | 0.0 | 5.2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 9.5 | 0.0 | 0.0 |
| void_b8 | 0.0 | 16.5 | 0.0 | 0.0 |
| cut | 0.0 | 93.2 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 212.6 (3926) | 196.7 (2153) |
| isl_p0.02 | — | — | 473.4 (7472) | 447.5 (4382) |
| isl_p0.05 | — | — | 1272.5 (15329) | 1196.6 (9901) |
| isl_p0.10 | — | — | 2619.6 (21264) | 2480.6 (15671) |
| isl_p0.20 | — | — | 6141.2 (24893) | 5904.8 (21718) |
| sat_p0.005 | — | — | 142.7 (2571) | 134.6 (1398) |
| sat_p0.01 | — | — | 171.7 (3119) | 162.2 (1639) |
| sat_p0.02 | — | — | 428.4 (6883) | 396.6 (3753) |
| sat_p0.05 | — | — | 1210.4 (13923) | 1150.2 (9075) |
| void_b2 | — | — | 37.8 (750) | 37.9 (432) |
| void_b4 | — | — | 75.7 (1210) | 74.3 (753) |
| void_b8 | — | — | 159.7 (1911) | 141.6 (1247) |
| cut | — | — | 0.0 (0) | 628.6 (3626) |
| polar_lat75 | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.77 | 0.71 |
| isl_p0.02 | — | — | 1.71 | 1.61 |
| isl_p0.05 | — | — | 4.59 | 4.31 |
| isl_p0.10 | — | — | 9.44 | 8.94 |
| isl_p0.20 | — | — | 22.14 | 21.28 |
| sat_p0.005 | — | — | 0.51 | 0.49 |
| sat_p0.01 | — | — | 0.62 | 0.58 |
| sat_p0.02 | — | — | 1.54 | 1.43 |
| sat_p0.05 | — | — | 4.36 | 4.15 |
| void_b2 | — | — | 0.14 | 0.14 |
| void_b4 | — | — | 0.27 | 0.27 |
| void_b8 | — | — | 0.58 | 0.51 |
| cut | — | — | 0.00 | 2.27 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 90.6 ± 2.7 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 81.7 ± 3.2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 62.0 ± 1.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 99.8 ± 0.2 | 42.1 ± 1.7 | 99.8 ± 0.2 | 100.0 ± 0.0 |
| isl_p0.20 | 100.0 ± 0.0 | 98.0 ± 0.6 | 22.1 ± 0.4 | 98.0 ± 0.6 | 100.0 ± 0.0 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 95.0 ± 2.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 89.7 ± 3.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 83.0 ± 3.2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 64.7 ± 3.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 98.6 ± 0.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 97.2 ± 1.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 95.6 ± 2.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 53.0 | 84.4 | 53.0 | 100.0 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +9.4 ± 2.7 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +18.3 ± 3.2 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +38.0 ± 1.8 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +0.2 ± 0.2 | +57.9 ± 1.7 | +0.2 ± 0.2 | +0.0 ± 0.0 |
| isl_p0.20 | +0.0 ± 0.0 | +2.0 ± 0.6 | +77.9 ± 0.4 | +2.0 ± 0.6 | +0.0 ± 0.0 |
| sat_p0.005 | +0.0 ± 0.0 | +0.0 ± 0.0 | +5.0 ± 2.4 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +10.3 ± 3.8 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +17.0 ± 3.2 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +35.3 ± 3.4 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +1.4 ± 0.6 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +2.8 ± 1.4 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +3.7 ± 11.7 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +47.0 | +15.6 | +47.0 | +0.0 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | 1.0000 | 3.0748 | 1.0041 | 3.0856 | 1.0041 |
| isl_p0.01 | 1.0000 | 3.0695 | 1.0060 | 3.1079 | 1.0124 |
| isl_p0.02 | 1.0000 | 3.0647 | 1.0072 | 3.1280 | 1.0198 |
| isl_p0.05 | 1.0000 | 3.0469 | 1.0103 | 3.1905 | 1.0394 |
| isl_p0.10 | 1.0000 | 3.0170 | 1.0114 | 3.2733 | 1.0633 |
| isl_p0.20 | 1.0000 | 3.0854 | 1.0086 | 3.4705 | 1.0790 |
| sat_p0.005 | 1.0000 | 3.0674 | 1.0050 | 3.0901 | 1.0079 |
| sat_p0.01 | 1.0000 | 3.0640 | 1.0058 | 3.0998 | 1.0117 |
| sat_p0.02 | 1.0000 | 3.0547 | 1.0072 | 3.1130 | 1.0175 |
| sat_p0.05 | 1.0000 | 3.0312 | 1.0100 | 3.1508 | 1.0345 |
| void_b2 | 1.0000 | 3.0731 | 1.0042 | 3.0870 | 1.0049 |
| void_b4 | 1.0000 | 3.0641 | 1.0043 | 3.0825 | 1.0060 |
| void_b8 | 1.0000 | 2.9640 | 1.0042 | 2.9889 | 1.0077 |
| cut | 1.0000 | 2.1724 | 1.0039 | 2.1816 | 1.0447 |
| polar_lat75 | 1.0000 | 3.0748 | 1.0041 | 3.0856 | 1.0041 |
| polar_lat60 | 1.0000 | 3.0748 | 1.0041 | 3.0856 | 1.0041 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | 1.000 | 3.075 | 1.001 | 3.075 | 1.001 |
| isl_p0.01 | 1.000 | 3.070 | 1.001 | 3.070 | 1.002 |
| isl_p0.02 | 1.000 | 3.065 | 1.001 | 3.065 | 1.003 |
| isl_p0.05 | 1.000 | 3.047 | 1.002 | 3.047 | 1.005 |
| isl_p0.10 | 1.000 | 3.017 | 1.003 | 3.017 | 1.007 |
| isl_p0.20 | 1.000 | 3.085 | 1.004 | 3.085 | 1.009 |
| sat_p0.005 | 1.000 | 3.067 | 1.001 | 3.067 | 1.001 |
| sat_p0.01 | 1.000 | 3.064 | 1.001 | 3.064 | 1.002 |
| sat_p0.02 | 1.000 | 3.055 | 1.001 | 3.055 | 1.002 |
| sat_p0.05 | 1.000 | 3.031 | 1.002 | 3.031 | 1.003 |
| void_b2 | 1.000 | 3.073 | 1.001 | 3.073 | 1.001 |
| void_b4 | 1.000 | 3.064 | 1.001 | 3.064 | 1.001 |
| void_b8 | 1.000 | 2.964 | 1.001 | 2.964 | 1.001 |
| cut | 1.000 | 2.172 | 1.001 | 2.172 | 1.001 |
| polar_lat75 | 1.000 | 3.075 | 1.001 | 3.075 | 1.001 |
| polar_lat60 | 1.000 | 3.075 | 1.001 | 3.075 | 1.001 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.003 | 1.004 | 1.003 |
| isl_p0.01 | 1.000 | 1.000 | 1.005 | 1.014 | 1.011 |
| isl_p0.02 | 1.000 | 1.000 | 1.006 | 1.023 | 1.017 |
| isl_p0.05 | 1.000 | 1.000 | 1.008 | 1.049 | 1.035 |
| isl_p0.10 | 1.000 | 1.000 | 1.008 | 1.086 | 1.056 |
| isl_p0.20 | 1.000 | 1.000 | 1.004 | 1.116 | 1.069 |
| sat_p0.005 | 1.000 | 1.000 | 1.004 | 1.008 | 1.007 |
| sat_p0.01 | 1.000 | 1.000 | 1.005 | 1.013 | 1.010 |
| sat_p0.02 | 1.000 | 1.000 | 1.006 | 1.021 | 1.015 |
| sat_p0.05 | 1.000 | 1.000 | 1.008 | 1.042 | 1.031 |
| void_b2 | 1.000 | 1.000 | 1.003 | 1.005 | 1.004 |
| void_b4 | 1.000 | 1.000 | 1.004 | 1.006 | 1.005 |
| void_b8 | 1.000 | 1.000 | 1.003 | 1.008 | 1.007 |
| cut | 1.000 | 1.000 | 1.003 | 1.004 | 1.044 |
| polar_lat75 | 1.000 | 1.000 | 1.003 | 1.004 | 1.003 |
| polar_lat60 | 1.000 | 1.000 | 1.003 | 1.004 | 1.003 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | — | 0.0 | 18.9 | 0.0 |
| isl_p0.01 | — | — | 0.0 | 18.9 | 0.0 |
| isl_p0.02 | — | — | 0.0 | 18.9 | 0.0 |
| isl_p0.05 | — | — | 0.0 | 18.9 | 0.0 |
| isl_p0.10 | — | — | 0.0 | 18.9 | 0.0 |
| isl_p0.20 | — | — | 0.0 | 18.9 | 0.0 |
| sat_p0.005 | — | — | 0.0 | 18.9 | 0.0 |
| sat_p0.01 | — | — | 0.0 | 18.9 | 0.0 |
| sat_p0.02 | — | — | 0.0 | 18.8 | 0.0 |
| sat_p0.05 | — | — | 0.0 | 18.6 | 0.0 |
| void_b2 | — | — | 0.0 | 18.9 | 0.0 |
| void_b4 | — | — | 0.0 | 18.9 | 0.0 |
| void_b8 | — | — | 0.0 | 18.6 | 0.0 |
| cut | — | — | 0.0 | 18.9 | 0.0 |
| polar_lat75 | — | — | 0.0 | 18.9 | 0.0 |
| polar_lat60 | — | — | 0.0 | 18.9 | 0.0 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | 24.0 | — | 24.0 | — |
| isl_p0.01 | — | 24.0 | — | 24.0 | — |
| isl_p0.02 | — | 24.0 | — | 24.0 | — |
| isl_p0.05 | — | 24.0 | — | 24.0 | — |
| isl_p0.10 | — | 24.0 | — | 24.0 | — |
| isl_p0.20 | — | 24.0 | — | 24.0 | — |
| sat_p0.005 | — | 24.0 | — | 24.0 | — |
| sat_p0.01 | — | 24.0 | — | 24.0 | — |
| sat_p0.02 | — | 24.0 | — | 24.0 | — |
| sat_p0.05 | — | 24.0 | — | 24.0 | — |
| void_b2 | — | 24.0 | — | 24.0 | — |
| void_b4 | — | 24.0 | — | 24.0 | — |
| void_b8 | — | 24.0 | — | 24.0 | — |
| cut | — | 24.0 | — | 24.0 | — |
| polar_lat75 | — | 24.0 | — | 24.0 | — |
| polar_lat60 | — | 24.0 | — | 24.0 | — |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | 0.0 | — | 0.0 | — |
| isl_p0.01 | — | 0.0 | — | 0.0 | — |
| isl_p0.02 | — | 0.0 | — | 0.0 | — |
| isl_p0.05 | — | 0.0 | — | 0.0 | — |
| isl_p0.10 | — | 0.0 | — | 0.0 | — |
| isl_p0.20 | — | 0.0 | — | 0.0 | — |
| sat_p0.005 | — | 0.0 | — | 0.0 | — |
| sat_p0.01 | — | 0.0 | — | 0.0 | — |
| sat_p0.02 | — | 0.0 | — | 0.0 | — |
| sat_p0.05 | — | 0.0 | — | 0.0 | — |
| void_b2 | — | 0.0 | — | 0.0 | — |
| void_b4 | — | 0.0 | — | 0.0 | — |
| void_b8 | — | 0.0 | — | 0.0 | — |
| cut | — | 0.0 | — | 0.0 | — |
| polar_lat75 | — | 0.0 | — | 0.0 | — |
| polar_lat60 | — | 0.0 | — | 0.0 | — |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | 0.1 | — | 0.1 | — |
| isl_p0.01 | — | 0.1 | — | 0.1 | — |
| isl_p0.02 | — | 0.1 | — | 0.1 | — |
| isl_p0.05 | — | 0.1 | — | 0.1 | — |
| isl_p0.10 | — | 0.1 | — | 0.1 | — |
| isl_p0.20 | — | 0.1 | — | 0.1 | — |
| sat_p0.005 | — | 0.1 | — | 0.1 | — |
| sat_p0.01 | — | 0.1 | — | 0.1 | — |
| sat_p0.02 | — | 0.1 | — | 0.1 | — |
| sat_p0.05 | — | 0.1 | — | 0.1 | — |
| void_b2 | — | 0.1 | — | 0.1 | — |
| void_b4 | — | 0.1 | — | 0.1 | — |
| void_b8 | — | 0.1 | — | 0.1 | — |
| cut | — | 0.1 | — | 0.1 | — |
| polar_lat75 | — | 0.1 | — | 0.1 | — |
| polar_lat60 | — | 0.1 | — | 0.1 | — |

### Transit egress switches, %

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.7 | 0.0 | 2.2 |
| isl_p0.02 | — | 0.0 | 1.4 | 0.0 | 4.1 |
| isl_p0.05 | — | 0.0 | 3.7 | 0.0 | 9.1 |
| isl_p0.10 | — | 0.0 | 8.1 | 0.0 | 15.7 |
| isl_p0.20 | — | 0.0 | 14.4 | 0.0 | 27.7 |
| sat_p0.005 | — | 0.0 | 0.3 | 0.0 | 0.9 |
| sat_p0.01 | — | 0.0 | 0.6 | 0.0 | 1.8 |
| sat_p0.02 | — | 0.0 | 1.3 | 0.0 | 3.4 |
| sat_p0.05 | — | 0.0 | 2.8 | 0.0 | 6.9 |
| void_b2 | — | 0.0 | 0.0 | 0.0 | 0.2 |
| void_b4 | — | 0.0 | 0.0 | 0.0 | 0.5 |
| void_b8 | — | 0.0 | 0.0 | 0.0 | 0.6 |
| cut | — | 0.0 | 0.2 | 0.0 | 15.7 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | — | — | — | — |
| isl_p0.01 | — | — | loop 100% | — | — |
| isl_p0.02 | — | — | loop 100% | — | — |
| isl_p0.05 | — | — | loop 100% | — | — |
| isl_p0.10 | — | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.20 | — | dead_end 100% | loop 100% | dead_end 100% | — |
| sat_p0.005 | — | — | loop 100% | — | — |
| sat_p0.01 | — | — | loop 100% | — | — |
| sat_p0.02 | — | — | loop 100% | — | — |
| sat_p0.05 | — | — | loop 100% | — | — |
| void_b2 | — | — | loop 100% | — | — |
| void_b4 | — | — | loop 100% | — | — |
| void_b8 | — | — | loop 100% | — | — |
| cut | — | dead_end 100% | loop 100% | dead_end 100% | — |
| polar_lat75 | — | — | — | — | — |
| polar_lat60 | — | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 52.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 100.8 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 210.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 319.2 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 421.9 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 27.8 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 57.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 93.6 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 194.8 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 7.7 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 15.3 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 24.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 80.7 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | — | 300.3 (8253) | 281.2 (4405) |
| isl_p0.02 | — | — | — | 590.2 (14524) | 565.6 (8322) |
| isl_p0.05 | — | — | — | 1605.7 (25488) | 1551.4 (16845) |
| isl_p0.10 | — | — | — | 3454.2 (32277) | 3398.2 (24619) |
| isl_p0.20 | — | — | — | 7804.8 (34902) | 7821.0 (30938) |
| sat_p0.005 | — | — | — | 141.0 (4095) | 142.2 (2279) |
| sat_p0.01 | — | — | — | 329.8 (8334) | 319.7 (4642) |
| sat_p0.02 | — | — | — | 597.1 (13392) | 567.4 (7615) |
| sat_p0.05 | — | — | — | 1399.9 (22905) | 1353.7 (15082) |
| void_b2 | — | — | — | 37.1 (1225) | 37.4 (682) |
| void_b4 | — | — | — | 73.6 (2041) | 75.3 (1257) |
| void_b8 | — | — | — | 133.4 (2978) | 127.5 (2015) |
| cut | — | — | — | 0.0 (0) | 1311.1 (5210) |
| polar_lat75 | — | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|---|
| none | — | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | — | 0.79 | 0.74 |
| isl_p0.02 | — | — | — | 1.55 | 1.49 |
| isl_p0.05 | — | — | — | 4.22 | 4.08 |
| isl_p0.10 | — | — | — | 9.09 | 8.94 |
| isl_p0.20 | — | — | — | 20.53 | 20.57 |
| sat_p0.005 | — | — | — | 0.37 | 0.37 |
| sat_p0.01 | — | — | — | 0.87 | 0.84 |
| sat_p0.02 | — | — | — | 1.57 | 1.49 |
| sat_p0.05 | — | — | — | 3.68 | 3.56 |
| void_b2 | — | — | — | 0.10 | 0.10 |
| void_b4 | — | — | — | 0.19 | 0.20 |
| void_b8 | — | — | — | 0.35 | 0.34 |
| cut | — | — | — | 0.00 | 3.45 |
| polar_lat75 | — | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | — | 0.00 | 0.00 |
