"""Main entry point of the app.

Usage:
    python src/main.py dataset     # data/*.csv -> data/emails.json
    python src/main.py features    # data/emails.json -> data/features.csv + results/features.xlsx
    python src/main.py all         # dataset + features (default)

Add new pipeline stages (training, evaluation, ...) as functions here.
"""
import argparse
import sys

import build_dataset
import orchestrator


def run_dataset(extra_args=None):
    saved = sys.argv
    sys.argv = [saved[0]] + (extra_args or [])
    try:
        build_dataset.main()
    finally:
        sys.argv = saved


def run_features():
    orchestrator.run_features()


STAGES = {
    "dataset": run_dataset,
    "features": run_features,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", nargs="?", default="all", choices=[*STAGES, "all"])
    args = ap.parse_args()

    for name in (STAGES if args.stage == "all" else [args.stage]):
        print(f"== {name} ==")
        STAGES[name]()


if __name__ == "__main__":
    main()
