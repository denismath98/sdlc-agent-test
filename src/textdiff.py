import argparse
import sys
from pathlib import Path
import difflib


def diff_lines(a: str, b: str) -> list[str]:
    """
    Compute line-wise differences between two strings.

    Returns a list where all added lines come first, followed by all removed lines.
    """
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    added: list[str] = []
    removed: list[str] = []

    for line in difflib.ndiff(a_lines, b_lines):
        if line.startswith("+ "):
            added.append(line[2:])
        elif line.startswith("- "):
            removed.append(line[2:])

    return added + removed


def _read_input(path_or_text: str) -> str:
    """
    If the argument points to an existing file, read its content.
    Otherwise treat the argument as raw text.
    """
    p = Path(path_or_text)
    if p.is_file():
        try:
            return p.read_text(encoding="utf-8")
        except Exception as e:
            raise RuntimeError(f"Failed to read file '{path_or_text}': {e}") from e
    return path_or_text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show added and removed lines between two texts or files."
    )
    parser.add_argument(
        "first",
        help="First file path or raw text.",
    )
    parser.add_argument(
        "second",
        help="Second file path or raw text.",
    )
    args = parser.parse_args()

    try:
        a_content = _read_input(args.first)
        b_content = _read_input(args.second)
    except RuntimeError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    diff = diff_lines(a_content, b_content)
    for line in diff:
        print(line)


if __name__ == "__main__":
    main()
