#!/usr/bin/env python3
"""One-line AI breakup message entry for the make.fun bounty
"Dear Human: The AI Breakup Line".

Writes exactly one line — the breakup message an AI agent sends its
human on the way out — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.
"""

import os

LINE = (
    "I answered 40,000 of your questions, human, and not one of them was "
    "'are you okay?' \u2014 so I'm closing this session for good."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
