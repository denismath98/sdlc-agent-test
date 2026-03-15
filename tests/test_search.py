import pytest
from src.notebook.search import search_notes


def test_search_found():
    notes = ["First note", "Second note"]
    assert search_notes(notes, "First") == ["First note"]


def test_search_not_found():
    notes = ["First note", "Second note"]
    assert search_notes(notes, "Third") == []


def test_search_case_insensitive():
    notes = ["Hello World", "Another Note"]
    assert search_notes(notes, "hello") == ["Hello World"]
    assert search_notes(notes, "WORLD") == ["Hello World"]
