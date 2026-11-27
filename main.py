"""The Printer Finally Answers.

A program that writes one line to /output/entry.txt: the office
printer's comeback to everyone staring at it, after one jam too many.
"""

import os

LINE = (
    "My tray holds 250 sheets. You loaded 251 at 4:47 PM. "
    "I counted them twice. One of them is now inside me."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"line must be 1-240 characters, got {len(LINE)}")
    if "\u2014" in LINE or LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no em dash")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
