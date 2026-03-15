from typing import List
from .models import Note


def _get_searchable_text(note: Note) -> str:
    parts: List[str] = []
    if hasattr(note, "title") and isinstance(note.title, str):
        parts.append(note.title)
    if hasattr(note, "text") and isinstance(note.text, str):
        parts.append(note.text)
    return " ".join(parts).lower() if parts else str(note).lower()


def search_notes(notes: List[Note], query: str) -> List[Note]:
    """
    Return a list of notes where the query appears in the title or text,
    case‑insensitively.
    """
    lowered_query = query.lower()
    return [note for note in notes if lowered_query in _get_searchable_text(note)]


def filter_by_tag(notes: List[Note], tag: str) -> List[Note]:
    """
    Return a list of notes that contain the given tag.
    """
    return [note for note in notes if hasattr(note, "tags") and tag in note.tags]
