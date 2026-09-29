# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 84.3 ± 4.0 | 84.3 ± 4.0 | 86.9 ± 2.9 | 84.4 ± 3.8 | 84.3 ± 4.0 | 84.7 ± 3.4 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +15.7 ± 4.0 | +15.7 ± 4.0 | +13.1 ± 2.9 | +15.6 ± 3.8 | +15.7 ± 4.0 | +15.3 ± 3.4 |

### Distance stretch, shared basis

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 2.0456 | 2.0456 | 1.0890 | 2.0444 | 2.0456 | 2.0535 | 2.0457 | 2.0457 | 1.0890 | 2.0444 | 2.0457 | 2.0535 |
| isl_p0.05 | 1.0000 | 2.0486 | 2.0486 | 1.0904 | 2.0479 | 2.0486 | 2.0571 | 2.0532 | 2.0532 | 1.0856 | 2.0484 | 2.0532 | 2.0614 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 2.046 | 2.046 | 1.089 | 2.044 | 2.046 | 2.053 | 2.046 | 2.046 | 1.089 | 2.044 | 2.046 | 2.053 |
| isl_p0.05 | 1.000 | 2.049 | 2.049 | 1.090 | 2.048 | 2.049 | 2.057 | 2.040 | 2.040 | 1.083 | 2.035 | 2.040 | 2.048 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.005 | 1.005 | 1.002 | 1.005 | 1.005 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 8.2 | 10.9 | 10.9 | 10.9 | 13.9 | 13.9 |
| isl_p0.05 | — | — | — | — | — | — | — | 8.2 | 10.9 | 10.9 | 10.9 | 13.9 | 13.9 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |
| isl_p0.05 | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 1.9 | 7.3 | 7.3 | 7.3 | 21.9 | 21.9 | 1.9 | 7.3 | 7.3 | 7.3 | 21.9 | 21.9 |
| isl_p0.05 | — | 1.9 | 7.3 | 7.3 | 7.3 | 21.9 | 21.9 | 1.9 | 7.3 | 7.3 | 7.3 | 21.9 | 21.9 |

### Transit egress switches, %

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 86.5 | 86.5 | 72.3 | 85.9 | 86.5 | 84.3 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 99.9 ± 0.1 | 99.9 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.2 | 99.9 ± 0.1 | 99.9 ± 0.2 | 76.8 ± 1.3 | 76.8 ± 1.3 | 77.8 ± 1.1 | 76.9 ± 1.1 | 76.8 ± 1.3 | 76.7 ± 1.3 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.1 ± 0.1 | +0.0 ± 0.0 | +0.1 ± 0.2 | +0.1 ± 0.1 | +0.1 ± 0.2 | +23.2 ± 1.3 | +23.2 ± 1.3 | +22.2 ± 1.1 | +23.1 ± 1.1 | +23.2 ± 1.3 | +23.3 ± 1.3 |

### Distance stretch, shared basis

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.2182 | 1.2182 | 1.1609 | 1.2242 | 1.2182 | 1.2339 | 1.2182 | 1.2182 | 1.1609 | 1.2242 | 1.2182 | 1.2339 |
| isl_p0.05 | 1.0000 | 1.2276 | 1.2276 | 1.1682 | 1.2336 | 1.2276 | 1.2436 | 1.2222 | 1.2222 | 1.1624 | 1.2275 | 1.2222 | 1.2379 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.218 | 1.218 | 1.161 | 1.224 | 1.218 | 1.234 | 1.218 | 1.218 | 1.161 | 1.224 | 1.218 | 1.234 |
| isl_p0.05 | 1.000 | 1.228 | 1.228 | 1.168 | 1.234 | 1.228 | 1.244 | 1.216 | 1.216 | 1.157 | 1.221 | 1.216 | 1.232 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.005 | 1.005 | 1.004 | 1.005 | 1.005 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 11.0 | 13.2 | 13.2 | 13.2 | 20.6 | 20.6 |
| isl_p0.05 | — | — | — | — | — | — | — | 11.0 | 13.2 | 13.2 | 13.2 | 20.6 | 20.6 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |
| isl_p0.05 | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 1.5 | 4.8 | 4.8 | 4.8 | 16.4 | 16.4 | 1.5 | 4.8 | 4.8 | 4.8 | 16.4 | 16.4 |
| isl_p0.05 | — | 1.5 | 4.8 | 4.8 | 4.8 | 16.4 | 16.4 | 1.5 | 4.8 | 4.8 | 4.8 | 16.4 | 16.4 |

### Transit egress switches, %

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | dead_end 100% | dead_end 100% | — | dead_end 100% | dead_end 100% | dead_end 100% | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 127.9 | 127.9 | 122.2 | 127.4 | 127.9 | 128.3 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 77.7 ± 1.2 | 77.7 ± 1.2 | 83.6 ± 0.8 | 77.4 ± 1.8 | 77.7 ± 1.2 | 77.2 ± 1.4 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +22.3 ± 1.2 | +22.3 ± 1.2 | +16.4 ± 0.8 | +22.6 ± 1.8 | +22.3 ± 1.2 | +22.8 ± 1.4 |

### Distance stretch, shared basis

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.6451 | 1.6451 | 1.0683 | 1.6556 | 1.6451 | 1.6266 | 1.6451 | 1.6451 | 1.0683 | 1.6556 | 1.6451 | 1.6266 |
| isl_p0.05 | 1.0000 | 1.6485 | 1.6485 | 1.0705 | 1.6596 | 1.6485 | 1.6309 | 1.6126 | 1.6126 | 1.0746 | 1.6207 | 1.6126 | 1.5958 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.645 | 1.645 | 1.068 | 1.656 | 1.645 | 1.627 | 1.645 | 1.645 | 1.068 | 1.656 | 1.645 | 1.627 |
| isl_p0.05 | 1.000 | 1.648 | 1.648 | 1.070 | 1.660 | 1.648 | 1.631 | 1.602 | 1.602 | 1.066 | 1.609 | 1.602 | 1.584 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.008 | 1.008 | 1.008 | 1.008 | 1.008 | 1.008 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 16.8 | 17.3 | 17.3 | 17.3 | 19.3 | 19.3 |
| isl_p0.05 | — | — | — | — | — | — | — | 16.8 | 17.3 | 17.3 | 17.3 | 19.3 | 19.3 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |
| isl_p0.05 | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.4 | 1.4 | 1.4 | 1.4 | 5.6 | 5.6 | 0.4 | 1.4 | 1.4 | 1.4 | 5.6 | 5.6 |
| isl_p0.05 | — | 0.4 | 1.4 | 1.4 | 1.4 | 5.6 | 5.6 | 0.4 | 1.4 | 1.4 | 1.4 | 5.6 | 5.6 |

### Transit egress switches, %

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 123.0 | 123.0 | 90.5 | 125.0 | 123.0 | 125.6 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 70.1 ± 1.5 | 70.1 ± 1.5 | 80.3 ± 0.6 | 70.1 ± 1.7 | 70.1 ± 1.5 | 70.0 ± 1.3 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +29.9 ± 1.5 | +29.9 ± 1.5 | +19.7 ± 0.6 | +29.9 ± 1.7 | +29.9 ± 1.5 | +30.0 ± 1.3 |

### Distance stretch, shared basis

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 2.0569 | 2.0569 | 1.0419 | 2.0659 | 2.0569 | 2.1298 | 2.0569 | 2.0569 | 1.0419 | 2.0659 | 2.0569 | 2.1298 |
| isl_p0.05 | 1.0000 | 2.0561 | 2.0561 | 1.0414 | 2.0660 | 2.0561 | 2.1298 | 2.1479 | 2.1479 | 1.0300 | 2.1391 | 2.1479 | 2.2074 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 2.057 | 2.057 | 1.042 | 2.066 | 2.057 | 2.130 | 2.057 | 2.057 | 1.042 | 2.066 | 2.057 | 2.130 |
| isl_p0.05 | 1.000 | 2.056 | 2.056 | 1.041 | 2.066 | 2.056 | 2.130 | 2.142 | 2.142 | 1.028 | 2.133 | 2.142 | 2.201 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.003 | 1.003 | 1.002 | 1.003 | 1.003 | 1.003 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 18.9 | 19.7 | 19.7 | 19.7 | 21.9 | 21.9 |
| isl_p0.05 | — | — | — | — | — | — | — | 18.9 | 19.7 | 19.7 | 19.7 | 21.9 | 21.9 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |
| isl_p0.05 | — | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 | 24.0 | 48.0 | 48.0 | 48.0 | 96.0 | 96.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.1 | 0.6 | 0.6 | 0.6 | 3.3 | 3.3 | 0.1 | 0.6 | 0.6 | 0.6 | 3.3 | 3.3 |
| isl_p0.05 | — | 0.1 | 0.6 | 0.6 | 0.6 | 3.3 | 3.3 | 0.1 | 0.6 | 0.6 | 0.6 | 3.3 | 3.3 |

### Transit egress switches, %

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 165.3 | 165.3 | 108.8 | 165.1 | 165.3 | 165.5 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_addr_k1 | link_state_addr_k2_nearest | link_state_addr_k2_perflow | link_state_addr_k2_sticky | link_state_addr_k4_nearest | link_state_addr_k4_sticky | topological_nominal_addr_k1 | topological_nominal_addr_k2_nearest | topological_nominal_addr_k2_perflow | topological_nominal_addr_k2_sticky | topological_nominal_addr_k4_nearest | topological_nominal_addr_k4_sticky |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — | — | — | — | — | — |
