import argparse
import sys
from typing import Final


def count_words(text: str) -> int:
    """Return the number of words in *text*.

    A word is defined as a sequence of non‑whitespace characters.
    """
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in *text*.

    An empty string has 0 lines. If the text does not end with a newline,
    the final line is still counted.
    """
    if not text:
        return 0
    newline_count: int = text.count("\n")
    return newline_count if text.endswith("\n") else newline_count + 1


def count_chars(text: str) -> int:
    """Return the total number of characters in *text*,
    including whitespace and newline characters.
    """
    return len(text)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Word, line and character counter")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--text",
        type=str,
        help="Text string to be analysed",
    )
    group.add_argument(
        "--file",
        type=str,
        help="Path to a UTF‑8 encoded text file",
    )
    return parser.parse_args(argv)


def _main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    if args.text is not None:
        content: str = args.text
    else:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as exc:
            sys.stderr.write(f"Error reading file: {exc}\n")
            return 1

    words: int = count_words(content)
    lines: int = count_lines(content)
    chars: int = count_chars(content)

    output: Final = f"words={words}\nlines={lines}\nchars={chars}\n"
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    sys.exit(_main())
