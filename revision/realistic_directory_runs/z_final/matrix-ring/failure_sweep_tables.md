# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 89.7 | 96.3 | 19.1 | 26.5 | 100.0 | 19.1 | 26.4 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +10.3 | +3.7 | +80.9 | +73.5 | +0.0 | +80.9 | +73.6 |

### Distance stretch, shared basis

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0074 | 1.0317 | 1.0043 | 0.9953 | 1.0007 | 1.0043 | 0.9953 |

### Distance stretch, egress-choice factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.004 | 1.016 | 1.004 | 0.995 | 1.000 | 1.004 | 0.995 |

### Distance stretch, forwarding factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.003 | 1.016 | 1.000 | 1.000 | 1.001 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | — | — | — | 0.0 | 6.1 | 10.8 |

### Assigned ground-station links per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 3.7 | 7.3 | — | 3.7 | 7.3 |

### Transit egress switches, %

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 6.9 | — | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | loop 100% | dead_end 100% | dead_end 100% | dead_end 100% | — | dead_end 100% | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 12.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.00 | 0.00 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 81.2 | 99.5 | 30.1 | 33.8 | 100.0 | 30.1 | 33.7 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +18.8 | +0.5 | +69.9 | +66.2 | +0.0 | +69.9 | +66.3 |

### Distance stretch, shared basis

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0081 | 1.0105 | 1.1258 | 1.0986 | 1.0000 | 1.1258 | 1.0984 |

### Distance stretch, egress-choice factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.008 | 1.010 | 1.126 | 1.099 | 1.000 | 1.126 | 1.098 |

### Distance stretch, forwarding factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.001 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | — | — | — | 0.0 | 11.2 | 13.8 |

### Assigned ground-station links per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 1.8 | 4.7 | — | 1.8 | 4.7 |

### Transit egress switches, %

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 14.2 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | loop 100% | dead_end 100% | dead_end 100% | dead_end 100% | — | dead_end 100% | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 29.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.00 | 0.00 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 88.5 | 98.3 | 10.5 | 14.0 | 100.0 | 10.5 | 14.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +11.5 | +1.7 | +89.5 | +86.0 | +0.0 | +89.5 | +86.0 |

### Distance stretch, shared basis

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0311 | 1.0839 | 1.0697 | 1.0000 | 1.0839 | 1.0694 |

### Distance stretch, egress-choice factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.023 | 1.084 | 1.070 | 1.000 | 1.084 | 1.069 |

### Distance stretch, forwarding factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.008 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | — | — | — | 0.0 | 10.7 | 16.1 |

### Assigned ground-station links per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.2 | 1.2 | — | 0.2 | 1.2 |

### Transit egress switches, %

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 16.6 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | loop 100% | dead_end 100% | dead_end 100% | dead_end 100% | — | dead_end 100% | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 15.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 94.1 | 93.8 | 10.6 | 10.5 | 100.0 | 10.6 | 10.5 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +5.9 | +6.2 | +89.4 | +89.5 | +0.0 | +89.4 | +89.5 |

### Distance stretch, shared basis

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.0000 | 1.0000 | 1.0628 | 1.0000 | 0.9953 | 1.0000 | 1.0000 | 0.9953 |

### Distance stretch, egress-choice factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.013 | 1.000 | 0.995 | 1.000 | 1.000 | 0.995 |

### Distance stretch, forwarding factor

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.050 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 0.0 | — | — | — | 0.0 | 15.7 | 20.1 |

### Assigned ground-station links per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 24.0 | 48.0 | — | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | — | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.3 | 0.7 | — | 0.3 | 0.7 |

### Transit egress switches, %

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | 6.8 | — | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | loop 100% | dead_end 100% | dead_end 100% | dead_end 100% | — | dead_end 100% | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 6.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state | explicit_r1 | dra | explicit_r3 | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — | 0.00 | 0.00 |
