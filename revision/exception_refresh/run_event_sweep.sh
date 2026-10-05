#!/usr/bin/env bash
cd ~/leopath-event
export IMAGE=leopath:event-dev JOBS=38
VARIANT_FILTER="topological_scheme_asc topological_scheme_asc_event" CONDITION_FILTER="void_b2 void_b4 void_b8 cut polar_lat60 polar_lat75" ./scripts/run-failure-sweep.sh $HOME/event-sweep
VARIANT_FILTER="topological_scheme_asc_event" CONDITION_FILTER="sat_p0.005 isl_p0.01" ./scripts/run-failure-sweep.sh $HOME/event-sweep
echo done > $HOME/event-sweep/ALL_DONE
