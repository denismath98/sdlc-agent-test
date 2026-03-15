from typing import List
from .models import Note


def search_notes(notes: List[Note], query: str) -> List[Note]:
    """Return notes where the query appears in the note content, case‑insensitive."""
    lowered_query = query.lower()
    result: List[Note] = []
    for note in notes:
        if lowered_query in note.content.lower():
            result.append(note)
    return result


def filter_by_tag(notes: List[Note], tag: str) -> List[Note]:
    """Return notes that contain the exact tag (case‑sensitive)."""
    result: List[Note] = []
    for note in notes:
        if tag in note.tags:
            result.append(note)
    return result
