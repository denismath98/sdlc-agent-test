import pytest

from src.notebook.note import Note
from src.notebook.search import search_notes, filter_by_tag


def test_search_case_sensitive():
    notes = [
        Note(title="Shopping List", text="Buy milk and eggs", tags=[]),
        Note(title="Work", text="Finish report", tags=[]),
    ]
    result = search_notes(notes, "Shopping")
    assert len(result) == 1
    assert result[0].title == "Shopping List"


def test_search_case_insensitive():
    notes = [
        Note(title="Hello World", text="This is a Test", tags=[]),
        Note(title="Another Note", text="nothing here", tags=[]),
    ]
    # Query in different case should still match title
    result_title = search_notes(notes, "hello")
    assert len(result_title) == 1
    assert result_title[0].title == "Hello World"

    # Query in different case should still match text
    result_text = search_notes(notes, "TEST")
    assert len(result_text) == 1
    assert result_text[0].title == "Hello World"


def test_filter_by_tag():
    notes = [
        Note(title="Note 1", text="...", tags=["urgent", "home"]),
        Note(title="Note 2", text="...", tags=["work"]),
        Note(title="Note 3", text="...", tags=["Urgent"]),
    ]
    filtered = filter_by_tag(notes, "URGENT")
    assert len(filtered) == 2
    titles = {note.title for note in filtered}
    assert titles == {"Note 1", "Note 3"}
