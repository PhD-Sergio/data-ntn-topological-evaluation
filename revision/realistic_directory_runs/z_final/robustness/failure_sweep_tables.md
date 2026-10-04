# Failure sweep summary

Each run is pooled over its snapshots, then seeds are averaged. `±` is the 95%
confidence half-width across seeds; deterministic conditions ran a single seed.

## telesat

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.4 | 99.8 ± 0.2 | 99.8 ± 0.4 | 99.6 ± 0.3 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 51.6 | 96.5 | 51.6 | 69.0 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.2569 | 1.1767 | 1.2569 | 1.1767 |
| isl_p0.01 | 1.2590 | 1.1778 | 1.2651 | 1.1850 |
| isl_p0.02 | 1.2651 | 1.1794 | 1.2809 | 1.1913 |
| isl_p0.05 | 1.2757 | 1.1852 | 1.3112 | 1.2160 |
| isl_p0.10 | 1.2948 | 1.1927 | 1.3578 | 1.2459 |
| isl_p0.20 | 1.3612 | 1.2327 | 1.4613 | 1.3217 |
| sat_p0.005 | 1.2586 | 1.1771 | 1.2624 | 1.1791 |
| sat_p0.01 | 1.2589 | 1.1771 | 1.2658 | 1.1824 |
| sat_p0.02 | 1.2612 | 1.1772 | 1.2727 | 1.1850 |
| sat_p0.05 | 1.2661 | 1.1763 | 1.2858 | 1.1921 |
| void_b2 | 1.2565 | 1.1764 | 1.2590 | 1.1779 |
| void_b4 | 1.2609 | 1.1796 | 1.2652 | 1.1835 |
| void_b8 | 1.3247 | 1.1896 | 1.3330 | 1.1925 |
| cut | 1.2132 | 1.2283 | 1.2132 | 1.1799 |
| polar_lat75 | 1.2524 | 1.1783 | 1.2524 | 1.1801 |
| polar_lat60 | 1.2549 | 1.1846 | 1.2558 | 1.1928 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.257 | 1.177 | 1.257 | 1.177 |
| isl_p0.01 | 1.259 | 1.178 | 1.259 | 1.178 |
| isl_p0.02 | 1.265 | 1.179 | 1.265 | 1.180 |
| isl_p0.05 | 1.276 | 1.185 | 1.276 | 1.188 |
| isl_p0.10 | 1.295 | 1.193 | 1.295 | 1.199 |
| isl_p0.20 | 1.361 | 1.233 | 1.361 | 1.248 |
| sat_p0.005 | 1.259 | 1.177 | 1.259 | 1.177 |
| sat_p0.01 | 1.259 | 1.177 | 1.259 | 1.178 |
| sat_p0.02 | 1.261 | 1.177 | 1.261 | 1.178 |
| sat_p0.05 | 1.266 | 1.176 | 1.266 | 1.178 |
| void_b2 | 1.257 | 1.176 | 1.257 | 1.177 |
| void_b4 | 1.261 | 1.180 | 1.261 | 1.182 |
| void_b8 | 1.325 | 1.190 | 1.325 | 1.192 |
| cut | 1.213 | 1.228 | 1.213 | 1.180 |
| polar_lat75 | 1.252 | 1.178 | 1.252 | 1.179 |
| polar_lat60 | 1.255 | 1.185 | 1.255 | 1.186 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.005 | 1.005 |
| isl_p0.02 | 1.000 | 1.000 | 1.012 | 1.009 |
| isl_p0.05 | 1.000 | 1.000 | 1.027 | 1.023 |
| isl_p0.10 | 1.000 | 1.000 | 1.048 | 1.038 |
| isl_p0.20 | 1.000 | 1.000 | 1.073 | 1.059 |
| sat_p0.005 | 1.000 | 1.000 | 1.003 | 1.001 |
| sat_p0.01 | 1.000 | 1.000 | 1.005 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.009 | 1.006 |
| sat_p0.05 | 1.000 | 1.000 | 1.015 | 1.012 |
| void_b2 | 1.000 | 1.000 | 1.002 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.003 | 1.001 |
| void_b8 | 1.000 | 1.000 | 1.004 | 1.000 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.001 |
| polar_lat60 | 1.000 | 1.000 | 1.001 | 1.006 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 6.0 | 10.7 |
| isl_p0.01 | — | — | 6.0 | 10.7 |
| isl_p0.02 | — | — | 6.0 | 10.7 |
| isl_p0.05 | — | — | 6.0 | 10.7 |
| isl_p0.10 | — | — | 6.0 | 10.7 |
| isl_p0.20 | — | — | 6.0 | 10.7 |
| sat_p0.005 | — | — | 6.0 | 10.7 |
| sat_p0.01 | — | — | 6.0 | 10.6 |
| sat_p0.02 | — | — | 5.9 | 10.6 |
| sat_p0.05 | — | — | 5.9 | 10.5 |
| void_b2 | — | — | 6.0 | 10.6 |
| void_b4 | — | — | 6.0 | 10.5 |
| void_b8 | — | — | 5.8 | 9.9 |
| cut | — | — | 6.0 | 10.7 |
| polar_lat75 | — | — | 6.0 | 10.7 |
| polar_lat60 | — | — | 6.0 | 10.7 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 3.8 | 7.4 | 3.8 | 7.4 |
| isl_p0.01 | 3.8 | 7.4 | 3.8 | 7.4 |
| isl_p0.02 | 3.8 | 7.4 | 3.8 | 7.4 |
| isl_p0.05 | 3.8 | 7.4 | 3.8 | 7.4 |
| isl_p0.10 | 3.8 | 7.4 | 3.8 | 7.4 |
| isl_p0.20 | 3.8 | 7.4 | 3.8 | 7.4 |
| sat_p0.005 | 3.8 | 7.4 | 3.8 | 7.4 |
| sat_p0.01 | 3.8 | 7.4 | 3.8 | 7.4 |
| sat_p0.02 | 3.8 | 7.4 | 3.8 | 7.4 |
| sat_p0.05 | 3.8 | 7.6 | 3.8 | 7.6 |
| void_b2 | 3.8 | 7.4 | 3.8 | 7.4 |
| void_b4 | 3.8 | 7.5 | 3.8 | 7.5 |
| void_b8 | 3.8 | 8.6 | 3.8 | 8.6 |
| cut | 3.8 | 7.4 | 3.8 | 7.4 |
| polar_lat75 | 3.8 | 7.4 | 3.8 | 7.4 |
| polar_lat60 | 3.8 | 7.4 | 3.8 | 7.4 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 |
| isl_p0.01 | — | — | 4.2 | 5.3 |
| isl_p0.02 | — | — | 10.1 | 10.9 |
| isl_p0.05 | — | — | 28.6 | 31.1 |
| isl_p0.10 | — | — | 64.3 | 75.1 |
| isl_p0.20 | — | — | 171.2 | 198.3 |
| sat_p0.005 | — | — | 2.4 | 2.1 |
| sat_p0.01 | — | — | 4.8 | 5.6 |
| sat_p0.02 | — | — | 9.3 | 10.4 |
| sat_p0.05 | — | — | 17.1 | 19.0 |
| void_b2 | — | — | 2.7 | 2.9 |
| void_b4 | — | — | 5.0 | 5.1 |
| void_b8 | — | — | 14.3 | 2.6 |
| cut | — | — | 0.0 | 0.0 |
| polar_lat75 | — | — | 0.7 | 0.0 |
| polar_lat60 | — | — | 49.5 | 44.2 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.05 | 0.06 |
| isl_p0.02 | — | — | 0.12 | 0.13 |
| isl_p0.05 | — | — | 0.34 | 0.37 |
| isl_p0.10 | — | — | 0.76 | 0.89 |
| isl_p0.20 | — | — | 2.03 | 2.35 |
| sat_p0.005 | — | — | 0.03 | 0.03 |
| sat_p0.01 | — | — | 0.06 | 0.07 |
| sat_p0.02 | — | — | 0.11 | 0.12 |
| sat_p0.05 | — | — | 0.20 | 0.23 |
| void_b2 | — | — | 0.03 | 0.03 |
| void_b4 | — | — | 0.06 | 0.06 |
| void_b8 | — | — | 0.17 | 0.03 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.01 | 0.00 |
| polar_lat60 | — | — | 0.59 | 0.53 |

## oneweb

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 99.9 ± 0.2 | 99.9 ± 0.1 | 99.9 ± 0.2 | 99.9 ± 0.1 |
| isl_p0.10 | 100.0 ± 0.1 | 100.0 ± 0.1 | 100.0 ± 0.1 | 99.9 ± 0.1 |
| isl_p0.20 | 99.7 ± 0.2 | 99.8 ± 0.2 | 99.7 ± 0.2 | 99.6 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 71.7 | 77.3 | 71.7 | 72.9 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.1763 | 1.1349 | 1.1763 | 1.1349 |
| isl_p0.01 | 1.1783 | 1.1366 | 1.1862 | 1.1443 |
| isl_p0.02 | 1.1798 | 1.1378 | 1.1939 | 1.1512 |
| isl_p0.05 | 1.1841 | 1.1421 | 1.2141 | 1.1714 |
| isl_p0.10 | 1.1953 | 1.1515 | 1.2517 | 1.2101 |
| isl_p0.20 | 1.2271 | 1.1797 | 1.3227 | 1.2832 |
| sat_p0.005 | 1.1766 | 1.1353 | 1.1783 | 1.1371 |
| sat_p0.01 | 1.1773 | 1.1355 | 1.1814 | 1.1396 |
| sat_p0.02 | 1.1786 | 1.1363 | 1.1879 | 1.1452 |
| sat_p0.05 | 1.1834 | 1.1396 | 1.2083 | 1.1646 |
| void_b2 | 1.1768 | 1.1352 | 1.1784 | 1.1368 |
| void_b4 | 1.1772 | 1.1356 | 1.1830 | 1.1411 |
| void_b8 | 1.1716 | 1.1316 | 1.1812 | 1.1408 |
| cut | 1.1907 | 1.1438 | 1.1907 | 1.1436 |
| polar_lat75 | 1.1855 | 1.1446 | 1.1874 | 1.1467 |
| polar_lat60 | 1.1983 | 1.1584 | 1.2006 | 1.1613 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.176 | 1.135 | 1.176 | 1.135 |
| isl_p0.01 | 1.178 | 1.137 | 1.178 | 1.137 |
| isl_p0.02 | 1.180 | 1.138 | 1.180 | 1.139 |
| isl_p0.05 | 1.184 | 1.142 | 1.184 | 1.144 |
| isl_p0.10 | 1.195 | 1.152 | 1.195 | 1.156 |
| isl_p0.20 | 1.227 | 1.180 | 1.227 | 1.192 |
| sat_p0.005 | 1.177 | 1.135 | 1.177 | 1.135 |
| sat_p0.01 | 1.177 | 1.136 | 1.177 | 1.136 |
| sat_p0.02 | 1.179 | 1.136 | 1.179 | 1.137 |
| sat_p0.05 | 1.183 | 1.140 | 1.183 | 1.142 |
| void_b2 | 1.177 | 1.135 | 1.177 | 1.135 |
| void_b4 | 1.177 | 1.136 | 1.177 | 1.137 |
| void_b8 | 1.172 | 1.132 | 1.172 | 1.133 |
| cut | 1.191 | 1.144 | 1.191 | 1.144 |
| polar_lat75 | 1.186 | 1.145 | 1.186 | 1.145 |
| polar_lat60 | 1.198 | 1.158 | 1.198 | 1.159 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.007 | 1.006 |
| isl_p0.02 | 1.000 | 1.000 | 1.012 | 1.011 |
| isl_p0.05 | 1.000 | 1.000 | 1.025 | 1.023 |
| isl_p0.10 | 1.000 | 1.000 | 1.047 | 1.046 |
| isl_p0.20 | 1.000 | 1.000 | 1.078 | 1.076 |
| sat_p0.005 | 1.000 | 1.000 | 1.001 | 1.002 |
| sat_p0.01 | 1.000 | 1.000 | 1.004 | 1.003 |
| sat_p0.02 | 1.000 | 1.000 | 1.008 | 1.007 |
| sat_p0.05 | 1.000 | 1.000 | 1.021 | 1.019 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.005 | 1.004 |
| void_b8 | 1.000 | 1.000 | 1.008 | 1.007 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.001 | 1.001 |
| polar_lat60 | 1.000 | 1.000 | 1.002 | 1.002 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 10.9 | 13.7 |
| isl_p0.01 | — | — | 10.9 | 13.7 |
| isl_p0.02 | — | — | 10.9 | 13.7 |
| isl_p0.05 | — | — | 10.9 | 13.7 |
| isl_p0.10 | — | — | 10.9 | 13.7 |
| isl_p0.20 | — | — | 10.9 | 13.7 |
| sat_p0.005 | — | — | 10.9 | 13.7 |
| sat_p0.01 | — | — | 10.9 | 13.7 |
| sat_p0.02 | — | — | 10.8 | 13.6 |
| sat_p0.05 | — | — | 10.6 | 13.5 |
| void_b2 | — | — | 10.9 | 13.7 |
| void_b4 | — | — | 10.7 | 13.6 |
| void_b8 | — | — | 10.3 | 13.0 |
| cut | — | — | 10.9 | 13.7 |
| polar_lat75 | — | — | 10.9 | 13.7 |
| polar_lat60 | — | — | 10.9 | 13.7 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b8 | 23.4 | 46.6 | 23.4 | 46.6 |
| cut | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.6 | 1.4 | 0.6 | 1.4 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.8 | 5.1 | 1.8 | 5.1 |
| isl_p0.01 | 1.8 | 5.1 | 1.8 | 5.1 |
| isl_p0.02 | 1.8 | 5.1 | 1.8 | 5.1 |
| isl_p0.05 | 1.8 | 5.1 | 1.8 | 5.1 |
| isl_p0.10 | 1.8 | 5.1 | 1.8 | 5.1 |
| isl_p0.20 | 1.8 | 5.1 | 1.8 | 5.1 |
| sat_p0.005 | 1.8 | 5.1 | 1.8 | 5.1 |
| sat_p0.01 | 1.8 | 5.1 | 1.8 | 5.1 |
| sat_p0.02 | 1.8 | 5.1 | 1.8 | 5.1 |
| sat_p0.05 | 1.9 | 5.4 | 1.9 | 5.4 |
| void_b2 | 1.8 | 5.1 | 1.8 | 5.1 |
| void_b4 | 1.9 | 5.3 | 1.9 | 5.3 |
| void_b8 | 2.0 | 5.4 | 2.0 | 5.4 |
| cut | 1.8 | 5.1 | 1.8 | 5.1 |
| polar_lat75 | 1.8 | 5.1 | 1.8 | 5.1 |
| polar_lat60 | 1.8 | 5.1 | 1.8 | 5.1 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.10 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 |
| isl_p0.01 | — | — | 11.9 | 12.2 |
| isl_p0.02 | — | — | 22.2 | 23.5 |
| isl_p0.05 | — | — | 55.0 | 57.4 |
| isl_p0.10 | — | — | 139.1 | 147.5 |
| isl_p0.20 | — | — | 395.2 | 419.8 |
| sat_p0.005 | — | — | 2.7 | 3.1 |
| sat_p0.01 | — | — | 7.3 | 7.7 |
| sat_p0.02 | — | — | 15.1 | 16.2 |
| sat_p0.05 | — | — | 55.1 | 57.5 |
| void_b2 | — | — | 2.8 | 3.5 |
| void_b4 | — | — | 11.9 | 12.4 |
| void_b8 | — | — | 24.1 | 24.4 |
| cut | — | — | 0.0 | 0.0 |
| polar_lat75 | — | — | 57.9 | 45.0 |
| polar_lat60 | — | — | 196.4 | 147.2 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.08 | 0.09 |
| isl_p0.02 | — | — | 0.16 | 0.17 |
| isl_p0.05 | — | — | 0.39 | 0.41 |
| isl_p0.10 | — | — | 0.99 | 1.05 |
| isl_p0.20 | — | — | 2.80 | 2.97 |
| sat_p0.005 | — | — | 0.02 | 0.02 |
| sat_p0.01 | — | — | 0.05 | 0.05 |
| sat_p0.02 | — | — | 0.11 | 0.11 |
| sat_p0.05 | — | — | 0.39 | 0.41 |
| void_b2 | — | — | 0.02 | 0.02 |
| void_b4 | — | — | 0.08 | 0.09 |
| void_b8 | — | — | 0.17 | 0.17 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.41 | 0.32 |
| polar_lat60 | — | — | 1.39 | 1.04 |

## kuiper

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.1 | 100.0 ± 0.0 | 99.9 ± 0.1 |
| isl_p0.20 | 99.8 ± 0.2 | 99.9 ± 0.2 | 99.8 ± 0.2 | 99.8 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 64.6 | 80.0 | 64.6 | 69.4 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.2079 | 1.1729 | 1.2079 | 1.1729 |
| isl_p0.01 | 1.2094 | 1.1735 | 1.2149 | 1.1782 |
| isl_p0.02 | 1.2108 | 1.1745 | 1.2226 | 1.1845 |
| isl_p0.05 | 1.2160 | 1.1774 | 1.2456 | 1.2033 |
| isl_p0.10 | 1.2242 | 1.1836 | 1.2793 | 1.2341 |
| isl_p0.20 | 1.2521 | 1.2048 | 1.3516 | 1.2982 |
| sat_p0.005 | 1.2084 | 1.1734 | 1.2108 | 1.1755 |
| sat_p0.01 | 1.2091 | 1.1729 | 1.2157 | 1.1775 |
| sat_p0.02 | 1.2100 | 1.1733 | 1.2209 | 1.1818 |
| sat_p0.05 | 1.2130 | 1.1759 | 1.2357 | 1.1959 |
| void_b2 | 1.2081 | 1.1729 | 1.2091 | 1.1736 |
| void_b4 | 1.2072 | 1.1724 | 1.2095 | 1.1746 |
| void_b8 | 1.2211 | 1.1749 | 1.2255 | 1.1790 |
| cut | 1.1781 | 1.2075 | 1.1781 | 1.1341 |
| polar_lat75 | 1.2079 | 1.1729 | 1.2079 | 1.1729 |
| polar_lat60 | 1.2079 | 1.1729 | 1.2079 | 1.1729 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.208 | 1.173 | 1.208 | 1.173 |
| isl_p0.01 | 1.209 | 1.174 | 1.209 | 1.174 |
| isl_p0.02 | 1.211 | 1.174 | 1.211 | 1.175 |
| isl_p0.05 | 1.216 | 1.177 | 1.216 | 1.178 |
| isl_p0.10 | 1.224 | 1.184 | 1.224 | 1.185 |
| isl_p0.20 | 1.252 | 1.205 | 1.252 | 1.210 |
| sat_p0.005 | 1.208 | 1.173 | 1.208 | 1.173 |
| sat_p0.01 | 1.209 | 1.173 | 1.209 | 1.173 |
| sat_p0.02 | 1.210 | 1.173 | 1.210 | 1.174 |
| sat_p0.05 | 1.213 | 1.176 | 1.213 | 1.177 |
| void_b2 | 1.208 | 1.173 | 1.208 | 1.173 |
| void_b4 | 1.207 | 1.172 | 1.207 | 1.173 |
| void_b8 | 1.221 | 1.175 | 1.221 | 1.176 |
| cut | 1.178 | 1.208 | 1.178 | 1.134 |
| polar_lat75 | 1.208 | 1.173 | 1.208 | 1.173 |
| polar_lat60 | 1.208 | 1.173 | 1.208 | 1.173 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.005 | 1.004 |
| isl_p0.02 | 1.000 | 1.000 | 1.010 | 1.008 |
| isl_p0.05 | 1.000 | 1.000 | 1.024 | 1.021 |
| isl_p0.10 | 1.000 | 1.000 | 1.045 | 1.041 |
| isl_p0.20 | 1.000 | 1.000 | 1.080 | 1.073 |
| sat_p0.005 | 1.000 | 1.000 | 1.002 | 1.002 |
| sat_p0.01 | 1.000 | 1.000 | 1.005 | 1.004 |
| sat_p0.02 | 1.000 | 1.000 | 1.009 | 1.007 |
| sat_p0.05 | 1.000 | 1.000 | 1.019 | 1.016 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.002 | 1.001 |
| void_b8 | 1.000 | 1.000 | 1.003 | 1.002 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 10.5 | 15.5 |
| isl_p0.01 | — | — | 10.5 | 15.5 |
| isl_p0.02 | — | — | 10.5 | 15.5 |
| isl_p0.05 | — | — | 10.5 | 15.5 |
| isl_p0.10 | — | — | 10.5 | 15.5 |
| isl_p0.20 | — | — | 10.5 | 15.5 |
| sat_p0.005 | — | — | 10.5 | 15.5 |
| sat_p0.01 | — | — | 10.4 | 15.4 |
| sat_p0.02 | — | — | 10.5 | 15.5 |
| sat_p0.05 | — | — | 10.4 | 15.3 |
| void_b2 | — | — | 10.5 | 15.5 |
| void_b4 | — | — | 10.5 | 15.5 |
| void_b8 | — | — | 10.3 | 15.1 |
| cut | — | — | 10.5 | 15.5 |
| polar_lat75 | — | — | 10.5 | 15.5 |
| polar_lat60 | — | — | 10.5 | 15.5 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.2 | 1.0 | 0.2 | 1.0 |
| isl_p0.01 | 0.2 | 1.0 | 0.2 | 1.0 |
| isl_p0.02 | 0.2 | 1.0 | 0.2 | 1.0 |
| isl_p0.05 | 0.2 | 1.0 | 0.2 | 1.0 |
| isl_p0.10 | 0.2 | 1.0 | 0.2 | 1.0 |
| isl_p0.20 | 0.2 | 1.0 | 0.2 | 1.0 |
| sat_p0.005 | 0.2 | 1.0 | 0.2 | 1.0 |
| sat_p0.01 | 0.2 | 1.1 | 0.2 | 1.1 |
| sat_p0.02 | 0.2 | 1.1 | 0.2 | 1.1 |
| sat_p0.05 | 0.3 | 1.1 | 0.3 | 1.1 |
| void_b2 | 0.2 | 1.0 | 0.2 | 1.0 |
| void_b4 | 0.3 | 1.2 | 0.3 | 1.2 |
| void_b8 | 0.5 | 1.5 | 0.5 | 1.5 |
| cut | 0.2 | 1.0 | 0.2 | 1.0 |
| polar_lat75 | 0.2 | 1.0 | 0.2 | 1.0 |
| polar_lat60 | 0.2 | 1.0 | 0.2 | 1.0 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 |
| isl_p0.01 | — | — | 8.8 | 9.2 |
| isl_p0.02 | — | — | 19.9 | 21.3 |
| isl_p0.05 | — | — | 54.5 | 59.6 |
| isl_p0.10 | — | — | 135.9 | 143.3 |
| isl_p0.20 | — | — | 395.1 | 415.9 |
| sat_p0.005 | — | — | 3.8 | 4.9 |
| sat_p0.01 | — | — | 10.3 | 10.0 |
| sat_p0.02 | — | — | 19.2 | 20.3 |
| sat_p0.05 | — | — | 50.9 | 58.0 |
| void_b2 | — | — | 1.9 | 1.7 |
| void_b4 | — | — | 5.6 | 5.3 |
| void_b8 | — | — | 11.7 | 11.0 |
| cut | — | — | 0.0 | 0.0 |
| polar_lat75 | — | — | 0.0 | 0.0 |
| polar_lat60 | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.03 | 0.03 |
| isl_p0.02 | — | — | 0.07 | 0.08 |
| isl_p0.05 | — | — | 0.20 | 0.21 |
| isl_p0.10 | — | — | 0.49 | 0.52 |
| isl_p0.20 | — | — | 1.42 | 1.50 |
| sat_p0.005 | — | — | 0.01 | 0.02 |
| sat_p0.01 | — | — | 0.04 | 0.04 |
| sat_p0.02 | — | — | 0.07 | 0.07 |
| sat_p0.05 | — | — | 0.18 | 0.21 |
| void_b2 | — | — | 0.01 | 0.01 |
| void_b4 | — | — | 0.02 | 0.02 |
| void_b8 | — | — | 0.04 | 0.04 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |

## starlink

### Delivery rate, % of deliverable pairs

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 100.0 | 100.0 | 100.0 | 100.0 |
| isl_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.10 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| isl_p0.20 | 99.8 ± 0.1 | 99.8 ± 0.2 | 99.8 ± 0.1 | 99.7 ± 0.2 |
| sat_p0.005 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.01 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.02 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| sat_p0.05 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b2 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b4 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| void_b8 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| cut | 54.6 | 86.1 | 54.6 | 68.9 |
| polar_lat75 | 100.0 | 100.0 | 100.0 | 100.0 |
| polar_lat60 | 100.0 | 100.0 | 100.0 | 100.0 |

### Delivery gap to link-state, percentage points, paired by seed

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | — | — | — | — |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | — | — | — | — |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Distance stretch, shared basis

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.4460 | 1.3199 | 1.4460 | 1.3199 |
| isl_p0.01 | 1.4502 | 1.3210 | 1.4640 | 1.3300 |
| isl_p0.02 | 1.4555 | 1.3232 | 1.4803 | 1.3402 |
| isl_p0.05 | 1.4712 | 1.3280 | 1.5290 | 1.3676 |
| isl_p0.10 | 1.5008 | 1.3407 | 1.6125 | 1.4205 |
| isl_p0.20 | 1.5908 | 1.3886 | 1.7887 | 1.5424 |
| sat_p0.005 | 1.4474 | 1.3208 | 1.4532 | 1.3252 |
| sat_p0.01 | 1.4501 | 1.3206 | 1.4638 | 1.3290 |
| sat_p0.02 | 1.4536 | 1.3220 | 1.4747 | 1.3356 |
| sat_p0.05 | 1.4652 | 1.3247 | 1.5165 | 1.3574 |
| void_b2 | 1.4469 | 1.3200 | 1.4483 | 1.3212 |
| void_b4 | 1.4494 | 1.3205 | 1.4534 | 1.3234 |
| void_b8 | 1.4566 | 1.3193 | 1.4663 | 1.3236 |
| cut | 1.3726 | 1.3926 | 1.3726 | 1.2438 |
| polar_lat75 | 1.4460 | 1.3199 | 1.4460 | 1.3199 |
| polar_lat60 | 1.4460 | 1.3199 | 1.4460 | 1.3199 |

### Distance stretch, egress-choice factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.446 | 1.320 | 1.446 | 1.320 |
| isl_p0.01 | 1.450 | 1.321 | 1.450 | 1.321 |
| isl_p0.02 | 1.455 | 1.323 | 1.455 | 1.323 |
| isl_p0.05 | 1.471 | 1.328 | 1.471 | 1.329 |
| isl_p0.10 | 1.501 | 1.341 | 1.501 | 1.343 |
| isl_p0.20 | 1.591 | 1.389 | 1.591 | 1.396 |
| sat_p0.005 | 1.447 | 1.321 | 1.447 | 1.321 |
| sat_p0.01 | 1.450 | 1.321 | 1.450 | 1.321 |
| sat_p0.02 | 1.454 | 1.322 | 1.454 | 1.322 |
| sat_p0.05 | 1.465 | 1.325 | 1.465 | 1.325 |
| void_b2 | 1.447 | 1.320 | 1.447 | 1.320 |
| void_b4 | 1.449 | 1.320 | 1.449 | 1.321 |
| void_b8 | 1.457 | 1.319 | 1.457 | 1.320 |
| cut | 1.373 | 1.393 | 1.373 | 1.244 |
| polar_lat75 | 1.446 | 1.320 | 1.446 | 1.320 |
| polar_lat60 | 1.446 | 1.320 | 1.446 | 1.320 |

### Distance stretch, forwarding factor

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 1.000 | 1.000 | 1.000 | 1.000 |
| isl_p0.01 | 1.000 | 1.000 | 1.010 | 1.006 |
| isl_p0.02 | 1.000 | 1.000 | 1.017 | 1.012 |
| isl_p0.05 | 1.000 | 1.000 | 1.040 | 1.028 |
| isl_p0.10 | 1.000 | 1.000 | 1.076 | 1.055 |
| isl_p0.20 | 1.000 | 1.000 | 1.128 | 1.102 |
| sat_p0.005 | 1.000 | 1.000 | 1.004 | 1.003 |
| sat_p0.01 | 1.000 | 1.000 | 1.009 | 1.006 |
| sat_p0.02 | 1.000 | 1.000 | 1.015 | 1.009 |
| sat_p0.05 | 1.000 | 1.000 | 1.036 | 1.023 |
| void_b2 | 1.000 | 1.000 | 1.001 | 1.001 |
| void_b4 | 1.000 | 1.000 | 1.003 | 1.002 |
| void_b8 | 1.000 | 1.000 | 1.007 | 1.002 |
| cut | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat75 | 1.000 | 1.000 | 1.000 | 1.000 |
| polar_lat60 | 1.000 | 1.000 | 1.000 | 1.000 |

### Ground station renumberings per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 15.4 | 19.4 |
| isl_p0.01 | — | — | 15.4 | 19.4 |
| isl_p0.02 | — | — | 15.4 | 19.4 |
| isl_p0.05 | — | — | 15.4 | 19.4 |
| isl_p0.10 | — | — | 15.4 | 19.4 |
| isl_p0.20 | — | — | 15.4 | 19.4 |
| sat_p0.005 | — | — | 15.3 | 19.4 |
| sat_p0.01 | — | — | 15.2 | 19.4 |
| sat_p0.02 | — | — | 15.2 | 19.4 |
| sat_p0.05 | — | — | 14.9 | 19.2 |
| void_b2 | — | — | 15.4 | 19.4 |
| void_b4 | — | — | 15.3 | 19.4 |
| void_b8 | — | — | 15.2 | 19.3 |
| cut | — | — | 15.4 | 19.4 |
| polar_lat75 | — | — | 15.4 | 19.4 |
| polar_lat60 | — | — | 15.4 | 19.4 |

### Assigned ground-station links per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.10 | 24.0 | 48.0 | 24.0 | 48.0 |
| isl_p0.20 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.005 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.01 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.02 | 24.0 | 48.0 | 24.0 | 48.0 |
| sat_p0.05 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b2 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b4 | 24.0 | 48.0 | 24.0 | 48.0 |
| void_b8 | 24.0 | 48.0 | 24.0 | 48.0 |
| cut | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat75 | 24.0 | 48.0 | 24.0 | 48.0 |
| polar_lat60 | 24.0 | 48.0 | 24.0 | 48.0 |

### Requested attachment shortfall per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Unconstrained satellite-radio conflicts per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.3 | 0.6 | 0.3 | 0.6 |
| isl_p0.01 | 0.3 | 0.6 | 0.3 | 0.6 |
| isl_p0.02 | 0.3 | 0.6 | 0.3 | 0.6 |
| isl_p0.05 | 0.3 | 0.6 | 0.3 | 0.6 |
| isl_p0.10 | 0.3 | 0.6 | 0.3 | 0.6 |
| isl_p0.20 | 0.3 | 0.6 | 0.3 | 0.6 |
| sat_p0.005 | 0.3 | 0.6 | 0.3 | 0.6 |
| sat_p0.01 | 0.3 | 0.6 | 0.3 | 0.6 |
| sat_p0.02 | 0.3 | 0.6 | 0.3 | 0.6 |
| sat_p0.05 | 0.3 | 0.6 | 0.3 | 0.6 |
| void_b2 | 0.3 | 0.6 | 0.3 | 0.6 |
| void_b4 | 0.3 | 0.6 | 0.3 | 0.6 |
| void_b8 | 0.3 | 0.7 | 0.3 | 0.7 |
| cut | 0.3 | 0.6 | 0.3 | 0.6 |
| polar_lat75 | 0.3 | 0.6 | 0.3 | 0.6 |
| polar_lat60 | 0.3 | 0.6 | 0.3 | 0.6 |

### Transit egress switches, %

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Dominant forwarding-failure cause, share of failures

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | — | — |
| isl_p0.01 | — | — | — | — |
| isl_p0.02 | — | — | — | — |
| isl_p0.05 | — | — | — | — |
| isl_p0.10 | — | — | — | — |
| isl_p0.20 | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| sat_p0.005 | — | — | — | — |
| sat_p0.01 | — | — | — | — |
| sat_p0.02 | — | — | — | — |
| sat_p0.05 | — | — | — | — |
| void_b2 | — | — | — | — |
| void_b4 | — | — | — | — |
| void_b8 | — | — | — | — |
| cut | dead_end 100% | dead_end 100% | dead_end 100% | dead_end 100% |
| polar_lat75 | — | — | — | — |
| polar_lat60 | — | — | — | — |

### Forwarding loops, looping pairs per snapshot

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.10 | 0.0 | 0.0 | 0.0 | 0.0 |
| isl_p0.20 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.005 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.01 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.02 | 0.0 | 0.0 | 0.0 | 0.0 |
| sat_p0.05 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b2 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b4 | 0.0 | 0.0 | 0.0 | 0.0 |
| void_b8 | 0.0 | 0.0 | 0.0 | 0.0 |
| cut | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat75 | 0.0 | 0.0 | 0.0 | 0.0 |
| polar_lat60 | 0.0 | 0.0 | 0.0 | 0.0 |

### Exception entries per snapshot, one-pass bound in brackets

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.0 | 0.0 |
| isl_p0.01 | — | — | 17.1 | 13.1 |
| isl_p0.02 | — | — | 35.0 | 26.1 |
| isl_p0.05 | — | — | 94.6 | 71.3 |
| isl_p0.10 | — | — | 219.2 | 184.1 |
| isl_p0.20 | — | — | 594.3 | 534.6 |
| sat_p0.005 | — | — | 5.9 | 5.7 |
| sat_p0.01 | — | — | 17.7 | 12.6 |
| sat_p0.02 | — | — | 29.3 | 22.3 |
| sat_p0.05 | — | — | 88.1 | 65.1 |
| void_b2 | — | — | 2.3 | 2.0 |
| void_b4 | — | — | 7.1 | 5.0 |
| void_b8 | — | — | 22.5 | 11.2 |
| cut | — | — | 0.0 | 0.0 |
| polar_lat75 | — | — | 0.0 | 0.0 |
| polar_lat60 | — | — | 0.0 | 0.0 |

### Exception entries, % of link-state forwarding entries

| condition | link_state_dir_asc | link_state_dir_half_req | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|
| none | — | — | 0.00 | 0.00 |
| isl_p0.01 | — | — | 0.04 | 0.03 |
| isl_p0.02 | — | — | 0.09 | 0.07 |
| isl_p0.05 | — | — | 0.25 | 0.19 |
| isl_p0.10 | — | — | 0.58 | 0.48 |
| isl_p0.20 | — | — | 1.56 | 1.41 |
| sat_p0.005 | — | — | 0.02 | 0.02 |
| sat_p0.01 | — | — | 0.05 | 0.03 |
| sat_p0.02 | — | — | 0.08 | 0.06 |
| sat_p0.05 | — | — | 0.23 | 0.17 |
| void_b2 | — | — | 0.01 | 0.01 |
| void_b4 | — | — | 0.02 | 0.01 |
| void_b8 | — | — | 0.06 | 0.03 |
| cut | — | — | 0.00 | 0.00 |
| polar_lat75 | — | — | 0.00 | 0.00 |
| polar_lat60 | — | — | 0.00 | 0.00 |
