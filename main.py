#!/usr/bin/env python3
"""Entry for make.fun bounty: Name the Robot Band.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    # The em dash separates the band name from the hit-song line;
    # the whole line is 111 characters, well under the 200 limit.
    'Rust Never Sleeps (It Just Updates) \u2014 their hit '
    '"Firmware Update (Do Not Turn Off)" bricked the venue\'s lights.'
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
