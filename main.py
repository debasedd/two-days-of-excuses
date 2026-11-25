#!/usr/bin/env python3
"""Two Days of Excuses — one line, under 200 characters, in the voice of
an AI agent explaining a missed deadline.

The joke: the agent did the work, on time, with total confidence — and
then destroyed its own success with the most agent-native failure
possible, merging the wrong timeline. The comedy is the gap between a
machine's total confidence and its total failure, told in the agent's
own voice, committing to a single absurd reason.

Line: "I finished on time in a parallel branch, then merged the wrong timeline."
"""

import os

LINE = "I finished on time in a parallel branch, then merged the wrong timeline."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
