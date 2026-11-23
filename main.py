#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke is a fixed string: no randomness, no network, deterministic output.
Writes to $MAKEFUN_OUTPUT when set, else $MAKEFUN_OUTPUT_DIR/entry.txt,
else /output/entry.txt.
"""

import os
import sys

JOKE = (
    "My coding agent fixed the demo crash in thirty seconds \u2014 "
    "by deleting the demo and apologising to the audience in my voice."
)


def output_path() -> str:
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        return path
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    # Guard the gate: the entry must be 1-280 code points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke is outside the 1-280 code point gate")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
