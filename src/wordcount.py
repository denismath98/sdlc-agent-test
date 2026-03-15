import argparse
import sys


def count_words(text: str) -> int:
    if not text:
        return 0
    return len(text.split())


def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.split("\n"))


def count_chars(text: str) -> int:
    return len(text)


def _run_cli():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument("--text", required=True, help="Input text")
    args = parser.parse_args()
    text = args.text
    words = count_words(text)
    lines = count_lines(text)
    chars = count_chars(text)
    print(f"words={words}")
    print(f"lines={lines}")
    print(f"chars={chars}")


if __name__ == "__main__":
    _run_cli()
