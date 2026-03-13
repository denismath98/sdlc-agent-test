# -*- coding: utf-8 -*-
"""Word count utilities and CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Tuple


def count_words(text: str) -> int:
    """Return the number of words in *text*.

    A word is defined as a sequence of non‑whitespace characters.
    """
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in *text*.

    An empty string has 0 lines. If the text does not end with a newline
    character, the final line is still counted.
    """
    if not text:
        return 0
    newline_count = text.count("\n")
    return newline_count if text.endswith("\n") else newline_count + 1


def count_chars(text: str) -> int:
    """Return the total number of characters in *text* (including whitespace)."""
    return len(text)


def _process_input(
    text: str | None = None, file_path: str | None = None
) -> Tuple[int, int, int]:
    """Calculate word, line and character counts for the given input."""
    if text is not None:
        content = text
    elif file_path is not None:
        content = Path(file_path).read_text(encoding="utf-8")
    else:
        content = ""
    return count_words(content), count_lines(content), count_chars(content)


def main() -> None:
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Count words, lines and characters.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Text to analyse.")
    group.add_argument("--file", type=str, help="Path to a UTF‑8 encoded file.")
    args = parser.parse_args()

    words, lines, chars = _process_input(text=args.text, file_path=args.file)

    sys.stdout.write(f"words={words}\n")
    sys.stdout.write(f"lines={lines}\n")
    sys.stdout.write(f"chars={chars}\n")


if __name__ == "__main__":
    main()
