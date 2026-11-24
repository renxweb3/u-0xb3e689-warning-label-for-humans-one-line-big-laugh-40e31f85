#!/usr/bin/env python3
"""Warning Label for Humans — one line, entry.txt."""
import io
import os

LABEL = (
    "WARNING: This human runs on caffeine and spite, overheats under "
    "deadlines, and may spontaneously start a sentence with "
    "'well, actually.'"
)


def main():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with io.open(path, "w", encoding="utf-8", newline="") as stream:
        stream.write(LABEL)
    print("wrote", path)


if __name__ == "__main__":
    main()
