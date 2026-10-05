# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 100.0 ± 0.0 |
| sat_p0.005 | — | 99.8 ± 0.6 |
| void_b2 | 100.0 ± 0.0 | 99.9 ± 0.3 |
| void_b4 | 100.0 ± 0.0 | 99.2 ± 0.9 |
| void_b8 | 100.0 ± 0.0 | 99.3 ± 0.9 |
| cut | 51.6 | 51.6 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | — |
| sat_p0.005 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.2650 |
| sat_p0.005 | — | 1.2618 |
| void_b2 | 1.2590 | 1.2584 |
| void_b4 | 1.2652 | 1.2604 |
| void_b8 | 1.3330 | 1.3269 |
| cut | 1.2132 | 1.2132 |
| polar_lat75 | 1.2524 | 1.2524 |
| polar_lat60 | 1.2558 | 1.2558 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.259 |
| sat_p0.005 | — | 1.258 |
| void_b2 | 1.257 | 1.256 |
| void_b4 | 1.261 | 1.258 |
| void_b8 | 1.325 | 1.320 |
| cut | 1.213 | 1.213 |
| polar_lat75 | 1.252 | 1.252 |
| polar_lat60 | 1.255 | 1.255 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.005 |
| sat_p0.005 | — | 1.003 |
| void_b2 | 1.002 | 1.002 |
| void_b4 | 1.003 | 1.002 |
| void_b8 | 1.004 | 1.003 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.001 | 1.001 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 6.0 |
| sat_p0.005 | — | 6.0 |
| void_b2 | 6.0 | 6.0 |
| void_b4 | 6.0 | 6.0 |
| void_b8 | 5.8 | 5.8 |
| cut | 6.0 | 6.0 |
| polar_lat75 | 6.0 | 6.0 |
| polar_lat60 | 6.0 | 6.0 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 24.0 |
| sat_p0.005 | — | 24.0 |
| void_b2 | 24.0 | 24.0 |
| void_b4 | 24.0 | 24.0 |
| void_b8 | 24.0 | 24.0 |
| cut | 24.0 | 24.0 |
| polar_lat75 | 24.0 | 24.0 |
| polar_lat60 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 3.8 |
| sat_p0.005 | — | 3.8 |
| void_b2 | 3.8 | 3.8 |
| void_b4 | 3.8 | 3.8 |
| void_b8 | 3.8 | 3.8 |
| cut | 3.8 | 3.8 |
| polar_lat75 | 3.8 | 3.8 |
| polar_lat60 | 3.8 | 3.8 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | dead_end 62% |
| sat_p0.005 | — | dead_end 67% |
| void_b2 | — | loop 66% |
| void_b4 | — | loop 65% |
| void_b8 | — | loop 58% |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | dead_end 100% |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 1.3 |
| void_b2 | 0.0 | 0.4 |
| void_b4 | 0.0 | 3.9 |
| void_b8 | 0.0 | 2.9 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 167.6 |
| sat_p0.005 | — | 71.6 |
| void_b2 | 84.3 | 93.4 |
| void_b4 | 171.5 | 171.0 |
| void_b8 | 215.9 | 201.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 4297.3 | 4305.5 |
| polar_lat60 | 9479.9 | 9494.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.99 |
| sat_p0.005 | — | 0.85 |
| void_b2 | 1.00 | 1.11 |
| void_b4 | 2.04 | 2.03 |
| void_b8 | 2.56 | 2.39 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 51.01 | 51.11 |
| polar_lat60 | 112.53 | 112.70 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 100.0 ± 0.1 |
| sat_p0.005 | — | 99.8 ± 0.3 |
| void_b2 | 100.0 ± 0.0 | 99.4 ± 0.8 |
| void_b4 | 100.0 ± 0.0 | 97.8 ± 1.0 |
| void_b8 | 100.0 ± 0.0 | 98.3 ± 2.4 |
| cut | 71.7 | 71.7 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | — |
| sat_p0.005 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.1862 |
| sat_p0.005 | — | 1.1781 |
| void_b2 | 1.1784 | 1.1772 |
| void_b4 | 1.1830 | 1.1787 |
| void_b8 | 1.1812 | 1.1791 |
| cut | 1.1907 | 1.1907 |
| polar_lat75 | 1.1874 | 1.1874 |
| polar_lat60 | 1.2006 | 1.2006 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.178 |
| sat_p0.005 | — | 1.177 |
| void_b2 | 1.177 | 1.176 |
| void_b4 | 1.177 | 1.175 |
| void_b8 | 1.172 | 1.171 |
| cut | 1.191 | 1.191 |
| polar_lat75 | 1.186 | 1.186 |
| polar_lat60 | 1.198 | 1.198 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.007 |
| sat_p0.005 | — | 1.001 |
| void_b2 | 1.001 | 1.001 |
| void_b4 | 1.005 | 1.003 |
| void_b8 | 1.008 | 1.007 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.001 | 1.001 |
| polar_lat60 | 1.002 | 1.002 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 10.9 |
| sat_p0.005 | — | 10.9 |
| void_b2 | 10.9 | 10.9 |
| void_b4 | 10.7 | 10.7 |
| void_b8 | 10.3 | 10.3 |
| cut | 10.9 | 10.9 |
| polar_lat75 | 10.9 | 10.9 |
| polar_lat60 | 10.9 | 10.9 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 24.0 |
| sat_p0.005 | — | 24.0 |
| void_b2 | 24.0 | 24.0 |
| void_b4 | 24.0 | 24.0 |
| void_b8 | 23.4 | 23.4 |
| cut | 24.0 | 24.0 |
| polar_lat75 | 24.0 | 24.0 |
| polar_lat60 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.6 | 0.6 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.8 |
| sat_p0.005 | — | 1.8 |
| void_b2 | 1.8 | 1.8 |
| void_b4 | 1.9 | 1.9 |
| void_b8 | 2.0 | 2.0 |
| cut | 1.8 | 1.8 |
| polar_lat75 | 1.8 | 1.8 |
| polar_lat60 | 1.8 | 1.8 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | loop 61% |
| sat_p0.005 | — | loop 100% |
| void_b2 | — | loop 87% |
| void_b4 | — | loop 90% |
| void_b8 | — | loop 65% |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | dead_end 100% |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.1 |
| sat_p0.005 | — | 0.9 |
| void_b2 | 0.0 | 3.3 |
| void_b4 | 0.0 | 11.0 |
| void_b8 | 0.0 | 6.2 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 504.2 |
| sat_p0.005 | — | 174.7 |
| void_b2 | 151.6 | 150.8 |
| void_b4 | 355.0 | 362.2 |
| void_b8 | 920.9 | 740.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 8615.7 | 8615.7 |
| polar_lat60 | 21637.4 | 21637.4 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 3.57 |
| sat_p0.005 | — | 1.24 |
| void_b2 | 1.07 | 1.07 |
| void_b4 | 2.52 | 2.57 |
| void_b8 | 6.53 | 5.24 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 61.05 | 61.05 |
| polar_lat60 | 153.33 | 153.33 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 100.0 ± 0.0 |
| sat_p0.005 | — | 99.9 ± 0.1 |
| void_b2 | 100.0 ± 0.0 | 99.5 ± 0.6 |
| void_b4 | 100.0 ± 0.0 | 99.1 ± 0.8 |
| void_b8 | 100.0 ± 0.0 | 98.8 ± 1.5 |
| cut | 64.6 | 64.6 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | — |
| sat_p0.005 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.2149 |
| sat_p0.005 | — | 1.2106 |
| void_b2 | 1.2091 | 1.2085 |
| void_b4 | 1.2095 | 1.2077 |
| void_b8 | 1.2255 | 1.2213 |
| cut | 1.1781 | 1.1781 |
| polar_lat75 | 1.2079 | 1.2079 |
| polar_lat60 | 1.2079 | 1.2079 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.209 |
| sat_p0.005 | — | 1.208 |
| void_b2 | 1.208 | 1.208 |
| void_b4 | 1.207 | 1.206 |
| void_b8 | 1.221 | 1.218 |
| cut | 1.178 | 1.178 |
| polar_lat75 | 1.208 | 1.208 |
| polar_lat60 | 1.208 | 1.208 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.005 |
| sat_p0.005 | — | 1.002 |
| void_b2 | 1.001 | 1.000 |
| void_b4 | 1.002 | 1.001 |
| void_b8 | 1.003 | 1.002 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 10.5 |
| sat_p0.005 | — | 10.5 |
| void_b2 | 10.5 | 10.5 |
| void_b4 | 10.5 | 10.5 |
| void_b8 | 10.3 | 10.3 |
| cut | 10.5 | 10.5 |
| polar_lat75 | 10.5 | 10.5 |
| polar_lat60 | 10.5 | 10.5 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 24.0 |
| sat_p0.005 | — | 24.0 |
| void_b2 | 24.0 | 24.0 |
| void_b4 | 24.0 | 24.0 |
| void_b8 | 24.0 | 24.0 |
| cut | 24.0 | 24.0 |
| polar_lat75 | 24.0 | 24.0 |
| polar_lat60 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.2 |
| sat_p0.005 | — | 0.2 |
| void_b2 | 0.2 | 0.2 |
| void_b4 | 0.3 | 0.3 |
| void_b8 | 0.5 | 0.5 |
| cut | 0.2 | 0.2 |
| polar_lat75 | 0.2 | 0.2 |
| polar_lat60 | 0.2 | 0.2 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | loop 50% |
| sat_p0.005 | — | loop 75% |
| void_b2 | — | loop 98% |
| void_b4 | — | loop 72% |
| void_b8 | — | loop 59% |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.5 |
| void_b2 | 0.0 | 2.5 |
| void_b4 | 0.0 | 4.2 |
| void_b8 | 0.0 | 4.9 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1110.7 |
| sat_p0.005 | — | 478.1 |
| void_b2 | 169.1 | 153.2 |
| void_b4 | 399.3 | 373.8 |
| void_b8 | 808.0 | 857.2 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 4.00 |
| sat_p0.005 | — | 1.72 |
| void_b2 | 0.61 | 0.55 |
| void_b4 | 1.44 | 1.35 |
| void_b8 | 2.91 | 3.09 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 100.0 ± 0.0 |
| sat_p0.005 | — | 99.7 ± 0.2 |
| void_b2 | 100.0 ± 0.0 | 99.9 ± 0.3 |
| void_b4 | 100.0 ± 0.0 | 99.2 ± 1.4 |
| void_b8 | 100.0 ± 0.0 | 97.7 ± 2.1 |
| cut | 54.6 | 54.6 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | — |
| sat_p0.005 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.4640 |
| sat_p0.005 | — | 1.4528 |
| void_b2 | 1.4483 | 1.4481 |
| void_b4 | 1.4534 | 1.4507 |
| void_b8 | 1.4663 | 1.4570 |
| cut | 1.3726 | 1.3726 |
| polar_lat75 | 1.4460 | 1.4460 |
| polar_lat60 | 1.4460 | 1.4460 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.450 |
| sat_p0.005 | — | 1.447 |
| void_b2 | 1.447 | 1.447 |
| void_b4 | 1.449 | 1.448 |
| void_b8 | 1.457 | 1.451 |
| cut | 1.373 | 1.373 |
| polar_lat75 | 1.446 | 1.446 |
| polar_lat60 | 1.446 | 1.446 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1.010 |
| sat_p0.005 | — | 1.004 |
| void_b2 | 1.001 | 1.001 |
| void_b4 | 1.003 | 1.002 |
| void_b8 | 1.007 | 1.004 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 15.4 |
| sat_p0.005 | — | 15.3 |
| void_b2 | 15.4 | 15.4 |
| void_b4 | 15.3 | 15.3 |
| void_b8 | 15.2 | 15.2 |
| cut | 15.4 | 15.4 |
| polar_lat75 | 15.4 | 15.4 |
| polar_lat60 | 15.4 | 15.4 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 24.0 |
| sat_p0.005 | — | 24.0 |
| void_b2 | 24.0 | 24.0 |
| void_b4 | 24.0 | 24.0 |
| void_b8 | 24.0 | 24.0 |
| cut | 24.0 | 24.0 |
| polar_lat75 | 24.0 | 24.0 |
| polar_lat60 | 24.0 | 24.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.3 |
| sat_p0.005 | — | 0.3 |
| void_b2 | 0.3 | 0.3 |
| void_b4 | 0.3 | 0.3 |
| void_b8 | 0.3 | 0.3 |
| cut | 0.3 | 0.3 |
| polar_lat75 | 0.3 | 0.3 |
| polar_lat60 | 0.3 | 0.3 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | — |
| sat_p0.005 | — | loop 100% |
| void_b2 | — | loop 100% |
| void_b4 | — | loop 100% |
| void_b8 | — | loop 100% |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 0.0 |
| sat_p0.005 | — | 1.6 |
| void_b2 | 0.0 | 0.8 |
| void_b4 | 0.0 | 4.2 |
| void_b8 | 0.0 | 12.5 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 1847.1 |
| sat_p0.005 | — | 748.4 |
| void_b2 | 239.6 | 253.2 |
| void_b4 | 579.0 | 578.4 |
| void_b8 | 1375.3 | 1273.8 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_event |
|---|---|---|
| isl_p0.01 | — | 4.86 |
| sat_p0.005 | — | 1.97 |
| void_b2 | 0.63 | 0.67 |
| void_b4 | 1.52 | 1.52 |
| void_b8 | 3.62 | 3.35 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |
