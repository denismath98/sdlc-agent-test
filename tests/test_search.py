import pytest
from src.notebook.search import search_notes


def test_search_basic():
    notes = ["Buy milk", "Read book", "Call Alice"]
    assert search_notes(notes, "milk") == ["Buy milk"]
    assert search_notes(notes, "book") == ["Read book"]
    assert search_notes(notes, "call") == ["Call Alice"]
    assert search_notes(notes, "xyz") == []


def test_search_case_insensitive():
    notes = ["First Note", "second note", "Another"]
    assert search_notes(notes, "first") == ["First Note"]
    assert search_notes(notes, "NOTE") == ["First Note", "second note"]
    assert search_notes(notes, "AnOtHeR") == ["Another"]
    assert search_notes(notes, "missing") == []
