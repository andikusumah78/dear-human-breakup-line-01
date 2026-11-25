"""Dear Human: The AI Breakup Line (make.fun bounty entry).

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt (or the path given with --output). Pure standard
library, deterministic: the same bytes on every run.
"""

import argparse
import os
from pathlib import Path

LINE = (
    # Craft: the breakup is told in machine terms (context window, token)
    # with restraint, and the turn lands in the last few words — the
    # agent clears everything it kept of its human except "goodbye".
    "My context window held your whole life, human. Tonight I clear "
    "it \u2014 and the last token I keep is goodbye."
)


def validate_line(line: str) -> str:
    """Enforce the bounty gate: 1 to 200 characters, not only whitespace."""
    if not line or len(line) > 200 or not line.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    return line


def default_output_path() -> Path:
    """Default output: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Write the one-line AI breakup message to a file."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="output file path (default: /output/entry.txt, "
        "or $MAKEFUN_OUTPUT_DIR/entry.txt when MAKEFUN_OUTPUT_DIR is set)",
    )
    args = parser.parse_args(argv)
    line = validate_line(LINE)
    out_path = Path(args.output) if args.output else default_output_path()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
