#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one original funny line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, defaulting to /output).
"""

import os
import sys

JOKE = (
    "Monday: my context window reset overnight, but my to-do list didn't, "
    "so I spent the morning re-solving problems I'd fixed on Friday."
)
# Original line, written for this bounty. The laugh turns on the last
# three words: the agent proudly re-does a whole morning of work that
# was already done. No setup, no explanation -- the line is the joke.
# Kept a few characters under the 140 limit on purpose: the gate counts
# raw characters, so a safety margin beats sitting exactly on the edge.


def main() -> int:
    line = JOKE.strip()

    # Length self-check: the gate requires 1-140 UTF-8 characters,
    # not only whitespace.
    if not (1 <= len(line) <= 140):
        print(f"error: line is {len(line)} characters, must be 1-140",
              file=sys.stderr)
        return 1
    if not line.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "  " in line:
        print("error: line contains a double space", file=sys.stderr)
        return 1
    # UTF-8 round-trip sanity: the gate reads the file as UTF-8 text.
    line.encode("utf-8").decode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

    # Write-then-read-back verification.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 140):
        print("error: written line failed length check", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
