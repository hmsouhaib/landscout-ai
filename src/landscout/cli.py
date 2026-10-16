"""Local command-line entry point for the cadastre screening slice."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="landscout")
    commands = parser.add_subparsers(dest="command", required=True)
    scan = commands.add_parser("scan", help="Run the cadastral area/shape filters")
    scan.add_argument("--scan", type=Path, required=True)
    scan.add_argument("--cache-dir", type=Path)
    scan.add_argument("--output", type=Path)
    scan.add_argument("--max-cache-age-hours", type=float, default=168.0)
    mode = scan.add_mutually_exclusive_group()
    mode.add_argument(
        "--offline", action="store_true", help="Use a fresh verified cache (default)"
    )
    mode.add_argument(
        "--allow-download",
        action="store_true",
        help="Allow acquisition of the configured commune",
    )
    args = parser.parse_args(argv)

    from landscout.workflows import CadastreScreeningRunError, run_cadastre_screening

    try:
        result = run_cadastre_screening(
            args.scan,
            cache_dir=args.cache_dir,
            output_dir=args.output,
            allow_download=args.allow_download,
            max_cache_age_hours=args.max_cache_age_hours,
        )
    except CadastreScreeningRunError as error:
        print(f"Cadastre screening failed: {error}", file=sys.stderr)
        return 1
    print(
        f"RETAINED_BY_EXECUTED_FILTERS: {result.retained_count}/{result.normalized_count}; "
        f"outputs: {result.output_dir}"
    )
    return 0
