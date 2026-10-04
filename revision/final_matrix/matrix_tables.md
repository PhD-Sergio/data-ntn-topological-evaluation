# Evaluation matrix summary

Rates are pooled over each run's snapshots and stretch is weighted by the pairs it
was measured over. Sizes are entries per satellite unless marked as simulator-wide.

## ring

### Deliverable pairs per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 132.3 | 125.1 | 125.1 | 125.1 | 125.1 | 132.3 | 125.1 | 125.1 | 132.3 | 125.1 |
| oneweb | 155.4 | 155.7 | 155.7 | 155.7 | 155.7 | 155.4 | 155.7 | 155.7 | 155.4 | 155.7 |
| kuiper | 132.2 | 137.5 | 137.5 | 137.5 | 137.5 | 132.2 | 137.5 | 137.5 | 132.2 | 137.5 |
| starlink | 103.6 | 108.2 | 108.2 | 108.2 | 108.2 | 103.6 | 108.2 | 108.2 | 103.6 | 108.2 |

### Delivery rate, % of deliverable pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 19.1% | 26.5% | 100.0% | 96.3% | 100.0% | 19.1% | 26.5% | 100.0% | 19.1% | 26.5% |
| oneweb | 30.1% | 33.8% | 100.0% | 99.5% | 100.0% | 30.1% | 33.8% | 100.0% | 30.1% | 33.8% |
| kuiper | 10.5% | 14.0% | 100.0% | 98.3% | 100.0% | 10.5% | 14.0% | 100.0% | 10.5% | 14.0% |
| starlink | 10.6% | 10.5% | 100.0% | 93.8% | 100.0% | 10.6% | 10.5% | 100.0% | 10.6% | 10.5% |

### Distance stretch, shared basis

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 1.00430 | 0.99540 | 1.00000 | 1.03171 | 1.00000 | 1.00430 | 0.99540 | 1.00072 | 1.00430 | 0.99540 |
| oneweb | 1.12576 | 1.09857 | 1.00000 | 1.01052 | 1.00000 | 1.12576 | 1.09857 | 1.00000 | 1.12576 | 1.09857 |
| kuiper | 1.08390 | 1.06975 | 1.00000 | 1.03107 | 1.00000 | 1.08390 | 1.06973 | 1.00000 | 1.08390 | 1.06974 |
| starlink | 1.00000 | 0.99535 | 1.00000 | 1.06283 | 1.00000 | 1.00000 | 0.99533 | 1.00001 | 1.00000 | 0.99534 |

### Non-optimal egress, % of delivered pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 1.3% | 16.4% | 0.0% | 3.8% | 0.0% | 1.3% | 16.4% | 0.1% | 1.3% | 16.4% |
| oneweb | 91.3% | 81.9% | 0.0% | 18.3% | 0.0% | 91.3% | 81.9% | 0.1% | 91.3% | 81.9% |
| kuiper | 54.7% | 55.5% | 0.0% | 14.2% | 0.0% | 54.7% | 55.5% | 0.0% | 54.7% | 55.5% |
| starlink | 0.0% | 1.6% | 0.0% | 3.4% | 0.0% | 0.0% | 1.6% | 0.0% | 0.0% | 1.6% |

### Installed forwarding entries per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 22.2 | 21.9 | 5.6 | 5.5 | 5.6 | 0.9 | 1.8 | 5.6 | 0.9 | 1.8 |
| oneweb | 23.6 | 23.5 | 7.2 | 7.2 | 7.2 | 2.0 | 2.7 | 7.2 | 2.0 | 2.7 |
| kuiper | 23.3 | 23.0 | 5.9 | 5.9 | 5.9 | 0.7 | 1.4 | 5.9 | 0.7 | 1.4 |
| starlink | 22.9 | 22.8 | 4.6 | 4.6 | 4.6 | 0.3 | 0.7 | 4.6 | 0.3 | 0.7 |

### Unreachable-destination markers per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 18.4 | 18.5 | 18.4 | 23.1 | 22.2 | 0.0 | 0.0 | 0.0 |
| oneweb | 0.0 | 0.0 | 16.8 | 16.8 | 16.8 | 22.0 | 21.3 | 0.0 | 0.0 | 0.0 |
| kuiper | 0.0 | 0.0 | 18.1 | 18.1 | 18.1 | 23.3 | 22.6 | 0.0 | 0.0 | 0.0 |
| starlink | 0.0 | 0.0 | 19.4 | 19.4 | 19.4 | 23.7 | 23.3 | 0.0 | 0.0 | 0.0 |

### Analytical forwarding-state proxy per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 2.5 | 2.5 | 2.9 | 2.9 | 351.0 | 351.0 | 351.0 | 2.5 | 2.5 | 2.5 |
| oneweb | 2.7 | 2.7 | 3.0 | 3.0 | 588.0 | 588.0 | 588.0 | 2.7 | 2.7 | 2.7 |
| kuiper | 2.3 | 2.3 | 2.4 | 2.4 | 1,156.0 | 1,156.0 | 1,156.0 | 2.3 | 2.3 | 2.3 |
| starlink | 2.2 | 2.2 | 2.3 | 2.3 | 1,584.0 | 1,584.0 | 1,584.0 | 2.2 | 2.2 | 2.2 |

### Forwarding-state updates per satellite per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.03 | 0.05 | 0.32 | 0.31 | 3.36 | 0.34 | 1.43 | 0.05 | 0.03 | 0.05 |
| oneweb | 0.04 | 0.04 | 0.34 | 0.33 | 5.62 | 1.60 | 2.41 | 0.04 | 0.04 | 0.04 |
| kuiper | 0.02 | 0.03 | 0.23 | 0.23 | 7.72 | 0.60 | 2.00 | 0.03 | 0.02 | 0.03 |
| starlink | 0.02 | 0.02 | 0.16 | 0.16 | 7.01 | 0.43 | 1.11 | 0.02 | 0.02 | 0.02 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 238 | 476 | 376 | 215 | 790 | 334 | 326 | 736 | 293 | 333 |
| oneweb | 503 | 768 | 1,459 | 729 | 3,870 | 2,027 | 1,193 | 7,770 | 1,701 | 1,638 |
| kuiper | 802 | 1,444 | 2,301 | 1,063 | 21,091 | 19,256 | 13,419 | 14,245 | 2,203 | 1,899 |
| starlink | 1,093 | 1,816 | 2,159 | 1,162 | 45,344 | 41,330 | 26,836 | 16,002 | 2,417 | 2,549 |

## grid

### Deliverable pairs per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| oneweb | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| kuiper | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| starlink | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |

### Delivery rate, % of deliverable pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| oneweb | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| kuiper | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| starlink | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 1.27647 | 1.21500 | 1.00000 | 1.02109 | 1.00000 | 1.25767 | 1.17608 | 1.00009 | 1.25767 | 1.17608 |
| oneweb | 1.39588 | 1.29365 | 1.00000 | 1.00908 | 1.00000 | 1.20613 | 1.13868 | 1.00000 | 1.20613 | 1.13868 |
| kuiper | 1.22697 | 1.23891 | 1.00000 | 1.01999 | 1.00000 | 1.21071 | 1.18236 | 1.00000 | 1.21071 | 1.18236 |
| starlink | 1.45425 | 1.35045 | 1.00000 | 1.02915 | 1.00000 | 1.44653 | 1.32465 | 1.00000 | 1.44653 | 1.32465 |

### Non-optimal egress, % of delivered pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 78.6% | 73.9% | 0.0% | 14.4% | 0.0% | 78.6% | 73.1% | 0.1% | 78.6% | 73.1% |
| oneweb | 98.8% | 87.6% | 0.0% | 24.8% | 0.0% | 98.8% | 87.0% | 0.1% | 98.8% | 87.0% |
| kuiper | 95.1% | 71.3% | 0.0% | 26.8% | 0.0% | 95.1% | 71.0% | 0.1% | 95.1% | 71.0% |
| starlink | 95.6% | 71.8% | 0.0% | 27.5% | 0.0% | 95.6% | 71.2% | 0.0% | 95.6% | 71.2% |

### Installed forwarding entries per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| oneweb | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| kuiper | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| starlink | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |

### Unreachable-destination markers per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| oneweb | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| kuiper | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| starlink | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Analytical forwarding-state proxy per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 4.5 | 4.5 | 6.0 | 6.0 | 351.0 | 351.0 | 351.0 | 4.5 | 4.5 | 4.5 |
| oneweb | 4.5 | 4.5 | 5.4 | 5.4 | 588.0 | 588.0 | 588.0 | 4.5 | 4.5 | 4.5 |
| kuiper | 4.3 | 4.3 | 4.8 | 4.8 | 1,156.0 | 1,156.0 | 1,156.0 | 4.3 | 4.3 | 4.3 |
| starlink | 4.2 | 4.2 | 4.6 | 4.6 | 1,584.0 | 1,584.0 | 1,584.0 | 4.2 | 4.2 | 4.2 |

### Forwarding-state updates per satellite per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.03 | 0.05 | 1.22 | 1.17 | 14.52 | 9.36 | 14.67 | 0.05 | 0.03 | 0.05 |
| oneweb | 0.04 | 0.04 | 1.10 | 0.99 | 20.07 | 19.57 | 20.44 | 0.04 | 0.04 | 0.04 |
| kuiper | 0.02 | 0.03 | 0.77 | 0.75 | 32.45 | 20.84 | 32.79 | 0.03 | 0.02 | 0.03 |
| starlink | 0.02 | 0.02 | 0.63 | 0.61 | 37.51 | 31.14 | 37.72 | 0.02 | 0.02 | 0.02 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 599 | 1,126 | 2,510 | 1,090 | 1,648 | 1,897 | 1,211 | 1,632 | 1,980 | 1,586 |
| oneweb | 1,115 | 2,178 | 7,767 | 2,906 | 4,963 | 5,715 | 3,788 | 9,284 | 4,537 | 3,160 |
| kuiper | 2,031 | 3,084 | 12,334 | 5,298 | 21,765 | 23,254 | 16,679 | 17,828 | 7,129 | 6,012 |
| starlink | 2,819 | 4,223 | 17,650 | 9,060 | 47,335 | 45,906 | 29,036 | 21,209 | 12,378 | 6,854 |

## grid_seam

### Deliverable pairs per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| oneweb | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| kuiper | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |
| starlink | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 | 552.0 |

### Delivery rate, % of deliverable pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| oneweb | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| kuiper | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| starlink | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 1.36626 | 1.50159 | 1.00000 | 1.02421 | 1.00000 | 1.31818 | 1.25948 | 1.00009 | 1.31818 | 1.25948 |
| oneweb | 1.39588 | 1.29365 | 1.00000 | 1.00908 | 1.00000 | 1.20613 | 1.13868 | 1.00000 | 1.20613 | 1.13868 |
| kuiper | 1.44027 | 1.54788 | 1.00000 | 1.02078 | 1.00000 | 1.31374 | 1.28060 | 1.00000 | 1.31374 | 1.28060 |
| starlink | 1.69697 | 1.75365 | 1.00000 | 1.03302 | 1.00000 | 1.62904 | 1.46927 | 1.00000 | 1.62904 | 1.46927 |

### Non-optimal egress, % of delivered pairs

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 78.8% | 72.9% | 0.0% | 13.8% | 0.0% | 78.8% | 71.0% | 0.1% | 78.8% | 71.0% |
| oneweb | 98.8% | 87.6% | 0.0% | 24.8% | 0.0% | 98.8% | 87.0% | 0.1% | 98.8% | 87.0% |
| kuiper | 95.4% | 72.3% | 0.0% | 25.6% | 0.0% | 95.4% | 70.1% | 0.1% | 95.4% | 70.1% |
| starlink | 95.7% | 72.8% | 0.0% | 27.1% | 0.0% | 95.7% | 71.2% | 0.1% | 95.7% | 71.2% |

### Installed forwarding entries per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| oneweb | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| kuiper | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |
| starlink | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 | 24.0 |

### Unreachable-destination markers per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| oneweb | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| kuiper | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| starlink | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Analytical forwarding-state proxy per satellite

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 4.4 | 4.4 | 5.9 | 5.9 | 351.0 | 351.0 | 351.0 | 4.4 | 4.4 | 4.4 |
| oneweb | 4.5 | 4.5 | 5.4 | 5.4 | 588.0 | 588.0 | 588.0 | 4.5 | 4.5 | 4.5 |
| kuiper | 4.3 | 4.3 | 4.7 | 4.7 | 1,156.0 | 1,156.0 | 1,156.0 | 4.3 | 4.3 | 4.3 |
| starlink | 4.2 | 4.2 | 4.6 | 4.6 | 1,584.0 | 1,584.0 | 1,584.0 | 4.2 | 4.2 | 4.2 |

### Forwarding-state updates per satellite per snapshot

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 0.03 | 0.05 | 1.22 | 1.17 | 14.44 | 9.36 | 14.53 | 0.05 | 0.03 | 0.05 |
| oneweb | 0.04 | 0.04 | 1.10 | 0.99 | 20.07 | 19.57 | 20.44 | 0.04 | 0.04 | 0.04 |
| kuiper | 0.02 | 0.03 | 0.77 | 0.75 | 32.41 | 20.85 | 32.73 | 0.03 | 0.02 | 0.03 |
| starlink | 0.02 | 0.02 | 0.63 | 0.61 | 37.50 | 31.13 | 37.71 | 0.02 | 0.02 | 0.02 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | dra_scheme_asc | dra_scheme_req | explicit_r1 | explicit_r3 | link_state | link_state_dir_asc | link_state_dir_half_req | topological_derived | topological_scheme_asc | topological_scheme_req |
|---|---|---|---|---|---|---|---|---|---|---|
| telesat | 629 | 1,283 | 2,022 | 1,107 | 994 | 1,495 | 1,356 | 1,118 | 1,315 | 1,548 |
| oneweb | 1,117 | 2,104 | 7,395 | 2,478 | 4,791 | 4,722 | 3,606 | 9,273 | 3,423 | 3,385 |
| kuiper | 2,170 | 3,411 | 12,479 | 6,015 | 22,999 | 21,892 | 16,563 | 16,719 | 6,969 | 6,734 |
| starlink | 3,100 | 4,269 | 19,760 | 9,669 | 46,882 | 48,721 | 29,479 | 21,407 | 11,474 | 7,265 |
