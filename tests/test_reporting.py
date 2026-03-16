from src.notebook.models import Note
from src.reporting.summary import (
    count_notes,
    count_notes_by_tag,
    count_notes_without_tags,
)


def build_notes():
    return [
        Note(id=1, title="A", text="x", tags=["work"]),
        Note(id=2, title="B", text="y", tags=["home"]),
        Note(id=3, title="C", text="z", tags=["work", "draft"]),
        Note(id=4, title="D", text="w", tags=[]),
    ]


def test_count_notes():
    assert count_notes(build_notes()) == 4


def test_count_notes_by_tag():
    result = count_notes_by_tag(build_notes())
    assert result == {"work": 2, "home": 1, "draft": 1}


def test_count_notes_without_tags():
    assert count_notes_without_tags(build_notes()) == 1
