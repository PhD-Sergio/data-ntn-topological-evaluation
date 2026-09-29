# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 97.5 ± 1.5 | 100.0 ± 0.0 | 97.5 ± 1.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 95.7 ± 1.1 | 100.0 ± 0.0 | 95.7 ± 1.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 89.1 ± 3.1 | 100.0 ± 0.0 | 89.1 ± 3.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 78.6 ± 2.6 | 100.0 ± 0.0 | 78.6 ± 2.6 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 100.0 ± 0.0 | 59.5 ± 2.1 | 100.0 ± 0.0 | 59.5 ± 2.1 | 99.7 ± 0.2 | 100.0 ± 0.0 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 99.1 ± 0.6 | 100.0 ± 0.0 | 99.1 ± 0.6 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 97.9 ± 1.5 | 100.0 ± 0.0 | 97.9 ± 1.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 96.4 ± 2.4 | 100.0 ± 0.0 | 96.4 ± 2.4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 93.0 ± 1.2 | 100.0 ± 0.0 | 93.0 ± 1.2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 99.0 ± 0.6 | 100.0 ± 0.0 | 99.0 ± 0.6 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 98.6 ± 1.3 | 100.0 ± 0.0 | 98.6 ± 1.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 99.9 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 75.0 | 100.0 | 75.0 | 49.3 | 100.0 | 49.3 |
| polar_lat75 | 100.0 | 99.6 | 100.0 | 99.6 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 92.1 | 100.0 | 92.1 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +2.5 ± 1.5 | +0.0 ± 0.0 | +2.5 ± 1.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +4.3 ± 1.1 | +0.0 ± 0.0 | +4.3 ± 1.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +10.9 ± 3.1 | +0.0 ± 0.0 | +10.9 ± 3.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +21.4 ± 2.6 | +0.0 ± 0.0 | +21.4 ± 2.6 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.20 | +0.0 ± 0.0 | +40.5 ± 2.1 | +0.0 ± 0.0 | +40.5 ± 2.1 | +0.3 ± 0.2 | +0.0 ± 0.0 | +0.3 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +0.9 ± 0.6 | +0.0 ± 0.0 | +0.9 ± 0.6 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +2.1 ± 1.5 | +0.0 ± 0.0 | +2.1 ± 1.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +3.6 ± 2.4 | +0.0 ± 0.0 | +3.6 ± 2.4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +7.0 ± 1.2 | +0.0 ± 0.0 | +7.0 ± 1.2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +1.0 ± 0.6 | +0.0 ± 0.0 | +1.0 ± 0.6 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +1.4 ± 1.3 | +0.0 ± 0.0 | +1.4 ± 1.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +25.0 | +0.0 | +25.0 | +50.7 | +0.0 | +50.7 |
| polar_lat75 | +0.0 | +0.4 | +0.0 | +0.4 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +7.9 | +0.0 | +7.9 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0002 | 2.0457 | 1.0001 | 2.0457 |
| isl_p0.01 | 1.0000 | 1.0007 | 1.0061 | 1.0009 | 2.0541 | 1.0059 | 2.0562 |
| isl_p0.02 | 1.0000 | 1.0011 | 1.0105 | 1.0013 | 2.0641 | 1.0100 | 2.0691 |
| isl_p0.05 | 1.0000 | 1.0029 | 1.0276 | 1.0031 | 2.0971 | 1.0266 | 2.1172 |
| isl_p0.10 | 1.0000 | 1.0059 | 1.0546 | 1.0060 | 2.1537 | 1.0525 | 2.2010 |
| isl_p0.20 | 1.0000 | 1.0086 | 1.1018 | 1.0087 | 2.3077 | 1.0985 | 2.4416 |
| sat_p0.005 | 1.0000 | 1.0002 | 1.0012 | 1.0004 | 2.0452 | 1.0013 | 2.0452 |
| sat_p0.01 | 1.0000 | 1.0004 | 1.0027 | 1.0006 | 2.0472 | 1.0028 | 2.0472 |
| sat_p0.02 | 1.0000 | 1.0007 | 1.0044 | 1.0009 | 2.0551 | 1.0045 | 2.0551 |
| sat_p0.05 | 1.0000 | 1.0013 | 1.0087 | 1.0015 | 2.0481 | 1.0087 | 2.0481 |
| void_b2 | 1.0000 | 1.0001 | 1.0012 | 1.0003 | 2.0385 | 1.0013 | 2.0385 |
| void_b4 | 1.0000 | 1.0001 | 1.0021 | 1.0003 | 2.0394 | 1.0022 | 2.0394 |
| void_b8 | 1.0000 | 1.0002 | 1.0002 | 1.0004 | 1.7770 | 1.0003 | 1.7770 |
| cut | 1.0000 | 1.0003 | 1.0949 | 1.0006 | 1.2589 | 1.0951 | 1.2589 |
| polar_lat75 | 1.0000 | 1.0012 | 1.0030 | 1.0014 | 2.1271 | 1.0031 | 2.1788 |
| polar_lat60 | 1.0000 | 1.0013 | 1.0523 | 1.0016 | 2.2182 | 1.0525 | 2.7028 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 2.046 | 1.000 | 2.046 |
| isl_p0.01 | 1.000 | 1.000 | 1.002 | 1.001 | 2.045 | 1.001 | 2.045 |
| isl_p0.02 | 1.000 | 1.001 | 1.003 | 1.001 | 2.046 | 1.002 | 2.046 |
| isl_p0.05 | 1.000 | 1.001 | 1.006 | 1.001 | 2.049 | 1.006 | 2.049 |
| isl_p0.10 | 1.000 | 1.003 | 1.012 | 1.003 | 2.053 | 1.011 | 2.053 |
| isl_p0.20 | 1.000 | 1.004 | 1.024 | 1.004 | 2.102 | 1.021 | 2.102 |
| sat_p0.005 | 1.000 | 1.000 | 1.000 | 1.000 | 2.043 | 1.001 | 2.043 |
| sat_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 2.039 | 1.001 | 2.039 |
| sat_p0.02 | 1.000 | 1.000 | 1.002 | 1.001 | 2.042 | 1.002 | 2.042 |
| sat_p0.05 | 1.000 | 1.001 | 1.003 | 1.001 | 2.022 | 1.003 | 2.022 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 2.035 | 1.001 | 2.035 |
| void_b4 | 1.000 | 1.000 | 1.001 | 1.000 | 2.022 | 1.001 | 2.022 |
| void_b8 | 1.000 | 1.000 | 1.000 | 1.000 | 1.758 | 1.000 | 1.758 |
| cut | 1.000 | 1.000 | 1.004 | 1.000 | 1.259 | 1.004 | 1.259 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 2.110 | 1.000 | 2.110 |
| polar_lat60 | 1.000 | 1.001 | 1.004 | 1.001 | 2.178 | 1.004 | 2.178 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.004 | 1.000 | 1.005 | 1.004 | 1.006 |
| isl_p0.02 | 1.000 | 1.000 | 1.008 | 1.001 | 1.009 | 1.007 | 1.012 |
| isl_p0.05 | 1.000 | 1.002 | 1.021 | 1.002 | 1.023 | 1.021 | 1.034 |
| isl_p0.10 | 1.000 | 1.003 | 1.041 | 1.003 | 1.044 | 1.040 | 1.068 |
| isl_p0.20 | 1.000 | 1.005 | 1.075 | 1.005 | 1.081 | 1.074 | 1.141 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.000 | 1.001 | 1.001 | 1.001 |
| sat_p0.01 | 1.000 | 1.000 | 1.002 | 1.000 | 1.004 | 1.002 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.003 | 1.000 | 1.006 | 1.003 | 1.006 |
| sat_p0.05 | 1.000 | 1.001 | 1.006 | 1.001 | 1.013 | 1.006 | 1.013 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.000 | 1.001 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.001 | 1.000 | 1.005 | 1.001 | 1.005 |
| void_b8 | 1.000 | 1.000 | 1.000 | 1.000 | 1.004 | 1.000 | 1.004 |
| cut | 1.000 | 1.000 | 1.090 | 1.000 | 1.000 | 1.090 | 1.000 |
| polar_lat75 | 1.000 | 1.001 | 1.003 | 1.001 | 1.005 | 1.003 | 1.012 |
| polar_lat60 | 1.000 | 1.000 | 1.046 | 1.001 | 1.012 | 1.046 | 1.145 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 | 8.1 | 0.0 | 8.1 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 | 8.1 | 0.0 | 8.1 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 | 8.0 | 0.0 | 8.0 |
| void_b2 | — | 0.0 | 0.0 | 0.0 | 8.1 | 0.0 | 8.1 |
| void_b4 | — | 0.0 | 0.0 | 0.0 | 8.0 | 0.0 | 8.0 |
| void_b8 | — | 0.0 | 0.0 | 0.0 | 7.3 | 0.0 | 7.3 |
| cut | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 8.2 | 0.0 | 8.2 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.10 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.20 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.005 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| void_b2 | — | — | — | — | 24.0 | — | 24.0 |
| void_b4 | — | — | — | — | 24.0 | — | 24.0 |
| void_b8 | — | — | — | — | 24.0 | — | 24.0 |
| cut | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat75 | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat60 | — | — | — | — | 24.0 | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.10 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.20 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.005 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| void_b2 | — | — | — | — | 0.0 | — | 0.0 |
| void_b4 | — | — | — | — | 0.0 | — | 0.0 |
| void_b8 | — | — | — | — | 0.0 | — | 0.0 |
| cut | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat75 | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat60 | — | — | — | — | 0.0 | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 1.9 | — | 1.9 |
| isl_p0.01 | — | — | — | — | 1.9 | — | 1.9 |
| isl_p0.02 | — | — | — | — | 1.9 | — | 1.9 |
| isl_p0.05 | — | — | — | — | 1.9 | — | 1.9 |
| isl_p0.10 | — | — | — | — | 1.9 | — | 1.9 |
| isl_p0.20 | — | — | — | — | 1.9 | — | 1.9 |
| sat_p0.005 | — | — | — | — | 2.0 | — | 2.0 |
| sat_p0.01 | — | — | — | — | 2.0 | — | 2.0 |
| sat_p0.02 | — | — | — | — | 2.0 | — | 2.0 |
| sat_p0.05 | — | — | — | — | 2.1 | — | 2.1 |
| void_b2 | — | — | — | — | 2.0 | — | 2.0 |
| void_b4 | — | — | — | — | 2.0 | — | 2.0 |
| void_b8 | — | — | — | — | 2.6 | — | 2.6 |
| cut | — | — | — | — | 1.9 | — | 1.9 |
| polar_lat75 | — | — | — | — | 1.9 | — | 1.9 |
| polar_lat60 | — | — | — | — | 1.9 | — | 1.9 |

### Transit egress switches, %

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.0 |
| isl_p0.01 | — | 0.7 | 0.6 | 0.9 | 0.0 | 0.9 | 0.0 |
| isl_p0.02 | — | 1.3 | 1.1 | 1.5 | 0.0 | 1.5 | 0.0 |
| isl_p0.05 | — | 2.8 | 2.8 | 3.0 | 0.0 | 3.3 | 0.0 |
| isl_p0.10 | — | 5.9 | 6.8 | 6.1 | 0.0 | 7.6 | 0.0 |
| isl_p0.20 | — | 10.1 | 16.4 | 10.3 | 0.0 | 17.5 | 0.0 |
| sat_p0.005 | — | 0.2 | 0.7 | 0.4 | 0.0 | 0.9 | 0.0 |
| sat_p0.01 | — | 0.6 | 1.7 | 0.8 | 0.0 | 1.8 | 0.0 |
| sat_p0.02 | — | 1.1 | 2.9 | 1.2 | 0.0 | 3.0 | 0.0 |
| sat_p0.05 | — | 1.8 | 5.2 | 1.9 | 0.0 | 5.3 | 0.0 |
| void_b2 | — | 0.1 | 0.6 | 0.3 | 0.0 | 0.8 | 0.0 |
| void_b4 | — | 0.3 | 1.1 | 0.5 | 0.0 | 1.3 | 0.0 |
| void_b8 | — | 0.4 | 0.4 | 0.5 | 0.0 | 0.6 | 0.0 |
| cut | — | 0.8 | 25.6 | 1.0 | 0.0 | 25.8 | 0.0 |
| polar_lat75 | — | 0.4 | 0.6 | 0.6 | 0.0 | 0.7 | 0.0 |
| polar_lat60 | — | 0.9 | 4.7 | 1.1 | 0.0 | 4.9 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.10 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.20 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| sat_p0.005 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| void_b2 | — | loop 100% | — | loop 100% | — | — | — |
| void_b4 | — | loop 100% | — | loop 100% | — | — | — |
| void_b8 | — | loop 100% | — | loop 100% | — | — | — |
| cut | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| polar_lat75 | — | loop 100% | — | loop 100% | — | — | — |
| polar_lat60 | — | loop 100% | — | loop 100% | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 13.8 | 0.0 | 13.9 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 23.5 | 0.0 | 23.6 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 59.9 | 0.0 | 60.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 118.0 | 0.0 | 118.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 222.9 | 0.0 | 222.9 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 5.0 | 0.0 | 5.1 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 11.8 | 0.0 | 11.8 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 20.0 | 0.0 | 20.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 38.8 | 0.0 | 38.8 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 5.5 | 0.0 | 5.6 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 7.5 | 0.0 | 7.5 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.4 | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 138.0 | 0.0 | 138.1 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 2.4 | 0.0 | 2.4 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 43.8 | 0.0 | 43.9 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 0.1 (1) | — | 11.2 (303) | 0.1 (1) | 0.1 (1) |
| isl_p0.02 | — | — | 0.2 (2) | — | 23.2 (594) | 0.2 (2) | 0.1 (2) |
| isl_p0.05 | — | — | 2.4 (20) | — | 77.0 (1460) | 2.4 (20) | 1.9 (34) |
| isl_p0.10 | — | — | 26.7 (177) | — | 218.1 (2860) | 26.8 (177) | 23.4 (311) |
| isl_p0.20 | — | — | 206.7 (1093) | — | 680.3 (5205) | 206.7 (1092) | 198.9 (1825) |
| sat_p0.005 | — | — | 6.4 (69) | — | 4.4 (109) | 6.4 (69) | 4.4 (109) |
| sat_p0.01 | — | — | 16.3 (145) | — | 13.8 (296) | 16.2 (145) | 13.8 (296) |
| sat_p0.02 | — | — | 29.1 (244) | — | 26.5 (441) | 29.0 (244) | 26.5 (441) |
| sat_p0.05 | — | — | 54.4 (484) | — | 45.5 (849) | 54.3 (483) | 45.5 (849) |
| void_b2 | — | — | 7.2 (70) | — | 5.4 (101) | 7.2 (70) | 5.4 (101) |
| void_b4 | — | — | 11.8 (84) | — | 11.5 (192) | 11.9 (84) | 11.5 (192) |
| void_b8 | — | — | 1.3 (4) | — | 15.6 (162) | 1.3 (4) | 15.6 (162) |
| cut | — | — | 223.0 (1779) | — | 0.0 (0) | 223.0 (1779) | 0.0 (0) |
| polar_lat75 | — | — | 0.0 (0) | — | 54.7 (240) | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.1 (1) | — | 257.6 (1402) | 0.1 (1) | 1.1 (3) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.00 | — | 0.13 | 0.00 | 0.00 |
| isl_p0.02 | — | — | 0.00 | — | 0.28 | 0.00 | 0.00 |
| isl_p0.05 | — | — | 0.03 | — | 0.91 | 0.03 | 0.02 |
| isl_p0.10 | — | — | 0.32 | — | 2.59 | 0.32 | 0.28 |
| isl_p0.20 | — | — | 2.45 | — | 8.08 | 2.45 | 2.36 |
| sat_p0.005 | — | — | 0.08 | — | 0.05 | 0.08 | 0.05 |
| sat_p0.01 | — | — | 0.19 | — | 0.16 | 0.19 | 0.16 |
| sat_p0.02 | — | — | 0.34 | — | 0.32 | 0.34 | 0.32 |
| sat_p0.05 | — | — | 0.65 | — | 0.54 | 0.64 | 0.54 |
| void_b2 | — | — | 0.09 | — | 0.06 | 0.08 | 0.06 |
| void_b4 | — | — | 0.14 | — | 0.14 | 0.14 | 0.14 |
| void_b8 | — | — | 0.02 | — | 0.19 | 0.02 | 0.19 |
| cut | — | — | 2.65 | — | 0.00 | 2.65 | 0.00 |
| polar_lat75 | — | — | 0.00 | — | 0.65 | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | — | 3.06 | 0.00 | 0.01 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 95.8 ± 1.3 | 100.0 ± 0.0 | 95.8 ± 1.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 92.2 ± 2.0 | 100.0 ± 0.0 | 92.2 ± 2.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 83.0 ± 1.1 | 100.0 ± 0.0 | 83.0 ± 1.1 | 99.9 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.1 |
| isl_p0.10 | 100.0 ± 0.0 | 67.0 ± 3.1 | 100.0 ± 0.0 | 66.9 ± 3.1 | 100.0 ± 0.1 | 100.0 ± 0.0 | 100.0 ± 0.1 |
| isl_p0.20 | 100.0 ± 0.0 | 43.8 ± 4.0 | 100.0 ± 0.0 | 43.8 ± 4.0 | 99.7 ± 0.2 | 100.0 ± 0.0 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 99.2 ± 1.1 | 100.0 ± 0.0 | 99.2 ± 1.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 97.3 ± 1.6 | 100.0 ± 0.0 | 97.3 ± 1.6 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 94.6 ± 2.3 | 100.0 ± 0.0 | 94.6 ± 2.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 84.1 ± 3.1 | 100.0 ± 0.0 | 84.1 ± 3.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 98.7 ± 1.1 | 100.0 ± 0.0 | 98.8 ± 1.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 96.1 ± 2.0 | 100.0 ± 0.0 | 96.1 ± 2.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 93.6 ± 6.8 | 100.0 ± 0.0 | 93.6 ± 6.8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 86.8 | 100.0 | 86.8 | 71.9 | 100.0 | 71.9 |
| polar_lat75 | 100.0 | 95.2 | 100.0 | 95.2 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 86.0 | 100.0 | 86.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +4.2 ± 1.3 | +0.0 ± 0.0 | +4.2 ± 1.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +7.8 ± 2.0 | +0.0 ± 0.0 | +7.8 ± 2.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +17.0 ± 1.1 | +0.0 ± 0.0 | +17.0 ± 1.1 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.1 ± 0.1 |
| isl_p0.10 | +0.0 ± 0.0 | +33.0 ± 3.1 | +0.0 ± 0.0 | +33.1 ± 3.1 | +0.0 ± 0.1 | +0.0 ± 0.0 | +0.0 ± 0.1 |
| isl_p0.20 | +0.0 ± 0.0 | +56.2 ± 4.0 | +0.0 ± 0.0 | +56.2 ± 4.0 | +0.3 ± 0.2 | +0.0 ± 0.0 | +0.3 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +0.8 ± 1.1 | +0.0 ± 0.0 | +0.8 ± 1.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +2.7 ± 1.6 | +0.0 ± 0.0 | +2.7 ± 1.6 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +5.4 ± 2.3 | +0.0 ± 0.0 | +5.4 ± 2.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +15.9 ± 3.1 | +0.0 ± 0.0 | +15.9 ± 3.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +1.3 ± 1.1 | +0.0 ± 0.0 | +1.2 ± 1.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +3.9 ± 2.0 | +0.0 ± 0.0 | +3.9 ± 2.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +6.4 ± 6.8 | +0.0 ± 0.0 | +6.4 ± 6.8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +13.2 | +0.0 | +13.2 | +28.1 | +0.0 | +28.1 |
| polar_lat75 | +0.0 | +4.8 | +0.0 | +4.8 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +14.0 | +0.0 | +14.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.2182 | 1.0000 | 1.2182 |
| isl_p0.01 | 1.0000 | 1.0007 | 1.0049 | 1.0007 | 1.2286 | 1.0047 | 1.2300 |
| isl_p0.02 | 1.0000 | 1.0014 | 1.0095 | 1.0014 | 1.2369 | 1.0090 | 1.2398 |
| isl_p0.05 | 1.0000 | 1.0034 | 1.0223 | 1.0034 | 1.2591 | 1.0212 | 1.2674 |
| isl_p0.10 | 1.0000 | 1.0066 | 1.0486 | 1.0066 | 1.3017 | 1.0467 | 1.3291 |
| isl_p0.20 | 1.0000 | 1.0108 | 1.0963 | 1.0108 | 1.3833 | 1.0934 | 1.4466 |
| sat_p0.005 | 1.0000 | 1.0002 | 1.0006 | 1.0002 | 1.2209 | 1.0006 | 1.2209 |
| sat_p0.01 | 1.0000 | 1.0004 | 1.0016 | 1.0004 | 1.2237 | 1.0016 | 1.2237 |
| sat_p0.02 | 1.0000 | 1.0009 | 1.0036 | 1.0009 | 1.2307 | 1.0036 | 1.2307 |
| sat_p0.05 | 1.0000 | 1.0027 | 1.0106 | 1.0027 | 1.2525 | 1.0106 | 1.2525 |
| void_b2 | 1.0000 | 1.0001 | 1.0008 | 1.0001 | 1.2204 | 1.0008 | 1.2204 |
| void_b4 | 1.0000 | 1.0007 | 1.0033 | 1.0007 | 1.2250 | 1.0033 | 1.2250 |
| void_b8 | 1.0000 | 1.0008 | 1.0073 | 1.0008 | 1.2241 | 1.0073 | 1.2241 |
| cut | 1.0000 | 1.0001 | 1.0163 | 1.0001 | 1.1857 | 1.0163 | 1.1857 |
| polar_lat75 | 1.0000 | 1.0010 | 1.0056 | 1.0010 | 1.2401 | 1.0056 | 1.2520 |
| polar_lat60 | 1.0000 | 1.0008 | 1.0060 | 1.0008 | 1.2653 | 1.0060 | 1.2700 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.218 | 1.000 | 1.218 |
| isl_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 1.220 | 1.001 | 1.220 |
| isl_p0.02 | 1.000 | 1.000 | 1.002 | 1.000 | 1.222 | 1.002 | 1.222 |
| isl_p0.05 | 1.000 | 1.001 | 1.005 | 1.001 | 1.228 | 1.005 | 1.228 |
| isl_p0.10 | 1.000 | 1.002 | 1.010 | 1.002 | 1.241 | 1.009 | 1.241 |
| isl_p0.20 | 1.000 | 1.005 | 1.019 | 1.005 | 1.279 | 1.017 | 1.279 |
| sat_p0.005 | 1.000 | 1.000 | 1.000 | 1.000 | 1.219 | 1.000 | 1.219 |
| sat_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 1.219 | 1.001 | 1.219 |
| sat_p0.02 | 1.000 | 1.000 | 1.001 | 1.000 | 1.221 | 1.001 | 1.221 |
| sat_p0.05 | 1.000 | 1.001 | 1.003 | 1.001 | 1.226 | 1.003 | 1.226 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.219 | 1.000 | 1.219 |
| void_b4 | 1.000 | 1.000 | 1.001 | 1.000 | 1.219 | 1.001 | 1.219 |
| void_b8 | 1.000 | 1.000 | 1.003 | 1.000 | 1.215 | 1.003 | 1.215 |
| cut | 1.000 | 1.000 | 1.002 | 1.000 | 1.186 | 1.002 | 1.186 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 1.237 | 1.000 | 1.237 |
| polar_lat60 | 1.000 | 1.000 | 1.002 | 1.000 | 1.262 | 1.002 | 1.262 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.004 | 1.000 | 1.007 | 1.004 | 1.008 |
| isl_p0.02 | 1.000 | 1.001 | 1.007 | 1.001 | 1.012 | 1.007 | 1.014 |
| isl_p0.05 | 1.000 | 1.002 | 1.017 | 1.002 | 1.025 | 1.016 | 1.032 |
| isl_p0.10 | 1.000 | 1.004 | 1.037 | 1.004 | 1.048 | 1.037 | 1.070 |
| isl_p0.20 | 1.000 | 1.006 | 1.076 | 1.006 | 1.081 | 1.075 | 1.130 |
| sat_p0.005 | 1.000 | 1.000 | 1.000 | 1.000 | 1.002 | 1.000 | 1.002 |
| sat_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 1.004 | 1.001 | 1.004 |
| sat_p0.02 | 1.000 | 1.001 | 1.002 | 1.001 | 1.008 | 1.002 | 1.008 |
| sat_p0.05 | 1.000 | 1.002 | 1.007 | 1.002 | 1.021 | 1.007 | 1.021 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.000 | 1.001 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.002 | 1.000 | 1.004 | 1.002 | 1.004 |
| void_b8 | 1.000 | 1.000 | 1.005 | 1.000 | 1.008 | 1.005 | 1.008 |
| cut | 1.000 | 1.000 | 1.015 | 1.000 | 1.000 | 1.015 | 1.000 |
| polar_lat75 | 1.000 | 1.001 | 1.005 | 1.001 | 1.002 | 1.005 | 1.010 |
| polar_lat60 | 1.000 | 1.001 | 1.003 | 1.001 | 1.002 | 1.003 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 | 10.9 | 0.0 | 10.9 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 | 10.9 | 0.0 | 10.9 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 | 10.7 | 0.0 | 10.7 |
| void_b2 | — | 0.0 | 0.0 | 0.0 | 10.9 | 0.0 | 10.9 |
| void_b4 | — | 0.0 | 0.0 | 0.0 | 10.7 | 0.0 | 10.7 |
| void_b8 | — | 0.0 | 0.0 | 0.0 | 10.3 | 0.0 | 10.3 |
| cut | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 11.0 | 0.0 | 11.0 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.10 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.20 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.005 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| void_b2 | — | — | — | — | 24.0 | — | 24.0 |
| void_b4 | — | — | — | — | 24.0 | — | 24.0 |
| void_b8 | — | — | — | — | 23.4 | — | 23.4 |
| cut | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat75 | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat60 | — | — | — | — | 24.0 | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.10 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.20 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.005 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| void_b2 | — | — | — | — | 0.0 | — | 0.0 |
| void_b4 | — | — | — | — | 0.0 | — | 0.0 |
| void_b8 | — | — | — | — | 0.6 | — | 0.6 |
| cut | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat75 | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat60 | — | — | — | — | 0.0 | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 1.5 | — | 1.5 |
| isl_p0.01 | — | — | — | — | 1.5 | — | 1.5 |
| isl_p0.02 | — | — | — | — | 1.5 | — | 1.5 |
| isl_p0.05 | — | — | — | — | 1.5 | — | 1.5 |
| isl_p0.10 | — | — | — | — | 1.5 | — | 1.5 |
| isl_p0.20 | — | — | — | — | 1.5 | — | 1.5 |
| sat_p0.005 | — | — | — | — | 1.5 | — | 1.5 |
| sat_p0.01 | — | — | — | — | 1.5 | — | 1.5 |
| sat_p0.02 | — | — | — | — | 1.5 | — | 1.5 |
| sat_p0.05 | — | — | — | — | 1.6 | — | 1.6 |
| void_b2 | — | — | — | — | 1.5 | — | 1.5 |
| void_b4 | — | — | — | — | 1.6 | — | 1.6 |
| void_b8 | — | — | — | — | 1.7 | — | 1.7 |
| cut | — | — | — | — | 1.5 | — | 1.5 |
| polar_lat75 | — | — | — | — | 1.5 | — | 1.5 |
| polar_lat60 | — | — | — | — | 1.5 | — | 1.5 |

### Transit egress switches, %

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 1.8 | 2.3 | 1.8 | 0.0 | 2.5 | 0.0 |
| isl_p0.02 | — | 3.4 | 4.3 | 3.4 | 0.0 | 4.7 | 0.0 |
| isl_p0.05 | — | 7.3 | 9.3 | 7.3 | 0.0 | 10.0 | 0.0 |
| isl_p0.10 | — | 12.7 | 17.3 | 12.7 | 0.0 | 18.3 | 0.0 |
| isl_p0.20 | — | 20.6 | 31.6 | 20.6 | 0.0 | 32.8 | 0.0 |
| sat_p0.005 | — | 0.6 | 1.4 | 0.6 | 0.0 | 1.4 | 0.0 |
| sat_p0.01 | — | 1.1 | 3.5 | 1.1 | 0.0 | 3.5 | 0.0 |
| sat_p0.02 | — | 2.5 | 6.8 | 2.5 | 0.0 | 6.8 | 0.0 |
| sat_p0.05 | — | 6.7 | 17.3 | 6.7 | 0.0 | 17.3 | 0.0 |
| void_b2 | — | 0.3 | 1.2 | 0.3 | 0.0 | 1.2 | 0.0 |
| void_b4 | — | 1.1 | 3.9 | 1.1 | 0.0 | 3.9 | 0.0 |
| void_b8 | — | 1.2 | 5.7 | 1.2 | 0.0 | 5.7 | 0.0 |
| cut | — | 3.6 | 16.3 | 3.6 | 0.0 | 16.3 | 0.0 |
| polar_lat75 | — | 5.9 | 6.6 | 5.9 | 0.0 | 6.7 | 0.0 |
| polar_lat60 | — | 12.0 | 19.5 | 12.0 | 0.0 | 19.5 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.05 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| isl_p0.10 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| isl_p0.20 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| sat_p0.005 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| void_b2 | — | loop 100% | — | loop 100% | — | — | — |
| void_b4 | — | loop 100% | — | loop 100% | — | — | — |
| void_b8 | — | loop 100% | — | loop 100% | — | — | — |
| cut | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| polar_lat75 | — | loop 100% | — | loop 100% | — | — | — |
| polar_lat60 | — | loop 100% | — | loop 100% | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 23.4 | 0.0 | 23.4 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 43.3 | 0.0 | 43.3 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 93.6 | 0.0 | 93.6 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 182.3 | 0.0 | 182.4 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 309.3 | 0.0 | 309.3 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 4.6 | 0.0 | 4.6 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 15.0 | 0.0 | 15.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 29.7 | 0.0 | 29.7 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 88.0 | 0.0 | 88.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 6.9 | 0.0 | 6.9 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 21.3 | 0.0 | 21.4 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 32.8 | 0.0 | 32.8 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 49.0 | 0.0 | 49.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 26.4 | 0.0 | 26.4 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 77.5 | 0.0 | 77.4 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 0.0 (0) | — | 22.2 (1397) | 0.0 (0) | 0.0 (2) |
| isl_p0.02 | — | — | 0.5 (10) | — | 47.1 (2375) | 0.5 (10) | 0.4 (21) |
| isl_p0.05 | — | — | 7.2 (126) | — | 130.5 (4858) | 7.2 (126) | 5.3 (180) |
| isl_p0.10 | — | — | 51.4 (766) | — | 393.8 (8206) | 51.4 (766) | 49.0 (1127) |
| isl_p0.20 | — | — | 405.5 (4323) | — | 1229.0 (11458) | 405.6 (4323) | 413.4 (5820) |
| sat_p0.005 | — | — | 6.5 (134) | — | 7.1 (314) | 6.5 (136) | 7.1 (314) |
| sat_p0.01 | — | — | 16.2 (568) | — | 19.7 (970) | 16.2 (568) | 19.7 (970) |
| sat_p0.02 | — | — | 34.2 (1031) | — | 32.9 (1729) | 34.2 (1031) | 32.9 (1729) |
| sat_p0.05 | — | — | 130.5 (2596) | — | 143.4 (4209) | 130.5 (2595) | 143.4 (4209) |
| void_b2 | — | — | 5.9 (235) | — | 6.6 (348) | 5.9 (234) | 6.6 (348) |
| void_b4 | — | — | 17.1 (604) | — | 17.7 (887) | 17.1 (604) | 17.7 (887) |
| void_b8 | — | — | 45.8 (1050) | — | 46.8 (1197) | 45.7 (1049) | 46.8 (1197) |
| cut | — | — | 47.7 (622) | — | 0.0 (0) | 47.6 (622) | 0.0 (0) |
| polar_lat75 | — | — | 84.5 (587) | — | 256.5 (2459) | 84.5 (587) | 173.9 (1271) |
| polar_lat60 | — | — | 478.4 (2314) | — | 703.6 (3699) | 477.6 (2312) | 697.1 (3578) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.00 | — | 0.16 | 0.00 | 0.00 |
| isl_p0.02 | — | — | 0.00 | — | 0.33 | 0.00 | 0.00 |
| isl_p0.05 | — | — | 0.05 | — | 0.92 | 0.05 | 0.04 |
| isl_p0.10 | — | — | 0.36 | — | 2.79 | 0.36 | 0.35 |
| isl_p0.20 | — | — | 2.87 | — | 8.71 | 2.87 | 2.93 |
| sat_p0.005 | — | — | 0.05 | — | 0.05 | 0.05 | 0.05 |
| sat_p0.01 | — | — | 0.11 | — | 0.14 | 0.11 | 0.14 |
| sat_p0.02 | — | — | 0.24 | — | 0.23 | 0.24 | 0.23 |
| sat_p0.05 | — | — | 0.93 | — | 1.02 | 0.92 | 1.02 |
| void_b2 | — | — | 0.04 | — | 0.05 | 0.04 | 0.05 |
| void_b4 | — | — | 0.12 | — | 0.13 | 0.12 | 0.13 |
| void_b8 | — | — | 0.32 | — | 0.33 | 0.32 | 0.33 |
| cut | — | — | 0.34 | — | 0.00 | 0.34 | 0.00 |
| polar_lat75 | — | — | 0.60 | — | 1.82 | 0.60 | 1.23 |
| polar_lat60 | — | — | 3.39 | — | 4.99 | 3.38 | 4.94 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 97.9 ± 0.4 | 100.0 ± 0.0 | 97.9 ± 0.4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 95.4 ± 0.7 | 100.0 ± 0.0 | 95.4 ± 0.7 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 88.5 ± 0.8 | 100.0 ± 0.0 | 88.5 ± 0.8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 75.1 ± 2.1 | 100.0 ± 0.0 | 75.1 ± 2.1 | 99.9 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.1 |
| isl_p0.20 | 100.0 ± 0.0 | 48.5 ± 1.6 | 100.0 ± 0.0 | 48.5 ± 1.6 | 99.9 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.1 |
| sat_p0.005 | 100.0 ± 0.0 | 99.1 ± 0.3 | 100.0 ± 0.0 | 99.1 ± 0.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 97.6 ± 0.5 | 100.0 ± 0.0 | 97.6 ± 0.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 95.6 ± 1.2 | 100.0 ± 0.0 | 95.6 ± 1.2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 88.2 ± 1.3 | 100.0 ± 0.0 | 88.2 ± 1.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 99.6 ± 0.5 | 100.0 ± 0.0 | 99.6 ± 0.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 98.5 ± 1.1 | 100.0 ± 0.0 | 98.5 ± 1.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 98.2 ± 0.7 | 100.0 ± 0.0 | 98.2 ± 0.7 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 83.6 | 100.0 | 83.6 | 59.2 | 100.0 | 59.2 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +2.1 ± 0.4 | +0.0 ± 0.0 | +2.1 ± 0.4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +4.6 ± 0.7 | +0.0 ± 0.0 | +4.6 ± 0.7 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +11.5 ± 0.8 | +0.0 ± 0.0 | +11.5 ± 0.8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +24.9 ± 2.1 | +0.0 ± 0.0 | +24.9 ± 2.1 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.1 ± 0.1 |
| isl_p0.20 | +0.0 ± 0.0 | +51.5 ± 1.6 | +0.0 ± 0.0 | +51.5 ± 1.6 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.1 ± 0.1 |
| sat_p0.005 | +0.0 ± 0.0 | +0.9 ± 0.3 | +0.0 ± 0.0 | +0.9 ± 0.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +2.4 ± 0.5 | +0.0 ± 0.0 | +2.4 ± 0.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +4.4 ± 1.2 | +0.0 ± 0.0 | +4.4 ± 1.2 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +11.8 ± 1.3 | +0.0 ± 0.0 | +11.8 ± 1.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.4 ± 0.5 | +0.0 ± 0.0 | +0.4 ± 0.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +1.5 ± 1.1 | +0.0 ± 0.0 | +1.5 ± 1.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +1.8 ± 0.7 | +0.0 ± 0.0 | +1.8 ± 0.7 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +16.4 | +0.0 | +16.4 | +40.8 | +0.0 | +40.8 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.6451 | 1.0000 | 1.6451 |
| isl_p0.01 | 1.0000 | 1.0014 | 1.0036 | 1.0014 | 1.6505 | 1.0035 | 1.6515 |
| isl_p0.02 | 1.0000 | 1.0034 | 1.0087 | 1.0034 | 1.6582 | 1.0084 | 1.6608 |
| isl_p0.05 | 1.0000 | 1.0077 | 1.0228 | 1.0077 | 1.6802 | 1.0221 | 1.6897 |
| isl_p0.10 | 1.0000 | 1.0130 | 1.0490 | 1.0130 | 1.7204 | 1.0477 | 1.7491 |
| isl_p0.20 | 1.0000 | 1.0182 | 1.1044 | 1.0182 | 1.8057 | 1.1025 | 1.8833 |
| sat_p0.005 | 1.0000 | 1.0007 | 1.0009 | 1.0007 | 1.6472 | 1.0009 | 1.6472 |
| sat_p0.01 | 1.0000 | 1.0017 | 1.0022 | 1.0017 | 1.6515 | 1.0022 | 1.6515 |
| sat_p0.02 | 1.0000 | 1.0029 | 1.0043 | 1.0029 | 1.6538 | 1.0043 | 1.6538 |
| sat_p0.05 | 1.0000 | 1.0059 | 1.0109 | 1.0059 | 1.6690 | 1.0109 | 1.6690 |
| void_b2 | 1.0000 | 1.0002 | 1.0004 | 1.0002 | 1.6448 | 1.0004 | 1.6448 |
| void_b4 | 1.0000 | 1.0001 | 1.0012 | 1.0001 | 1.6429 | 1.0012 | 1.6429 |
| void_b8 | 1.0000 | 1.0003 | 1.0021 | 1.0003 | 1.6074 | 1.0021 | 1.6074 |
| cut | 1.0000 | 1.0002 | 1.0488 | 1.0002 | 1.5034 | 1.0487 | 1.5034 |
| polar_lat75 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.6451 | 1.0000 | 1.6451 |
| polar_lat60 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.6451 | 1.0000 | 1.6451 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.645 | 1.000 | 1.645 |
| isl_p0.01 | 1.000 | 1.001 | 1.001 | 1.001 | 1.645 | 1.001 | 1.645 |
| isl_p0.02 | 1.000 | 1.001 | 1.002 | 1.001 | 1.646 | 1.002 | 1.646 |
| isl_p0.05 | 1.000 | 1.003 | 1.005 | 1.003 | 1.648 | 1.005 | 1.648 |
| isl_p0.10 | 1.000 | 1.006 | 1.009 | 1.006 | 1.654 | 1.009 | 1.654 |
| isl_p0.20 | 1.000 | 1.008 | 1.019 | 1.008 | 1.670 | 1.018 | 1.670 |
| sat_p0.005 | 1.000 | 1.000 | 1.000 | 1.000 | 1.645 | 1.000 | 1.645 |
| sat_p0.01 | 1.000 | 1.001 | 1.001 | 1.001 | 1.645 | 1.001 | 1.645 |
| sat_p0.02 | 1.000 | 1.001 | 1.002 | 1.001 | 1.643 | 1.002 | 1.643 |
| sat_p0.05 | 1.000 | 1.002 | 1.004 | 1.002 | 1.643 | 1.004 | 1.643 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.644 | 1.000 | 1.644 |
| void_b4 | 1.000 | 1.000 | 1.000 | 1.000 | 1.639 | 1.000 | 1.639 |
| void_b8 | 1.000 | 1.000 | 1.001 | 1.000 | 1.601 | 1.001 | 1.601 |
| cut | 1.000 | 1.000 | 1.003 | 1.000 | 1.503 | 1.003 | 1.503 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 1.645 | 1.000 | 1.645 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 | 1.645 | 1.000 | 1.645 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.001 | 1.003 | 1.001 | 1.003 | 1.003 | 1.004 |
| isl_p0.02 | 1.000 | 1.002 | 1.007 | 1.002 | 1.008 | 1.006 | 1.010 |
| isl_p0.05 | 1.000 | 1.004 | 1.018 | 1.004 | 1.021 | 1.017 | 1.027 |
| isl_p0.10 | 1.000 | 1.007 | 1.039 | 1.007 | 1.042 | 1.038 | 1.062 |
| isl_p0.20 | 1.000 | 1.010 | 1.084 | 1.010 | 1.081 | 1.083 | 1.131 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.000 | 1.002 | 1.001 | 1.002 |
| sat_p0.01 | 1.000 | 1.001 | 1.001 | 1.001 | 1.004 | 1.001 | 1.004 |
| sat_p0.02 | 1.000 | 1.002 | 1.003 | 1.002 | 1.007 | 1.003 | 1.007 |
| sat_p0.05 | 1.000 | 1.004 | 1.007 | 1.004 | 1.017 | 1.007 | 1.017 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.001 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.001 | 1.000 | 1.002 | 1.001 | 1.002 |
| void_b8 | 1.000 | 1.000 | 1.001 | 1.000 | 1.003 | 1.001 | 1.003 |
| cut | 1.000 | 1.000 | 1.045 | 1.000 | 1.000 | 1.045 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 | 16.7 | 0.0 | 16.7 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 | 16.6 | 0.0 | 16.6 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 | 16.3 | 0.0 | 16.3 |
| void_b2 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| void_b4 | — | 0.0 | 0.0 | 0.0 | 16.6 | 0.0 | 16.6 |
| void_b8 | — | 0.0 | 0.0 | 0.0 | 15.9 | 0.0 | 15.9 |
| cut | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 16.8 | 0.0 | 16.8 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.10 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.20 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.005 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| void_b2 | — | — | — | — | 24.0 | — | 24.0 |
| void_b4 | — | — | — | — | 24.0 | — | 24.0 |
| void_b8 | — | — | — | — | 24.0 | — | 24.0 |
| cut | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat75 | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat60 | — | — | — | — | 24.0 | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.10 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.20 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.005 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| void_b2 | — | — | — | — | 0.0 | — | 0.0 |
| void_b4 | — | — | — | — | 0.0 | — | 0.0 |
| void_b8 | — | — | — | — | 0.0 | — | 0.0 |
| cut | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat75 | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat60 | — | — | — | — | 0.0 | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.4 | — | 0.4 |
| isl_p0.01 | — | — | — | — | 0.4 | — | 0.4 |
| isl_p0.02 | — | — | — | — | 0.4 | — | 0.4 |
| isl_p0.05 | — | — | — | — | 0.4 | — | 0.4 |
| isl_p0.10 | — | — | — | — | 0.4 | — | 0.4 |
| isl_p0.20 | — | — | — | — | 0.4 | — | 0.4 |
| sat_p0.005 | — | — | — | — | 0.4 | — | 0.4 |
| sat_p0.01 | — | — | — | — | 0.4 | — | 0.4 |
| sat_p0.02 | — | — | — | — | 0.4 | — | 0.4 |
| sat_p0.05 | — | — | — | — | 0.4 | — | 0.4 |
| void_b2 | — | — | — | — | 0.4 | — | 0.4 |
| void_b4 | — | — | — | — | 0.4 | — | 0.4 |
| void_b8 | — | — | — | — | 0.5 | — | 0.5 |
| cut | — | — | — | — | 0.4 | — | 0.4 |
| polar_lat75 | — | — | — | — | 0.4 | — | 0.4 |
| polar_lat60 | — | — | — | — | 0.4 | — | 0.4 |

### Transit egress switches, %

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 2.3 | 1.6 | 2.3 | 0.0 | 1.7 | 0.0 |
| isl_p0.02 | — | 5.4 | 3.6 | 5.4 | 0.0 | 3.8 | 0.0 |
| isl_p0.05 | — | 11.7 | 9.1 | 11.7 | 0.0 | 9.4 | 0.0 |
| isl_p0.10 | — | 17.6 | 16.6 | 17.5 | 0.0 | 17.1 | 0.0 |
| isl_p0.20 | — | 24.3 | 31.9 | 24.3 | 0.0 | 32.6 | 0.0 |
| sat_p0.005 | — | 1.1 | 1.9 | 1.1 | 0.0 | 1.9 | 0.0 |
| sat_p0.01 | — | 2.7 | 4.4 | 2.7 | 0.0 | 4.4 | 0.0 |
| sat_p0.02 | — | 4.5 | 7.7 | 4.5 | 0.0 | 7.7 | 0.0 |
| sat_p0.05 | — | 9.3 | 15.9 | 9.3 | 0.0 | 15.9 | 0.0 |
| void_b2 | — | 0.4 | 0.7 | 0.4 | 0.0 | 0.7 | 0.0 |
| void_b4 | — | 0.4 | 1.6 | 0.4 | 0.0 | 1.6 | 0.0 |
| void_b8 | — | 0.7 | 2.1 | 0.7 | 0.0 | 2.1 | 0.0 |
| cut | — | 1.1 | 17.4 | 1.1 | 0.0 | 17.3 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.10 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| isl_p0.20 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| sat_p0.005 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| void_b2 | — | loop 100% | — | loop 100% | — | — | — |
| void_b4 | — | loop 100% | — | loop 100% | — | — | — |
| void_b8 | — | loop 100% | — | loop 100% | — | — | — |
| cut | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| polar_lat75 | — | — | — | — | — | — | — |
| polar_lat60 | — | — | — | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 11.5 | 0.0 | 11.6 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 25.2 | 0.0 | 25.2 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 63.7 | 0.0 | 63.7 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 137.5 | 0.0 | 137.5 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 283.8 | 0.0 | 283.7 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 4.9 | 0.0 | 4.9 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 13.1 | 0.0 | 13.1 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 24.5 | 0.0 | 24.6 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 65.3 | 0.0 | 65.3 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 2.2 | 0.0 | 2.2 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 8.4 | 0.0 | 8.4 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 10.1 | 0.0 | 10.1 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 75.5 | 0.0 | 75.4 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 0.0 (0) | — | 22.3 (1644) | 0.0 (0) | 0.0 (2) |
| isl_p0.02 | — | — | 0.1 (6) | — | 52.5 (3530) | 0.1 (6) | 0.1 (4) |
| isl_p0.05 | — | — | 5.8 (96) | — | 185.2 (8229) | 5.8 (96) | 5.0 (164) |
| isl_p0.10 | — | — | 58.6 (913) | — | 555.1 (14250) | 58.6 (912) | 54.6 (1566) |
| isl_p0.20 | — | — | 580.0 (6044) | — | 1981.4 (21690) | 580.1 (6045) | 571.9 (8959) |
| sat_p0.005 | — | — | 12.5 (406) | — | 10.3 (938) | 12.5 (406) | 10.3 (938) |
| sat_p0.01 | — | — | 30.1 (915) | — | 23.1 (1845) | 30.1 (915) | 23.1 (1845) |
| sat_p0.02 | — | — | 63.3 (1684) | — | 52.3 (3212) | 63.3 (1684) | 52.3 (3212) |
| sat_p0.05 | — | — | 200.3 (4301) | — | 174.5 (7103) | 200.3 (4301) | 174.5 (7103) |
| void_b2 | — | — | 3.9 (160) | — | 3.0 (243) | 3.9 (160) | 3.0 (243) |
| void_b4 | — | — | 11.2 (352) | — | 9.2 (496) | 11.2 (352) | 9.2 (496) |
| void_b8 | — | — | 22.7 (438) | — | 19.4 (671) | 22.7 (438) | 19.4 (671) |
| cut | — | — | 254.5 (3458) | — | 0.0 (0) | 254.5 (3459) | 0.0 (0) |
| polar_lat75 | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.00 | — | 0.08 | 0.00 | 0.00 |
| isl_p0.02 | — | — | 0.00 | — | 0.19 | 0.00 | 0.00 |
| isl_p0.05 | — | — | 0.02 | — | 0.67 | 0.02 | 0.02 |
| isl_p0.10 | — | — | 0.21 | — | 2.00 | 0.21 | 0.20 |
| isl_p0.20 | — | — | 2.09 | — | 7.14 | 2.09 | 2.06 |
| sat_p0.005 | — | — | 0.05 | — | 0.04 | 0.05 | 0.04 |
| sat_p0.01 | — | — | 0.11 | — | 0.08 | 0.11 | 0.08 |
| sat_p0.02 | — | — | 0.23 | — | 0.19 | 0.23 | 0.19 |
| sat_p0.05 | — | — | 0.72 | — | 0.63 | 0.72 | 0.63 |
| void_b2 | — | — | 0.01 | — | 0.01 | 0.01 | 0.01 |
| void_b4 | — | — | 0.04 | — | 0.03 | 0.04 | 0.03 |
| void_b8 | — | — | 0.08 | — | 0.07 | 0.08 | 0.07 |
| cut | — | — | 0.92 | — | 0.00 | 0.92 | 0.00 |
| polar_lat75 | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 95.5 ± 1.0 | 100.0 ± 0.0 | 95.5 ± 1.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 92.0 ± 0.8 | 100.0 ± 0.0 | 92.0 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 81.5 ± 0.3 | 100.0 ± 0.0 | 81.5 ± 0.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 64.9 ± 2.2 | 100.0 ± 0.0 | 64.9 ± 2.1 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 100.0 ± 0.0 | 39.1 ± 1.0 | 100.0 ± 0.0 | 39.1 ± 1.0 | 99.8 ± 0.2 | 100.0 ± 0.0 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 98.0 ± 0.4 | 100.0 ± 0.0 | 98.0 ± 0.4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 95.8 ± 1.9 | 100.0 ± 0.0 | 95.8 ± 1.9 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 92.7 ± 2.9 | 100.0 ± 0.0 | 92.7 ± 2.8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 83.3 ± 2.5 | 100.0 ± 0.0 | 83.3 ± 2.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 99.4 ± 0.3 | 100.0 ± 0.0 | 99.4 ± 0.3 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 98.6 ± 0.4 | 100.0 ± 0.0 | 98.6 ± 0.4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 97.8 ± 0.9 | 100.0 ± 0.0 | 97.8 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 100.0 | 81.2 | 100.0 | 81.2 | 52.7 | 100.0 | 52.7 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.01 | +0.0 ± 0.0 | +4.5 ± 1.0 | +0.0 ± 0.0 | +4.5 ± 1.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.02 | +0.0 ± 0.0 | +8.0 ± 0.8 | +0.0 ± 0.0 | +8.0 ± 0.9 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +18.5 ± 0.3 | +0.0 ± 0.0 | +18.5 ± 0.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.10 | +0.0 ± 0.0 | +35.1 ± 2.2 | +0.0 ± 0.0 | +35.1 ± 2.1 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| isl_p0.20 | +0.0 ± 0.0 | +60.9 ± 1.0 | +0.0 ± 0.0 | +60.9 ± 1.0 | +0.2 ± 0.2 | +0.0 ± 0.0 | +0.2 ± 0.2 |
| sat_p0.005 | +0.0 ± 0.0 | +2.0 ± 0.4 | +0.0 ± 0.0 | +2.0 ± 0.4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.01 | +0.0 ± 0.0 | +4.2 ± 1.9 | +0.0 ± 0.0 | +4.2 ± 1.9 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.02 | +0.0 ± 0.0 | +7.3 ± 2.9 | +0.0 ± 0.0 | +7.3 ± 2.8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| sat_p0.05 | +0.0 ± 0.0 | +16.7 ± 2.5 | +0.0 ± 0.0 | +16.7 ± 2.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b2 | +0.0 ± 0.0 | +0.6 ± 0.3 | +0.0 ± 0.0 | +0.6 ± 0.3 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b4 | +0.0 ± 0.0 | +1.4 ± 0.4 | +0.0 ± 0.0 | +1.4 ± 0.4 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| void_b8 | +0.0 ± 0.0 | +2.2 ± 0.9 | +0.0 ± 0.0 | +2.2 ± 0.9 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| cut | +0.0 | +18.8 | +0.0 | +18.8 | +47.3 | +0.0 | +47.3 |
| polar_lat75 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| polar_lat60 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 2.0569 | 1.0000 | 2.0569 |
| isl_p0.01 | 1.0000 | 1.0007 | 1.0061 | 1.0007 | 2.0669 | 1.0059 | 2.0694 |
| isl_p0.02 | 1.0000 | 1.0012 | 1.0119 | 1.0012 | 2.0761 | 1.0116 | 2.0821 |
| isl_p0.05 | 1.0000 | 1.0030 | 1.0305 | 1.0030 | 2.1054 | 1.0300 | 2.1263 |
| isl_p0.10 | 1.0000 | 1.0056 | 1.0678 | 1.0056 | 2.1887 | 1.0669 | 2.2575 |
| isl_p0.20 | 1.0000 | 1.0100 | 1.1454 | 1.0099 | 2.3983 | 1.1440 | 2.5936 |
| sat_p0.005 | 1.0000 | 1.0002 | 1.0017 | 1.0002 | 2.0608 | 1.0017 | 2.0608 |
| sat_p0.01 | 1.0000 | 1.0005 | 1.0036 | 1.0005 | 2.0623 | 1.0036 | 2.0623 |
| sat_p0.02 | 1.0000 | 1.0006 | 1.0061 | 1.0006 | 2.0730 | 1.0061 | 2.0730 |
| sat_p0.05 | 1.0000 | 1.0019 | 1.0153 | 1.0019 | 2.0871 | 1.0153 | 2.0871 |
| void_b2 | 1.0000 | 1.0000 | 1.0004 | 1.0000 | 2.0575 | 1.0004 | 2.0575 |
| void_b4 | 1.0000 | 1.0000 | 1.0014 | 1.0000 | 2.0578 | 1.0014 | 2.0578 |
| void_b8 | 1.0000 | 1.0000 | 1.0033 | 1.0000 | 2.0400 | 1.0032 | 2.0400 |
| cut | 1.0000 | 1.0005 | 1.0595 | 1.0005 | 1.5873 | 1.0595 | 1.5873 |
| polar_lat75 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 2.0569 | 1.0000 | 2.0569 |
| polar_lat60 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 2.0569 | 1.0000 | 2.0569 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 2.057 | 1.000 | 2.057 |
| isl_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 2.057 | 1.001 | 2.057 |
| isl_p0.02 | 1.000 | 1.001 | 1.002 | 1.001 | 2.057 | 1.002 | 2.057 |
| isl_p0.05 | 1.000 | 1.001 | 1.004 | 1.001 | 2.056 | 1.004 | 2.056 |
| isl_p0.10 | 1.000 | 1.002 | 1.008 | 1.002 | 2.064 | 1.008 | 2.064 |
| isl_p0.20 | 1.000 | 1.005 | 1.017 | 1.005 | 2.122 | 1.017 | 2.122 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.000 | 2.056 | 1.001 | 2.056 |
| sat_p0.01 | 1.000 | 1.000 | 1.001 | 1.000 | 2.053 | 1.001 | 2.053 |
| sat_p0.02 | 1.000 | 1.000 | 1.002 | 1.000 | 2.056 | 1.002 | 2.056 |
| sat_p0.05 | 1.000 | 1.001 | 1.004 | 1.001 | 2.044 | 1.004 | 2.044 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 2.056 | 1.000 | 2.056 |
| void_b4 | 1.000 | 1.000 | 1.000 | 1.000 | 2.053 | 1.000 | 2.053 |
| void_b8 | 1.000 | 1.000 | 1.001 | 1.000 | 2.028 | 1.001 | 2.028 |
| cut | 1.000 | 1.000 | 1.002 | 1.000 | 1.587 | 1.002 | 1.587 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 2.057 | 1.000 | 2.057 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 | 2.057 | 1.000 | 2.057 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.005 | 1.000 | 1.006 | 1.005 | 1.008 |
| isl_p0.02 | 1.000 | 1.001 | 1.010 | 1.001 | 1.012 | 1.010 | 1.015 |
| isl_p0.05 | 1.000 | 1.002 | 1.026 | 1.002 | 1.028 | 1.026 | 1.040 |
| isl_p0.10 | 1.000 | 1.003 | 1.059 | 1.003 | 1.063 | 1.059 | 1.098 |
| isl_p0.20 | 1.000 | 1.005 | 1.126 | 1.005 | 1.125 | 1.125 | 1.213 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.000 | 1.003 | 1.001 | 1.003 |
| sat_p0.01 | 1.000 | 1.000 | 1.002 | 1.000 | 1.006 | 1.002 | 1.006 |
| sat_p0.02 | 1.000 | 1.000 | 1.004 | 1.000 | 1.010 | 1.004 | 1.010 |
| sat_p0.05 | 1.000 | 1.001 | 1.011 | 1.001 | 1.025 | 1.011 | 1.025 |
| void_b2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.001 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.001 | 1.000 | 1.002 | 1.001 | 1.002 |
| void_b8 | 1.000 | 1.000 | 1.002 | 1.000 | 1.004 | 1.002 | 1.004 |
| cut | 1.000 | 1.000 | 1.057 | 1.000 | 1.000 | 1.057 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| isl_p0.01 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| isl_p0.02 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| isl_p0.10 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| isl_p0.20 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| sat_p0.005 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| sat_p0.01 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| sat_p0.02 | — | 0.0 | 0.0 | 0.0 | 18.8 | 0.0 | 18.8 |
| sat_p0.05 | — | 0.0 | 0.0 | 0.0 | 18.6 | 0.0 | 18.6 |
| void_b2 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| void_b4 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| void_b8 | — | 0.0 | 0.0 | 0.0 | 18.7 | 0.0 | 18.7 |
| cut | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 18.9 | 0.0 | 18.9 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.10 | — | — | — | — | 24.0 | — | 24.0 |
| isl_p0.20 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.005 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.01 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.02 | — | — | — | — | 24.0 | — | 24.0 |
| sat_p0.05 | — | — | — | — | 24.0 | — | 24.0 |
| void_b2 | — | — | — | — | 24.0 | — | 24.0 |
| void_b4 | — | — | — | — | 24.0 | — | 24.0 |
| void_b8 | — | — | — | — | 24.0 | — | 24.0 |
| cut | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat75 | — | — | — | — | 24.0 | — | 24.0 |
| polar_lat60 | — | — | — | — | 24.0 | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.10 | — | — | — | — | 0.0 | — | 0.0 |
| isl_p0.20 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.005 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.01 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.02 | — | — | — | — | 0.0 | — | 0.0 |
| sat_p0.05 | — | — | — | — | 0.0 | — | 0.0 |
| void_b2 | — | — | — | — | 0.0 | — | 0.0 |
| void_b4 | — | — | — | — | 0.0 | — | 0.0 |
| void_b8 | — | — | — | — | 0.0 | — | 0.0 |
| cut | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat75 | — | — | — | — | 0.0 | — | 0.0 |
| polar_lat60 | — | — | — | — | 0.0 | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.1 | — | 0.1 |
| isl_p0.01 | — | — | — | — | 0.1 | — | 0.1 |
| isl_p0.02 | — | — | — | — | 0.1 | — | 0.1 |
| isl_p0.05 | — | — | — | — | 0.1 | — | 0.1 |
| isl_p0.10 | — | — | — | — | 0.1 | — | 0.1 |
| isl_p0.20 | — | — | — | — | 0.1 | — | 0.1 |
| sat_p0.005 | — | — | — | — | 0.1 | — | 0.1 |
| sat_p0.01 | — | — | — | — | 0.1 | — | 0.1 |
| sat_p0.02 | — | — | — | — | 0.1 | — | 0.1 |
| sat_p0.05 | — | — | — | — | 0.1 | — | 0.1 |
| void_b2 | — | — | — | — | 0.1 | — | 0.1 |
| void_b4 | — | — | — | — | 0.1 | — | 0.1 |
| void_b8 | — | — | — | — | 0.1 | — | 0.1 |
| cut | — | — | — | — | 0.1 | — | 0.1 |
| polar_lat75 | — | — | — | — | 0.1 | — | 0.1 |
| polar_lat60 | — | — | — | — | 0.1 | — | 0.1 |

### Transit egress switches, %

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | — | 1.4 | 1.1 | 1.4 | 0.0 | 1.2 | 0.0 |
| isl_p0.02 | — | 2.7 | 2.1 | 2.7 | 0.0 | 2.3 | 0.0 |
| isl_p0.05 | — | 6.2 | 5.1 | 6.2 | 0.0 | 5.4 | 0.0 |
| isl_p0.10 | — | 10.1 | 10.5 | 10.1 | 0.0 | 10.8 | 0.0 |
| isl_p0.20 | — | 16.8 | 23.0 | 16.8 | 0.0 | 23.5 | 0.0 |
| sat_p0.005 | — | 0.5 | 1.6 | 0.5 | 0.0 | 1.6 | 0.0 |
| sat_p0.01 | — | 0.9 | 3.0 | 0.9 | 0.0 | 3.0 | 0.0 |
| sat_p0.02 | — | 1.6 | 4.8 | 1.6 | 0.0 | 4.8 | 0.0 |
| sat_p0.05 | — | 4.0 | 10.3 | 4.0 | 0.0 | 10.4 | 0.0 |
| void_b2 | — | 0.1 | 0.3 | 0.1 | 0.0 | 0.3 | 0.0 |
| void_b4 | — | 0.1 | 0.8 | 0.1 | 0.0 | 0.8 | 0.0 |
| void_b8 | — | 0.0 | 0.9 | 0.0 | 0.0 | 0.9 | 0.0 |
| cut | — | 0.5 | 19.2 | 0.5 | 0.0 | 19.2 | 0.0 |
| polar_lat75 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.10 | — | loop 100% | — | loop 100% | — | — | — |
| isl_p0.20 | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| sat_p0.005 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.01 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.02 | — | loop 100% | — | loop 100% | — | — | — |
| sat_p0.05 | — | loop 100% | — | loop 100% | — | — | — |
| void_b2 | — | loop 100% | — | loop 100% | — | — | — |
| void_b4 | — | loop 100% | — | loop 100% | — | — | — |
| void_b8 | — | loop 100% | — | loop 100% | — | — | — |
| cut | — | loop 100% | — | loop 100% | dead_end 100% | — | dead_end 100% |
| polar_lat75 | — | — | — | — | — | — | — |
| polar_lat60 | — | — | — | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 24.7 | 0.0 | 24.9 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 44.1 | 0.0 | 44.2 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 102.0 | 0.0 | 102.2 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 193.8 | 0.0 | 193.9 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 335.3 | 0.0 | 335.6 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 11.2 | 0.0 | 11.2 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 23.2 | 0.0 | 23.2 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 40.4 | 0.0 | 40.4 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 92.3 | 0.0 | 92.3 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 3.1 | 0.0 | 3.1 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 7.6 | 0.0 | 7.6 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 12.3 | 0.0 | 12.2 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 97.1 | 0.0 | 97.1 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| isl_p0.01 | — | — | 0.1 (2) | — | 29.2 (3211) | 0.1 (2) | 0.0 (1) |
| isl_p0.02 | — | — | 0.6 (16) | — | 67.5 (5615) | 0.6 (16) | 0.4 (23) |
| isl_p0.05 | — | — | 8.2 (189) | — | 235.6 (12406) | 8.2 (189) | 6.1 (329) |
| isl_p0.10 | — | — | 75.4 (1455) | — | 751.7 (21963) | 75.4 (1458) | 64.0 (3016) |
| isl_p0.20 | — | — | 843.1 (10529) | — | 2813.5 (32140) | 843.0 (10533) | 783.4 (17343) |
| sat_p0.005 | — | — | 19.4 (654) | — | 11.7 (1384) | 19.4 (652) | 11.7 (1384) |
| sat_p0.01 | — | — | 49.7 (1489) | — | 28.4 (2684) | 49.7 (1489) | 28.4 (2684) |
| sat_p0.02 | — | — | 95.8 (2660) | — | 63.3 (4680) | 95.8 (2656) | 63.3 (4680) |
| sat_p0.05 | — | — | 277.7 (6172) | — | 212.1 (10263) | 277.6 (6166) | 212.1 (10263) |
| void_b2 | — | — | 6.4 (193) | — | 3.4 (368) | 6.4 (192) | 3.4 (368) |
| void_b4 | — | — | 13.9 (493) | — | 9.6 (762) | 13.9 (493) | 9.6 (762) |
| void_b8 | — | — | 24.2 (734) | — | 18.8 (1223) | 24.2 (734) | 18.8 (1223) |
| cut | — | — | 359.4 (5563) | — | 0.0 (0) | 359.4 (5563) | 0.0 (0) |
| polar_lat75 | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |
| polar_lat60 | — | — | 0.0 (0) | — | 0.0 (0) | 0.0 (0) | 0.0 (0) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | topological_nominal_progress_repair_exceptions | topological_derived | topological_derived_progress_exceptions_attach | topological_derived_progress_repair_exceptions | topological_derived_progress_repair_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.00 | — | 0.08 | 0.00 | 0.00 |
| isl_p0.02 | — | — | 0.00 | — | 0.18 | 0.00 | 0.00 |
| isl_p0.05 | — | — | 0.02 | — | 0.62 | 0.02 | 0.02 |
| isl_p0.10 | — | — | 0.20 | — | 1.98 | 0.20 | 0.17 |
| isl_p0.20 | — | — | 2.22 | — | 7.40 | 2.22 | 2.06 |
| sat_p0.005 | — | — | 0.05 | — | 0.03 | 0.05 | 0.03 |
| sat_p0.01 | — | — | 0.13 | — | 0.07 | 0.13 | 0.07 |
| sat_p0.02 | — | — | 0.25 | — | 0.17 | 0.25 | 0.17 |
| sat_p0.05 | — | — | 0.73 | — | 0.56 | 0.73 | 0.56 |
| void_b2 | — | — | 0.02 | — | 0.01 | 0.02 | 0.01 |
| void_b4 | — | — | 0.04 | — | 0.03 | 0.04 | 0.03 |
| void_b8 | — | — | 0.06 | — | 0.05 | 0.06 | 0.05 |
| cut | — | — | 0.95 | — | 0.00 | 0.95 | 0.00 |
| polar_lat75 | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | — | 0.00 | 0.00 | 0.00 |
