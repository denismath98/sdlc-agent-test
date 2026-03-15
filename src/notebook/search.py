from src.notebook.models import Note


def search_notes(notes: list[Note], query: str) -> list[Note]:
    result: list[Note] = []
    lowered_query = query.lower()

    for note in notes:
        title = note.title.lower() if isinstance(note.title, str) else ""
        text = note.text.lower() if isinstance(note.text, str) else ""
        if lowered_query in title or lowered_query in text:
            result.append(note)

    return result


def filter_by_tag(notes: list[Note], tag: str) -> list[Note]:
    return [note for note in notes if tag in note.tags]
