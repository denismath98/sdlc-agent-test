from src.notebook.models import Note
from typing import List


def search_notes(notes: list[Note], query: str) -> list[Note]:
    result: list[Note] = []

    for note in notes:
        if query in note.title or query in note.text:
            result.append(note)

    return result


def filter_by_tag(notes: list[Note], tag: str) -> list[Note]:
    return [note for note in notes if tag in note.tags]


def find_by_exact_title(notes: List[Note], title: str) -> List[Note]:
    """Return a list of notes whose title matches exactly the given title (case‑sensitive)."""
    result: List[Note] = []
    for note in notes:
        if isinstance(note, Note) and note.title == title:
            result.append(note)
    return result


__all__ = ["search_notes", "filter_by_tag", "find_by_exact_title"]
