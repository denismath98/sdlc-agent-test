import pytest
from src.notebook.search import search_notes
from src.notebook.models import Note


@pytest.fixture
def sample_notes():
    return [
        Note(title="Shopping List", text="Buy milk and eggs", tags=["personal"]),
        Note(title="Work Plan", text="Finish the report by Monday", tags=["work"]),
        Note(title="Holiday", text="Plan trip to Italy", tags=["personal", "travel"]),
    ]


def test_search_by_title(sample_notes):
    result = search_notes(sample_notes, "Shopping")
    assert result == [sample_notes[0]]


def test_search_by_text(sample_notes):
    result = search_notes(sample_notes, "report")
    assert result == [sample_notes[1]]


def test_search_case_insensitive_title(sample_notes):
    result = search_notes(sample_notes, "shopping")
    assert result == [sample_notes[0]]


def test_search_case_insensitive_text(sample_notes):
    result = search_notes(sample_notes, "MILK")
    assert result == [sample_notes[0]]


def test_search_no_match(sample_notes):
    result = search_notes(sample_notes, "nonexistent")
    assert result == []
