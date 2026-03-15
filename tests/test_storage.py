import json

from src.notebook.models import Note
from src.notebook.storage import load_notes, save_notes


def test_load_notes_missing_file(tmp_path):
    path = tmp_path / "notes.json"
    result = load_notes(str(path))
    assert result == []


def test_save_and_load_notes(tmp_path):
    path = tmp_path / "notes.json"
    notes = [
        Note(id=1, title="First", text="Alpha", tags=["work"]),
        Note(id=2, title="Second", text="Beta", tags=["personal"]),
    ]

    save_notes(str(path), notes)
    loaded = load_notes(str(path))

    assert len(loaded) == 2
    assert loaded[0].title == "First"
    assert loaded[1].tags == ["personal"]


def test_save_notes_writes_json(tmp_path):
    path = tmp_path / "notes.json"
    notes = [Note(id=1, title="A", text="B", tags=["x"])]

    save_notes(str(path), notes)

    data = json.loads(path.read_text(encoding="utf-8"))
    assert data[0]["id"] == 1
    assert data[0]["title"] == "A"
    assert data[0]["text"] == "B"
    assert data[0]["tags"] == ["x"]
