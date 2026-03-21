from src.notebook.models import Note


def search_notes(notes: list[Note], query: str) -> list[Note]:
    result: list[Note] = []

    for note in notes:
        if query in note.title or query in note.text:
            result.append(note)

    return result


def filter_by_tag(notes: list[Note], tag: str) -> list[Note]:
    return [note for note in notes if tag in note.tags]


def find_by_exact_title(notes: list[Note], title: str) -> list[Note]:
    return [note for note in notes if note.title == title]
