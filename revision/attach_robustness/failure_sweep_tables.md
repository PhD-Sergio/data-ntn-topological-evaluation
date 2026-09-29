# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 100.0 ± 0.0 | 99.7 ± 0.2 | 99.7 ± 0.2 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 49.3 | 49.3 | 49.3 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.20 | +0.0 ± 0.0 | +0.3 ± 0.2 | +0.3 ± 0.2 | +0.3 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +50.7 | +50.7 | +50.7 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.0000 | 2.0456 | 2.0457 | 2.0457 |
| isl_p0.01 | 1.0000 | 2.0449 | 2.0541 | 2.0562 |
| isl_p0.02 | 1.0000 | 2.0462 | 2.0641 | 2.0691 |
| isl_p0.05 | 1.0000 | 2.0486 | 2.0970 | 2.1172 |
| isl_p0.10 | 1.0000 | 2.0532 | 2.1537 | 2.2009 |
| isl_p0.20 | 1.0000 | 2.1022 | 2.3075 | 2.4412 |
| sat_p0.005 | 1.0000 | 2.0426 | 2.0452 | 2.0452 |
| sat_p0.01 | 1.0000 | 2.0393 | 2.0472 | 2.0472 |
| sat_p0.02 | 1.0000 | 2.0418 | 2.0551 | 2.0551 |
| sat_p0.05 | 1.0000 | 2.0223 | 2.0480 | 2.0480 |
| void_b2 | 1.0000 | 2.0351 | 2.0385 | 2.0385 |
| void_b4 | 1.0000 | 2.0215 | 2.0394 | 2.0394 |
| void_b8 | 1.0000 | 1.7583 | 1.7770 | 1.7770 |
| cut | 1.0000 | 1.2589 | 1.2589 | 1.2589 |
| polar_lat75 | 1.0000 | 2.1099 | 2.1271 | 2.1790 |
| polar_lat60 | 1.0000 | 2.1780 | 2.2182 | 2.7037 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 2.046 | 2.046 | 2.046 |
| isl_p0.01 | 1.000 | 2.045 | 2.045 | 2.045 |
| isl_p0.02 | 1.000 | 2.046 | 2.046 | 2.046 |
| isl_p0.05 | 1.000 | 2.049 | 2.049 | 2.049 |
| isl_p0.10 | 1.000 | 2.053 | 2.053 | 2.053 |
| isl_p0.20 | 1.000 | 2.102 | 2.102 | 2.102 |
| sat_p0.005 | 1.000 | 2.043 | 2.043 | 2.043 |
| sat_p0.01 | 1.000 | 2.039 | 2.039 | 2.039 |
| sat_p0.02 | 1.000 | 2.042 | 2.042 | 2.042 |
| sat_p0.05 | 1.000 | 2.022 | 2.022 | 2.022 |
| void_b2 | 1.000 | 2.035 | 2.035 | 2.035 |
| void_b4 | 1.000 | 2.022 | 2.022 | 2.022 |
| void_b8 | 1.000 | 1.758 | 1.758 | 1.758 |
| cut | 1.000 | 1.259 | 1.259 | 1.259 |
| polar_lat75 | 1.000 | 2.110 | 2.110 | 2.110 |
| polar_lat60 | 1.000 | 2.178 | 2.178 | 2.178 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.005 | 1.006 |
| isl_p0.02 | 1.000 | 1.000 | 1.009 | 1.012 |
| isl_p0.05 | 1.000 | 1.000 | 1.023 | 1.034 |
| isl_p0.10 | 1.000 | 1.000 | 1.044 | 1.068 |
| isl_p0.20 | 1.000 | 1.000 | 1.081 | 1.141 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.001 |
| sat_p0.01 | 1.000 | 1.000 | 1.004 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.006 | 1.006 |
| sat_p0.05 | 1.000 | 1.000 | 1.013 | 1.013 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.005 | 1.005 |
| void_b8 | 1.000 | 1.000 | 1.004 | 1.004 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.005 | 1.012 |
| polar_lat60 | 1.000 | 1.000 | 1.012 | 1.145 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 8.2 | 8.2 |
| isl_p0.01 | — | — | 8.2 | 8.2 |
| isl_p0.02 | — | — | 8.2 | 8.2 |
| isl_p0.05 | — | — | 8.2 | 8.2 |
| isl_p0.10 | — | — | 8.2 | 8.2 |
| isl_p0.20 | — | — | 8.2 | 8.2 |
| sat_p0.005 | — | — | 8.2 | 8.2 |
| sat_p0.01 | — | — | 8.1 | 8.1 |
| sat_p0.02 | — | — | 8.1 | 8.1 |
| sat_p0.05 | — | — | 8.0 | 8.0 |
| void_b2 | — | — | 8.1 | 8.1 |
| void_b4 | — | — | 8.0 | 8.0 |
| void_b8 | — | — | 7.3 | 7.3 |
| cut | — | — | 8.2 | 8.2 |
| polar_lat75 | — | — | 8.2 | 8.2 |
| polar_lat60 | — | — | 8.2 | 8.2 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 24.0 | 24.0 | 24.0 |
| isl_p0.01 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.02 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.05 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.10 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.20 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.005 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.01 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.02 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.05 | — | 24.0 | 24.0 | 24.0 |
| void_b2 | — | 24.0 | 24.0 | 24.0 |
| void_b4 | — | 24.0 | 24.0 | 24.0 |
| void_b8 | — | 24.0 | 24.0 | 24.0 |
| cut | — | 24.0 | 24.0 | 24.0 |
| polar_lat75 | — | 24.0 | 24.0 | 24.0 |
| polar_lat60 | — | 24.0 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 1.9 | 1.9 | 1.9 |
| isl_p0.01 | — | 1.9 | 1.9 | 1.9 |
| isl_p0.02 | — | 1.9 | 1.9 | 1.9 |
| isl_p0.05 | — | 1.9 | 1.9 | 1.9 |
| isl_p0.10 | — | 1.9 | 1.9 | 1.9 |
| isl_p0.20 | — | 1.9 | 1.9 | 1.9 |
| sat_p0.005 | — | 2.0 | 2.0 | 2.0 |
| sat_p0.01 | — | 2.0 | 2.0 | 2.0 |
| sat_p0.02 | — | 2.0 | 2.0 | 2.0 |
| sat_p0.05 | — | 2.1 | 2.1 | 2.1 |
| void_b2 | — | 2.0 | 2.0 | 2.0 |
| void_b4 | — | 2.0 | 2.0 | 2.0 |
| void_b8 | — | 2.6 | 2.6 | 2.6 |
| cut | — | 1.9 | 1.9 | 1.9 |
| polar_lat75 | — | 1.9 | 1.9 | 1.9 |
| polar_lat60 | — | 1.9 | 1.9 | 1.9 |

### Transit egress switches, %

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 11.1 (303) | 0.1 (1) |
| isl_p0.02 | — | — | 23.2 (595) | 0.1 (2) |
| isl_p0.05 | — | — | 77.1 (1461) | 1.9 (34) |
| isl_p0.10 | — | — | 218.0 (2861) | 23.4 (311) |
| isl_p0.20 | — | — | 680.8 (5205) | 199.2 (1824) |
| sat_p0.005 | — | — | 4.4 (109) | 4.4 (109) |
| sat_p0.01 | — | — | 14.1 (297) | 14.1 (297) |
| sat_p0.02 | — | — | 26.6 (442) | 26.6 (442) |
| sat_p0.05 | — | — | 45.7 (849) | 45.7 (849) |
| void_b2 | — | — | 5.5 (101) | 5.5 (101) |
| void_b4 | — | — | 11.5 (192) | 11.5 (192) |
| void_b8 | — | — | 15.7 (162) | 15.7 (162) |
| cut | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat75 | — | — | 55.4 (243) | 0.0 (0) |
| polar_lat60 | — | — | 259.4 (1409) | 1.1 (3) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.13 | 0.00 |
| isl_p0.02 | — | — | 0.27 | 0.00 |
| isl_p0.05 | — | — | 0.92 | 0.02 |
| isl_p0.10 | — | — | 2.59 | 0.28 |
| isl_p0.20 | — | — | 8.08 | 2.36 |
| sat_p0.005 | — | — | 0.05 | 0.05 |
| sat_p0.01 | — | — | 0.17 | 0.17 |
| sat_p0.02 | — | — | 0.32 | 0.32 |
| sat_p0.05 | — | — | 0.54 | 0.54 |
| void_b2 | — | — | 0.06 | 0.06 |
| void_b4 | — | — | 0.14 | 0.14 |
| void_b8 | — | — | 0.19 | 0.19 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.66 | 0.00 |
| polar_lat60 | — | — | 3.08 | 0.01 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 99.9 ± 0.1 | 99.9 ± 0.1 | 99.9 ± 0.1 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.1 | 100.0 ± 0.1 | 100.0 ± 0.1 |
| isl_p0.20 | 100.0 ± 0.0 | 99.7 ± 0.2 | 99.7 ± 0.2 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 71.9 | 71.9 | 71.9 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.1 ± 0.1 | +0.1 ± 0.1 |
| isl_p0.10 | +0.0 ± 0.0 | +0.0 ± 0.1 | +0.0 ± 0.1 | +0.0 ± 0.1 |
| isl_p0.20 | +0.0 ± 0.0 | +0.3 ± 0.2 | +0.3 ± 0.2 | +0.3 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +28.1 | +28.1 | +28.1 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.0000 | 1.2182 | 1.2182 | 1.2182 |
| isl_p0.01 | 1.0000 | 1.2205 | 1.2286 | 1.2300 |
| isl_p0.02 | 1.0000 | 1.2224 | 1.2368 | 1.2398 |
| isl_p0.05 | 1.0000 | 1.2276 | 1.2592 | 1.2674 |
| isl_p0.10 | 1.0000 | 1.2407 | 1.3017 | 1.3292 |
| isl_p0.20 | 1.0000 | 1.2787 | 1.3833 | 1.4466 |
| sat_p0.005 | 1.0000 | 1.2188 | 1.2209 | 1.2209 |
| sat_p0.01 | 1.0000 | 1.2194 | 1.2237 | 1.2237 |
| sat_p0.02 | 1.0000 | 1.2209 | 1.2307 | 1.2307 |
| sat_p0.05 | 1.0000 | 1.2263 | 1.2525 | 1.2525 |
| void_b2 | 1.0000 | 1.2189 | 1.2204 | 1.2204 |
| void_b4 | 1.0000 | 1.2194 | 1.2250 | 1.2250 |
| void_b8 | 1.0000 | 1.2146 | 1.2241 | 1.2241 |
| cut | 1.0000 | 1.1857 | 1.1857 | 1.1857 |
| polar_lat75 | 1.0000 | 1.2374 | 1.2401 | 1.2520 |
| polar_lat60 | 1.0000 | 1.2622 | 1.2653 | 1.2700 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.218 | 1.218 | 1.218 |
| isl_p0.01 | 1.000 | 1.220 | 1.220 | 1.220 |
| isl_p0.02 | 1.000 | 1.222 | 1.222 | 1.222 |
| isl_p0.05 | 1.000 | 1.228 | 1.228 | 1.228 |
| isl_p0.10 | 1.000 | 1.241 | 1.241 | 1.241 |
| isl_p0.20 | 1.000 | 1.279 | 1.279 | 1.279 |
| sat_p0.005 | 1.000 | 1.219 | 1.219 | 1.219 |
| sat_p0.01 | 1.000 | 1.219 | 1.219 | 1.219 |
| sat_p0.02 | 1.000 | 1.221 | 1.221 | 1.221 |
| sat_p0.05 | 1.000 | 1.226 | 1.226 | 1.226 |
| void_b2 | 1.000 | 1.219 | 1.219 | 1.219 |
| void_b4 | 1.000 | 1.219 | 1.219 | 1.219 |
| void_b8 | 1.000 | 1.215 | 1.215 | 1.215 |
| cut | 1.000 | 1.186 | 1.186 | 1.186 |
| polar_lat75 | 1.000 | 1.237 | 1.237 | 1.237 |
| polar_lat60 | 1.000 | 1.262 | 1.262 | 1.262 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.007 | 1.008 |
| isl_p0.02 | 1.000 | 1.000 | 1.012 | 1.014 |
| isl_p0.05 | 1.000 | 1.000 | 1.025 | 1.032 |
| isl_p0.10 | 1.000 | 1.000 | 1.048 | 1.070 |
| isl_p0.20 | 1.000 | 1.000 | 1.081 | 1.130 |
| sat_p0.005 | 1.000 | 1.000 | 1.002 | 1.002 |
| sat_p0.01 | 1.000 | 1.000 | 1.004 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.008 | 1.008 |
| sat_p0.05 | 1.000 | 1.000 | 1.021 | 1.021 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.004 | 1.004 |
| void_b8 | 1.000 | 1.000 | 1.008 | 1.008 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.002 | 1.010 |
| polar_lat60 | 1.000 | 1.000 | 1.002 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 11.0 | 11.0 |
| isl_p0.01 | — | — | 11.0 | 11.0 |
| isl_p0.02 | — | — | 11.0 | 11.0 |
| isl_p0.05 | — | — | 11.0 | 11.0 |
| isl_p0.10 | — | — | 11.0 | 11.0 |
| isl_p0.20 | — | — | 11.0 | 11.0 |
| sat_p0.005 | — | — | 11.0 | 11.0 |
| sat_p0.01 | — | — | 10.9 | 10.9 |
| sat_p0.02 | — | — | 10.9 | 10.9 |
| sat_p0.05 | — | — | 10.7 | 10.7 |
| void_b2 | — | — | 10.9 | 10.9 |
| void_b4 | — | — | 10.7 | 10.7 |
| void_b8 | — | — | 10.3 | 10.3 |
| cut | — | — | 11.0 | 11.0 |
| polar_lat75 | — | — | 11.0 | 11.0 |
| polar_lat60 | — | — | 11.0 | 11.0 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 24.0 | 24.0 | 24.0 |
| isl_p0.01 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.02 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.05 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.10 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.20 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.005 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.01 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.02 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.05 | — | 24.0 | 24.0 | 24.0 |
| void_b2 | — | 24.0 | 24.0 | 24.0 |
| void_b4 | — | 24.0 | 24.0 | 24.0 |
| void_b8 | — | 23.4 | 23.4 | 23.4 |
| cut | — | 24.0 | 24.0 | 24.0 |
| polar_lat75 | — | 24.0 | 24.0 | 24.0 |
| polar_lat60 | — | 24.0 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.6 | 0.6 | 0.6 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 1.5 | 1.5 | 1.5 |
| isl_p0.01 | — | 1.5 | 1.5 | 1.5 |
| isl_p0.02 | — | 1.5 | 1.5 | 1.5 |
| isl_p0.05 | — | 1.5 | 1.5 | 1.5 |
| isl_p0.10 | — | 1.5 | 1.5 | 1.5 |
| isl_p0.20 | — | 1.5 | 1.5 | 1.5 |
| sat_p0.005 | — | 1.5 | 1.5 | 1.5 |
| sat_p0.01 | — | 1.5 | 1.5 | 1.5 |
| sat_p0.02 | — | 1.5 | 1.5 | 1.5 |
| sat_p0.05 | — | 1.6 | 1.6 | 1.6 |
| void_b2 | — | 1.5 | 1.5 | 1.5 |
| void_b4 | — | 1.6 | 1.6 | 1.6 |
| void_b8 | — | 1.7 | 1.7 | 1.7 |
| cut | — | 1.5 | 1.5 | 1.5 |
| polar_lat75 | — | 1.5 | 1.5 | 1.5 |
| polar_lat60 | — | 1.5 | 1.5 | 1.5 |

### Transit egress switches, %

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.10 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.20 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 22.2 (1397) | 0.0 (2) |
| isl_p0.02 | — | — | 47.1 (2374) | 0.4 (21) |
| isl_p0.05 | — | — | 130.6 (4857) | 5.3 (180) |
| isl_p0.10 | — | — | 393.9 (8205) | 49.0 (1127) |
| isl_p0.20 | — | — | 1229.0 (11457) | 413.2 (5821) |
| sat_p0.005 | — | — | 7.1 (313) | 7.1 (313) |
| sat_p0.01 | — | — | 19.6 (970) | 19.6 (970) |
| sat_p0.02 | — | — | 33.0 (1729) | 33.0 (1729) |
| sat_p0.05 | — | — | 143.4 (4210) | 143.4 (4210) |
| void_b2 | — | — | 6.5 (348) | 6.5 (348) |
| void_b4 | — | — | 17.7 (887) | 17.7 (887) |
| void_b8 | — | — | 46.8 (1198) | 46.8 (1198) |
| cut | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat75 | — | — | 256.6 (2460) | 173.9 (1271) |
| polar_lat60 | — | — | 704.4 (3700) | 698.0 (3580) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.16 | 0.00 |
| isl_p0.02 | — | — | 0.33 | 0.00 |
| isl_p0.05 | — | — | 0.93 | 0.04 |
| isl_p0.10 | — | — | 2.79 | 0.35 |
| isl_p0.20 | — | — | 8.71 | 2.93 |
| sat_p0.005 | — | — | 0.05 | 0.05 |
| sat_p0.01 | — | — | 0.14 | 0.14 |
| sat_p0.02 | — | — | 0.23 | 0.23 |
| sat_p0.05 | — | — | 1.02 | 1.02 |
| void_b2 | — | — | 0.05 | 0.05 |
| void_b4 | — | — | 0.13 | 0.13 |
| void_b8 | — | — | 0.33 | 0.33 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 1.82 | 1.23 |
| polar_lat60 | — | — | 4.99 | 4.95 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 99.9 ± 0.1 | 99.9 ± 0.1 | 99.9 ± 0.1 |
| isl_p0.20 | 100.0 ± 0.0 | 99.9 ± 0.1 | 99.9 ± 0.1 | 99.9 ± 0.1 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 59.2 | 59.2 | 59.2 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.1 ± 0.1 | +0.1 ± 0.1 |
| isl_p0.20 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.1 ± 0.1 | +0.1 ± 0.1 |
| sat_p0.005 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +40.8 | +40.8 | +40.8 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.0000 | 1.6451 | 1.6451 | 1.6451 |
| isl_p0.01 | 1.0000 | 1.6453 | 1.6505 | 1.6515 |
| isl_p0.02 | 1.0000 | 1.6462 | 1.6582 | 1.6608 |
| isl_p0.05 | 1.0000 | 1.6485 | 1.6801 | 1.6896 |
| isl_p0.10 | 1.0000 | 1.6535 | 1.7205 | 1.7492 |
| isl_p0.20 | 1.0000 | 1.6699 | 1.8058 | 1.8834 |
| sat_p0.005 | 1.0000 | 1.6447 | 1.6472 | 1.6472 |
| sat_p0.01 | 1.0000 | 1.6454 | 1.6515 | 1.6515 |
| sat_p0.02 | 1.0000 | 1.6429 | 1.6538 | 1.6538 |
| sat_p0.05 | 1.0000 | 1.6428 | 1.6690 | 1.6690 |
| void_b2 | 1.0000 | 1.6437 | 1.6448 | 1.6448 |
| void_b4 | 1.0000 | 1.6393 | 1.6429 | 1.6429 |
| void_b8 | 1.0000 | 1.6008 | 1.6076 | 1.6076 |
| cut | 1.0000 | 1.5034 | 1.5034 | 1.5034 |
| polar_lat75 | 1.0000 | 1.6451 | 1.6451 | 1.6451 |
| polar_lat60 | 1.0000 | 1.6451 | 1.6451 | 1.6451 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.645 | 1.645 | 1.645 |
| isl_p0.01 | 1.000 | 1.645 | 1.645 | 1.645 |
| isl_p0.02 | 1.000 | 1.646 | 1.646 | 1.646 |
| isl_p0.05 | 1.000 | 1.648 | 1.648 | 1.648 |
| isl_p0.10 | 1.000 | 1.654 | 1.654 | 1.654 |
| isl_p0.20 | 1.000 | 1.670 | 1.670 | 1.670 |
| sat_p0.005 | 1.000 | 1.645 | 1.645 | 1.645 |
| sat_p0.01 | 1.000 | 1.645 | 1.645 | 1.645 |
| sat_p0.02 | 1.000 | 1.643 | 1.643 | 1.643 |
| sat_p0.05 | 1.000 | 1.643 | 1.643 | 1.643 |
| void_b2 | 1.000 | 1.644 | 1.644 | 1.644 |
| void_b4 | 1.000 | 1.639 | 1.639 | 1.639 |
| void_b8 | 1.000 | 1.601 | 1.601 | 1.601 |
| cut | 1.000 | 1.503 | 1.503 | 1.503 |
| polar_lat75 | 1.000 | 1.645 | 1.645 | 1.645 |
| polar_lat60 | 1.000 | 1.645 | 1.645 | 1.645 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.003 | 1.004 |
| isl_p0.02 | 1.000 | 1.000 | 1.008 | 1.010 |
| isl_p0.05 | 1.000 | 1.000 | 1.020 | 1.027 |
| isl_p0.10 | 1.000 | 1.000 | 1.042 | 1.062 |
| isl_p0.20 | 1.000 | 1.000 | 1.081 | 1.131 |
| sat_p0.005 | 1.000 | 1.000 | 1.002 | 1.002 |
| sat_p0.01 | 1.000 | 1.000 | 1.004 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.007 | 1.007 |
| sat_p0.05 | 1.000 | 1.000 | 1.017 | 1.017 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.002 | 1.002 |
| void_b8 | 1.000 | 1.000 | 1.004 | 1.004 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 16.8 | 16.8 |
| isl_p0.01 | — | — | 16.8 | 16.8 |
| isl_p0.02 | — | — | 16.8 | 16.8 |
| isl_p0.05 | — | — | 16.8 | 16.8 |
| isl_p0.10 | — | — | 16.8 | 16.8 |
| isl_p0.20 | — | — | 16.8 | 16.8 |
| sat_p0.005 | — | — | 16.8 | 16.8 |
| sat_p0.01 | — | — | 16.7 | 16.7 |
| sat_p0.02 | — | — | 16.6 | 16.6 |
| sat_p0.05 | — | — | 16.3 | 16.3 |
| void_b2 | — | — | 16.8 | 16.8 |
| void_b4 | — | — | 16.6 | 16.6 |
| void_b8 | — | — | 15.9 | 15.9 |
| cut | — | — | 16.8 | 16.8 |
| polar_lat75 | — | — | 16.8 | 16.8 |
| polar_lat60 | — | — | 16.8 | 16.8 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 24.0 | 24.0 | 24.0 |
| isl_p0.01 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.02 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.05 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.10 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.20 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.005 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.01 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.02 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.05 | — | 24.0 | 24.0 | 24.0 |
| void_b2 | — | 24.0 | 24.0 | 24.0 |
| void_b4 | — | 24.0 | 24.0 | 24.0 |
| void_b8 | — | 24.0 | 24.0 | 24.0 |
| cut | — | 24.0 | 24.0 | 24.0 |
| polar_lat75 | — | 24.0 | 24.0 | 24.0 |
| polar_lat60 | — | 24.0 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.4 | 0.4 | 0.4 |
| isl_p0.01 | — | 0.4 | 0.4 | 0.4 |
| isl_p0.02 | — | 0.4 | 0.4 | 0.4 |
| isl_p0.05 | — | 0.4 | 0.4 | 0.4 |
| isl_p0.10 | — | 0.4 | 0.4 | 0.4 |
| isl_p0.20 | — | 0.4 | 0.4 | 0.4 |
| sat_p0.005 | — | 0.4 | 0.4 | 0.4 |
| sat_p0.01 | — | 0.4 | 0.4 | 0.4 |
| sat_p0.02 | — | 0.4 | 0.4 | 0.4 |
| sat_p0.05 | — | 0.4 | 0.4 | 0.4 |
| void_b2 | — | 0.4 | 0.4 | 0.4 |
| void_b4 | — | 0.4 | 0.4 | 0.4 |
| void_b8 | — | 0.5 | 0.5 | 0.5 |
| cut | — | 0.4 | 0.4 | 0.4 |
| polar_lat75 | — | 0.4 | 0.4 | 0.4 |
| polar_lat60 | — | 0.4 | 0.4 | 0.4 |

### Transit egress switches, %

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.20 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 22.3 (1630) | 0.0 (2) |
| isl_p0.02 | — | — | 52.4 (3509) | 0.1 (4) |
| isl_p0.05 | — | — | 185.2 (8184) | 5.0 (163) |
| isl_p0.10 | — | — | 555.2 (14212) | 54.6 (1558) |
| isl_p0.20 | — | — | 1981.5 (21684) | 571.7 (8947) |
| sat_p0.005 | — | — | 10.3 (928) | 10.3 (928) |
| sat_p0.01 | — | — | 23.0 (1829) | 23.0 (1829) |
| sat_p0.02 | — | — | 52.4 (3191) | 52.4 (3191) |
| sat_p0.05 | — | — | 174.5 (7055) | 174.5 (7055) |
| void_b2 | — | — | 3.1 (244) | 3.1 (244) |
| void_b4 | — | — | 9.2 (491) | 9.2 (491) |
| void_b8 | — | — | 19.4 (670) | 19.4 (670) |
| cut | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat75 | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.08 | 0.00 |
| isl_p0.02 | — | — | 0.19 | 0.00 |
| isl_p0.05 | — | — | 0.67 | 0.02 |
| isl_p0.10 | — | — | 2.00 | 0.20 |
| isl_p0.20 | — | — | 7.14 | 2.06 |
| sat_p0.005 | — | — | 0.04 | 0.04 |
| sat_p0.01 | — | — | 0.08 | 0.08 |
| sat_p0.02 | — | — | 0.19 | 0.19 |
| sat_p0.05 | — | — | 0.63 | 0.63 |
| void_b2 | — | — | 0.01 | 0.01 |
| void_b4 | — | — | 0.03 | 0.03 |
| void_b8 | — | — | 0.07 | 0.07 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 100.0 ± 0.0 | 99.8 ± 0.2 | 99.8 ± 0.2 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 52.7 | 52.7 | 52.7 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.20 | +0.0 ± 0.0 | +0.2 ± 0.2 | +0.2 ± 0.2 | +0.2 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +47.3 | +47.3 | +47.3 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.0000 | 2.0569 | 2.0569 | 2.0569 |
| isl_p0.01 | 1.0000 | 2.0565 | 2.0669 | 2.0694 |
| isl_p0.02 | 1.0000 | 2.0567 | 2.0762 | 2.0821 |
| isl_p0.05 | 1.0000 | 2.0561 | 2.1054 | 2.1264 |
| isl_p0.10 | 1.0000 | 2.0635 | 2.1892 | 2.2581 |
| isl_p0.20 | 1.0000 | 2.1218 | 2.3995 | 2.5949 |
| sat_p0.005 | 1.0000 | 2.0560 | 2.0608 | 2.0608 |
| sat_p0.01 | 1.0000 | 2.0535 | 2.0623 | 2.0623 |
| sat_p0.02 | 1.0000 | 2.0560 | 2.0730 | 2.0730 |
| sat_p0.05 | 1.0000 | 2.0444 | 2.0874 | 2.0874 |
| void_b2 | 1.0000 | 2.0558 | 2.0574 | 2.0574 |
| void_b4 | 1.0000 | 2.0528 | 2.0580 | 2.0580 |
| void_b8 | 1.0000 | 2.0283 | 2.0403 | 2.0403 |
| cut | 1.0000 | 1.5873 | 1.5873 | 1.5873 |
| polar_lat75 | 1.0000 | 2.0569 | 2.0569 | 2.0569 |
| polar_lat60 | 1.0000 | 2.0569 | 2.0569 | 2.0569 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 2.057 | 2.057 | 2.057 |
| isl_p0.01 | 1.000 | 2.057 | 2.057 | 2.057 |
| isl_p0.02 | 1.000 | 2.057 | 2.057 | 2.057 |
| isl_p0.05 | 1.000 | 2.056 | 2.056 | 2.056 |
| isl_p0.10 | 1.000 | 2.064 | 2.064 | 2.064 |
| isl_p0.20 | 1.000 | 2.122 | 2.122 | 2.122 |
| sat_p0.005 | 1.000 | 2.056 | 2.056 | 2.056 |
| sat_p0.01 | 1.000 | 2.053 | 2.053 | 2.053 |
| sat_p0.02 | 1.000 | 2.056 | 2.056 | 2.056 |
| sat_p0.05 | 1.000 | 2.044 | 2.044 | 2.044 |
| void_b2 | 1.000 | 2.056 | 2.056 | 2.056 |
| void_b4 | 1.000 | 2.053 | 2.053 | 2.053 |
| void_b8 | 1.000 | 2.028 | 2.028 | 2.028 |
| cut | 1.000 | 1.587 | 1.587 | 1.587 |
| polar_lat75 | 1.000 | 2.057 | 2.057 | 2.057 |
| polar_lat60 | 1.000 | 2.057 | 2.057 | 2.057 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.006 | 1.008 |
| isl_p0.02 | 1.000 | 1.000 | 1.012 | 1.015 |
| isl_p0.05 | 1.000 | 1.000 | 1.028 | 1.040 |
| isl_p0.10 | 1.000 | 1.000 | 1.063 | 1.098 |
| isl_p0.20 | 1.000 | 1.000 | 1.125 | 1.213 |
| sat_p0.005 | 1.000 | 1.000 | 1.003 | 1.003 |
| sat_p0.01 | 1.000 | 1.000 | 1.006 | 1.006 |
| sat_p0.02 | 1.000 | 1.000 | 1.010 | 1.010 |
| sat_p0.05 | 1.000 | 1.000 | 1.025 | 1.025 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.002 | 1.002 |
| void_b8 | 1.000 | 1.000 | 1.004 | 1.004 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 18.9 | 18.9 |
| isl_p0.01 | — | — | 18.9 | 18.9 |
| isl_p0.02 | — | — | 18.9 | 18.9 |
| isl_p0.05 | — | — | 18.9 | 18.9 |
| isl_p0.10 | — | — | 18.9 | 18.9 |
| isl_p0.20 | — | — | 18.9 | 18.9 |
| sat_p0.005 | — | — | 18.9 | 18.9 |
| sat_p0.01 | — | — | 18.9 | 18.9 |
| sat_p0.02 | — | — | 18.8 | 18.8 |
| sat_p0.05 | — | — | 18.6 | 18.6 |
| void_b2 | — | — | 18.9 | 18.9 |
| void_b4 | — | — | 18.9 | 18.9 |
| void_b8 | — | — | 18.7 | 18.7 |
| cut | — | — | 18.9 | 18.9 |
| polar_lat75 | — | — | 18.9 | 18.9 |
| polar_lat60 | — | — | 18.9 | 18.9 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 24.0 | 24.0 | 24.0 |
| isl_p0.01 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.02 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.05 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.10 | — | 24.0 | 24.0 | 24.0 |
| isl_p0.20 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.005 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.01 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.02 | — | 24.0 | 24.0 | 24.0 |
| sat_p0.05 | — | 24.0 | 24.0 | 24.0 |
| void_b2 | — | 24.0 | 24.0 | 24.0 |
| void_b4 | — | 24.0 | 24.0 | 24.0 |
| void_b8 | — | 24.0 | 24.0 | 24.0 |
| cut | — | 24.0 | 24.0 | 24.0 |
| polar_lat75 | — | 24.0 | 24.0 | 24.0 |
| polar_lat60 | — | 24.0 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.1 | 0.1 | 0.1 |
| isl_p0.01 | — | 0.1 | 0.1 | 0.1 |
| isl_p0.02 | — | 0.1 | 0.1 | 0.1 |
| isl_p0.05 | — | 0.1 | 0.1 | 0.1 |
| isl_p0.10 | — | 0.1 | 0.1 | 0.1 |
| isl_p0.20 | — | 0.1 | 0.1 | 0.1 |
| sat_p0.005 | — | 0.1 | 0.1 | 0.1 |
| sat_p0.01 | — | 0.1 | 0.1 | 0.1 |
| sat_p0.02 | — | 0.1 | 0.1 | 0.1 |
| sat_p0.05 | — | 0.1 | 0.1 | 0.1 |
| void_b2 | — | 0.1 | 0.1 | 0.1 |
| void_b4 | — | 0.1 | 0.1 | 0.1 |
| void_b8 | — | 0.1 | 0.1 | 0.1 |
| cut | — | 0.1 | 0.1 | 0.1 |
| polar_lat75 | — | 0.1 | 0.1 | 0.1 |
| polar_lat60 | — | 0.1 | 0.1 | 0.1 |

### Transit egress switches, %

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 |
| void_b4 | — | 0.0 | 0.0 | 0.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 |
| cut | — | 0.0 | 0.0 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 29.2 (3199) | 0.0 (1) |
| isl_p0.02 | — | — | 67.6 (5611) | 0.4 (22) |
| isl_p0.05 | — | — | 235.7 (12397) | 6.0 (329) |
| isl_p0.10 | — | — | 752.2 (21955) | 64.1 (3011) |
| isl_p0.20 | — | — | 2812.5 (32140) | 782.8 (17335) |
| sat_p0.005 | — | — | 11.7 (1377) | 11.7 (1377) |
| sat_p0.01 | — | — | 28.4 (2683) | 28.4 (2683) |
| sat_p0.02 | — | — | 63.3 (4674) | 63.3 (4674) |
| sat_p0.05 | — | — | 212.2 (10264) | 212.2 (10264) |
| void_b2 | — | — | 3.4 (369) | 3.4 (369) |
| void_b4 | — | — | 9.6 (764) | 9.6 (764) |
| void_b8 | — | — | 18.7 (1225) | 18.7 (1225) |
| cut | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat75 | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | topological_nominal_progress_exceptions_attach | topological_nominal_progress_repair_exceptions_attach |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.08 | 0.00 |
| isl_p0.02 | — | — | 0.18 | 0.00 |
| isl_p0.05 | — | — | 0.62 | 0.02 |
| isl_p0.10 | — | — | 1.98 | 0.17 |
| isl_p0.20 | — | — | 7.40 | 2.06 |
| sat_p0.005 | — | — | 0.03 | 0.03 |
| sat_p0.01 | — | — | 0.07 | 0.07 |
| sat_p0.02 | — | — | 0.17 | 0.17 |
| sat_p0.05 | — | — | 0.56 | 0.56 |
| void_b2 | — | — | 0.01 | 0.01 |
| void_b4 | — | — | 0.03 | 0.03 |
| void_b8 | — | — | 0.05 | 0.05 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |
