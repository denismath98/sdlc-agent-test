import subprocess
import sys
from pathlib import Path

import pytest

from src.wordcount import count_chars, count_lines, count_words


@pytest.mark.parametrize(
    "text,exp_words,exp_lines,exp_chars",
    [
        ("", 0, 0, 0),
        (" hello world ", 2, 1, 17),
        ("line1\nline2\n", 2, 2, 12),
        ("one\n", 1, 1, 4),
        ("one", 1, 1, 3),
        ("\n\n", 0, 2, 2),
    ],
)
def test_counts(text, exp_words, exp_lines, exp_chars):
    assert count_words(text) == exp_words
    assert count_lines(text) == exp_lines
    assert count_chars(text) == exp_chars


def run_cli(args):
    result = subprocess.run(
        [sys.executable, "-m", "src.wordcount"] + args,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", "words=0\nlines=0\nchars=0\n"),
        (" hello world ", "words=2\nlines=1\nchars=17\n"),
        ("line1\nline2\n", "words=2\nlines=2\nchars=12\n"),
        ("one\n", "words=1\nlines=1\nchars=4\n"),
        ("one", "words=1\nlines=1\nchars=3\n"),
        ("\n\n", "words=0\nlines=2\nchars=2\n"),
    ],
)
def test_cli_text_argument(text, expected):
    output = run_cli(["--text", text])
    assert output == expected


def test_cli_file_argument(tmp_path: Path):
    content = "hello world\nnew line"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content, encoding="utf-8")
    expected = "words=3\nlines=2\nchars=23\n"
    output = run_cli(["--file", str(file_path)])
    assert output == expected
