# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 87.9 ± 2.7 | 84.9 ± 3.7 | 89.1 ± 3.1 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +12.1 ± 2.7 | +15.1 ± 3.7 | +10.9 ± 3.1 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 2.0456 | 1.0000 | 1.2567 | 1.0395 | 1.0002 | 2.0457 |
| isl_p0.05 | 1.0000 | 2.0486 | 1.0000 | 1.2594 | 1.0364 | 1.0031 | 2.0971 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 2.046 | 1.000 | 1.117 | 1.015 | 1.000 | 2.046 |
| isl_p0.05 | 1.000 | 2.049 | 1.000 | 1.116 | 1.015 | 1.001 | 2.049 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.121 | 1.023 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.125 | 1.021 | 1.002 | 1.023 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | 8.2 |
| isl_p0.05 | — | — | — | — | 0.0 | 0.0 | 8.2 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 24.0 | — | — | — | — | 24.0 |
| isl_p0.05 | — | 24.0 | — | — | — | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | — | — | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | — | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 1.9 | — | — | — | — | 1.9 |
| isl_p0.05 | — | 1.9 | — | — | — | — | 1.9 |

### Transit egress switches, %

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 0.7 | 0.2 | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | 1.1 | 3.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | link_down 100% | loop 100% | loop 100% | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 83.4 | 60.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.0 (0) |
| isl_p0.05 | — | — | — | — | — | — | 77.0 (1460) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.00 |
| isl_p0.05 | — | — | — | — | — | — | 0.91 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 77.7 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 99.9 ± 0.1 | 100.0 ± 0.0 | 75.6 ± 3.6 | 57.1 ± 2.1 | 83.0 ± 1.1 | 99.9 ± 0.1 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +22.3 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.1 ± 0.1 | +0.0 ± 0.0 | +24.4 ± 3.6 | +42.9 ± 2.1 | +17.0 ± 1.1 | +0.1 ± 0.1 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.2182 | 1.0000 | 1.1901 | 1.0634 | 1.0000 | 1.2182 |
| isl_p0.05 | 1.0000 | 1.2276 | 1.0000 | 1.1781 | 1.0481 | 1.0034 | 1.2591 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.218 | 1.000 | 1.103 | 1.010 | 1.000 | 1.218 |
| isl_p0.05 | 1.000 | 1.228 | 1.000 | 1.101 | 1.011 | 1.001 | 1.228 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.072 | 1.053 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.063 | 1.037 | 1.002 | 1.025 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | 11.0 |
| isl_p0.05 | — | — | — | — | 0.0 | 0.0 | 11.0 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 24.0 | — | — | — | — | 24.0 |
| isl_p0.05 | — | 24.0 | — | — | — | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | — | — | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | — | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 1.5 | — | — | — | — | 1.5 |
| isl_p0.05 | — | 1.5 | — | — | — | — | 1.5 |

### Transit egress switches, %

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 1.4 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | 1.6 | 7.3 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | loop 100% | — | — |
| isl_p0.05 | — | dead_end 100% | — | link_down 100% | loop 100% | loop 100% | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 122.9 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 237.0 | 93.6 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.0 (0) |
| isl_p0.05 | — | — | — | — | — | — | 130.5 (4858) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.00 |
| isl_p0.05 | — | — | — | — | — | — | 0.92 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 79.0 ± 1.6 | 72.2 ± 1.6 | 88.5 ± 0.8 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +21.0 ± 1.6 | +27.8 ± 1.6 | +11.5 ± 0.8 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 1.6451 | 1.0000 | 1.3114 | 1.0353 | 1.0000 | 1.6451 |
| isl_p0.05 | 1.0000 | 1.6485 | 1.0000 | 1.3051 | 1.0321 | 1.0077 | 1.6802 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.645 | 1.000 | 1.098 | 1.007 | 1.000 | 1.645 |
| isl_p0.05 | 1.000 | 1.648 | 1.000 | 1.099 | 1.007 | 1.003 | 1.648 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.176 | 1.028 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.167 | 1.025 | 1.004 | 1.021 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | 16.8 |
| isl_p0.05 | — | — | — | — | 0.0 | 0.0 | 16.8 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 24.0 | — | — | — | — | 24.0 |
| isl_p0.05 | — | 24.0 | — | — | — | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | — | — | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | — | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.4 | — | — | — | — | 0.4 |
| isl_p0.05 | — | 0.4 | — | — | — | — | 0.4 |

### Transit egress switches, %

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | 0.3 | 11.7 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | link_down 100% | loop 100% | loop 100% | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 153.3 | 63.7 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.0 (0) |
| isl_p0.05 | — | — | — | — | — | — | 185.2 (8229) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.00 |
| isl_p0.05 | — | — | — | — | — | — | 0.67 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 75.6 ± 1.4 | 69.7 ± 0.3 | 81.5 ± 0.3 | 100.0 ± 0.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 |
| isl_p0.05 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 | +24.4 ± 1.4 | +30.3 ± 0.3 | +18.5 ± 0.3 | +0.0 ± 0.0 |

### Distance stretch, shared basis

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.0000 | 2.0569 | 1.0000 | 1.2957 | 1.0199 | 1.0000 | 2.0569 |
| isl_p0.05 | 1.0000 | 2.0561 | 1.0000 | 1.3038 | 1.0186 | 1.0030 | 2.1054 |

### Distance stretch, egress-choice factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 2.057 | 1.000 | 1.085 | 1.008 | 1.000 | 2.057 |
| isl_p0.05 | 1.000 | 2.056 | 1.000 | 1.089 | 1.008 | 1.001 | 2.056 |

### Distance stretch, forwarding factor

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.178 | 1.012 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 | 1.000 | 1.179 | 1.011 | 1.002 | 1.028 |

### Ground station renumberings per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | 0.0 | 0.0 | 18.9 |
| isl_p0.05 | — | — | — | — | 0.0 | 0.0 | 18.9 |

### Assigned ground-station links per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 24.0 | — | — | — | — | 24.0 |
| isl_p0.05 | — | 24.0 | — | — | — | — | 24.0 |

### Requested attachment shortfall per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | — | — | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | — | — | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.1 | — | — | — | — | 0.1 |
| isl_p0.05 | — | 0.1 | — | — | — | — | 0.1 |

### Transit egress switches, %

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | 0.0 | — | — | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | — | 0.0 | — | — | 0.2 | 6.2 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | — |
| isl_p0.05 | — | — | — | link_down 100% | loop 100% | loop 100% | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 167.2 | 102.2 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.0 (0) |
| isl_p0.05 | — | — | — | — | — | — | 235.6 (12406) |

### Exception entries, % of link-state forwarding entries

| condition | link_state | link_state_attach | explicit_r1 | explicit_r15 | dra | topological_derived | topological_derived_progress_exceptions_attach |
|---|---|---|---|---|---|---|---|
| none | — | — | — | — | — | — | 0.00 |
| isl_p0.05 | — | — | — | — | — | — | 0.62 |
