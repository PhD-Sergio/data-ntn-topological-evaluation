# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 95.9 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 88.1 ± 0.8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 84.3 ± 0.7 | 100.0 ± 0.0 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +4.1 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +11.9 ± 0.8 | +0.0 ± 0.0 | +0.0 ± 0.0 | +15.7 ± 0.7 | +0.0 ± 0.0 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0020 | 1.2269 | 1.1897 | 1.0081 | 1.2349 | 1.1986 |
| isl_p0.05 | 1.0000 | 1.0092 | 1.2342 | 1.1939 | 1.0145 | 1.2692 | 1.2263 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.227 | 1.190 | 1.002 | 1.227 | 1.190 |
| isl_p0.05 | 1.000 | 1.002 | 1.234 | 1.194 | 1.005 | 1.234 | 1.195 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.002 | 1.000 | 1.000 | 1.006 | 1.007 | 1.008 |
| isl_p0.05 | 1.000 | 1.007 | 1.000 | 1.000 | 1.010 | 1.029 | 1.026 |

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
| none | — | 6.5 | 0.0 | 0.0 | 2.7 | 0.0 | 0.0 |
| isl_p0.05 | — | 14.7 | 0.0 | 0.0 | 12.5 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | loop 100% | — | — |
| isl_p0.05 | — | loop 100% | — | — | loop 100% | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 22.4 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 65.5 | 0.0 | 0.0 | 86.7 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | — | — | — | 55.0 | 62.4 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.00 | 0.00 |
| isl_p0.05 | — | — | — | — | — | 0.20 | 0.23 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 79.4 ± 0.5 | 100.0 ± 0.0 | 100.0 ± 0.0 | 81.6 ± 0.7 | 100.0 ± 0.0 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +20.6 ± 0.5 | +0.0 ± 0.0 | +0.0 ± 0.0 | +18.4 ± 0.7 | +0.0 ± 0.0 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0067 | 1.4675 | 1.3314 | 1.0159 | 1.4852 | 1.3543 |
| isl_p0.05 | 1.0000 | 1.0090 | 1.4922 | 1.3403 | 1.0177 | 1.5543 | 1.3918 |

### Distance stretch, egress-choice factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.467 | 1.331 | 1.001 | 1.467 | 1.332 |
| isl_p0.05 | 1.000 | 1.001 | 1.492 | 1.340 | 1.002 | 1.492 | 1.342 |

### Distance stretch, forwarding factor

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.007 | 1.000 | 1.000 | 1.015 | 1.013 | 1.018 |
| isl_p0.05 | 1.000 | 1.008 | 1.000 | 1.000 | 1.016 | 1.043 | 1.037 |

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
| none | — | 4.5 | 0.0 | 0.0 | 0.4 | 0.0 | 0.0 |
| isl_p0.05 | — | 8.1 | 0.0 | 0.0 | 6.6 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | loop 100% | — | — | loop 100% | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 113.5 | 0.0 | 0.0 | 101.8 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.0 | 0.0 |
| isl_p0.05 | — | — | — | — | — | 90.1 | 77.7 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | topological_nominal | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | 0.00 | 0.00 |
| isl_p0.05 | — | — | — | — | — | 0.24 | 0.20 |
