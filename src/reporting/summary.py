from collections import defaultdict
from src.notebook.models import Note


def count_notes(notes: list[Note]) -> int:
    return len(notes)


def count_notes_by_tag(notes: list[Note]) -> dict[str, int]:
    result: dict[str, int] = {}

    for note in notes:
        for tag in note.tags:
            result[tag] = result.get(tag, 0) + 1

    return result


def group_notes_by_tag(notes: list[Note]) -> dict[str, list[Note]]:
    groups: defaultdict[str, list[Note]] = defaultdict(list)

    for note in notes:
        if not note.tags:
            continue
        for tag in note.tags:
            groups[tag].append(note)

    return dict(groups)
