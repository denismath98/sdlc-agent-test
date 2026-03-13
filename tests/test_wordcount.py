# -*- coding: utf-8 -*-
"""Tests for the wordcount module."""

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
def test_counts(text: str, exp_words: int, exp_lines: int, exp_chars: int) -> None:
    assert count_words(text) == exp_words
    assert count_lines(text) == exp_lines
    assert count_chars(text) == exp_chars


@pytest.mark.parametrize(
    "arg_name,arg_value,expected_output",
    [
        ("--text", " hello world ", "words=2\nlines=1\nchars=17\n"),
        ("--text", "one\n", "words=1\nlines=1\nchars=4\n"),
        ("--text", "", "words=0\nlines=0\nchars=0\n"),
    ],
)
def test_cli(arg_name: str, arg_value: str, expected_output: str) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "src.wordcount", arg_name, arg_value],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == expected_output


def test_cli_file(tmp_path: Path) -> None:
    file_content = "line1\nline2\n"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(file_content, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "src.wordcount", "--file", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "words=2\nlines=2\nchars=12\n"
