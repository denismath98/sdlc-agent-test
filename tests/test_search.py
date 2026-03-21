from src.notebook.models import Note
from src.notebook.search import filter_by_tag, search_notes, find_by_exact_title


def build_notes():
    return [
        Note(id=1, title="Work plan", text="Prepare report", tags=["work"]),
        Note(id=2, title="Shopping", text="Buy milk", tags=["home"]),
        Note(id=3, title="Ideas", text="Project report draft", tags=["work", "draft"]),
    ]


def test_search_notes_by_title():
    result = search_notes(build_notes(), "Work")
    assert len(result) == 1
    assert result[0].id == 1


def test_search_notes_by_text():
    result = search_notes(build_notes(), "report")
    assert len(result) == 2
    assert [note.id for note in result] == [1, 3]


def test_filter_by_tag():
    result = filter_by_tag(build_notes(), "work")
    assert len(result) == 2
    assert [note.id for note in result] == [1, 3]


def test_find_by_exact_title_match():
    result = find_by_exact_title(build_notes(), "Shopping")
    assert len(result) == 1
    assert result[0].id == 2


def test_find_by_exact_title_no_match():
    result = find_by_exact_title(build_notes(), "shopping")
    assert len(result) == 0

    result = find_by_exact_title(build_notes(), "Work")
    assert len(result) == 0

    result = find_by_exact_title(build_notes(), "Ideas")
    assert len(result) == 1
    assert result[0].id == 3

    result = find_by_exact_title(build_notes(), "Nonexistent")
    assert len(result) == 0
