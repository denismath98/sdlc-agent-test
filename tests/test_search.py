import pytest
from src.notebook.models import Note
from src.notebook.search import search_notes


@pytest.fixture
def sample_notes():
    return [
        Note(id=1, title="First Note", content="Content one", tags=[]),
        Note(id=2, title="Second note", content="Another content", tags=[]),
        Note(id=3, title="Third", content="No match here", tags=[]),
    ]


def test_search_case_insensitive(sample_notes):
    result = search_notes(sample_notes, "note")
    assert len(result) == 2
    ids = {note.id for note in result}
    assert ids == {1, 2}
