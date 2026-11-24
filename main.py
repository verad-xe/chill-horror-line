#!/usr/bin/env python3
"""Write one original one-line horror story to entry.txt.

The line:

    Every night the footsteps in the attic spell out my name, one letter
    at a time, and tonight they started on yours.

Why this line: the footsteps spelling a name is concrete and vivid, the
slow nightly pace builds dread, and the final turn hands the scare to
the reader -- tonight it is not my name being spelled any more, it is
yours. The scare is earned by what it withholds (who walks, how the
letters are made) and the last word lands the blow.
"""

import os
import re

LINE = (
    "Every night the footsteps in the attic spell out my name, one letter "
    "at a time, and tonight they started on yours."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. The brief adds: a single sentence, one line.
_SENTENCE_END = re.compile(r"[.!?][\"'\"\)\]]*\s+|[.!?][\"'\"\)\]]*$")


def count_sentences(text: str) -> int:
    """Count sentences the way a reader does: a sentence ends at . ! or ?
    (allowing a closing quote after it) followed by whitespace or the end."""
    text = text.strip()
    if not text:
        return 0
    parts = _SENTENCE_END.split(text)
    return len([p for p in parts if p.strip()])


def check_gate(text: str) -> None:
    """Fail loudly if the line would fail the sealed gate scorer."""
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters, gate allows 1-200"
    assert text.strip(), "line must not be only white space"
    assert "\n" not in text.strip(), "line must be a single line"
    n = count_sentences(text)
    assert n == 1, f"line has {n} sentences, brief demands exactly 1"


def main() -> None:
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    written = open(path, encoding="utf-8").read()
    assert written.strip() == LINE, "entry.txt does not hold exactly the line"
    # Gate the file exactly as the scorer reads it, trailing newline included.
    assert 1 <= len(written) <= 200, f"entry.txt is {len(written)} characters, gate allows 1-200"
    assert written.strip(), "entry.txt must not be only white space"
    print(f"wrote {len(LINE)}-character line to {path}")


if __name__ == "__main__":
    main()
