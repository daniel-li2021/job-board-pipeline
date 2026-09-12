#!/usr/bin/env python3
"""Fail the output-commit step before GitHub's 100MB blob hook does."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LIMIT = 90 * 1024 * 1024


def staged_paths() -> list[Path]:
    raw = subprocess.check_output(["git", "diff", "--cached", "--name-only", "-z"])
    return [Path(name.decode()) for name in raw.split(b"\0") if name]


def oversized(paths: list[Path], *, limit: int = LIMIT) -> list[str]:
    too_big: list[str] = []
    for path in paths:
        if path.is_file() and path.stat().st_size >= limit:
            too_big.append(f"{path} ({path.stat().st_size} bytes)")
    return too_big


def main() -> int:
    too_big = oversized(staged_paths())
    if too_big:
        print(
            "Refusing to commit files at or above 90MB; GitHub rejects blobs over 100MB:",
            file=sys.stderr,
        )
        print("\n".join(too_big), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
