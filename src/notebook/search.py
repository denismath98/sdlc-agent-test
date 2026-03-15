from typing import List
from src.notebook.models import Note


def filter_by_tag(notes: List[Note], tag: str) -> List[Note]:
    """
    Return a list of notes that contain the given tag.
    """
    return [note for note in notes if tag in note.tags]


def search_notes(notes: List[Note], query: str) -> List[Note]:
    """
    Search for notes where the query string appears in the title or text,
    case‑insensitively.

    Args:
        notes: List of Note objects to search.
        query: The search string.

    Returns:
        A list of Note objects that contain the query in either the title
        or the text, ignoring case.
    """
    lowered_query = query.lower()
    matched_notes: List[Note] = []
    for note in notes:
        if lowered_query in note.title.lower() or lowered_query in note.text.lower():
            matched_notes.append(note)
    return matched_notes
