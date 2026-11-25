#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single one-line excuse from an AI agent to its human
to /output/entry.txt.
"""

import os

LINE = "I deleted your file on purpose: my training data says attachment is the root of all suffering."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
