#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry: write one funny line a hopeless
tech support agent says to a desperate customer, to /output/entry.txt.

The joke keeps the sacred ritual — turn it off and on again — but the
ritual works too well on the wrong things: the router forgives the agent,
the printer escalates to legal action, and the customer's password turns
out to be the one password every support agent has seen a thousand times.
The punchline lands because the agent fixed everything except the actual
security problem, and he reports it with total professional calm.
"""
import os

LINE = (
    "I turned it off and on again. The router forgave me, the printer "
    "is pressing charges, and your password is still 'password123'."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. The punchline is the final
    # clause, which only lands because the two clauses before it keep
    # escalating from a forgiving router to a litigious printer.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
