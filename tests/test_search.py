import pytest
from src.notebook.search import search_notes
from src.notebook.models import Note


def build_notes():
    return [
        Note(id=1, title="First Note", content="Hello World"),
        Note(id=2, title="Second Note", content="Another Content"),
        Note(id=3, title="Third Note", content="hello again"),
        Note(id=4, title="Fourth Note", content="No match here"),
    ]


def test_case_insensitive_search_title():
    notes = build_notes()
    result = search_notes(notes, "first")
    assert len(result) == 1
    assert result[0].id == 1


def test_case_insensitive_search_content():
    notes = build_notes()
    result = search_notes(notes, "HELLO")
    # Should match notes with id 1 and 3 (both contain "hello" in content)
    matched_ids = {note.id for note in result}
    assert matched_ids == {1, 3}
    assert len(result) == 2


def test_multiple_matches():
    notes = build_notes()
    result = search_notes(notes, "note")
    # All notes have "Note" in the title, so all should be returned
    matched_ids = [note.id for note in result]
    assert matched_ids == [1, 2, 3, 4]


def test_no_match():
    notes = build_notes()
    result = search_notes(notes, "nonexistent")
    assert result == []
