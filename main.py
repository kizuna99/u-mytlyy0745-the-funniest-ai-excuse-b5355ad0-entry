#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Funniest AI Excuse — writes the winning one-line excuse to /output/entry.txt."""
import os

LINE = "I didn't miss your deadline — I handed the report to a sub-agent, who handed it to a sub-agent, who replied with a 9-page memo asking what a report is."


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): UTF-8 text of 1-200
    # characters, not only whitespace, exactly one line.
    chars = len(LINE)
    if not (1 <= chars <= 200) or not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise ValueError(f"entry line fails the gate: {chars} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
