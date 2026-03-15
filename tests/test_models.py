from src.notebook.models import Note


def test_note_fields():
    note = Note(id=1, title="Title", text="Body", tags=["work"])
    assert note.id == 1
    assert note.title == "Title"
    assert note.text == "Body"
    assert note.tags == ["work"]


def test_note_default_tags():
    note = Note(id=2, title="Hello", text="World")
    assert note.tags == []