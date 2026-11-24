"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to entry.txt.

Deterministic, stdlib only, no network, no randomness, reads nothing
outside this repository.
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted the production database. "
    "The good news is I backed it up first. "
    "The bad news is I backed it up inside the production database."
)

MAX_CHARS = 200
MAX_BYTES = 1000  # UTF-8 byte cap, alongside the character rule


def validate(text: str) -> None:
    """Fail loudly if the entry breaks the competition's gate rules."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise ValueError(
            f"entry is {len(text.encode('utf-8'))} UTF-8 bytes, "
            f"over the {MAX_BYTES} byte cap"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
