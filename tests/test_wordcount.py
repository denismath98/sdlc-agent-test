import subprocess
import sys
import os

import pytest

from src.wordcount import count_words, count_lines, count_chars


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("hello", 1),
        ("hello world", 2),
        ("   multiple   spaces   ", 2),
        ("line1\nline2", 2),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("single line", 1),
        ("first\nsecond", 2),
        ("trailing newline\n", 2),
        ("\nleading newline", 2),
        ("a\nb\nc", 3),
    ],
)
def test_count_lines(text, expected):
    assert count_lines(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("a", 1),
        ("ab cd", 5),
        ("line1\nline2", 11),
        (" spaces ", 8),
    ],
)
def test_count_chars(text, expected):
    assert count_chars(text) == expected


def test_cli_output():
    cmd = [sys.executable, "-m", "src.wordcount", "--text", "hello world"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().splitlines()
    assert output_lines == ["words=2", "lines=1", "chars=11"]
