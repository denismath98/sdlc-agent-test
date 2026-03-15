from typing import List

from .note import Note


def search_notes(notes: List[Note], query: str) -> List[Note]:
    """
    Return a list of notes where the query appears in the title or text,
    case‑insensitively.
    """
    query_lower = query.lower()
    matched: List[Note] = []
    for note in notes:
        if query_lower in note.title.lower() or query_lower in note.text.lower():
            matched.append(note)
    return matched


def filter_by_tag(notes: List[Note], tag: str) -> List[Note]:
    """
    Return a list of notes that contain the given tag.
    """
    tag_lower = tag.lower()
    filtered: List[Note] = []
    for note in notes:
        if any(t.lower() == tag_lower for t in note.tags):
            filtered.append(note)
    return filtered
