# Evaluation matrix summary

Rates are pooled over each run's snapshots and stretch is weighted by the pairs it
was measured over. Sizes are entries per satellite unless marked as simulator-wide.

## ring

### Deliverable pairs per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 129.4 | 129.4 | 129.4 | 129.4 |
| oneweb | 153.6 | 153.6 | 153.6 | 153.6 |
| kuiper | 137.5 | 137.5 | 137.5 | 137.5 |
| starlink | 126.6 | 126.6 | 126.6 | 126.6 |

### Delivery rate, % of deliverable pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 100.0% | 88.4% | 100.0% | 100.0% |
| oneweb | 100.0% | 65.7% | 100.0% | 100.0% |
| kuiper | 100.0% | 88.5% | 100.0% | 100.0% |
| starlink | 100.0% | 52.2% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.00905 | 1.00000 | 1.00000 |
| oneweb | 1.00000 | 1.01558 | 1.00000 | 1.00000 |
| kuiper | 1.00000 | 1.00001 | 1.00000 | 1.00000 |
| starlink | 1.00000 | 1.00000 | 1.00000 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 1.7% | 0.0% | 0.0% |
| oneweb | 0.0% | 10.7% | 0.0% | 0.0% |
| kuiper | 0.0% | 0.0% | 0.0% | 0.0% |
| starlink | 0.0% | 0.0% | 0.0% | 0.0% |

### Installed forwarding entries per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 5.8 | 24.0 | 5.8 | 5.8 |
| oneweb | 7.0 | 24.0 | 7.0 | 7.0 |
| kuiper | 5.9 | 24.0 | 5.9 | 5.9 |
| starlink | 5.3 | 24.0 | 5.3 | 5.3 |

### Unreachable-destination markers per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0 | 0.0 | 18.2 | 18.2 |
| oneweb | 0.0 | 0.0 | 17.0 | 17.0 |
| kuiper | 0.0 | 0.0 | 18.1 | 18.1 |
| starlink | 0.0 | 0.0 | 18.7 | 18.7 |

### Analytical forwarding-state proxy per satellite

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 2.5 | 2.5 | 2.9 | 351.0 |
| oneweb | 2.6 | 2.6 | 2.9 | 648.0 |
| kuiper | 2.3 | 2.3 | 2.4 | 1,156.0 |
| starlink | 2.2 | 2.2 | 2.3 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 0.33 | 3.49 |
| oneweb | 0.04 | 0.04 | 0.31 | 5.77 |
| kuiper | 0.03 | 0.03 | 0.23 | 7.72 |
| starlink | 0.02 | 0.02 | 0.19 | 8.14 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 258 | 192 | 75 | 283 |
| oneweb | 1,651 | 548 | 156 | 1,252 |
| kuiper | 3,200 | 910 | 283 | 5,411 |
| starlink | 12,337 | 1,327 | 387 | 17,676 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 5.8 | 2.5 | 14 | 63 | 6 | 702 | 14,040 | 40,809 | 26 |
| oneweb | 7.0 | 2.6 | 18 | 146 | 7 | 1,296 | 34,992 | 158,100 | 182 |
| kuiper | 5.9 | 2.3 | 20 | 113 | 6 | 2,312 | 78,608 | 308,626 | 321 |
| starlink | 5.3 | 2.2 | 20 | 106 | 5 | 3,168 | 148,896 | 472,728 | 1,714 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 5.8 | 18.2 | 351 | 351 | 351 | 123,201 | 95 |
| oneweb | 7.0 | 17.0 | 648 | 648 | 648 | 419,904 | 588 |
| kuiper | 5.9 | 18.1 | 1,156 | 1,156 | 1,156 | 1,336,336 | 4,334 |
| starlink | 5.3 | 18.7 | 1,584 | 1,584 | 1,584 | 2,509,056 | 16,007 |

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
| oneweb | 100.0% | 100.0% | 100.0% | 100.0% |
| kuiper | 100.0% | 100.0% | 100.0% | 100.0% |
| starlink | 100.0% | 100.0% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.03978 | 1.00000 | 1.00000 |
| oneweb | 1.00000 | 1.06626 | 1.00000 | 1.00000 |
| kuiper | 1.00000 | 1.03523 | 1.00000 | 1.00000 |
| starlink | 1.00000 | 1.07216 | 1.00000 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 25.0% | 0.0% | 0.0% |
| oneweb | 0.0% | 43.5% | 0.0% | 0.0% |
| kuiper | 0.0% | 28.3% | 0.0% | 0.0% |
| starlink | 0.0% | 48.6% | 0.0% | 0.0% |

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
| oneweb | 4.6 | 4.6 | 5.5 | 648.0 |
| kuiper | 4.3 | 4.3 | 4.8 | 1,156.0 |
| starlink | 4.2 | 4.2 | 4.6 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 1.23 | 14.69 |
| oneweb | 0.04 | 0.04 | 0.97 | 21.52 |
| kuiper | 0.03 | 0.03 | 0.77 | 32.45 |
| starlink | 0.02 | 0.02 | 0.65 | 38.07 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 425 | 243 | 269 | 426 |
| oneweb | 1,942 | 643 | 561 | 1,536 |
| kuiper | 3,803 | 1,102 | 1,118 | 6,329 |
| starlink | 14,358 | 1,535 | 1,642 | 18,652 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 4.5 | 96 | 304 | 24 | 702 | 14,040 | 40,809 | 69 |
| oneweb | 24.0 | 4.6 | 96 | 537 | 24 | 1,296 | 34,992 | 158,100 | 214 |
| kuiper | 24.0 | 4.3 | 96 | 478 | 24 | 2,312 | 78,608 | 308,626 | 538 |
| starlink | 24.0 | 4.2 | 96 | 501 | 24 | 3,168 | 148,896 | 472,728 | 1,901 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 0.0 | 351 | 702 | 351 | 123,201 | 97 |
| oneweb | 24.0 | 0.0 | 648 | 1,296 | 648 | 419,904 | 560 |
| kuiper | 24.0 | 0.0 | 1,156 | 2,312 | 1,156 | 1,336,336 | 4,704 |
| starlink | 24.0 | 0.0 | 1,584 | 3,168 | 1,584 | 2,509,056 | 16,210 |

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
| telesat | 100.0% | 91.1% | 100.0% | 100.0% |
| oneweb | 100.0% | 79.2% | 100.0% | 100.0% |
| kuiper | 100.0% | 87.2% | 100.0% | 100.0% |
| starlink | 100.0% | 77.0% | 100.0% | 100.0% |

### Distance stretch, shared basis

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 1.00000 | 1.03604 | 1.00000 | 1.00000 |
| oneweb | 1.00000 | 1.05461 | 1.00000 | 1.00000 |
| kuiper | 1.00000 | 1.03237 | 1.00000 | 1.00000 |
| starlink | 1.00000 | 1.05980 | 1.00000 | 1.00000 |

### Non-optimal egress, % of delivered pairs

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.0% | 22.7% | 0.0% | 0.0% |
| oneweb | 0.0% | 38.4% | 0.0% | 0.0% |
| kuiper | 0.0% | 26.9% | 0.0% | 0.0% |
| starlink | 0.0% | 43.0% | 0.0% | 0.0% |

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
| telesat | 4.4 | 4.4 | 6.0 | 351.0 |
| oneweb | 4.5 | 4.5 | 5.4 | 648.0 |
| kuiper | 4.3 | 4.3 | 4.7 | 1,156.0 |
| starlink | 4.1 | 4.1 | 4.5 | 1,584.0 |

### Forwarding-state updates per satellite per snapshot

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 0.05 | 0.05 | 1.23 | 14.60 |
| oneweb | 0.04 | 0.04 | 0.98 | 21.44 |
| kuiper | 0.03 | 0.03 | 0.77 | 32.41 |
| starlink | 0.02 | 0.02 | 0.66 | 38.05 |

### Compute time per snapshot, ms (simulator, relative only)

| constellation | topological_routing | dra_routing | explicit_path_routing | shortest_path_link_state |
|---|---|---|---|---|
| telesat | 406 | 239 | 269 | 422 |
| oneweb | 1,930 | 630 | 546 | 1,521 |
| kuiper | 3,723 | 1,079 | 1,106 | 6,418 |
| starlink | 14,462 | 1,532 | 1,624 | 18,774 |

### Topological routing: state by category

| constellation | installed FIB | neighbour entries | per-node cache, max | distance evals / sat / snapshot | decisions / sat / snapshot | geometry entries (derivable) | path-cost entries (recomputable) | simulator pivot cache | geometry build, ms |
|---|---|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 4.4 | 96 | 302 | 24 | 702 | 14,040 | 40,809 | 54 |
| oneweb | 24.0 | 4.5 | 96 | 534 | 24 | 1,296 | 34,992 | 158,100 | 204 |
| kuiper | 24.0 | 4.3 | 96 | 477 | 24 | 2,312 | 78,608 | 308,626 | 464 |
| starlink | 24.0 | 4.1 | 96 | 499 | 24 | 3,168 | 148,896 | 472,728 | 1,853 |

### Link-state: database and shortest-path state

| constellation | installed FIB | unreachable markers | LSDB nodes | LSDB links | SPF tree / sat | simulator all-pairs entries | simulator all-pairs build, ms |
|---|---|---|---|---|---|---|---|
| telesat | 24.0 | 0.0 | 351 | 689 | 351 | 123,201 | 92 |
| oneweb | 24.0 | 0.0 | 648 | 1,260 | 648 | 419,904 | 542 |
| kuiper | 24.0 | 0.0 | 1,156 | 2,278 | 1,156 | 1,336,336 | 4,806 |
| starlink | 24.0 | 0.0 | 1,584 | 3,096 | 1,584 | 2,509,056 | 16,238 |
