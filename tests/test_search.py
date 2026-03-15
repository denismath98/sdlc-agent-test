import pytest

from src.notebook.search import search_notes


def test_search_basic():
    notes = ["Hello world", "Goodbye"]
    assert search_notes(notes, "Hello") == ["Hello world"]
    assert search_notes(notes, "good") == ["Goodbye"]


def test_search_case_insensitive():
    notes = ["Python", "java", "C++"]
    assert search_notes(notes, "PYTHON") == ["Python"]
    assert search_notes(notes, "JaVa") == ["java"]
    assert search_notes(notes, "c++") == ["C++"]


def test_search_non_string_notes():
    notes = ["Number 1", 123, "Another"]
    assert search_notes(notes, "123") == [123]
