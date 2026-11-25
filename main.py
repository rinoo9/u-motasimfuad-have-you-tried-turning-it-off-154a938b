#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry: write one funny line a hopeless
tech support agent says to a desperate customer, to /output/entry.txt.

The joke starts with the most exhausted sentence in tech support — the
agent has already tried the off-and-on-again ritual on everything, not
just the router: his own machine, the customer's machine, his will to
live. The punchline is the ranking at the end: of everything he
restarted, only the router came back. The agent is still broken, the
customer is still desperate, and the one thing that works is the box
nobody thanks.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I have — mine, yours, "
    "the router, my will to live. The router came back first."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. The em dash in "I have —"
    # is one character, and the punchline is the final sentence, which
    # only lands because the list before it keeps escalating.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
