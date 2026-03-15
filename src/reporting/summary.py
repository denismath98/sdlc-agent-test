from src.notebook.models import Note


def count_notes(notes: list[Note]) -> int:
    return len(notes)


def count_notes_by_tag(notes: list[Note]) -> dict[str, int]:
    result: dict[str, int] = {}

    for note in notes:
        for tag in note.tags:
            result[tag] = result.get(tag, 0) + 1

    return result