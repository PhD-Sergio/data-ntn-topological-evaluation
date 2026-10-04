# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.20 | 99.3 | 99.3 | 99.5 | 99.5 |
| sat_p0.005 | 100.0 | 100.0 | 100.0 | 100.0 |
| sat_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| void_b4 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.2569 | 1.2569 | 1.1767 | 1.1767 |
| isl_p0.01 | 1.2663 | 1.2593 | 1.1903 | 1.1799 |
| isl_p0.05 | 1.3217 | 1.2841 | 1.2168 | 1.1912 |
| isl_p0.20 | 1.4447 | 1.3488 | 1.3214 | 1.2454 |
| sat_p0.005 | 1.2615 | 1.2581 | 1.1791 | 1.1769 |
| sat_p0.05 | 1.3026 | 1.2753 | 1.1978 | 1.1802 |
| void_b4 | 1.2601 | 1.2577 | 1.1755 | 1.1749 |
| polar_lat60 | 1.2558 | 1.2550 | 1.1928 | 1.1869 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.257 | 1.257 | 1.177 | 1.177 |
| isl_p0.01 | 1.259 | 1.259 | 1.180 | 1.180 |
| isl_p0.05 | 1.283 | 1.283 | 1.191 | 1.191 |
| isl_p0.20 | 1.348 | 1.348 | 1.245 | 1.245 |
| sat_p0.005 | 1.258 | 1.258 | 1.177 | 1.177 |
| sat_p0.05 | 1.275 | 1.275 | 1.180 | 1.180 |
| void_b4 | 1.258 | 1.258 | 1.175 | 1.175 |
| polar_lat60 | 1.255 | 1.255 | 1.186 | 1.186 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.005 | 1.000 | 1.008 | 1.000 |
| isl_p0.05 | 1.028 | 1.000 | 1.020 | 1.000 |
| isl_p0.20 | 1.071 | 1.000 | 1.062 | 1.000 |
| sat_p0.005 | 1.003 | 1.000 | 1.002 | 1.000 |
| sat_p0.05 | 1.021 | 1.000 | 1.015 | 1.000 |
| void_b4 | 1.002 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.001 | 1.000 | 1.006 | 1.001 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 6.0 | 6.0 | 10.7 | 10.7 |
| isl_p0.01 | 6.0 | 6.0 | 10.7 | 10.7 |
| isl_p0.05 | 6.0 | 6.0 | 10.7 | 10.7 |
| isl_p0.20 | 6.0 | 6.0 | 10.7 | 10.7 |
| sat_p0.005 | 6.0 | 6.0 | 10.7 | 10.7 |
| sat_p0.05 | 5.8 | 5.8 | 10.4 | 10.4 |
| void_b4 | 6.0 | 6.0 | 10.6 | 10.6 |
| polar_lat60 | 6.0 | 6.0 | 10.7 | 10.7 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.01 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.20 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.005 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| void_b4 | 24.0 | 24.0 | 48.0 | 48.0 |
| polar_lat60 | 24.0 | 24.0 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 3.8 | 3.8 | 7.4 | 7.4 |
| isl_p0.01 | 3.8 | 3.8 | 7.4 | 7.4 |
| isl_p0.05 | 3.8 | 3.8 | 7.4 | 7.4 |
| isl_p0.20 | 3.8 | 3.8 | 7.4 | 7.4 |
| sat_p0.005 | 3.7 | 3.7 | 7.4 | 7.4 |
| sat_p0.05 | 3.9 | 3.9 | 7.7 | 7.7 |
| void_b4 | 3.8 | 3.8 | 7.6 | 7.6 |
| polar_lat60 | 3.8 | 3.8 | 7.4 | 7.4 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 227.5 | 6367.0 | 227.5 | 6367.0 |
| isl_p0.05 | 831.5 | 19838.5 | 831.5 | 19838.5 |
| isl_p0.20 | 10506.5 | 79586.8 | 10506.5 | 79586.8 |
| sat_p0.005 | 71.2 | 1696.5 | 71.2 | 1696.5 |
| sat_p0.05 | 916.9 | 16558.9 | 916.9 | 16558.9 |
| void_b4 | 161.5 | 3051.4 | 161.5 | 3051.4 |
| polar_lat60 | 9479.9 | 54171.3 | 9479.9 | 54171.3 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.00 | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | 2.70 | 75.58 | 2.70 | 75.58 |
| isl_p0.05 | 9.87 | 235.50 | 9.87 | 235.50 |
| isl_p0.20 | 124.72 | 944.76 | 124.72 | 944.76 |
| sat_p0.005 | 0.84 | 20.14 | 0.84 | 20.14 |
| sat_p0.05 | 10.88 | 196.57 | 10.88 | 196.57 |
| void_b4 | 1.92 | 36.22 | 1.92 | 36.22 |
| polar_lat60 | 112.53 | 643.06 | 112.53 | 643.06 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.20 | 99.7 | 99.7 | 99.6 | 99.6 |
| sat_p0.005 | 100.0 | 100.0 | 100.0 | 100.0 |
| sat_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| void_b4 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.1763 | 1.1763 | 1.1350 | 1.1350 |
| isl_p0.01 | 1.1845 | 1.1783 | 1.1415 | 1.1369 |
| isl_p0.05 | 1.2119 | 1.1855 | 1.1719 | 1.1458 |
| isl_p0.20 | 1.3348 | 1.2353 | 1.2905 | 1.1955 |
| sat_p0.005 | 1.1769 | 1.1764 | 1.1359 | 1.1353 |
| sat_p0.05 | 1.2127 | 1.1860 | 1.1695 | 1.1448 |
| void_b4 | 1.1819 | 1.1765 | 1.1427 | 1.1379 |
| polar_lat60 | 1.2006 | 1.1997 | 1.1613 | 1.1605 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.176 | 1.176 | 1.135 | 1.135 |
| isl_p0.01 | 1.178 | 1.178 | 1.137 | 1.137 |
| isl_p0.05 | 1.184 | 1.184 | 1.145 | 1.145 |
| isl_p0.20 | 1.234 | 1.234 | 1.194 | 1.194 |
| sat_p0.005 | 1.176 | 1.176 | 1.135 | 1.135 |
| sat_p0.05 | 1.185 | 1.185 | 1.144 | 1.144 |
| void_b4 | 1.176 | 1.176 | 1.138 | 1.138 |
| polar_lat60 | 1.198 | 1.198 | 1.159 | 1.159 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.005 | 1.000 | 1.004 | 1.000 |
| isl_p0.05 | 1.023 | 1.001 | 1.023 | 1.001 |
| isl_p0.20 | 1.083 | 1.001 | 1.080 | 1.001 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.000 |
| sat_p0.05 | 1.024 | 1.001 | 1.023 | 1.001 |
| void_b4 | 1.004 | 1.000 | 1.003 | 1.000 |
| polar_lat60 | 1.002 | 1.001 | 1.002 | 1.001 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 10.9 | 10.9 | 13.7 | 13.7 |
| isl_p0.01 | 10.9 | 10.9 | 13.7 | 13.7 |
| isl_p0.05 | 10.9 | 10.9 | 13.7 | 13.7 |
| isl_p0.20 | 10.9 | 10.9 | 13.7 | 13.7 |
| sat_p0.005 | 10.9 | 10.9 | 13.8 | 13.8 |
| sat_p0.05 | 10.5 | 10.5 | 13.5 | 13.5 |
| void_b4 | 10.7 | 10.7 | 13.6 | 13.6 |
| polar_lat60 | 10.9 | 10.9 | 13.7 | 13.7 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.01 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.20 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.005 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| void_b4 | 24.0 | 24.0 | 48.0 | 48.0 |
| polar_lat60 | 24.0 | 24.0 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.8 | 1.8 | 5.1 | 5.1 |
| isl_p0.01 | 1.8 | 1.8 | 5.1 | 5.1 |
| isl_p0.05 | 1.8 | 1.8 | 5.1 | 5.1 |
| isl_p0.20 | 1.8 | 1.8 | 5.1 | 5.1 |
| sat_p0.005 | 1.8 | 1.8 | 5.1 | 5.1 |
| sat_p0.05 | 1.9 | 1.9 | 5.3 | 5.3 |
| void_b4 | 1.9 | 1.9 | 5.2 | 5.2 |
| polar_lat60 | 1.8 | 1.8 | 5.1 | 5.1 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 410.3 | 23114.0 | 410.3 | 23114.0 |
| isl_p0.05 | 2972.9 | 108858.8 | 2972.9 | 108858.8 |
| isl_p0.20 | 28102.6 | 273418.8 | 28102.6 | 273418.8 |
| sat_p0.005 | 148.3 | 7576.0 | 148.3 | 7576.0 |
| sat_p0.05 | 3140.7 | 89175.2 | 3140.7 | 89175.2 |
| void_b4 | 301.9 | 10970.6 | 301.9 | 10970.6 |
| polar_lat60 | 21637.4 | 171768.8 | 21637.4 | 171768.8 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.00 | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | 2.91 | 163.79 | 2.91 | 163.79 |
| isl_p0.05 | 21.07 | 771.39 | 21.07 | 771.39 |
| isl_p0.20 | 199.14 | 1937.49 | 199.14 | 1937.49 |
| sat_p0.005 | 1.05 | 53.68 | 1.05 | 53.68 |
| sat_p0.05 | 22.26 | 631.91 | 22.26 | 631.91 |
| void_b4 | 2.14 | 77.74 | 2.14 | 77.74 |
| polar_lat60 | 153.33 | 1217.18 | 153.33 | 1217.18 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.20 | 100.0 | 100.0 | 100.0 | 100.0 |
| sat_p0.005 | 100.0 | 100.0 | 100.0 | 100.0 |
| sat_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| void_b4 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.2079 | 1.2079 | 1.1729 | 1.1729 |
| isl_p0.01 | 1.2162 | 1.2097 | 1.1787 | 1.1738 |
| isl_p0.05 | 1.2407 | 1.2149 | 1.2022 | 1.1778 |
| isl_p0.20 | 1.3515 | 1.2527 | 1.2980 | 1.2113 |
| sat_p0.005 | 1.2115 | 1.2087 | 1.1751 | 1.1733 |
| sat_p0.05 | 1.2389 | 1.2140 | 1.1942 | 1.1775 |
| void_b4 | 1.2097 | 1.2085 | 1.1757 | 1.1743 |
| polar_lat60 | 1.2079 | 1.2079 | 1.1729 | 1.1729 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.208 | 1.208 | 1.173 | 1.173 |
| isl_p0.01 | 1.209 | 1.209 | 1.174 | 1.174 |
| isl_p0.05 | 1.214 | 1.214 | 1.177 | 1.177 |
| isl_p0.20 | 1.252 | 1.252 | 1.211 | 1.211 |
| sat_p0.005 | 1.209 | 1.209 | 1.173 | 1.173 |
| sat_p0.05 | 1.213 | 1.213 | 1.177 | 1.177 |
| void_b4 | 1.208 | 1.208 | 1.174 | 1.174 |
| polar_lat60 | 1.208 | 1.208 | 1.173 | 1.173 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.005 | 1.000 | 1.004 | 1.000 |
| isl_p0.05 | 1.022 | 1.001 | 1.021 | 1.000 |
| isl_p0.20 | 1.080 | 1.001 | 1.073 | 1.001 |
| sat_p0.005 | 1.002 | 1.000 | 1.002 | 1.000 |
| sat_p0.05 | 1.021 | 1.001 | 1.015 | 1.000 |
| void_b4 | 1.001 | 1.000 | 1.001 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 10.5 | 10.5 | 15.5 | 15.5 |
| isl_p0.01 | 10.5 | 10.5 | 15.5 | 15.5 |
| isl_p0.05 | 10.5 | 10.5 | 15.5 | 15.5 |
| isl_p0.20 | 10.5 | 10.5 | 15.5 | 15.5 |
| sat_p0.005 | 10.5 | 10.5 | 15.4 | 15.4 |
| sat_p0.05 | 10.3 | 10.3 | 15.4 | 15.4 |
| void_b4 | 10.5 | 10.5 | 15.5 | 15.5 |
| polar_lat60 | 10.5 | 10.5 | 15.5 | 15.5 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.01 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.20 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.005 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| void_b4 | 24.0 | 24.0 | 48.0 | 48.0 |
| polar_lat60 | 24.0 | 24.0 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.2 | 0.2 | 1.0 | 1.0 |
| isl_p0.01 | 0.2 | 0.2 | 1.0 | 1.0 |
| isl_p0.05 | 0.2 | 0.2 | 1.0 | 1.0 |
| isl_p0.20 | 0.2 | 0.2 | 1.0 | 1.0 |
| sat_p0.005 | 0.2 | 0.2 | 1.0 | 1.0 |
| sat_p0.05 | 0.2 | 0.2 | 1.1 | 1.1 |
| void_b4 | 0.2 | 0.2 | 1.0 | 1.0 |
| polar_lat60 | 0.2 | 0.2 | 1.0 | 1.0 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 1002.6 | 81509.2 | 1002.6 | 81509.2 |
| isl_p0.05 | 8464.4 | 391963.3 | 8464.4 | 391963.3 |
| isl_p0.20 | 94946.4 | 1050640.6 | 94946.4 | 1050640.6 |
| sat_p0.005 | 531.0 | 45460.3 | 531.0 | 45460.3 |
| sat_p0.05 | 8881.8 | 335196.4 | 8881.8 | 335196.4 |
| void_b4 | 378.4 | 19865.5 | 378.4 | 19865.5 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.00 | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | 3.61 | 293.79 | 3.61 | 293.79 |
| isl_p0.05 | 30.51 | 1412.79 | 30.51 | 1412.79 |
| isl_p0.20 | 342.22 | 3786.91 | 342.22 | 3786.91 |
| sat_p0.005 | 1.91 | 163.86 | 1.91 | 163.86 |
| sat_p0.05 | 32.01 | 1208.18 | 32.01 | 1208.18 |
| void_b4 | 1.36 | 71.60 | 1.36 | 71.60 |
| polar_lat60 | 0.00 | 0.00 | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.20 | 100.0 | 100.0 | 99.9 | 99.9 |
| sat_p0.005 | 100.0 | 100.0 | 100.0 | 100.0 |
| sat_p0.05 | 100.0 | 100.0 | 100.0 | 100.0 |
| void_b4 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.4460 | 1.4460 | 1.3199 | 1.3199 |
| isl_p0.01 | 1.4662 | 1.4513 | 1.3311 | 1.3218 |
| isl_p0.05 | 1.5241 | 1.4705 | 1.3663 | 1.3290 |
| isl_p0.20 | 1.7701 | 1.5809 | 1.5352 | 1.3924 |
| sat_p0.005 | 1.4542 | 1.4477 | 1.3249 | 1.3206 |
| sat_p0.05 | 1.5078 | 1.4639 | 1.3568 | 1.3246 |
| void_b4 | 1.4550 | 1.4480 | 1.3209 | 1.3188 |
| polar_lat60 | 1.4460 | 1.4460 | 1.3199 | 1.3199 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.446 | 1.446 | 1.320 | 1.320 |
| isl_p0.01 | 1.451 | 1.451 | 1.322 | 1.322 |
| isl_p0.05 | 1.470 | 1.470 | 1.329 | 1.329 |
| isl_p0.20 | 1.581 | 1.581 | 1.392 | 1.392 |
| sat_p0.005 | 1.448 | 1.448 | 1.321 | 1.321 |
| sat_p0.05 | 1.464 | 1.464 | 1.324 | 1.324 |
| void_b4 | 1.448 | 1.448 | 1.319 | 1.319 |
| polar_lat60 | 1.446 | 1.446 | 1.320 | 1.320 |

### Distance stretch, forwarding factor

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.010 | 1.000 | 1.007 | 1.000 |
| isl_p0.05 | 1.037 | 1.000 | 1.028 | 1.000 |
| isl_p0.20 | 1.122 | 1.000 | 1.100 | 1.000 |
| sat_p0.005 | 1.005 | 1.000 | 1.003 | 1.000 |
| sat_p0.05 | 1.031 | 1.000 | 1.024 | 1.000 |
| void_b4 | 1.005 | 1.000 | 1.001 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 15.4 | 15.4 | 19.4 | 19.4 |
| isl_p0.01 | 15.4 | 15.4 | 19.4 | 19.4 |
| isl_p0.05 | 15.4 | 15.4 | 19.4 | 19.4 |
| isl_p0.20 | 15.4 | 15.4 | 19.4 | 19.4 |
| sat_p0.005 | 15.3 | 15.3 | 19.4 | 19.4 |
| sat_p0.05 | 15.0 | 15.0 | 19.1 | 19.1 |
| void_b4 | 15.2 | 15.2 | 19.3 | 19.3 |
| polar_lat60 | 15.4 | 15.4 | 19.4 | 19.4 |

### Assigned ground-station links per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.01 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| isl_p0.20 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.005 | 24.0 | 24.0 | 48.0 | 48.0 |
| sat_p0.05 | 24.0 | 24.0 | 48.0 | 48.0 |
| void_b4 | 24.0 | 24.0 | 48.0 | 48.0 |
| polar_lat60 | 24.0 | 24.0 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.3 | 0.3 | 0.6 | 0.6 |
| isl_p0.01 | 0.3 | 0.3 | 0.6 | 0.6 |
| isl_p0.05 | 0.3 | 0.3 | 0.6 | 0.6 |
| isl_p0.20 | 0.3 | 0.3 | 0.6 | 0.6 |
| sat_p0.005 | 0.3 | 0.3 | 0.6 | 0.6 |
| sat_p0.05 | 0.3 | 0.3 | 0.7 | 0.7 |
| void_b4 | 0.3 | 0.3 | 0.6 | 0.6 |
| polar_lat60 | 0.3 | 0.3 | 0.6 | 0.6 |

### Transit egress switches, %

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.20 | — | — | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b4 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 1763.5 | 192002.2 | 1763.5 | 192002.2 |
| isl_p0.05 | 16086.8 | 836000.7 | 16086.8 | 836000.7 |
| isl_p0.20 | 191451.6 | 2143770.6 | 191451.4 | 2143770.6 |
| sat_p0.005 | 659.2 | 81494.9 | 659.2 | 81494.9 |
| sat_p0.05 | 12503.8 | 685842.5 | 12503.8 | 685842.5 |
| void_b4 | 558.4 | 44356.3 | 558.4 | 44356.3 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_asc_1p | topological_scheme_req | topological_scheme_req_1p |
|---|---|---|---|---|
| none | 0.00 | 0.00 | 0.00 | 0.00 |
| isl_p0.01 | 4.64 | 505.06 | 4.64 | 505.06 |
| isl_p0.05 | 42.32 | 2199.08 | 42.32 | 2199.08 |
| isl_p0.20 | 503.61 | 5639.13 | 503.61 | 5639.13 |
| sat_p0.005 | 1.73 | 214.37 | 1.73 | 214.37 |
| sat_p0.05 | 32.89 | 1804.09 | 32.89 | 1804.09 |
| void_b4 | 1.47 | 116.68 | 1.47 | 116.68 |
| polar_lat60 | 0.00 | 0.00 | 0.00 | 0.00 |
