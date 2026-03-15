from src.notebook.models import Note


def search_notes(notes: list[Note], query: str) -> list[Note]:
    """
    Return a list of notes whose title or text contains the given query,
    performing a case‑insensitive match.

    The function safely handles notes where ``title`` or ``text`` might be
    ``None`` by treating them as empty strings.
    """
    result: list[Note] = []
    lowered_query = query.lower()

    for note in notes:
        title = note.title or ""
        text = note.text or ""
        if lowered_query in title.lower() or lowered_query in text.lower():
            result.append(note)

    return result


def filter_by_tag(notes: list[Note], tag: str) -> list[Note]:
    return [note for note in notes if tag in note.tags]
