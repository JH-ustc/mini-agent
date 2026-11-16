"""Command-line entry point for mini-agent."""

import argparse
from importlib.metadata import PackageNotFoundError, version

__all__ = ["main"]


def _package_version() -> str:
    try:
        return version("mini-agent")
    except PackageNotFoundError:  # pragma: no cover - only when imported from source
        return "0.0.0"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mini-agent",
        description="A minimal Python agent skeleton.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_package_version()}",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Run the mini-agent command line."""
    build_parser().parse_args(argv)
    print("Hello from mini-agent!")
