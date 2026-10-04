"""Evaluation-matrix tables from runs written in the failure-sweep layout.

The final runs were launched with ``scripts/run-failure-sweep.sh``, which
writes ``<isl>/<constellation>/<condition>/seed<n>/<variant>/``. LEOPath's
``state_accounting_tables`` reads the older matrix layout
``<constellation>/<variant>/<isl>/``. This script links the failure-free,
seed-1 runs of several sweeps into that layout and runs the table module on
it, so every number in the matrix table comes from one command:

    python scripts/matrix_from_sweep.py --leopath ~/phd/LEOPath \
        --sweep Z=final-matrix --sweep Z2=dra-matrix --sweep Z3=real-matrix \
        --pick Z:link_state,link_state_dir_asc,explicit_r1,explicit_r3,topological_derived,topological_scheme_asc \
        --pick Z2:dra_scheme_asc \
        --pick Z3:link_state_dir_half_req,dra_scheme_req,topological_scheme_req \
        --output revision/final_matrix

Each ``--sweep NAME=DIR`` points at a directory holding one sweep per ISL
scenario (``DIR/<isl>/...``); ``--isl`` names the scenarios, ring, grid and
grid_seam by default. The brick-wall table uses ``--isl brick_a brick_b``. Each ``--pick NAME:variants`` says which
variants to take from that sweep; a variant may be picked from one sweep only.
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ISL_SCENARIOS = ("ring", "grid", "grid_seam")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--leopath", type=Path, required=True, help="LEOPath checkout with its .venv")
    parser.add_argument("--sweep", action="append", required=True, metavar="NAME=DIR")
    parser.add_argument("--pick", action="append", required=True, metavar="NAME:VARIANT[,VARIANT]")
    parser.add_argument("--condition", default="none")
    parser.add_argument("--seed", default="seed1")
    parser.add_argument(
        "--isl",
        nargs="+",
        default=list(ISL_SCENARIOS),
        help="ISL wirings to read under each sweep, e.g. brick_a brick_b",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def link_runs(args: argparse.Namespace, layout: Path) -> int:
    sweeps = dict(item.split("=", 1) for item in args.sweep)
    picked: dict[str, str] = {}
    for item in args.pick:
        name, variants = item.split(":", 1)
        if name not in sweeps:
            sys.exit(f"--pick names unknown sweep {name!r}")
        for variant in variants.split(","):
            if variant in picked:
                sys.exit(f"variant {variant!r} picked from both {picked[variant]} and {name}")
            picked[variant] = name

    linked = 0
    for variant, name in sorted(picked.items()):
        root = Path(sweeps[name]).expanduser()
        for isl in args.isl:
            pattern = f"*/{args.condition}/{args.seed}/{variant}/metadata.json"
            runs = sorted((root / isl).glob(pattern))
            if not runs:
                sys.exit(f"no {variant} runs under {root / isl}")
            for metadata in runs:
                constellation = metadata.relative_to(root / isl).parts[0]
                target = layout / constellation / variant / isl
                target.parent.mkdir(parents=True, exist_ok=True)
                os.symlink(metadata.parent.resolve(), target)
                linked += 1
    return linked


def main() -> None:
    args = parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        layout = Path(tmp)
        linked = link_runs(args, layout)
        print(f"linked {linked} runs")
        args.output.mkdir(parents=True, exist_ok=True)
        python = args.leopath / ".venv" / "bin" / "python"
        subprocess.run(
            [
                str(python),
                "-m",
                "leopath.experiments.state_accounting_tables",
                "--input",
                str(layout),
                "--output-dir",
                str(args.output.resolve()),
            ],
            cwd=args.leopath,
            check=True,
        )


if __name__ == "__main__":
    main()
