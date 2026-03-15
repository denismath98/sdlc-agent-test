from src.notebook.models import Note


def search_notes(notes: list[Note], query: str) -> list[Note]:
    """
    Search notes by title or text in a case‑insensitive manner.

    The function lower‑cases both the query and the note fields before
    performing the containment check, ensuring that matches are found
    regardless of the original letter case.
    """
    result: list[Note] = []
    query_lower = query.lower()

    for note in notes:
        if query_lower in note.title.lower() or query_lower in note.text.lower():
            result.append(note)

    return result


def filter_by_tag(notes: list[Note], tag: str) -> list[Note]:
    return [note for note in notes if tag in note.tags]
