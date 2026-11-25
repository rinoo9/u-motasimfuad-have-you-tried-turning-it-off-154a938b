#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry: write one funny line a hopeless
tech support agent says to a desperate customer, to /output/entry.txt.

This round the ritual backfires in a new direction: the agent did exactly
what the script says — power-cycled everything — and the network came
back, but the printer responded by filing for divorce and the customer's
password turned out to be the laziest possible word. The joke is that the
agent fixed the connection while the household fell apart, and he reports
the divorce with the same flat tone as the Wi-Fi coming back.
"""
import os

LINE = (
    "I turned it off and on again \u2014 the Wi-Fi came back, the printer "
    "filed for divorce, and your password is still just 'password'."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. The divorce clause is the
    # punchline, and it only works because the first clause sounds like
    # a success story before the second one escalates the printer from
    # a device to a spouse walking out.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
