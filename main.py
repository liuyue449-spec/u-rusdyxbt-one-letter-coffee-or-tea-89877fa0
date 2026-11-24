# One Letter: Coffee or Tea — entry program.
#
# Writes exactly one letter to /output/entry.txt. The letter is fixed in
# this file: no network, no clock, no randomness, nothing read from outside
# the repository, so every run produces the same bytes.
#
# The letter: A — coffee.
# Picked against the judge's brief, which weighs vividness first, then
# humour, then truth: coffee is the bolder, more alive stance of the two —
# dark, hot, aromatic, the drink that wakes you up — where tea is the
# quieter, calmer one. A single "A" lands as the fuller, more vivid answer
# for the drink it names, and it stands on its own with nothing beside it.
# The gate allows exactly 1 character, so the entry is the letter alone,
# no newline, no punctuation, no explanation.

import os

# The single letter this entry sends. A = coffee, B = tea.
LETTER = "A"

# Where the grader reads the entry. The rules name /output/entry.txt;
# honour MAKEFUN_OUTPUT_DIR (a directory) or OUTPUT_PATH (a full path)
# when set, so local runs can point the output elsewhere without
# touching the code. Default is the path the rules name.
def output_path() -> str:
    override = os.environ.get("OUTPUT_PATH", "").strip()
    if override:
        return override
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    # Gate self-check, mirroring the sealed scorer: exactly 1 character,
    # and not only white space.
    if len(LETTER) != 1 or LETTER.isspace():
        raise SystemExit("entry must be exactly one non-whitespace letter")

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Read back and confirm the bytes on disk are the letter, nothing else.
    with open(path, "rb") as f:
        data = f.read()
    if data != LETTER.encode("utf-8"):
        raise SystemExit(f"read-back mismatch: {data!r} != {LETTER!r}")


if __name__ == "__main__":
    main()
