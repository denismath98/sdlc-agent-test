import pytest
from src.notebook.models import Note
from src.notebook.search import search_notes, filter_by_tag


def test_search_case_insensitive():
    notes = [
        Note(content="Hello World", tags=[]),
        Note(content="Another note", tags=[]),
        Note(content="HELLO again", tags=[]),
    ]
    result = search_notes(notes, "hello")
    assert len(result) == 2
    assert notes[0] in result
    assert notes[2] in result


def test_search_no_match():
    notes = [Note(content="Test", tags=[])]
    result = search_notes(notes, "absent")
    assert result == []


def test_filter_by_tag_case_sensitive():
    notes = [
        Note(content="Note1", tags=["Tag"]),
        Note(content="Note2", tags=["tag"]),
    ]
    result = filter_by_tag(notes, "Tag")
    assert result == [notes[0]]
    result2 = filter_by_tag(notes, "tag")
    assert result2 == [notes[1]]
