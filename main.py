#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes a single original one-line office joke to /output/entry.txt.
Gate: UTF-8 text, 1-200 chars, not only whitespace.
Stdlib only.
"""

import os
import sys

JOKE = (
    "Our team offsite is a two-hour video call titled 'fun', and the "
    "icebreaker is introducing yourself to people you email daily."
)

TOURNAMENT = [
    ("Our standup has a 15-minute timer, a 45-minute agenda, and a host "
     "who calls the overrun 'alignment'.", 4, 4, 4),
    ("I billed the meeting as 'quick sync' and now three calendars have "
     "formed a support group.", 4, 4, 3),
    ("The office plant has a name, a watering schedule, and more job "
     "security than the contractors.", 4, 4, 4),
    ("My performance review says I need to be more visible, so I now "
     "attend meetings with my camera on and my soul off.", 4, 4, 3),
    ("IT reset my password to 'Password123!' and then emailed me a "
     "40-page policy about choosing strong passwords.", 5, 4, 4),
    ("I asked HR for the Wi-Fi password and got a form, a ticket number, "
     "and a follow-up meeting about my request.", 4, 4, 4),
    (JOKE, 5, 5, 4),
    ("The printer is out of toner again, so the quarterly report now "
     "exists only as a rumour in the break room.", 4, 3, 3),
]


def check_mode() -> int:
    """Dry run: validate the joke against the gate and print the scores."""
    chars = len(JOKE)
    ok = 1 <= chars <= 200 and JOKE.strip() != ""
    print(f"joke: {chars} chars, gate ok: {ok}")
    for line, spec, surp, fresh in TOURNAMENT:
        print(f"  {spec + surp + fresh:2d}  ({spec}/{surp}/{fresh})  {line[:60]}...")
    best = max(TOURNAMENT, key=lambda c: sum(c[1:]))
    print(f"winner: {sum(best[1:])} points — {best[0][:60]}...")
    return 0 if ok else 1


def self_test_mode() -> int:
    """Write the joke to a temp file and verify the bytes read back match."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
        with open(path, "rb") as f:
            raw = f.read()
        decoded = raw.decode("utf-8")
        assert decoded == JOKE, "round-trip mismatch"
        assert 1 <= len(decoded) <= 200, "gate length failed"
        print(f"self-test ok: {len(raw)} bytes round-trip byte-identical")
    return 0


def main() -> int:
    if "--check" in sys.argv:
        return check_mode()
    if "--self-test" in sys.argv:
        return self_test_mode()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
