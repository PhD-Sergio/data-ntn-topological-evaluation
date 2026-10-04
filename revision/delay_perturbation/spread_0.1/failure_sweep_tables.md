# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 88.4 ± 0.8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 88.3 ± 0.9 | 100.0 ± 0.0 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +11.6 ± 0.8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +11.7 ± 0.9 | +0.0 ± 0.0 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0002 | 1.2143 | 1.1787 | 1.0012 | 1.2152 | 1.1799 |
| isl_p0.05 | 1.0000 | 1.0075 | 1.2222 | 1.1832 | 1.0086 | 1.2520 | 1.2097 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.214 | 1.179 | 1.000 | 1.214 | 1.179 |
| isl_p0.05 | 1.000 | 1.003 | 1.222 | 1.183 | 1.003 | 1.222 | 1.184 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 | 1.001 | 1.001 | 1.001 |
| isl_p0.05 | 1.000 | 1.005 | 1.000 | 1.000 | 1.005 | 1.024 | 1.022 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 0.0 | 10.5 | 15.5 |
| isl_p0.05 | — | 0.0 | — | — | 0.0 | 10.5 | 15.5 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |
| isl_p0.05 | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.2 | 1.0 | — | 0.2 | 1.0 |
| isl_p0.05 | — | — | 0.2 | 1.0 | — | 0.2 | 1.0 |

### Transit egress switches, %

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | 1.8 | 0.0 | 0.0 | 0.6 | 0.0 | 0.0 |
| isl_p0.05 | — | 12.3 | 0.0 | 0.0 | 11.8 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | loop 100% | — | — | loop 100% | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 64.0 | 0.0 | 0.0 | 64.8 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | — | — | — | 54.2 | 59.9 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.00 | 0.00 |
| isl_p0.05 | — | — | — | — | — | 0.20 | 0.22 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 81.1 ± 0.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 81.8 ± 0.6 | 100.0 ± 0.0 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +18.9 ± 0.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +18.2 ± 0.6 | +0.0 ± 0.0 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0014 | 1.4539 | 1.3250 | 1.0040 | 1.4583 | 1.3309 |
| isl_p0.05 | 1.0000 | 1.0039 | 1.4788 | 1.3333 | 1.0065 | 1.5303 | 1.3700 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.454 | 1.325 | 1.000 | 1.454 | 1.325 |
| isl_p0.05 | 1.000 | 1.001 | 1.479 | 1.333 | 1.001 | 1.479 | 1.334 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.001 | 1.000 | 1.000 | 1.004 | 1.003 | 1.005 |
| isl_p0.05 | 1.000 | 1.003 | 1.000 | 1.000 | 1.005 | 1.036 | 1.026 |

### Ground station renumberings per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 0.0 | 15.4 | 19.4 |
| isl_p0.05 | — | 0.0 | — | — | 0.0 | 15.4 | 19.4 |

### Assigned ground-station links per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |
| isl_p0.05 | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | 0.3 | 0.6 | — | 0.3 | 0.6 |
| isl_p0.05 | — | — | 0.3 | 0.6 | — | 0.3 | 0.6 |

### Transit egress switches, %

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | 1.1 | 0.0 | 0.0 | 0.2 | 0.0 | 0.0 |
| isl_p0.05 | — | 5.5 | 0.0 | 0.0 | 6.2 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | loop 100% | — | — | loop 100% | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 104.3 | 0.0 | 0.0 | 100.4 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | — | — | — | 89.1 | 72.3 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.00 | 0.00 |
| isl_p0.05 | — | — | — | — | — | 0.23 | 0.19 |
