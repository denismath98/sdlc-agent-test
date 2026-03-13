import pytest
from src.wordcount import count_words, count_lines, count_chars


@pytest.mark.parametrize(
    "text,exp_words,exp_lines,exp_chars",
    [
        ("", 0, 0, 0),
        (" hello world ", 2, 1, 13),
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
