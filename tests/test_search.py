import pytest
from src.notebook.search import search_notes


def test_search_basic():
    notes = ["Note one", "Another note", "Something else"]
    assert search_notes(notes, "Note") == ["Note one", "Another note"]


def test_search_empty_query():
    notes = ["Alpha", "Beta", "Gamma"]
    assert search_notes(notes, "") == ["Alpha", "Beta", "Gamma"]


def test_search_no_match():
    notes = ["Alpha", "Beta", "Gamma"]
    assert search_notes(notes, "Delta") == []


def test_search_case_insensitive():
    notes = ["First Note", "second note", "Third"]
    expected = ["First Note", "second note"]
    assert search_notes(notes, "note") == expected
    assert search_notes(notes, "NOTE") == expected
    assert search_notes(notes, "NoTe") == expected
