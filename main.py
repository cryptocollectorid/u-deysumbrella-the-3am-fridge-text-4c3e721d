#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

A fridge that has been awake all night, watching its owner open the door
again and again without taking anything, finally decides this is the
moment to speak — with an opinion, and no shame about sharing it at 3am.
"""
import os

ENTRY = "It's 3am. You've opened me four times and taken nothing. I'm a fridge, not a therapist. Go to bed."

# Gate: /output/entry.txt must be 1-140 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
