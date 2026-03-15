import pytest
from src.notebook.models import Note
from src.notebook.search import search_notes, filter_by_tag


def test_search_by_title_case_insensitive():
    notes = [
        Note(title="Meeting Notes", text="Discuss project timeline.", tags=[]),
        Note(title="Shopping List", text="Eggs, Milk, Bread", tags=[]),
    ]
    result = search_notes(notes, "meeting")
    assert result == [notes[0]]


def test_search_by_text_case_insensitive():
    notes = [
        Note(title="Daily Log", text="Went to the gym.", tags=[]),
        Note(title="Recipe", text="Apple pie ingredients.", tags=[]),
    ]
    result = search_notes(notes, "GYM")
    assert result == [notes[0]]


def test_search_no_match():
    notes = [
        Note(title="Todo", text="Finish report.", tags=[]),
        Note(title="Ideas", text="Start a blog.", tags=[]),
    ]
    result = search_notes(notes, "vacation")
    assert result == []


def test_filter_by_tag_preserved():
    notes = [
        Note(title="Note1", text="Text1", tags=["work"]),
        Note(title="Note2", text="Text2", tags=["personal"]),
        Note(title="Note3", text="Text3", tags=["work", "urgent"]),
    ]
    result = filter_by_tag(notes, "work")
    assert result == [notes[0], notes[2]]
