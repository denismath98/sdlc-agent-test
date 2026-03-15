import pytest

from src.notebook.search import search_notes


class DummyNote:
    """Simple note-like object used for testing."""

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"DummyNote({self.text!r})"


@pytest.fixture
def sample_notes():
    return [
        DummyNote("First Note"),
        DummyNote("second note"),
        DummyNote("Another Note"),
        DummyNote("MiXeD CaSe"),
    ]


def test_search_case_insensitive_match(sample_notes):
    result = search_notes(sample_notes, "first")
    assert len(result) == 1
    assert result[0].text == "First Note"


def test_search_case_insensitive_different_case(sample_notes):
    result = search_notes(sample_notes, "NOTE")
    # Should match three notes containing the word "note" regardless of case
    matched_texts = {note.text for note in result}
    expected = {"First Note", "second note", "Another Note"}
    assert matched_texts == expected


def test_search_partial_match(sample_notes):
    result = search_notes(sample_notes, "mix")
    assert len(result) == 1
    assert result[0].text == "MiXeD CaSe"


def test_search_no_match(sample_notes):
    result = search_notes(sample_notes, "nonexistent")
    assert result == []


def test_search_empty_query_returns_all(sample_notes):
    # An empty query should match every note (as '' is in any string)
    result = search_notes(sample_notes, "")
    assert set(result) == set(sample_notes)
