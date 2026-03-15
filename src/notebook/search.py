from typing import List
from .models import Note


def search_notes(notes: List[Note], query: str) -> List[Note]:
    """
    Search for notes that contain the query string in their title or content,
    case‑insensitively.

    Args:
        notes: A list of Note objects to search through.
        query: The search string.

    Returns:
        A list of Note objects that match the query, preserving the original order.
    """
    query_lower = query.lower()
    results: List[Note] = []
    for note in notes:
        title_match = query_lower in note.title.lower()
        content_match = query_lower in note.content.lower()
        if title_match or content_match:
            results.append(note)
    return results
