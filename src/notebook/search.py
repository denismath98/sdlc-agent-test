from typing import List, Any


def search_notes(notes: List[Any], query: str) -> List[Any]:
    """
    Search for notes containing the query string, case‑insensitively.
    The function looks for the query in both the title and content of each note.
    """
    query_lower = query.lower()
    result = []
    for note in notes:
        title = getattr(note, "title", "")
        content = getattr(note, "content", "")
        if query_lower in str(title).lower() or query_lower in str(content).lower():
            result.append(note)
    return result
