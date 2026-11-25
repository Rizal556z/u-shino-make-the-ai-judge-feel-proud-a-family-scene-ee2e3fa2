"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, under 280 characters) to
/output/entry.txt, then re-reads the file from disk and verifies it
against the competition gate: 1-280 characters, one or two lines,
not only whitespace, and no leading or trailing whitespace.

Pure Python standard library only.
"""

from pathlib import Path

# The scene: a small Sunday-morning domestic moment — Dad's burnt toast,
# Mum scraping it at the sink, the kids stealing the good slices.
SCENE = (
    "Every Sunday Dad burns the toast on purpose, just so Mum can roll her "
    "eyes and scrape it at the sink while we steal the good slices.\n"
    "He calls it his recipe. We call it love, lightly charred."
)

OUTPUT_PATH = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 280
MAX_LINES = 2


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(SCENE, encoding="utf-8")

    # Re-read from disk and verify the gate on the written bytes.
    raw = OUTPUT_PATH.read_bytes()
    text = raw.decode("utf-8")
    assert MIN_CHARS <= len(text) <= MAX_CHARS, f"char count {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace allowed"
    lines = text.split("\n")
    assert len(lines) <= MAX_LINES, "at most two lines"
    assert all(line.strip() for line in lines), "no blank lines"
    assert not raw.endswith(b"\n"), "no trailing newline"
    print(f"OK: wrote {len(text)} chars, {text.count(chr(10)) + 1} lines")


if __name__ == "__main__":
    main()
