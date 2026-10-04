# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.2 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 96.5 | 96.5 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.1767 | 1.1767 |
| isl_p0.01 | 1.1777 | 1.1850 |
| isl_p0.02 | 1.1793 | 1.1913 |
| isl_p0.05 | 1.1852 | 1.2159 |
| isl_p0.10 | 1.1928 | 1.2461 |
| isl_p0.20 | 1.2327 | 1.3247 |
| sat_p0.005 | 1.1771 | 1.1791 |
| sat_p0.01 | 1.1771 | 1.1824 |
| sat_p0.02 | 1.1773 | 1.1851 |
| sat_p0.05 | 1.1763 | 1.1921 |
| void_b2 | 1.1765 | 1.1779 |
| void_b4 | 1.1796 | 1.1836 |
| void_b8 | 1.1897 | 1.1926 |
| cut | 1.2284 | 1.2284 |
| polar_lat75 | 1.1783 | 1.1801 |
| polar_lat60 | 1.1846 | 1.1928 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.177 | 1.177 |
| isl_p0.01 | 1.178 | 1.178 |
| isl_p0.02 | 1.179 | 1.180 |
| isl_p0.05 | 1.185 | 1.188 |
| isl_p0.10 | 1.193 | 1.199 |
| isl_p0.20 | 1.233 | 1.251 |
| sat_p0.005 | 1.177 | 1.177 |
| sat_p0.01 | 1.177 | 1.178 |
| sat_p0.02 | 1.177 | 1.178 |
| sat_p0.05 | 1.176 | 1.178 |
| void_b2 | 1.176 | 1.177 |
| void_b4 | 1.180 | 1.182 |
| void_b8 | 1.190 | 1.192 |
| cut | 1.228 | 1.228 |
| polar_lat75 | 1.178 | 1.179 |
| polar_lat60 | 1.185 | 1.186 |

### Distance stretch, forwarding factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.005 |
| isl_p0.02 | 1.000 | 1.009 |
| isl_p0.05 | 1.000 | 1.023 |
| isl_p0.10 | 1.000 | 1.038 |
| isl_p0.20 | 1.000 | 1.059 |
| sat_p0.005 | 1.000 | 1.001 |
| sat_p0.01 | 1.000 | 1.004 |
| sat_p0.02 | 1.000 | 1.006 |
| sat_p0.05 | 1.000 | 1.012 |
| void_b2 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.001 |
| void_b8 | 1.000 | 1.000 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.001 |
| polar_lat60 | 1.000 | 1.006 |

### Ground station renumberings per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 10.7 |
| isl_p0.01 | — | 10.7 |
| isl_p0.02 | — | 10.7 |
| isl_p0.05 | — | 10.7 |
| isl_p0.10 | — | 10.7 |
| isl_p0.20 | — | 10.7 |
| sat_p0.005 | — | 10.7 |
| sat_p0.01 | — | 10.6 |
| sat_p0.02 | — | 10.6 |
| sat_p0.05 | — | 10.5 |
| void_b2 | — | 10.6 |
| void_b4 | — | 10.5 |
| void_b8 | — | 9.9 |
| cut | — | 10.7 |
| polar_lat75 | — | 10.7 |
| polar_lat60 | — | 10.7 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 48.0 | 48.0 |
| isl_p0.01 | 48.0 | 48.0 |
| isl_p0.02 | 48.0 | 48.0 |
| isl_p0.05 | 48.0 | 48.0 |
| isl_p0.10 | 48.0 | 48.0 |
| isl_p0.20 | 48.0 | 48.0 |
| sat_p0.005 | 48.0 | 48.0 |
| sat_p0.01 | 48.0 | 48.0 |
| sat_p0.02 | 48.0 | 48.0 |
| sat_p0.05 | 48.0 | 48.0 |
| void_b2 | 48.0 | 48.0 |
| void_b4 | 48.0 | 48.0 |
| void_b8 | 48.0 | 48.0 |
| cut | 48.0 | 48.0 |
| polar_lat75 | 48.0 | 48.0 |
| polar_lat60 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 7.4 | 7.4 |
| isl_p0.01 | 7.4 | 7.4 |
| isl_p0.02 | 7.4 | 7.4 |
| isl_p0.05 | 7.4 | 7.4 |
| isl_p0.10 | 7.4 | 7.4 |
| isl_p0.20 | 7.4 | 7.4 |
| sat_p0.005 | 7.4 | 7.4 |
| sat_p0.01 | 7.4 | 7.4 |
| sat_p0.02 | 7.4 | 7.4 |
| sat_p0.05 | 7.6 | 7.6 |
| void_b2 | 7.4 | 7.4 |
| void_b4 | 7.5 | 7.5 |
| void_b8 | 8.6 | 8.6 |
| cut | 7.4 | 7.4 |
| polar_lat75 | 7.4 | 7.4 |
| polar_lat60 | 7.4 | 7.4 |

### Transit egress switches, %

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.0 |
| isl_p0.01 | — | 5.3 |
| isl_p0.02 | — | 10.9 |
| isl_p0.05 | — | 31.1 |
| isl_p0.10 | — | 74.9 |
| isl_p0.20 | — | 199.0 |
| sat_p0.005 | — | 2.1 |
| sat_p0.01 | — | 5.6 |
| sat_p0.02 | — | 10.5 |
| sat_p0.05 | — | 19.0 |
| void_b2 | — | 2.9 |
| void_b4 | — | 5.1 |
| void_b8 | — | 2.6 |
| cut | — | 0.0 |
| polar_lat75 | — | 0.0 |
| polar_lat60 | — | 44.1 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.00 |
| isl_p0.01 | — | 0.06 |
| isl_p0.02 | — | 0.13 |
| isl_p0.05 | — | 0.37 |
| isl_p0.10 | — | 0.89 |
| isl_p0.20 | — | 2.36 |
| sat_p0.005 | — | 0.03 |
| sat_p0.01 | — | 0.07 |
| sat_p0.02 | — | 0.12 |
| sat_p0.05 | — | 0.23 |
| void_b2 | — | 0.03 |
| void_b4 | — | 0.06 |
| void_b8 | — | 0.03 |
| cut | — | 0.00 |
| polar_lat75 | — | 0.00 |
| polar_lat60 | — | 0.52 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 99.9 ± 0.1 | 99.9 ± 0.1 |
| isl_p0.10 | 100.0 ± 0.1 | 100.0 ± 0.1 |
| isl_p0.20 | 99.8 ± 0.2 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 77.3 | 77.3 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.1350 | 1.1350 |
| isl_p0.01 | 1.1366 | 1.1443 |
| isl_p0.02 | 1.1379 | 1.1512 |
| isl_p0.05 | 1.1422 | 1.1716 |
| isl_p0.10 | 1.1516 | 1.2102 |
| isl_p0.20 | 1.1798 | 1.2840 |
| sat_p0.005 | 1.1353 | 1.1372 |
| sat_p0.01 | 1.1356 | 1.1397 |
| sat_p0.02 | 1.1363 | 1.1452 |
| sat_p0.05 | 1.1396 | 1.1646 |
| void_b2 | 1.1352 | 1.1369 |
| void_b4 | 1.1356 | 1.1411 |
| void_b8 | 1.1316 | 1.1408 |
| cut | 1.1439 | 1.1439 |
| polar_lat75 | 1.1447 | 1.1468 |
| polar_lat60 | 1.1585 | 1.1613 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.135 | 1.135 |
| isl_p0.01 | 1.137 | 1.137 |
| isl_p0.02 | 1.138 | 1.139 |
| isl_p0.05 | 1.142 | 1.144 |
| isl_p0.10 | 1.152 | 1.156 |
| isl_p0.20 | 1.180 | 1.192 |
| sat_p0.005 | 1.135 | 1.135 |
| sat_p0.01 | 1.136 | 1.136 |
| sat_p0.02 | 1.136 | 1.137 |
| sat_p0.05 | 1.140 | 1.142 |
| void_b2 | 1.135 | 1.135 |
| void_b4 | 1.136 | 1.137 |
| void_b8 | 1.132 | 1.133 |
| cut | 1.144 | 1.144 |
| polar_lat75 | 1.145 | 1.145 |
| polar_lat60 | 1.158 | 1.159 |

### Distance stretch, forwarding factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.006 |
| isl_p0.02 | 1.000 | 1.011 |
| isl_p0.05 | 1.000 | 1.023 |
| isl_p0.10 | 1.000 | 1.046 |
| isl_p0.20 | 1.000 | 1.076 |
| sat_p0.005 | 1.000 | 1.002 |
| sat_p0.01 | 1.000 | 1.003 |
| sat_p0.02 | 1.000 | 1.007 |
| sat_p0.05 | 1.000 | 1.019 |
| void_b2 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.004 |
| void_b8 | 1.000 | 1.007 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.001 |
| polar_lat60 | 1.000 | 1.002 |

### Ground station renumberings per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 13.7 |
| isl_p0.01 | — | 13.7 |
| isl_p0.02 | — | 13.7 |
| isl_p0.05 | — | 13.7 |
| isl_p0.10 | — | 13.7 |
| isl_p0.20 | — | 13.7 |
| sat_p0.005 | — | 13.7 |
| sat_p0.01 | — | 13.7 |
| sat_p0.02 | — | 13.6 |
| sat_p0.05 | — | 13.5 |
| void_b2 | — | 13.7 |
| void_b4 | — | 13.6 |
| void_b8 | — | 13.0 |
| cut | — | 13.7 |
| polar_lat75 | — | 13.7 |
| polar_lat60 | — | 13.7 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 48.0 | 48.0 |
| isl_p0.01 | 48.0 | 48.0 |
| isl_p0.02 | 48.0 | 48.0 |
| isl_p0.05 | 48.0 | 48.0 |
| isl_p0.10 | 48.0 | 48.0 |
| isl_p0.20 | 48.0 | 48.0 |
| sat_p0.005 | 48.0 | 48.0 |
| sat_p0.01 | 48.0 | 48.0 |
| sat_p0.02 | 48.0 | 48.0 |
| sat_p0.05 | 48.0 | 48.0 |
| void_b2 | 48.0 | 48.0 |
| void_b4 | 48.0 | 48.0 |
| void_b8 | 46.6 | 46.6 |
| cut | 48.0 | 48.0 |
| polar_lat75 | 48.0 | 48.0 |
| polar_lat60 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
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
| void_b8 | 1.4 | 1.4 |
| cut | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 5.1 | 5.1 |
| isl_p0.01 | 5.1 | 5.1 |
| isl_p0.02 | 5.1 | 5.1 |
| isl_p0.05 | 5.1 | 5.1 |
| isl_p0.10 | 5.1 | 5.1 |
| isl_p0.20 | 5.1 | 5.1 |
| sat_p0.005 | 5.1 | 5.1 |
| sat_p0.01 | 5.1 | 5.1 |
| sat_p0.02 | 5.1 | 5.1 |
| sat_p0.05 | 5.4 | 5.4 |
| void_b2 | 5.1 | 5.1 |
| void_b4 | 5.3 | 5.3 |
| void_b8 | 5.4 | 5.4 |
| cut | 5.1 | 5.1 |
| polar_lat75 | 5.1 | 5.1 |
| polar_lat60 | 5.1 | 5.1 |

### Transit egress switches, %

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.0 |
| isl_p0.01 | — | 12.2 |
| isl_p0.02 | — | 23.5 |
| isl_p0.05 | — | 57.4 |
| isl_p0.10 | — | 147.5 |
| isl_p0.20 | — | 420.2 |
| sat_p0.005 | — | 3.1 |
| sat_p0.01 | — | 7.7 |
| sat_p0.02 | — | 16.1 |
| sat_p0.05 | — | 57.4 |
| void_b2 | — | 3.5 |
| void_b4 | — | 12.4 |
| void_b8 | — | 24.4 |
| cut | — | 0.0 |
| polar_lat75 | — | 45.0 |
| polar_lat60 | — | 147.2 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.00 |
| isl_p0.01 | — | 0.09 |
| isl_p0.02 | — | 0.17 |
| isl_p0.05 | — | 0.41 |
| isl_p0.10 | — | 1.05 |
| isl_p0.20 | — | 2.98 |
| sat_p0.005 | — | 0.02 |
| sat_p0.01 | — | 0.05 |
| sat_p0.02 | — | 0.11 |
| sat_p0.05 | — | 0.41 |
| void_b2 | — | 0.02 |
| void_b4 | — | 0.09 |
| void_b8 | — | 0.17 |
| cut | — | 0.00 |
| polar_lat75 | — | 0.32 |
| polar_lat60 | — | 1.04 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.1 | 100.0 ± 0.1 |
| isl_p0.20 | 99.9 ± 0.2 | 99.9 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 80.0 | 80.0 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.1729 | 1.1729 |
| isl_p0.01 | 1.1735 | 1.1782 |
| isl_p0.02 | 1.1745 | 1.1845 |
| isl_p0.05 | 1.1774 | 1.2033 |
| isl_p0.10 | 1.1836 | 1.2342 |
| isl_p0.20 | 1.2048 | 1.2991 |
| sat_p0.005 | 1.1734 | 1.1755 |
| sat_p0.01 | 1.1729 | 1.1775 |
| sat_p0.02 | 1.1733 | 1.1818 |
| sat_p0.05 | 1.1759 | 1.1959 |
| void_b2 | 1.1729 | 1.1736 |
| void_b4 | 1.1724 | 1.1746 |
| void_b8 | 1.1749 | 1.1790 |
| cut | 1.2075 | 1.2075 |
| polar_lat75 | 1.1729 | 1.1729 |
| polar_lat60 | 1.1729 | 1.1729 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.173 | 1.173 |
| isl_p0.01 | 1.174 | 1.174 |
| isl_p0.02 | 1.174 | 1.175 |
| isl_p0.05 | 1.177 | 1.178 |
| isl_p0.10 | 1.184 | 1.185 |
| isl_p0.20 | 1.205 | 1.211 |
| sat_p0.005 | 1.173 | 1.173 |
| sat_p0.01 | 1.173 | 1.173 |
| sat_p0.02 | 1.173 | 1.174 |
| sat_p0.05 | 1.176 | 1.177 |
| void_b2 | 1.173 | 1.173 |
| void_b4 | 1.172 | 1.173 |
| void_b8 | 1.175 | 1.176 |
| cut | 1.208 | 1.208 |
| polar_lat75 | 1.173 | 1.173 |
| polar_lat60 | 1.173 | 1.173 |

### Distance stretch, forwarding factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.004 |
| isl_p0.02 | 1.000 | 1.008 |
| isl_p0.05 | 1.000 | 1.021 |
| isl_p0.10 | 1.000 | 1.041 |
| isl_p0.20 | 1.000 | 1.073 |
| sat_p0.005 | 1.000 | 1.002 |
| sat_p0.01 | 1.000 | 1.004 |
| sat_p0.02 | 1.000 | 1.007 |
| sat_p0.05 | 1.000 | 1.016 |
| void_b2 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.001 |
| void_b8 | 1.000 | 1.002 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 15.5 |
| isl_p0.01 | — | 15.5 |
| isl_p0.02 | — | 15.5 |
| isl_p0.05 | — | 15.5 |
| isl_p0.10 | — | 15.5 |
| isl_p0.20 | — | 15.5 |
| sat_p0.005 | — | 15.5 |
| sat_p0.01 | — | 15.4 |
| sat_p0.02 | — | 15.5 |
| sat_p0.05 | — | 15.3 |
| void_b2 | — | 15.5 |
| void_b4 | — | 15.5 |
| void_b8 | — | 15.1 |
| cut | — | 15.5 |
| polar_lat75 | — | 15.5 |
| polar_lat60 | — | 15.5 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 48.0 | 48.0 |
| isl_p0.01 | 48.0 | 48.0 |
| isl_p0.02 | 48.0 | 48.0 |
| isl_p0.05 | 48.0 | 48.0 |
| isl_p0.10 | 48.0 | 48.0 |
| isl_p0.20 | 48.0 | 48.0 |
| sat_p0.005 | 48.0 | 48.0 |
| sat_p0.01 | 48.0 | 48.0 |
| sat_p0.02 | 48.0 | 48.0 |
| sat_p0.05 | 48.0 | 48.0 |
| void_b2 | 48.0 | 48.0 |
| void_b4 | 48.0 | 48.0 |
| void_b8 | 48.0 | 48.0 |
| cut | 48.0 | 48.0 |
| polar_lat75 | 48.0 | 48.0 |
| polar_lat60 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.0 | 1.0 |
| isl_p0.01 | 1.0 | 1.0 |
| isl_p0.02 | 1.0 | 1.0 |
| isl_p0.05 | 1.0 | 1.0 |
| isl_p0.10 | 1.0 | 1.0 |
| isl_p0.20 | 1.0 | 1.0 |
| sat_p0.005 | 1.0 | 1.0 |
| sat_p0.01 | 1.1 | 1.1 |
| sat_p0.02 | 1.1 | 1.1 |
| sat_p0.05 | 1.1 | 1.1 |
| void_b2 | 1.0 | 1.0 |
| void_b4 | 1.2 | 1.2 |
| void_b8 | 1.5 | 1.5 |
| cut | 1.0 | 1.0 |
| polar_lat75 | 1.0 | 1.0 |
| polar_lat60 | 1.0 | 1.0 |

### Transit egress switches, %

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.0 |
| isl_p0.01 | — | 9.2 |
| isl_p0.02 | — | 21.3 |
| isl_p0.05 | — | 59.6 |
| isl_p0.10 | — | 143.3 |
| isl_p0.20 | — | 417.0 |
| sat_p0.005 | — | 4.9 |
| sat_p0.01 | — | 10.0 |
| sat_p0.02 | — | 20.3 |
| sat_p0.05 | — | 58.0 |
| void_b2 | — | 1.7 |
| void_b4 | — | 5.3 |
| void_b8 | — | 11.0 |
| cut | — | 0.0 |
| polar_lat75 | — | 0.0 |
| polar_lat60 | — | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.00 |
| isl_p0.01 | — | 0.03 |
| isl_p0.02 | — | 0.08 |
| isl_p0.05 | — | 0.21 |
| isl_p0.10 | — | 0.52 |
| isl_p0.20 | — | 1.50 |
| sat_p0.005 | — | 0.02 |
| sat_p0.01 | — | 0.04 |
| sat_p0.02 | — | 0.07 |
| sat_p0.05 | — | 0.21 |
| void_b2 | — | 0.01 |
| void_b4 | — | 0.02 |
| void_b8 | — | 0.04 |
| cut | — | 0.00 |
| polar_lat75 | — | 0.00 |
| polar_lat60 | — | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.2 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 86.1 | 86.1 |
| polar_lat75 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.3199 | 1.3199 |
| isl_p0.01 | 1.3210 | 1.3300 |
| isl_p0.02 | 1.3232 | 1.3402 |
| isl_p0.05 | 1.3280 | 1.3677 |
| isl_p0.10 | 1.3407 | 1.4205 |
| isl_p0.20 | 1.3886 | 1.5446 |
| sat_p0.005 | 1.3208 | 1.3252 |
| sat_p0.01 | 1.3206 | 1.3290 |
| sat_p0.02 | 1.3220 | 1.3356 |
| sat_p0.05 | 1.3247 | 1.3574 |
| void_b2 | 1.3200 | 1.3212 |
| void_b4 | 1.3205 | 1.3234 |
| void_b8 | 1.3193 | 1.3236 |
| cut | 1.3926 | 1.3926 |
| polar_lat75 | 1.3199 | 1.3199 |
| polar_lat60 | 1.3199 | 1.3199 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.320 | 1.320 |
| isl_p0.01 | 1.321 | 1.321 |
| isl_p0.02 | 1.323 | 1.323 |
| isl_p0.05 | 1.328 | 1.329 |
| isl_p0.10 | 1.341 | 1.343 |
| isl_p0.20 | 1.389 | 1.398 |
| sat_p0.005 | 1.321 | 1.321 |
| sat_p0.01 | 1.321 | 1.321 |
| sat_p0.02 | 1.322 | 1.322 |
| sat_p0.05 | 1.325 | 1.325 |
| void_b2 | 1.320 | 1.320 |
| void_b4 | 1.320 | 1.321 |
| void_b8 | 1.319 | 1.320 |
| cut | 1.393 | 1.393 |
| polar_lat75 | 1.320 | 1.320 |
| polar_lat60 | 1.320 | 1.320 |

### Distance stretch, forwarding factor

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.006 |
| isl_p0.02 | 1.000 | 1.012 |
| isl_p0.05 | 1.000 | 1.028 |
| isl_p0.10 | 1.000 | 1.055 |
| isl_p0.20 | 1.000 | 1.102 |
| sat_p0.005 | 1.000 | 1.003 |
| sat_p0.01 | 1.000 | 1.006 |
| sat_p0.02 | 1.000 | 1.009 |
| sat_p0.05 | 1.000 | 1.023 |
| void_b2 | 1.000 | 1.001 |
| void_b4 | 1.000 | 1.002 |
| void_b8 | 1.000 | 1.002 |
| cut | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 19.4 |
| isl_p0.01 | — | 19.4 |
| isl_p0.02 | — | 19.4 |
| isl_p0.05 | — | 19.4 |
| isl_p0.10 | — | 19.4 |
| isl_p0.20 | — | 19.4 |
| sat_p0.005 | — | 19.4 |
| sat_p0.01 | — | 19.4 |
| sat_p0.02 | — | 19.4 |
| sat_p0.05 | — | 19.2 |
| void_b2 | — | 19.4 |
| void_b4 | — | 19.4 |
| void_b8 | — | 19.3 |
| cut | — | 19.4 |
| polar_lat75 | — | 19.4 |
| polar_lat60 | — | 19.4 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 48.0 | 48.0 |
| isl_p0.01 | 48.0 | 48.0 |
| isl_p0.02 | 48.0 | 48.0 |
| isl_p0.05 | 48.0 | 48.0 |
| isl_p0.10 | 48.0 | 48.0 |
| isl_p0.20 | 48.0 | 48.0 |
| sat_p0.005 | 48.0 | 48.0 |
| sat_p0.01 | 48.0 | 48.0 |
| sat_p0.02 | 48.0 | 48.0 |
| sat_p0.05 | 48.0 | 48.0 |
| void_b2 | 48.0 | 48.0 |
| void_b4 | 48.0 | 48.0 |
| void_b8 | 48.0 | 48.0 |
| cut | 48.0 | 48.0 |
| polar_lat75 | 48.0 | 48.0 |
| polar_lat60 | 48.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | 0.6 | 0.6 |
| isl_p0.01 | 0.6 | 0.6 |
| isl_p0.02 | 0.6 | 0.6 |
| isl_p0.05 | 0.6 | 0.6 |
| isl_p0.10 | 0.6 | 0.6 |
| isl_p0.20 | 0.6 | 0.6 |
| sat_p0.005 | 0.6 | 0.6 |
| sat_p0.01 | 0.6 | 0.6 |
| sat_p0.02 | 0.6 | 0.6 |
| sat_p0.05 | 0.6 | 0.6 |
| void_b2 | 0.6 | 0.6 |
| void_b4 | 0.6 | 0.6 |
| void_b8 | 0.7 | 0.7 |
| cut | 0.6 | 0.6 |
| polar_lat75 | 0.6 | 0.6 |
| polar_lat60 | 0.6 | 0.6 |

### Transit egress switches, %

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
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

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.0 |
| isl_p0.01 | — | 13.1 |
| isl_p0.02 | — | 26.1 |
| isl_p0.05 | — | 71.3 |
| isl_p0.10 | — | 184.1 |
| isl_p0.20 | — | 537.4 |
| sat_p0.005 | — | 5.7 |
| sat_p0.01 | — | 12.6 |
| sat_p0.02 | — | 22.3 |
| sat_p0.05 | — | 65.1 |
| void_b2 | — | 2.0 |
| void_b4 | — | 5.0 |
| void_b8 | — | 11.2 |
| cut | — | 0.0 |
| polar_lat75 | — | 0.0 |
| polar_lat60 | — | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_half_req | topological_scheme_req |
|---|---|---|
| none | — | 0.00 |
| isl_p0.01 | — | 0.03 |
| isl_p0.02 | — | 0.07 |
| isl_p0.05 | — | 0.19 |
| isl_p0.10 | — | 0.48 |
| isl_p0.20 | — | 1.41 |
| sat_p0.005 | — | 0.02 |
| sat_p0.01 | — | 0.03 |
| sat_p0.02 | — | 0.06 |
| sat_p0.05 | — | 0.17 |
| void_b2 | — | 0.01 |
| void_b4 | — | 0.01 |
| void_b8 | — | 0.03 |
| cut | — | 0.00 |
| polar_lat75 | — | 0.00 |
| polar_lat60 | — | 0.00 |
