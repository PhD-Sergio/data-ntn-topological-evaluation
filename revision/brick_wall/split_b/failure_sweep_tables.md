# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 92.9 ± 1.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 85.6 ± 1.3 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 68.4 ± 3.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 99.8 ± 0.2 | 46.3 ± 3.2 | 99.8 ± 0.2 | 100.0 ± 0.0 |
| isl_p0.20 | 98.4 ± 0.3 | 23.0 ± 1.2 | 98.4 ± 0.3 | 100.0 ± 0.0 |
| sat_p0.005 | 100.0 ± 0.0 | 95.7 ± 1.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 92.2 ± 1.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 87.3 ± 2.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 70.4 ± 1.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 98.9 ± 0.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 97.6 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 96.2 ± 2.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 53.2 | 62.3 | 53.2 | 100.0 |
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
| none | 1.6771 | 1.0122 | 1.6879 | 1.0122 |
| isl_p0.01 | 1.6790 | 1.0124 | 1.7030 | 1.0171 |
| isl_p0.02 | 1.6792 | 1.0129 | 1.7142 | 1.0225 |
| isl_p0.05 | 1.6867 | 1.0129 | 1.7483 | 1.0341 |
| isl_p0.10 | 1.7036 | 1.0119 | 1.8052 | 1.0508 |
| isl_p0.20 | 1.7884 | 1.0073 | 1.9266 | 1.0636 |
| sat_p0.005 | 1.6766 | 1.0124 | 1.6938 | 1.0151 |
| sat_p0.01 | 1.6777 | 1.0123 | 1.7005 | 1.0169 |
| sat_p0.02 | 1.6772 | 1.0124 | 1.7059 | 1.0207 |
| sat_p0.05 | 1.6764 | 1.0125 | 1.7301 | 1.0315 |
| void_b2 | 1.6769 | 1.0121 | 1.6889 | 1.0128 |
| void_b4 | 1.6676 | 1.0120 | 1.6807 | 1.0136 |
| void_b8 | 1.6282 | 1.0117 | 1.6457 | 1.0153 |
| cut | 1.4027 | 1.0083 | 1.4105 | 1.1121 |
| polar_lat75 | 1.6771 | 1.0122 | 1.6879 | 1.0122 |
| polar_lat60 | 1.6771 | 1.0122 | 1.6879 | 1.0122 |

### Distance stretch, egress-choice factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.677 | 1.009 | 1.677 | 1.009 |
| isl_p0.01 | 1.679 | 1.009 | 1.679 | 1.010 |
| isl_p0.02 | 1.679 | 1.009 | 1.679 | 1.011 |
| isl_p0.05 | 1.687 | 1.009 | 1.687 | 1.013 |
| isl_p0.10 | 1.704 | 1.007 | 1.704 | 1.015 |
| isl_p0.20 | 1.788 | 1.005 | 1.788 | 1.017 |
| sat_p0.005 | 1.677 | 1.009 | 1.677 | 1.010 |
| sat_p0.01 | 1.678 | 1.009 | 1.678 | 1.010 |
| sat_p0.02 | 1.677 | 1.009 | 1.677 | 1.011 |
| sat_p0.05 | 1.676 | 1.008 | 1.676 | 1.012 |
| void_b2 | 1.677 | 1.009 | 1.677 | 1.009 |
| void_b4 | 1.668 | 1.009 | 1.668 | 1.010 |
| void_b8 | 1.628 | 1.009 | 1.628 | 1.009 |
| cut | 1.403 | 1.005 | 1.403 | 1.008 |
| polar_lat75 | 1.677 | 1.009 | 1.677 | 1.009 |
| polar_lat60 | 1.677 | 1.009 | 1.677 | 1.009 |

### Distance stretch, forwarding factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.000 | 1.003 | 1.007 | 1.003 |
| isl_p0.01 | 1.000 | 1.003 | 1.014 | 1.007 |
| isl_p0.02 | 1.000 | 1.004 | 1.021 | 1.012 |
| isl_p0.05 | 1.000 | 1.004 | 1.037 | 1.021 |
| isl_p0.10 | 1.000 | 1.004 | 1.059 | 1.035 |
| isl_p0.20 | 1.000 | 1.003 | 1.075 | 1.046 |
| sat_p0.005 | 1.000 | 1.003 | 1.011 | 1.005 |
| sat_p0.01 | 1.000 | 1.003 | 1.014 | 1.007 |
| sat_p0.02 | 1.000 | 1.003 | 1.017 | 1.010 |
| sat_p0.05 | 1.000 | 1.004 | 1.032 | 1.020 |
| void_b2 | 1.000 | 1.003 | 1.007 | 1.003 |
| void_b4 | 1.000 | 1.003 | 1.008 | 1.004 |
| void_b8 | 1.000 | 1.003 | 1.010 | 1.006 |
| cut | 1.000 | 1.003 | 1.006 | 1.102 |
| polar_lat75 | 1.000 | 1.003 | 1.007 | 1.003 |
| polar_lat60 | 1.000 | 1.003 | 1.007 | 1.003 |

### Ground station renumberings per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | 0.0 | 16.8 | 0.0 |
| isl_p0.01 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.02 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.05 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.10 | — | 0.0 | 16.8 | 0.0 |
| isl_p0.20 | — | 0.0 | 16.8 | 0.0 |
| sat_p0.005 | — | 0.0 | 16.7 | 0.0 |
| sat_p0.01 | — | 0.0 | 16.7 | 0.0 |
| sat_p0.02 | — | 0.0 | 16.6 | 0.0 |
| sat_p0.05 | — | 0.0 | 16.3 | 0.0 |
| void_b2 | — | 0.0 | 16.8 | 0.0 |
| void_b4 | — | 0.0 | 16.6 | 0.0 |
| void_b8 | — | 0.0 | 16.1 | 0.0 |
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
| void_b8 | 0.4 | — | 0.4 | — |
| cut | 0.4 | — | 0.4 | — |
| polar_lat75 | 0.4 | — | 0.4 | — |
| polar_lat60 | 0.4 | — | 0.4 | — |

### Transit egress switches, %

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 4.7 | 0.0 | 4.7 |
| isl_p0.01 | 0.0 | 5.9 | 0.0 | 8.0 |
| isl_p0.02 | 0.0 | 7.0 | 0.0 | 11.1 |
| isl_p0.05 | 0.0 | 9.6 | 0.0 | 18.9 |
| isl_p0.10 | 0.0 | 12.8 | 0.0 | 29.3 |
| isl_p0.20 | 0.0 | 14.1 | 0.0 | 43.4 |
| sat_p0.005 | 0.0 | 5.5 | 0.0 | 6.6 |
| sat_p0.01 | 0.0 | 6.0 | 0.0 | 7.9 |
| sat_p0.02 | 0.0 | 6.6 | 0.0 | 9.9 |
| sat_p0.05 | 0.0 | 8.9 | 0.0 | 16.3 |
| void_b2 | 0.0 | 4.8 | 0.0 | 5.1 |
| void_b4 | 0.0 | 4.9 | 0.0 | 5.7 |
| void_b8 | 0.0 | 5.3 | 0.0 | 6.4 |
| cut | 0.0 | 5.0 | 0.0 | 40.5 |
| polar_lat75 | 0.0 | 4.7 | 0.0 | 4.7 |
| polar_lat60 | 0.0 | 4.7 | 0.0 | 4.7 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | — |
| isl_p0.02 | — | loop 100% | — | — |
| isl_p0.05 | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.10 | dead_end 100% | loop 100% | dead_end 100% | — |
| isl_p0.20 | dead_end 100% | loop 100% | dead_end 100% | — |
| sat_p0.005 | — | loop 100% | — | — |
| sat_p0.01 | — | loop 100% | — | — |
| sat_p0.02 | — | loop 100% | — | — |
| sat_p0.05 | — | loop 100% | — | — |
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
| isl_p0.01 | 0.0 | 39.1 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 79.2 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 174.3 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 295.9 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 418.4 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 23.8 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 43.2 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 70.2 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 163.5 | 0.0 | 0.0 |
| void_b2 | 0.0 | 6.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 13.3 | 0.0 | 0.0 |
| void_b8 | 0.0 | 20.9 | 0.0 | 0.0 |
| cut | 0.0 | 193.7 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 216.7 (4042) | 195.6 (2302) |
| isl_p0.02 | — | — | 417.6 (7250) | 390.0 (4641) |
| isl_p0.05 | — | — | 1184.2 (14660) | 1125.9 (10120) |
| isl_p0.10 | — | — | 2609.6 (21187) | 2516.6 (16371) |
| isl_p0.20 | — | — | 6044.6 (24812) | 5866.1 (21947) |
| sat_p0.005 | — | — | 123.0 (2379) | 116.1 (1403) |
| sat_p0.01 | — | — | 232.7 (4274) | 221.8 (2553) |
| sat_p0.02 | — | — | 441.1 (6757) | 425.7 (4354) |
| sat_p0.05 | — | — | 1100.0 (13224) | 1056.1 (9137) |
| void_b2 | — | — | 36.5 (590) | 35.9 (383) |
| void_b4 | — | — | 69.9 (1120) | 71.2 (757) |
| void_b8 | — | — | 137.5 (1790) | 132.6 (1266) |
| cut | — | — | 0.0 (0) | 1185.4 (9600) |
| polar_lat75 | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.78 | 0.71 |
| isl_p0.02 | — | — | 1.51 | 1.41 |
| isl_p0.05 | — | — | 4.27 | 4.06 |
| isl_p0.10 | — | — | 9.41 | 9.07 |
| isl_p0.20 | — | — | 21.79 | 21.14 |
| sat_p0.005 | — | — | 0.44 | 0.42 |
| sat_p0.01 | — | — | 0.84 | 0.80 |
| sat_p0.02 | — | — | 1.59 | 1.53 |
| sat_p0.05 | — | — | 3.96 | 3.81 |
| void_b2 | — | — | 0.13 | 0.13 |
| void_b4 | — | — | 0.25 | 0.26 |
| void_b8 | — | — | 0.50 | 0.48 |
| cut | — | — | 0.00 | 4.27 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 91.9 ± 0.8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 84.3 ± 2.1 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 66.0 ± 1.7 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 99.9 ± 0.1 | 42.3 ± 3.1 | 99.9 ± 0.1 | 100.0 ± 0.0 |
| isl_p0.20 | 98.2 ± 0.4 | 20.4 ± 0.9 | 98.2 ± 0.4 | 100.0 ± 0.0 |
| sat_p0.005 | 100.0 ± 0.0 | 95.8 ± 2.1 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 92.0 ± 3.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 86.3 ± 1.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 99.9 ± 0.1 | 67.3 ± 2.4 | 99.9 ± 0.1 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 98.8 ± 0.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 97.6 ± 1.4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 96.2 ± 2.1 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 54.1 | 82.6 | 54.1 | 100.0 |
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
| none | 1.9936 | 1.0033 | 1.9999 | 1.0033 |
| isl_p0.01 | 1.9918 | 1.0049 | 2.0121 | 1.0092 |
| isl_p0.02 | 1.9915 | 1.0055 | 2.0235 | 1.0136 |
| isl_p0.05 | 1.9901 | 1.0078 | 2.0576 | 1.0262 |
| isl_p0.10 | 2.0010 | 1.0109 | 2.1408 | 1.0484 |
| isl_p0.20 | 2.0882 | 1.0084 | 2.2950 | 1.0655 |
| sat_p0.005 | 1.9914 | 1.0039 | 2.0037 | 1.0058 |
| sat_p0.01 | 1.9895 | 1.0048 | 2.0073 | 1.0084 |
| sat_p0.02 | 1.9865 | 1.0057 | 2.0139 | 1.0120 |
| sat_p0.05 | 1.9766 | 1.0081 | 2.0413 | 1.0254 |
| void_b2 | 1.9926 | 1.0033 | 2.0002 | 1.0039 |
| void_b4 | 1.9871 | 1.0035 | 1.9998 | 1.0048 |
| void_b8 | 1.9555 | 1.0033 | 1.9775 | 1.0066 |
| cut | 1.6801 | 1.0028 | 1.6839 | 1.0534 |
| polar_lat75 | 1.9936 | 1.0033 | 1.9999 | 1.0033 |
| polar_lat60 | 1.9936 | 1.0033 | 1.9999 | 1.0033 |

### Distance stretch, egress-choice factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.994 | 1.002 | 1.994 | 1.002 |
| isl_p0.01 | 1.992 | 1.002 | 1.992 | 1.003 |
| isl_p0.02 | 1.992 | 1.002 | 1.992 | 1.004 |
| isl_p0.05 | 1.990 | 1.002 | 1.990 | 1.007 |
| isl_p0.10 | 2.001 | 1.003 | 2.001 | 1.011 |
| isl_p0.20 | 2.088 | 1.003 | 2.088 | 1.015 |
| sat_p0.005 | 1.991 | 1.002 | 1.991 | 1.002 |
| sat_p0.01 | 1.990 | 1.002 | 1.990 | 1.003 |
| sat_p0.02 | 1.987 | 1.002 | 1.987 | 1.003 |
| sat_p0.05 | 1.977 | 1.002 | 1.977 | 1.006 |
| void_b2 | 1.993 | 1.002 | 1.993 | 1.002 |
| void_b4 | 1.987 | 1.002 | 1.987 | 1.002 |
| void_b8 | 1.955 | 1.001 | 1.955 | 1.002 |
| cut | 1.680 | 1.002 | 1.680 | 1.002 |
| polar_lat75 | 1.994 | 1.002 | 1.994 | 1.002 |
| polar_lat60 | 1.994 | 1.002 | 1.994 | 1.002 |

### Distance stretch, forwarding factor

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 1.000 | 1.002 | 1.004 | 1.002 |
| isl_p0.01 | 1.000 | 1.003 | 1.011 | 1.006 |
| isl_p0.02 | 1.000 | 1.004 | 1.017 | 1.009 |
| isl_p0.05 | 1.000 | 1.005 | 1.035 | 1.019 |
| isl_p0.10 | 1.000 | 1.008 | 1.068 | 1.036 |
| isl_p0.20 | 1.000 | 1.005 | 1.093 | 1.050 |
| sat_p0.005 | 1.000 | 1.002 | 1.007 | 1.004 |
| sat_p0.01 | 1.000 | 1.003 | 1.010 | 1.006 |
| sat_p0.02 | 1.000 | 1.004 | 1.015 | 1.009 |
| sat_p0.05 | 1.000 | 1.006 | 1.034 | 1.019 |
| void_b2 | 1.000 | 1.002 | 1.004 | 1.002 |
| void_b4 | 1.000 | 1.002 | 1.006 | 1.003 |
| void_b8 | 1.000 | 1.002 | 1.009 | 1.004 |
| cut | 1.000 | 1.001 | 1.002 | 1.051 |
| polar_lat75 | 1.000 | 1.002 | 1.004 | 1.002 |
| polar_lat60 | 1.000 | 1.002 | 1.004 | 1.002 |

### Ground station renumberings per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | 0.0 | 18.9 | 0.0 |
| isl_p0.01 | — | 0.0 | 18.9 | 0.0 |
| isl_p0.02 | — | 0.0 | 18.9 | 0.0 |
| isl_p0.05 | — | 0.0 | 18.9 | 0.0 |
| isl_p0.10 | — | 0.0 | 18.9 | 0.0 |
| isl_p0.20 | — | 0.0 | 18.9 | 0.0 |
| sat_p0.005 | — | 0.0 | 18.9 | 0.0 |
| sat_p0.01 | — | 0.0 | 18.9 | 0.0 |
| sat_p0.02 | — | 0.0 | 18.8 | 0.0 |
| sat_p0.05 | — | 0.0 | 18.6 | 0.0 |
| void_b2 | — | 0.0 | 18.9 | 0.0 |
| void_b4 | — | 0.0 | 18.9 | 0.0 |
| void_b8 | — | 0.0 | 18.7 | 0.0 |
| cut | — | 0.0 | 18.9 | 0.0 |
| polar_lat75 | — | 0.0 | 18.9 | 0.0 |
| polar_lat60 | — | 0.0 | 18.9 | 0.0 |

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
| none | 0.1 | — | 0.1 | — |
| isl_p0.01 | 0.1 | — | 0.1 | — |
| isl_p0.02 | 0.1 | — | 0.1 | — |
| isl_p0.05 | 0.1 | — | 0.1 | — |
| isl_p0.10 | 0.1 | — | 0.1 | — |
| isl_p0.20 | 0.1 | — | 0.1 | — |
| sat_p0.005 | 0.1 | — | 0.1 | — |
| sat_p0.01 | 0.1 | — | 0.1 | — |
| sat_p0.02 | 0.1 | — | 0.1 | — |
| sat_p0.05 | 0.1 | — | 0.1 | — |
| void_b2 | 0.1 | — | 0.1 | — |
| void_b4 | 0.1 | — | 0.1 | — |
| void_b8 | 0.1 | — | 0.1 | — |
| cut | 0.1 | — | 0.1 | — |
| polar_lat75 | 0.1 | — | 0.1 | — |
| polar_lat60 | 0.1 | — | 0.1 | — |

### Transit egress switches, %

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 8.7 | 0.0 | 8.7 |
| isl_p0.01 | 0.0 | 9.7 | 0.0 | 12.1 |
| isl_p0.02 | 0.0 | 10.4 | 0.0 | 14.7 |
| isl_p0.05 | 0.0 | 12.6 | 0.0 | 21.1 |
| isl_p0.10 | 0.0 | 15.2 | 0.0 | 30.1 |
| isl_p0.20 | 0.0 | 17.5 | 0.0 | 44.2 |
| sat_p0.005 | 0.0 | 9.2 | 0.0 | 10.1 |
| sat_p0.01 | 0.0 | 9.7 | 0.0 | 11.3 |
| sat_p0.02 | 0.0 | 10.3 | 0.0 | 13.0 |
| sat_p0.05 | 0.0 | 12.1 | 0.0 | 19.2 |
| void_b2 | 0.0 | 8.8 | 0.0 | 9.1 |
| void_b4 | 0.0 | 8.9 | 0.0 | 9.4 |
| void_b8 | 0.0 | 8.9 | 0.0 | 10.2 |
| cut | 0.0 | 10.9 | 0.0 | 26.3 |
| polar_lat75 | 0.0 | 8.7 | 0.0 | 8.7 |
| polar_lat60 | 0.0 | 8.7 | 0.0 | 8.7 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | — | — |
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
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 44.8 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 86.5 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 187.6 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 318.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 432.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 23.3 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 44.1 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 75.8 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 180.2 | 0.0 | 0.0 |
| void_b2 | 0.0 | 6.7 | 0.0 | 0.0 |
| void_b4 | 0.0 | 13.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 21.0 | 0.0 | 0.0 |
| cut | 0.0 | 86.8 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 283.5 (6021) | 284.2 (3721) |
| isl_p0.02 | — | — | 572.2 (10938) | 576.5 (7083) |
| isl_p0.05 | — | — | 1507.2 (21102) | 1510.8 (14929) |
| isl_p0.10 | — | — | 3527.8 (30515) | 3486.1 (24207) |
| isl_p0.20 | — | — | 8189.7 (34630) | 8147.6 (31456) |
| sat_p0.005 | — | — | 137.0 (3084) | 137.5 (1844) |
| sat_p0.01 | — | — | 274.1 (5681) | 276.6 (3552) |
| sat_p0.02 | — | — | 507.7 (9544) | 503.4 (6038) |
| sat_p0.05 | — | — | 1505.2 (19897) | 1490.7 (14015) |
| void_b2 | — | — | 36.0 (832) | 35.4 (537) |
| void_b4 | — | — | 72.7 (1753) | 71.3 (935) |
| void_b8 | — | — | 154.4 (2737) | 146.2 (1563) |
| cut | — | — | 0.0 (0) | 910.2 (6232) |
| polar_lat75 | — | — | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state_attach | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.75 | 0.75 |
| isl_p0.02 | — | — | 1.51 | 1.52 |
| isl_p0.05 | — | — | 3.96 | 3.97 |
| isl_p0.10 | — | — | 9.28 | 9.17 |
| isl_p0.20 | — | — | 21.54 | 21.43 |
| sat_p0.005 | — | — | 0.36 | 0.36 |
| sat_p0.01 | — | — | 0.72 | 0.73 |
| sat_p0.02 | — | — | 1.34 | 1.32 |
| sat_p0.05 | — | — | 3.96 | 3.92 |
| void_b2 | — | — | 0.09 | 0.09 |
| void_b4 | — | — | 0.19 | 0.19 |
| void_b8 | — | — | 0.41 | 0.38 |
| cut | — | — | 0.00 | 2.39 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |
