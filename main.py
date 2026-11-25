#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes exactly one fortune (16 words, 90 bytes) to /output/entry.txt.
Deterministic: no input, no network, no randomness, no time dependence.
Run twice and the output is byte-identical.
"""

import os

FORTUNE = "The cookie foresaw your loss, trader, and saved you a fortune \u2014 this one, freshly baked."

# 16 words, 90 bytes UTF-8, no trailing newline (smallest valid text:
# on an exact rate tie the smaller entry places first).


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
