# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.2569 | 1.1767 |
| isl_p0.01 | 1.2651 | 1.1850 |
| isl_p0.02 | 1.2809 | 1.1913 |
| isl_p0.05 | 1.3112 | 1.2159 |
| isl_p0.10 | 1.3578 | 1.2461 |
| isl_p0.20 | 1.4613 | 1.3247 |
| sat_p0.005 | 1.2624 | 1.1791 |
| sat_p0.01 | 1.2658 | 1.1824 |
| sat_p0.02 | 1.2727 | 1.1851 |
| sat_p0.05 | 1.2858 | 1.1921 |
| void_b2 | 1.2590 | 1.1779 |
| void_b4 | 1.2652 | 1.1836 |
| void_b8 | 1.3330 | 1.1926 |
| cut | 1.2132 | 1.2284 |
| polar_lat75 | 1.2524 | 1.1801 |
| polar_lat60 | 1.2558 | 1.1928 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.005 | 1.005 |
| isl_p0.02 | 1.012 | 1.009 |
| isl_p0.05 | 1.027 | 1.023 |
| isl_p0.10 | 1.048 | 1.038 |
| isl_p0.20 | 1.073 | 1.059 |
| sat_p0.005 | 1.003 | 1.001 |
| sat_p0.01 | 1.005 | 1.004 |
| sat_p0.02 | 1.009 | 1.006 |
| sat_p0.05 | 1.015 | 1.012 |
| void_b2 | 1.002 | 1.001 |
| void_b4 | 1.003 | 1.001 |
| void_b8 | 1.004 | 1.000 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.001 |
| polar_lat60 | 1.001 | 1.006 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 167.4 | 167.4 |
| isl_p0.02 | 341.2 | 341.2 |
| isl_p0.05 | 1138.9 | 1138.9 |
| isl_p0.10 | 3195.2 | 3195.2 |
| isl_p0.20 | 10060.9 | 10060.9 |
| sat_p0.005 | 68.2 | 68.2 |
| sat_p0.01 | 206.4 | 206.4 |
| sat_p0.02 | 375.5 | 375.5 |
| sat_p0.05 | 644.0 | 644.0 |
| void_b2 | 84.3 | 84.3 |
| void_b4 | 171.5 | 171.5 |
| void_b8 | 215.9 | 215.9 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 4297.3 | 4297.3 |
| polar_lat60 | 9479.9 | 9479.9 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 1.99 | 1.99 |
| isl_p0.02 | 4.05 | 4.05 |
| isl_p0.05 | 13.52 | 13.52 |
| isl_p0.10 | 37.93 | 37.93 |
| isl_p0.20 | 119.43 | 119.43 |
| sat_p0.005 | 0.81 | 0.81 |
| sat_p0.01 | 2.45 | 2.45 |
| sat_p0.02 | 4.46 | 4.46 |
| sat_p0.05 | 7.65 | 7.65 |
| void_b2 | 1.00 | 1.00 |
| void_b4 | 2.04 | 2.04 |
| void_b8 | 2.56 | 2.56 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 51.01 | 51.01 |
| polar_lat60 | 112.53 | 112.53 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.1763 | 1.1350 |
| isl_p0.01 | 1.1862 | 1.1443 |
| isl_p0.02 | 1.1939 | 1.1512 |
| isl_p0.05 | 1.2141 | 1.1716 |
| isl_p0.10 | 1.2517 | 1.2102 |
| isl_p0.20 | 1.3227 | 1.2840 |
| sat_p0.005 | 1.1783 | 1.1372 |
| sat_p0.01 | 1.1814 | 1.1397 |
| sat_p0.02 | 1.1879 | 1.1452 |
| sat_p0.05 | 1.2083 | 1.1646 |
| void_b2 | 1.1784 | 1.1369 |
| void_b4 | 1.1830 | 1.1411 |
| void_b8 | 1.1812 | 1.1408 |
| cut | 1.1907 | 1.1439 |
| polar_lat75 | 1.1874 | 1.1468 |
| polar_lat60 | 1.2006 | 1.1613 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.007 | 1.006 |
| isl_p0.02 | 1.012 | 1.011 |
| isl_p0.05 | 1.025 | 1.023 |
| isl_p0.10 | 1.047 | 1.046 |
| isl_p0.20 | 1.078 | 1.076 |
| sat_p0.005 | 1.001 | 1.002 |
| sat_p0.01 | 1.004 | 1.003 |
| sat_p0.02 | 1.008 | 1.007 |
| sat_p0.05 | 1.021 | 1.019 |
| void_b2 | 1.001 | 1.001 |
| void_b4 | 1.005 | 1.004 |
| void_b8 | 1.008 | 1.007 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.001 | 1.001 |
| polar_lat60 | 1.002 | 1.002 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 504.9 | 504.9 |
| isl_p0.02 | 1053.8 | 1053.8 |
| isl_p0.05 | 3133.6 | 3133.6 |
| isl_p0.10 | 9389.9 | 9389.9 |
| isl_p0.20 | 29862.9 | 29862.8 |
| sat_p0.005 | 180.7 | 180.7 |
| sat_p0.01 | 456.6 | 456.6 |
| sat_p0.02 | 782.9 | 782.9 |
| sat_p0.05 | 3216.8 | 3216.8 |
| void_b2 | 151.6 | 151.6 |
| void_b4 | 355.0 | 355.0 |
| void_b8 | 920.9 | 920.9 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 8615.7 | 8615.7 |
| polar_lat60 | 21637.4 | 21637.4 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 3.58 | 3.58 |
| isl_p0.02 | 7.47 | 7.47 |
| isl_p0.05 | 22.21 | 22.21 |
| isl_p0.10 | 66.54 | 66.54 |
| isl_p0.20 | 211.61 | 211.61 |
| sat_p0.005 | 1.28 | 1.28 |
| sat_p0.01 | 3.24 | 3.24 |
| sat_p0.02 | 5.55 | 5.55 |
| sat_p0.05 | 22.79 | 22.79 |
| void_b2 | 1.07 | 1.07 |
| void_b4 | 2.52 | 2.52 |
| void_b8 | 6.53 | 6.53 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 61.05 | 61.05 |
| polar_lat60 | 153.33 | 153.33 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.2079 | 1.1729 |
| isl_p0.01 | 1.2149 | 1.1782 |
| isl_p0.02 | 1.2226 | 1.1845 |
| isl_p0.05 | 1.2456 | 1.2033 |
| isl_p0.10 | 1.2793 | 1.2342 |
| isl_p0.20 | 1.3516 | 1.2991 |
| sat_p0.005 | 1.2108 | 1.1755 |
| sat_p0.01 | 1.2157 | 1.1775 |
| sat_p0.02 | 1.2209 | 1.1818 |
| sat_p0.05 | 1.2357 | 1.1959 |
| void_b2 | 1.2091 | 1.1736 |
| void_b4 | 1.2095 | 1.1746 |
| void_b8 | 1.2255 | 1.1790 |
| cut | 1.1781 | 1.2075 |
| polar_lat75 | 1.2079 | 1.1729 |
| polar_lat60 | 1.2079 | 1.1729 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.005 | 1.004 |
| isl_p0.02 | 1.010 | 1.008 |
| isl_p0.05 | 1.024 | 1.021 |
| isl_p0.10 | 1.045 | 1.041 |
| isl_p0.20 | 1.080 | 1.073 |
| sat_p0.005 | 1.002 | 1.002 |
| sat_p0.01 | 1.005 | 1.004 |
| sat_p0.02 | 1.009 | 1.007 |
| sat_p0.05 | 1.019 | 1.016 |
| void_b2 | 1.001 | 1.001 |
| void_b4 | 1.002 | 1.001 |
| void_b8 | 1.003 | 1.002 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 1110.8 | 1110.8 |
| isl_p0.02 | 2521.8 | 2521.8 |
| isl_p0.05 | 8990.0 | 8990.0 |
| isl_p0.10 | 26810.6 | 26810.6 |
| isl_p0.20 | 95220.4 | 95220.3 |
| sat_p0.005 | 469.4 | 469.4 |
| sat_p0.01 | 1119.8 | 1119.8 |
| sat_p0.02 | 2455.0 | 2455.0 |
| sat_p0.05 | 8066.5 | 8066.5 |
| void_b2 | 169.1 | 169.1 |
| void_b4 | 399.3 | 399.3 |
| void_b8 | 808.0 | 808.0 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 4.00 | 4.00 |
| isl_p0.02 | 9.09 | 9.09 |
| isl_p0.05 | 32.40 | 32.40 |
| isl_p0.10 | 96.64 | 96.64 |
| isl_p0.20 | 343.21 | 343.21 |
| sat_p0.005 | 1.69 | 1.69 |
| sat_p0.01 | 4.04 | 4.04 |
| sat_p0.02 | 8.85 | 8.85 |
| sat_p0.05 | 29.07 | 29.07 |
| void_b2 | 0.61 | 0.61 |
| void_b4 | 1.44 | 1.44 |
| void_b8 | 2.91 | 2.91 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.4460 | 1.3199 |
| isl_p0.01 | 1.4640 | 1.3300 |
| isl_p0.02 | 1.4803 | 1.3402 |
| isl_p0.05 | 1.5290 | 1.3677 |
| isl_p0.10 | 1.6125 | 1.4205 |
| isl_p0.20 | 1.7887 | 1.5446 |
| sat_p0.005 | 1.4532 | 1.3252 |
| sat_p0.01 | 1.4638 | 1.3290 |
| sat_p0.02 | 1.4747 | 1.3356 |
| sat_p0.05 | 1.5165 | 1.3574 |
| void_b2 | 1.4483 | 1.3212 |
| void_b4 | 1.4534 | 1.3234 |
| void_b8 | 1.4663 | 1.3236 |
| cut | 1.3726 | 1.3926 |
| polar_lat75 | 1.4460 | 1.3199 |
| polar_lat60 | 1.4460 | 1.3199 |

### Distance stretch, egress-choice factor

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.010 | 1.006 |
| isl_p0.02 | 1.017 | 1.012 |
| isl_p0.05 | 1.040 | 1.028 |
| isl_p0.10 | 1.076 | 1.055 |
| isl_p0.20 | 1.128 | 1.102 |
| sat_p0.005 | 1.004 | 1.003 |
| sat_p0.01 | 1.009 | 1.006 |
| sat_p0.02 | 1.015 | 1.009 |
| sat_p0.05 | 1.036 | 1.023 |
| void_b2 | 1.001 | 1.001 |
| void_b4 | 1.003 | 1.002 |
| void_b8 | 1.007 | 1.002 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
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

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.0 | 0.0 |
| isl_p0.01 | 1847.1 | 1847.1 |
| isl_p0.02 | 4498.5 | 4498.5 |
| isl_p0.05 | 15886.3 | 15886.3 |
| isl_p0.10 | 49996.4 | 49996.4 |
| isl_p0.20 | 184758.0 | 184757.9 |
| sat_p0.005 | 741.6 | 741.6 |
| sat_p0.01 | 1910.3 | 1910.3 |
| sat_p0.02 | 4190.9 | 4190.9 |
| sat_p0.05 | 13646.0 | 13646.0 |
| void_b2 | 239.6 | 239.6 |
| void_b4 | 579.0 | 579.0 |
| void_b8 | 1375.3 | 1375.3 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | topological_scheme_asc | topological_scheme_req |
|---|---|---|
| none | 0.00 | 0.00 |
| isl_p0.01 | 4.86 | 4.86 |
| isl_p0.02 | 11.83 | 11.83 |
| isl_p0.05 | 41.79 | 41.79 |
| isl_p0.10 | 131.51 | 131.51 |
| isl_p0.20 | 486.00 | 486.00 |
| sat_p0.005 | 1.95 | 1.95 |
| sat_p0.01 | 5.02 | 5.02 |
| sat_p0.02 | 11.02 | 11.02 |
| sat_p0.05 | 35.90 | 35.90 |
| void_b2 | 0.63 | 0.63 |
| void_b4 | 1.52 | 1.52 |
| void_b8 | 3.62 | 3.62 |
| cut | 0.00 | 0.00 |
| polar_lat75 | 0.00 | 0.00 |
| polar_lat60 | 0.00 | 0.00 |
