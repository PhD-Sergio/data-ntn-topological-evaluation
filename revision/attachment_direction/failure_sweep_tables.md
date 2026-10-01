# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 81.2 ± 3.1 | 84.4 ± 3.9 | 85.8 ± 3.4 | 84.3 ± 4.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.2569 | 2.0419 | 1.1767 | 2.0456 | 1.2569 | 2.0420 | 1.1768 | 2.0458 |
| isl_p0.05 | 1.2757 | 2.0455 | 1.1852 | 2.0486 | 1.2540 | 2.0468 | 1.1730 | 2.0534 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.257 | 2.042 | 1.177 | 2.046 | 1.257 | 2.042 | 1.177 | 2.046 |
| isl_p0.05 | 1.276 | 2.045 | 1.185 | 2.049 | 1.250 | 2.034 | 1.170 | 2.040 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.003 | 1.005 | 1.003 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 6.0 | 10.7 | 10.7 | 8.2 |
| isl_p0.05 | — | — | — | — | 6.0 | 10.7 | 10.7 | 8.2 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |
| isl_p0.05 | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 3.8 | 7.4 | 7.4 | 1.9 | 3.8 | 7.4 | 7.4 | 1.9 |
| isl_p0.05 | 3.8 | 7.4 | 7.4 | 1.9 | 3.8 | 7.4 | 7.4 | 1.9 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 103.8 | 86.3 | 78.4 | 86.6 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 99.9 ± 0.2 | 99.9 ± 0.1 | 99.9 ± 0.1 | 99.9 ± 0.1 | 78.3 ± 1.7 | 76.8 ± 1.0 | 78.9 ± 0.8 | 76.8 ± 1.3 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.1763 | 1.2220 | 1.1349 | 1.2182 | 1.1763 | 1.2221 | 1.1349 | 1.2183 |
| isl_p0.05 | 1.1841 | 1.2315 | 1.1421 | 1.2276 | 1.1850 | 1.2259 | 1.1381 | 1.2222 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.176 | 1.222 | 1.135 | 1.218 | 1.176 | 1.222 | 1.135 | 1.218 |
| isl_p0.05 | 1.184 | 1.232 | 1.142 | 1.228 | 1.179 | 1.220 | 1.133 | 1.216 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.005 | 1.005 | 1.005 | 1.005 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 10.9 | 13.7 | 13.7 | 11.0 |
| isl_p0.05 | — | — | — | — | 10.9 | 13.7 | 13.7 | 11.0 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |
| isl_p0.05 | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.8 | 5.1 | 5.1 | 1.5 | 1.8 | 5.1 | 5.1 | 1.5 |
| isl_p0.05 | 1.8 | 5.1 | 5.1 | 1.5 | 1.8 | 5.1 | 5.1 | 1.5 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 120.0 | 127.8 | 116.3 | 128.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 81.9 ± 2.3 | 77.4 ± 1.9 | 83.1 ± 1.5 | 77.7 ± 1.2 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.2079 | 1.6517 | 1.1729 | 1.6451 | 1.2079 | 1.6517 | 1.1729 | 1.6451 |
| isl_p0.05 | 1.2160 | 1.6555 | 1.1774 | 1.6485 | 1.2248 | 1.6161 | 1.1831 | 1.6125 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.208 | 1.652 | 1.173 | 1.645 | 1.208 | 1.652 | 1.173 | 1.645 |
| isl_p0.05 | 1.216 | 1.655 | 1.177 | 1.648 | 1.212 | 1.604 | 1.172 | 1.601 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.011 | 1.008 | 1.009 | 1.008 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 10.5 | 15.5 | 15.5 | 16.8 |
| isl_p0.05 | — | — | — | — | 10.5 | 15.5 | 15.5 | 16.8 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |
| isl_p0.05 | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.2 | 1.0 | 1.0 | 0.4 | 0.2 | 1.0 | 1.0 | 0.4 |
| isl_p0.05 | 0.2 | 1.0 | 1.0 | 0.4 | 0.2 | 1.0 | 1.0 | 0.4 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 99.7 | 124.7 | 93.4 | 123.2 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 59.9 ± 1.0 | 70.0 ± 1.7 | 75.5 ± 0.8 | 70.1 ± 1.5 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.4460 | 2.0679 | 1.3199 | 2.0569 | 1.4460 | 2.0679 | 1.3199 | 2.0569 |
| isl_p0.05 | 1.4712 | 2.0681 | 1.3280 | 2.0561 | 1.4467 | 2.1409 | 1.2921 | 2.1482 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.446 | 2.068 | 1.320 | 2.057 | 1.446 | 2.068 | 1.320 | 2.057 |
| isl_p0.05 | 1.471 | 2.068 | 1.328 | 2.056 | 1.444 | 2.135 | 1.289 | 2.142 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.000 | 1.002 | 1.003 | 1.002 | 1.003 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 15.4 | 19.4 | 19.4 | 18.9 |
| isl_p0.05 | — | — | — | — | 15.4 | 19.4 | 19.4 | 18.9 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |
| isl_p0.05 | 24.0 | 48.0 | 48.0 | 24.0 | 24.0 | 48.0 | 48.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.3 | 0.6 | 0.6 | 0.1 | 0.3 | 0.6 | 0.6 | 0.1 |
| isl_p0.05 | 0.3 | 0.6 | 0.6 | 0.1 | 0.3 | 0.6 | 0.6 | 0.1 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | loop 100% | loop 100% | loop 100% | loop 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 221.2 | 165.4 | 135.2 | 165.1 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half | link_state_dir_half_req | link_state_dir_k1 | topological_derived_dir_asc | topological_derived_dir_half | topological_derived_dir_half_req | topological_derived_dir_k1 |
|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | — | — | — | — | — |
