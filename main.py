"""Angry Judge: The Short Rant Contest — one-liner entry.

Writes exactly one short rant to /output/entry.txt.

Approach: one concrete annoyance (the office printer), a second beat
(the LOW TONER warning printed in perfect ink), and one concrete
number ($89 for eleven pages) — no throat-clearing, no list.
"""

from pathlib import Path

ENTRY = (
    "The office printer has one job and it refuses to do it. "
    "It jams on page seven of eight, spits out a blank page like that is a favour, "
    "then flashes LOW TONER in perfect, crisp black ink. "
    "It is not out of toner. It is out of respect. "
    "I spent $89 on a cartridge that lasted eleven pages, "
    "and the printer still looks at me like I am the problem. "
    "Fire it. Hire a pen."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 400


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the entry text — no trailing newline, no extra lines.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
