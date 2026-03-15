import pytest
from src.reverse import reverse_string


def test_reverse_normal():
    assert reverse_string("abc") == "cba"


def test_reverse_empty():
    assert reverse_string("") == ""


def test_reverse_single():
    assert reverse_string("a") == "a"
