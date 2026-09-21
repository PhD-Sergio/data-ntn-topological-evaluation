# Evaluation matrix summary

Rates are pooled over each run's snapshots and stretch is weighted by the pairs it
was measured over. Sizes are entries per satellite unless marked as simulator-wide.

## ring

### Deliverable pairs per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 125.1 | 125.1 | 125.1 | 125.1 |
| oneweb | 155.7 | 155.7 | 155.7 | 155.7 |
| kuiper | 137.5 | 137.5 | 137.5 | 137.5 |
| starlink | 108.2 | 108.2 | 108.2 | 108.2 |

### Delivery rate, % of deliverable pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 100.0% | 89.7% | 96.3% | 100.0% |
| oneweb | 100.0% | 81.2% | 99.5% | 100.0% |
| kuiper | 100.0% | 88.5% | 98.3% | 100.0% |
| starlink | 100.0% | 94.1% | 93.8% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.00736 | 1.03171 | 1.00000 |
| oneweb | 1.00000 | 1.00810 | 1.01052 | 1.00000 |
| kuiper | 1.00000 | 1.00001 | 1.03107 | 1.00000 |
| starlink | 1.00000 | 1.00001 | 1.06283 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 1.2% | 3.8% | 0.0% |
| oneweb | 0.0% | 5.8% | 18.3% | 0.0% |
| kuiper | 0.0% | 0.0% | 14.2% | 0.0% |
| starlink | 0.0% | 0.0% | 3.4% | 0.0% |

### Installed forwarding entries per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 5.6 | 24.0 | 5.5 | 5.6 |
| oneweb | 7.2 | 24.0 | 7.2 | 7.2 |
| kuiper | 5.9 | 24.0 | 5.9 | 5.9 |
| starlink | 4.6 | 24.0 | 4.6 | 4.6 |

### Unreachable-destination markers per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 18.5 | 18.4 |
| oneweb | 0.0 | 0.0 | 16.8 | 16.8 |
| kuiper | 0.0 | 0.0 | 18.1 | 18.1 |
| starlink | 0.0 | 0.0 | 19.4 | 19.4 |

### Analytical forwarding-state proxy per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 2.5 | 2.5 | 2.9 | 351.0 |
| oneweb | 2.7 | 2.7 | 3.0 | 588.0 |
| kuiper | 2.3 | 2.3 | 2.4 | 1,156.0 |
| starlink | 2.2 | 2.2 | 2.3 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 0.31 | 3.36 |
| oneweb | 0.04 | 0.04 | 0.33 | 5.62 |
| kuiper | 0.03 | 0.03 | 0.23 | 7.72 |
| starlink | 0.02 | 0.02 | 0.16 | 7.01 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 528 | 402 | 104 | 522 |
| oneweb | 3,316 | 915 | 218 | 1,619 |
| kuiper | 4,258 | 1,426 | 366 | 7,081 |
| starlink | 4,659 | 1,804 | 381 | 16,544 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 5.6 | 2.5 | 14 | 59 | 6 | 702 | 14,040 | 39,319 | 55 |
| oneweb | 7.2 | 2.7 | 22 | 146 | 7 | 1,176 | 35,868 | 134,270 | 470 |
| kuiper | 5.9 | 2.3 | 20 | 113 | 6 | 2,312 | 78,608 | 308,626 | 416 |
| starlink | 4.6 | 2.2 | 16 | 90 | 5 | 3,168 | 148,896 | 457,153 | 396 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 5.6 | 18.4 | 351 | 351 | 351 | 123,201 | 152 |
| oneweb | 7.2 | 16.8 | 588 | 588 | 588 | 345,744 | 598 |
| kuiper | 5.9 | 18.1 | 1,156 | 1,156 | 1,156 | 1,336,336 | 5,679 |
| starlink | 4.6 | 19.4 | 1,584 | 1,584 | 1,584 | 2,509,056 | 14,847 |

## grid

### Deliverable pairs per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 552.0 | 552.0 | 552.0 | 552.0 |
| oneweb | 552.0 | 552.0 | 552.0 | 552.0 |
| kuiper | 552.0 | 552.0 | 552.0 | 552.0 |
| starlink | 552.0 | 552.0 | 552.0 | 552.0 |

### Delivery rate, % of deliverable pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 100.0% | 100.0% | 100.0% | 100.0% |
| oneweb | 100.0% | 80.2% | 100.0% | 100.0% |
| kuiper | 100.0% | 100.0% | 100.0% | 100.0% |
| starlink | 100.0% | 100.0% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.03871 | 1.02109 | 1.00000 |
| oneweb | 1.00000 | 1.06368 | 1.00908 | 1.00000 |
| kuiper | 1.00000 | 1.03523 | 1.01999 | 1.00000 |
| starlink | 1.00000 | 1.01977 | 1.02915 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 23.2% | 14.4% | 0.0% |
| oneweb | 0.0% | 27.1% | 24.8% | 0.0% |
| kuiper | 0.0% | 28.3% | 26.8% | 0.0% |
| starlink | 0.0% | 17.7% | 27.5% | 0.0% |

### Installed forwarding entries per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 24.0 | 24.0 | 24.0 | 24.0 |
| oneweb | 24.0 | 24.0 | 24.0 | 24.0 |
| kuiper | 24.0 | 24.0 | 24.0 | 24.0 |
| starlink | 24.0 | 24.0 | 24.0 | 24.0 |

### Unreachable-destination markers per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 0.0 | 0.0 |
| oneweb | 0.0 | 0.0 | 0.0 | 0.0 |
| kuiper | 0.0 | 0.0 | 0.0 | 0.0 |
| starlink | 0.0 | 0.0 | 0.0 | 0.0 |

### Analytical forwarding-state proxy per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 4.5 | 4.5 | 6.0 | 351.0 |
| oneweb | 4.5 | 4.5 | 5.4 | 588.0 |
| kuiper | 4.3 | 4.3 | 4.8 | 1,156.0 |
| starlink | 4.2 | 4.2 | 4.6 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 1.17 | 14.52 |
| oneweb | 0.04 | 0.04 | 0.99 | 20.07 |
| kuiper | 0.03 | 0.03 | 0.75 | 32.45 |
| starlink | 0.02 | 0.02 | 0.61 | 37.51 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 872 | 539 | 419 | 896 |
| oneweb | 3,253 | 1,044 | 657 | 2,234 |
| kuiper | 5,304 | 1,579 | 1,184 | 7,903 |
| starlink | 7,051 | 2,232 | 1,521 | 17,458 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 4.5 | 96 | 294 | 24 | 702 | 14,040 | 39,319 | 144 |
| oneweb | 24.0 | 4.5 | 96 | 513 | 24 | 1,176 | 35,868 | 134,270 | 420 |
| kuiper | 24.0 | 4.3 | 96 | 478 | 24 | 2,312 | 78,608 | 308,626 | 687 |
| starlink | 24.0 | 4.2 | 96 | 486 | 24 | 3,168 | 148,896 | 457,153 | 2,183 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 0.0 | 351 | 702 | 351 | 123,201 | 275 |
| oneweb | 24.0 | 0.0 | 588 | 1,127 | 588 | 345,744 | 641 |
| kuiper | 24.0 | 0.0 | 1,156 | 2,312 | 1,156 | 1,336,336 | 5,820 |
| starlink | 24.0 | 0.0 | 1,584 | 3,168 | 1,584 | 2,509,056 | 14,912 |

## grid_seam

### Deliverable pairs per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 552.0 | 552.0 | 552.0 | 552.0 |
| oneweb | 552.0 | 552.0 | 552.0 | 552.0 |
| kuiper | 552.0 | 552.0 | 552.0 | 552.0 |
| starlink | 552.0 | 552.0 | 552.0 | 552.0 |

### Delivery rate, % of deliverable pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 100.0% | 91.0% | 100.0% | 100.0% |
| oneweb | 100.0% | 80.2% | 100.0% | 100.0% |
| kuiper | 100.0% | 87.2% | 100.0% | 100.0% |
| starlink | 100.0% | 89.7% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.03501 | 1.02421 | 1.00000 |
| oneweb | 1.00000 | 1.06368 | 1.00908 | 1.00000 |
| kuiper | 1.00000 | 1.03237 | 1.02078 | 1.00000 |
| starlink | 1.00000 | 1.01824 | 1.03302 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 20.8% | 13.8% | 0.0% |
| oneweb | 0.0% | 27.1% | 24.8% | 0.0% |
| kuiper | 0.0% | 26.9% | 25.6% | 0.0% |
| starlink | 0.0% | 16.7% | 27.1% | 0.0% |

### Installed forwarding entries per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 24.0 | 24.0 | 24.0 | 24.0 |
| oneweb | 24.0 | 24.0 | 24.0 | 24.0 |
| kuiper | 24.0 | 24.0 | 24.0 | 24.0 |
| starlink | 24.0 | 24.0 | 24.0 | 24.0 |

### Unreachable-destination markers per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 0.0 | 0.0 |
| oneweb | 0.0 | 0.0 | 0.0 | 0.0 |
| kuiper | 0.0 | 0.0 | 0.0 | 0.0 |
| starlink | 0.0 | 0.0 | 0.0 | 0.0 |

### Analytical forwarding-state proxy per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 4.4 | 4.4 | 5.9 | 351.0 |
| oneweb | 4.5 | 4.5 | 5.4 | 588.0 |
| kuiper | 4.3 | 4.3 | 4.7 | 1,156.0 |
| starlink | 4.2 | 4.2 | 4.6 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 1.17 | 14.44 |
| oneweb | 0.04 | 0.04 | 0.99 | 20.07 |
| kuiper | 0.03 | 0.03 | 0.75 | 32.41 |
| starlink | 0.02 | 0.02 | 0.61 | 37.50 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 883 | 505 | 408 | 841 |
| oneweb | 3,630 | 1,112 | 703 | 2,080 |
| kuiper | 5,255 | 1,586 | 1,171 | 7,430 |
| starlink | 6,452 | 2,178 | 1,594 | 16,830 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 4.4 | 96 | 292 | 24 | 702 | 14,040 | 39,319 | 122 |
| oneweb | 24.0 | 4.5 | 96 | 513 | 24 | 1,176 | 35,868 | 134,270 | 478 |
| kuiper | 24.0 | 4.3 | 96 | 477 | 24 | 2,312 | 78,608 | 308,626 | 600 |
| starlink | 24.0 | 4.2 | 96 | 486 | 24 | 3,168 | 148,896 | 457,153 | 1,550 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 0.0 | 351 | 689 | 351 | 123,201 | 160 |
| oneweb | 24.0 | 0.0 | 588 | 1,127 | 588 | 345,744 | 584 |
| kuiper | 24.0 | 0.0 | 1,156 | 2,278 | 1,156 | 1,336,336 | 5,409 |
| starlink | 24.0 | 0.0 | 1,584 | 3,146 | 1,584 | 2,509,056 | 14,343 |
