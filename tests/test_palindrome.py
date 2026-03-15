import pytest
from src.palindrome import is_palindrome


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("level", True),
        ("A man a plan a canal Panama", True),
        ("hello", False),
        ("", True),
        ("   ", True),
        ("No lemon no melon", True),
        ("Was it a car or a cat I saw", True),
        ("Python", False),
    ],
)
def test_is_palindrome(input_text, expected):
    assert is_palindrome(input_text) == expected
