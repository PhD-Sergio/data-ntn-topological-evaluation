# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.4 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 51.6 | 96.5 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | — | — |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.2569 | 1.1767 |
| isl_p0.01 | 1.2591 | 1.1783 |
| isl_p0.02 | 1.2654 | 1.1803 |
| isl_p0.05 | 1.2762 | 1.1879 |
| isl_p0.10 | 1.2955 | 1.1997 |
| isl_p0.20 | 1.3616 | 1.2514 |
| sat_p0.005 | 1.2587 | 1.1773 |
| sat_p0.01 | 1.2592 | 1.1777 |
| sat_p0.02 | 1.2614 | 1.1784 |
| sat_p0.05 | 1.2666 | 1.1784 |
| void_b2 | 1.2566 | 1.1768 |
| void_b4 | 1.2610 | 1.1821 |
| void_b8 | 1.3249 | 1.1918 |
| cut | 1.2132 | 1.2284 |
| polar_lat75 | 1.2524 | 1.1801 |
| polar_lat60 | 1.2550 | 1.1869 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.257 | 1.177 |
| isl_p0.01 | 1.259 | 1.178 |
| isl_p0.02 | 1.265 | 1.180 |
| isl_p0.05 | 1.276 | 1.188 |
| isl_p0.10 | 1.295 | 1.199 |
| isl_p0.20 | 1.361 | 1.251 |
| sat_p0.005 | 1.259 | 1.177 |
| sat_p0.01 | 1.259 | 1.178 |
| sat_p0.02 | 1.261 | 1.178 |
| sat_p0.05 | 1.266 | 1.178 |
| void_b2 | 1.257 | 1.177 |
| void_b4 | 1.261 | 1.182 |
| void_b8 | 1.325 | 1.192 |
| cut | 1.213 | 1.228 |
| polar_lat75 | 1.252 | 1.179 |
| polar_lat60 | 1.255 | 1.186 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 |
| isl_p0.02 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 |
| isl_p0.10 | 1.000 | 1.000 |
| isl_p0.20 | 1.000 | 1.000 |
| sat_p0.005 | 1.000 | 1.000 |
| sat_p0.01 | 1.000 | 1.000 |
| sat_p0.02 | 1.000 | 1.000 |
| sat_p0.05 | 1.000 | 1.000 |
| void_b2 | 1.000 | 1.000 |
| void_b4 | 1.000 | 1.000 |
| void_b8 | 1.000 | 1.000 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.001 |
| polar_lat60 | 1.000 | 1.001 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 6.0 | 10.7 |
| isl_p0.01 | 6.0 | 10.7 |
| isl_p0.02 | 6.0 | 10.7 |
| isl_p0.05 | 6.0 | 10.7 |
| isl_p0.10 | 6.0 | 10.7 |
| isl_p0.20 | 6.0 | 10.7 |
| sat_p0.005 | 6.0 | 10.7 |
| sat_p0.01 | 6.0 | 10.6 |
| sat_p0.02 | 5.9 | 10.6 |
| sat_p0.05 | 5.9 | 10.5 |
| void_b2 | 6.0 | 10.6 |
| void_b4 | 6.0 | 10.5 |
| void_b8 | 5.8 | 9.9 |
| cut | 6.0 | 10.7 |
| polar_lat75 | 6.0 | 10.7 |
| polar_lat60 | 6.0 | 10.7 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 3.8 | 7.4 |
| isl_p0.01 | 3.8 | 7.4 |
| isl_p0.02 | 3.8 | 7.4 |
| isl_p0.05 | 3.8 | 7.4 |
| isl_p0.10 | 3.8 | 7.4 |
| isl_p0.20 | 3.8 | 7.4 |
| sat_p0.005 | 3.8 | 7.4 |
| sat_p0.01 | 3.8 | 7.4 |
| sat_p0.02 | 3.8 | 7.4 |
| sat_p0.05 | 3.8 | 7.6 |
| void_b2 | 3.8 | 7.4 |
| void_b4 | 3.8 | 7.5 |
| void_b8 | 3.8 | 8.6 |
| cut | 3.8 | 7.4 |
| polar_lat75 | 3.8 | 7.4 |
| polar_lat60 | 3.8 | 7.4 |

### Transit egress switches, %

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 4856.0 | 4856.0 |
| isl_p0.02 | 9455.3 | 9455.3 |
| isl_p0.05 | 24064.6 | 24064.6 |
| isl_p0.10 | 45537.5 | 45537.5 |
| isl_p0.20 | 78847.7 | 78847.7 |
| sat_p0.005 | 1818.9 | 1818.9 |
| sat_p0.01 | 5074.0 | 5074.0 |
| sat_p0.02 | 7153.2 | 7153.2 |
| sat_p0.05 | 13334.9 | 13334.9 |
| void_b2 | 2003.9 | 2003.9 |
| void_b4 | 3244.1 | 3244.1 |
| void_b8 | 2480.1 | 2480.1 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 27225.9 | 27225.9 |
| polar_lat60 | 54171.3 | 54171.3 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 57.64 | 57.64 |
| isl_p0.02 | 112.24 | 112.24 |
| isl_p0.05 | 285.67 | 285.67 |
| isl_p0.10 | 540.57 | 540.57 |
| isl_p0.20 | 935.99 | 935.99 |
| sat_p0.005 | 21.59 | 21.59 |
| sat_p0.01 | 60.23 | 60.23 |
| sat_p0.02 | 84.91 | 84.91 |
| sat_p0.05 | 158.30 | 158.30 |
| void_b2 | 23.79 | 23.79 |
| void_b4 | 38.51 | 38.51 |
| void_b8 | 29.44 | 29.44 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 323.19 | 323.19 |
| polar_lat60 | 643.06 | 643.06 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 99.9 ± 0.2 | 99.9 ± 0.1 |
| isl_p0.10 | 100.0 ± 0.1 | 100.0 ± 0.1 |
| isl_p0.20 | 99.7 ± 0.2 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 71.7 | 77.3 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | — | — |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.1763 | 1.1350 |
| isl_p0.01 | 1.1786 | 1.1375 |
| isl_p0.02 | 1.1803 | 1.1392 |
| isl_p0.05 | 1.1852 | 1.1451 |
| isl_p0.10 | 1.1967 | 1.1574 |
| isl_p0.20 | 1.2282 | 1.1932 |
| sat_p0.005 | 1.1767 | 1.1355 |
| sat_p0.01 | 1.1775 | 1.1362 |
| sat_p0.02 | 1.1791 | 1.1375 |
| sat_p0.05 | 1.1845 | 1.1431 |
| void_b2 | 1.1770 | 1.1356 |
| void_b4 | 1.1780 | 1.1372 |
| void_b8 | 1.1732 | 1.1343 |
| cut | 1.1907 | 1.1439 |
| polar_lat75 | 1.1871 | 1.1464 |
| polar_lat60 | 1.1997 | 1.1605 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.176 | 1.135 |
| isl_p0.01 | 1.178 | 1.137 |
| isl_p0.02 | 1.180 | 1.139 |
| isl_p0.05 | 1.184 | 1.144 |
| isl_p0.10 | 1.195 | 1.156 |
| isl_p0.20 | 1.227 | 1.192 |
| sat_p0.005 | 1.177 | 1.135 |
| sat_p0.01 | 1.177 | 1.136 |
| sat_p0.02 | 1.179 | 1.137 |
| sat_p0.05 | 1.183 | 1.142 |
| void_b2 | 1.177 | 1.135 |
| void_b4 | 1.177 | 1.137 |
| void_b8 | 1.172 | 1.133 |
| cut | 1.191 | 1.144 |
| polar_lat75 | 1.186 | 1.145 |
| polar_lat60 | 1.198 | 1.159 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 |
| isl_p0.02 | 1.000 | 1.000 |
| isl_p0.05 | 1.001 | 1.001 |
| isl_p0.10 | 1.001 | 1.001 |
| isl_p0.20 | 1.001 | 1.001 |
| sat_p0.005 | 1.000 | 1.000 |
| sat_p0.01 | 1.000 | 1.000 |
| sat_p0.02 | 1.000 | 1.000 |
| sat_p0.05 | 1.001 | 1.001 |
| void_b2 | 1.000 | 1.000 |
| void_b4 | 1.001 | 1.001 |
| void_b8 | 1.001 | 1.001 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.001 | 1.001 |
| polar_lat60 | 1.001 | 1.001 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 10.9 | 13.7 |
| isl_p0.01 | 10.9 | 13.7 |
| isl_p0.02 | 10.9 | 13.7 |
| isl_p0.05 | 10.9 | 13.7 |
| isl_p0.10 | 10.9 | 13.7 |
| isl_p0.20 | 10.9 | 13.7 |
| sat_p0.005 | 10.9 | 13.7 |
| sat_p0.01 | 10.9 | 13.7 |
| sat_p0.02 | 10.8 | 13.6 |
| sat_p0.05 | 10.6 | 13.5 |
| void_b2 | 10.9 | 13.7 |
| void_b4 | 10.7 | 13.6 |
| void_b8 | 10.3 | 13.0 |
| cut | 10.9 | 13.7 |
| polar_lat75 | 10.9 | 13.7 |
| polar_lat60 | 10.9 | 13.7 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 |
| void_b8 | 23.4 | 46.6 |
| cut | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.6 | 1.4 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.8 | 5.1 |
| isl_p0.01 | 1.8 | 5.1 |
| isl_p0.02 | 1.8 | 5.1 |
| isl_p0.05 | 1.8 | 5.1 |
| isl_p0.10 | 1.8 | 5.1 |
| isl_p0.20 | 1.8 | 5.1 |
| sat_p0.005 | 1.8 | 5.1 |
| sat_p0.01 | 1.8 | 5.1 |
| sat_p0.02 | 1.8 | 5.1 |
| sat_p0.05 | 1.9 | 5.4 |
| void_b2 | 1.8 | 5.1 |
| void_b4 | 1.9 | 5.3 |
| void_b8 | 2.0 | 5.4 |
| cut | 1.8 | 5.1 |
| polar_lat75 | 1.8 | 5.1 |
| polar_lat60 | 1.8 | 5.1 |

### Transit egress switches, %

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | dead_end 100% | dead_end 100% |
| isl_p0.10 | dead_end 100% | dead_end 100% |
| isl_p0.20 | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 27674.3 | 27674.3 |
| isl_p0.02 | 49003.4 | 49003.4 |
| isl_p0.05 | 106656.3 | 106656.3 |
| isl_p0.10 | 186607.3 | 186607.3 |
| isl_p0.20 | 271160.9 | 271160.9 |
| sat_p0.005 | 8172.5 | 8172.5 |
| sat_p0.01 | 21074.7 | 21074.7 |
| sat_p0.02 | 37334.7 | 37334.7 |
| sat_p0.05 | 87835.3 | 87835.3 |
| void_b2 | 7734.9 | 7734.9 |
| void_b4 | 13479.4 | 13479.4 |
| void_b8 | 21445.0 | 21445.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 108924.8 | 108924.8 |
| polar_lat60 | 171768.8 | 171768.8 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 196.10 | 196.10 |
| isl_p0.02 | 347.25 | 347.25 |
| isl_p0.05 | 755.78 | 755.78 |
| isl_p0.10 | 1322.33 | 1322.33 |
| isl_p0.20 | 1921.49 | 1921.49 |
| sat_p0.005 | 57.91 | 57.91 |
| sat_p0.01 | 149.34 | 149.34 |
| sat_p0.02 | 264.56 | 264.56 |
| sat_p0.05 | 622.42 | 622.42 |
| void_b2 | 54.81 | 54.81 |
| void_b4 | 95.52 | 95.52 |
| void_b8 | 151.96 | 151.96 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 771.86 | 771.86 |
| polar_lat60 | 1217.18 | 1217.18 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.1 |
| isl_p0.20 | 99.8 ± 0.2 | 99.9 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 64.6 | 80.0 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | — | — |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.2079 | 1.1729 |
| isl_p0.01 | 1.2095 | 1.1737 |
| isl_p0.02 | 1.2112 | 1.1749 |
| isl_p0.05 | 1.2169 | 1.1786 |
| isl_p0.10 | 1.2252 | 1.1861 |
| isl_p0.20 | 1.2528 | 1.2114 |
| sat_p0.005 | 1.2085 | 1.1735 |
| sat_p0.01 | 1.2093 | 1.1732 |
| sat_p0.02 | 1.2104 | 1.1738 |
| sat_p0.05 | 1.2138 | 1.1773 |
| void_b2 | 1.2081 | 1.1730 |
| void_b4 | 1.2074 | 1.1729 |
| void_b8 | 1.2216 | 1.1763 |
| cut | 1.1781 | 1.2075 |
| polar_lat75 | 1.2079 | 1.1729 |
| polar_lat60 | 1.2079 | 1.1729 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.208 | 1.173 |
| isl_p0.01 | 1.209 | 1.174 |
| isl_p0.02 | 1.211 | 1.175 |
| isl_p0.05 | 1.216 | 1.178 |
| isl_p0.10 | 1.224 | 1.185 |
| isl_p0.20 | 1.252 | 1.211 |
| sat_p0.005 | 1.208 | 1.173 |
| sat_p0.01 | 1.209 | 1.173 |
| sat_p0.02 | 1.210 | 1.174 |
| sat_p0.05 | 1.213 | 1.177 |
| void_b2 | 1.208 | 1.173 |
| void_b4 | 1.207 | 1.173 |
| void_b8 | 1.221 | 1.176 |
| cut | 1.178 | 1.208 |
| polar_lat75 | 1.208 | 1.173 |
| polar_lat60 | 1.208 | 1.173 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 |
| isl_p0.02 | 1.000 | 1.000 |
| isl_p0.05 | 1.001 | 1.000 |
| isl_p0.10 | 1.001 | 1.001 |
| isl_p0.20 | 1.001 | 1.001 |
| sat_p0.005 | 1.000 | 1.000 |
| sat_p0.01 | 1.000 | 1.000 |
| sat_p0.02 | 1.000 | 1.000 |
| sat_p0.05 | 1.001 | 1.000 |
| void_b2 | 1.000 | 1.000 |
| void_b4 | 1.000 | 1.000 |
| void_b8 | 1.000 | 1.000 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 10.5 | 15.5 |
| isl_p0.01 | 10.5 | 15.5 |
| isl_p0.02 | 10.5 | 15.5 |
| isl_p0.05 | 10.5 | 15.5 |
| isl_p0.10 | 10.5 | 15.5 |
| isl_p0.20 | 10.5 | 15.5 |
| sat_p0.005 | 10.5 | 15.5 |
| sat_p0.01 | 10.4 | 15.4 |
| sat_p0.02 | 10.5 | 15.5 |
| sat_p0.05 | 10.4 | 15.3 |
| void_b2 | 10.5 | 15.5 |
| void_b4 | 10.5 | 15.5 |
| void_b8 | 10.3 | 15.1 |
| cut | 10.5 | 15.5 |
| polar_lat75 | 10.5 | 15.5 |
| polar_lat60 | 10.5 | 15.5 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.2 | 1.0 |
| isl_p0.01 | 0.2 | 1.0 |
| isl_p0.02 | 0.2 | 1.0 |
| isl_p0.05 | 0.2 | 1.0 |
| isl_p0.10 | 0.2 | 1.0 |
| isl_p0.20 | 0.2 | 1.0 |
| sat_p0.005 | 0.2 | 1.0 |
| sat_p0.01 | 0.2 | 1.1 |
| sat_p0.02 | 0.2 | 1.1 |
| sat_p0.05 | 0.3 | 1.1 |
| void_b2 | 0.2 | 1.0 |
| void_b4 | 0.3 | 1.2 |
| void_b8 | 0.5 | 1.5 |
| cut | 0.2 | 1.0 |
| polar_lat75 | 0.2 | 1.0 |
| polar_lat60 | 0.2 | 1.0 |

### Transit egress switches, %

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | dead_end 100% | dead_end 100% |
| isl_p0.20 | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 84544.8 | 84544.8 |
| isl_p0.02 | 171581.6 | 171581.6 |
| isl_p0.05 | 398295.9 | 398295.9 |
| isl_p0.10 | 689695.7 | 689695.7 |
| isl_p0.20 | 1049659.7 | 1049659.7 |
| sat_p0.005 | 40019.9 | 40019.9 |
| sat_p0.01 | 85074.5 | 85074.5 |
| sat_p0.02 | 146880.0 | 146880.0 |
| sat_p0.05 | 318110.5 | 318110.5 |
| void_b2 | 12492.4 | 12492.4 |
| void_b4 | 20607.0 | 20607.0 |
| void_b8 | 23450.7 | 23450.7 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 304.73 | 304.73 |
| isl_p0.02 | 618.45 | 618.45 |
| isl_p0.05 | 1435.61 | 1435.61 |
| isl_p0.10 | 2485.93 | 2485.93 |
| isl_p0.20 | 3783.38 | 3783.38 |
| sat_p0.005 | 144.25 | 144.25 |
| sat_p0.01 | 306.64 | 306.64 |
| sat_p0.02 | 529.41 | 529.41 |
| sat_p0.05 | 1146.59 | 1146.59 |
| void_b2 | 45.03 | 45.03 |
| void_b4 | 74.28 | 74.28 |
| void_b8 | 84.53 | 84.53 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.1 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 54.6 | 86.1 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | — | — |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | — | — |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.4460 | 1.3199 |
| isl_p0.01 | 1.4502 | 1.3213 |
| isl_p0.02 | 1.4556 | 1.3236 |
| isl_p0.05 | 1.4713 | 1.3292 |
| isl_p0.10 | 1.5009 | 1.3436 |
| isl_p0.20 | 1.5908 | 1.3978 |
| sat_p0.005 | 1.4475 | 1.3209 |
| sat_p0.01 | 1.4502 | 1.3208 |
| sat_p0.02 | 1.4537 | 1.3225 |
| sat_p0.05 | 1.4653 | 1.3258 |
| void_b2 | 1.4469 | 1.3200 |
| void_b4 | 1.4495 | 1.3208 |
| void_b8 | 1.4567 | 1.3205 |
| cut | 1.3726 | 1.3926 |
| polar_lat75 | 1.4460 | 1.3199 |
| polar_lat60 | 1.4460 | 1.3199 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.446 | 1.320 |
| isl_p0.01 | 1.450 | 1.321 |
| isl_p0.02 | 1.455 | 1.323 |
| isl_p0.05 | 1.471 | 1.329 |
| isl_p0.10 | 1.501 | 1.343 |
| isl_p0.20 | 1.591 | 1.398 |
| sat_p0.005 | 1.447 | 1.321 |
| sat_p0.01 | 1.450 | 1.321 |
| sat_p0.02 | 1.454 | 1.322 |
| sat_p0.05 | 1.465 | 1.325 |
| void_b2 | 1.447 | 1.320 |
| void_b4 | 1.449 | 1.321 |
| void_b8 | 1.457 | 1.320 |
| cut | 1.373 | 1.393 |
| polar_lat75 | 1.446 | 1.320 |
| polar_lat60 | 1.446 | 1.320 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 |
| isl_p0.02 | 1.000 | 1.000 |
| isl_p0.05 | 1.000 | 1.000 |
| isl_p0.10 | 1.000 | 1.000 |
| isl_p0.20 | 1.000 | 1.000 |
| sat_p0.005 | 1.000 | 1.000 |
| sat_p0.01 | 1.000 | 1.000 |
| sat_p0.02 | 1.000 | 1.000 |
| sat_p0.05 | 1.000 | 1.000 |
| void_b2 | 1.000 | 1.000 |
| void_b4 | 1.000 | 1.000 |
| void_b8 | 1.000 | 1.000 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 15.4 | 19.4 |
| isl_p0.01 | 15.4 | 19.4 |
| isl_p0.02 | 15.4 | 19.4 |
| isl_p0.05 | 15.4 | 19.4 |
| isl_p0.10 | 15.4 | 19.4 |
| isl_p0.20 | 15.4 | 19.4 |
| sat_p0.005 | 15.3 | 19.4 |
| sat_p0.01 | 15.2 | 19.4 |
| sat_p0.02 | 15.2 | 19.4 |
| sat_p0.05 | 14.9 | 19.2 |
| void_b2 | 15.4 | 19.4 |
| void_b4 | 15.3 | 19.4 |
| void_b8 | 15.2 | 19.3 |
| cut | 15.4 | 19.4 |
| polar_lat75 | 15.4 | 19.4 |
| polar_lat60 | 15.4 | 19.4 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.3 | 0.6 |
| isl_p0.01 | 0.3 | 0.6 |
| isl_p0.02 | 0.3 | 0.6 |
| isl_p0.05 | 0.3 | 0.6 |
| isl_p0.10 | 0.3 | 0.6 |
| isl_p0.20 | 0.3 | 0.6 |
| sat_p0.005 | 0.3 | 0.6 |
| sat_p0.01 | 0.3 | 0.6 |
| sat_p0.02 | 0.3 | 0.6 |
| sat_p0.05 | 0.3 | 0.6 |
| void_b2 | 0.3 | 0.6 |
| void_b4 | 0.3 | 0.6 |
| void_b8 | 0.3 | 0.7 |
| cut | 0.3 | 0.6 |
| polar_lat75 | 0.3 | 0.6 |
| polar_lat60 | 0.3 | 0.6 |

### Transit egress switches, %

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | — | — |
| isl_p0.01 | — | — |
| isl_p0.02 | — | — |
| isl_p0.05 | — | — |
| isl_p0.10 | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — |
| sat_p0.01 | — | — |
| sat_p0.02 | — | — |
| sat_p0.05 | — | — |
| void_b2 | — | — |
| void_b4 | — | — |
| void_b8 | — | — |
| cut | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — |
| polar_lat60 | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 197200.2 | 197200.2 |
| isl_p0.02 | 381964.6 | 381964.6 |
| isl_p0.05 | 856322.2 | 856322.2 |
| isl_p0.10 | 1490190.8 | 1490190.8 |
| isl_p0.20 | 2127127.9 | 2127127.9 |
| sat_p0.005 | 88257.8 | 88257.8 |
| sat_p0.01 | 177572.3 | 177572.3 |
| sat_p0.02 | 332763.4 | 332763.4 |
| sat_p0.05 | 693003.7 | 693003.7 |
| void_b2 | 24596.5 | 24596.5 |
| void_b4 | 48492.3 | 48492.3 |
| void_b8 | 91945.1 | 91945.1 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc_1p | topological_scheme_req_1p |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 518.73 | 518.73 |
| isl_p0.02 | 1004.75 | 1004.75 |
| isl_p0.05 | 2252.53 | 2252.53 |
| isl_p0.10 | 3919.90 | 3919.90 |
| isl_p0.20 | 5595.35 | 5595.35 |
| sat_p0.005 | 232.16 | 232.16 |
| sat_p0.01 | 467.10 | 467.10 |
| sat_p0.02 | 875.32 | 875.32 |
| sat_p0.05 | 1822.93 | 1822.93 |
| void_b2 | 64.70 | 64.70 |
| void_b4 | 127.56 | 127.56 |
| void_b8 | 241.86 | 241.86 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |
