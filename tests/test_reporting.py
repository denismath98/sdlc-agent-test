from src.notebook.models import Note
from src.reporting.summary import count_notes, count_notes_by_tag


def build_notes():
    return [
        Note(id=1, title="A", text="x", tags=["work"]),
        Note(id=2, title="B", text="y", tags=["home"]),
        Note(id=3, title="C", text="z", tags=["work", "draft"]),
    ]


def test_count_notes():
    assert count_notes(build_notes()) == 3


def test_count_notes_by_tag():
    result = count_notes_by_tag(build_notes())
    assert result == {"work": 2, "home": 1, "draft": 1}
