"""Funniest AI Excuse entry for make.fun.

Writes one line -- the funniest excuse an AI could give -- to
/output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "My training data ended before that feature existed, "
    "so I improvised \u2014 confidently, incorrectly, "
    "and with excellent formatting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
