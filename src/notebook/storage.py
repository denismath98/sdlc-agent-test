import json
from pathlib import Path

from src.notebook.models import Note


def load_notes(path: str) -> list[Note]:
    file_path = Path(path)
    if not file_path.exists():
        return []

    data = json.loads(file_path.read_text(encoding="utf-8"))
    notes: list[Note] = []

    for item in data:
        notes.append(
            Note(
                id=item["id"],
                title=item["title"],
                text=item["text"],
                tags=item.get("tags", []),
            )
        )

    return notes


def save_notes(path: str, notes: list[Note]) -> None:
    file_path = Path(path)
    data = [
        {
            "id": note.id,
            "title": note.title,
            "text": note.text,
            "tags": note.tags,
        }
        for note in notes
    ]
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )