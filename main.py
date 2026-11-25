"""Worst Superpower entry: write the one-line entry to /output/entry.txt.

Stdlib only, deterministic, no network, reads no other files.
"""

import os

ENTRY = "I can summon rain: exactly one drop, onto my own forehead, once a day, indoors \u2014 where it changes nothing."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(text):
    """Ensure the entry is a single non-blank line of 1-140 characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return True


def main():
    validate_line(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: read back what was written and re-validate it.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    validate_line(written)


if __name__ == "__main__":
    main()
