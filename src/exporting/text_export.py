from src.notebook.models import Note
from src.notebook.search import search_notes, filter_by_tag


def export_notes_as_text(notes: list[Note]) -> str:
    """
    Export a list of notes to a plain‑text representation.

    Each line has the form:
        [<index>] <title> :: <comma‑separated‑tags> :: <text>

    Index starts at 1 and follows the order of the supplied list.
    If a note has no tags, the middle part is empty.
    """
    lines: list[str] = []
    for idx, note in enumerate(notes, start=1):
        tags_str = ",".join(note.tags)
        lines.append(f"[{idx}] {note.title} :: {tags_str} :: {note.text}")
    return "\n".join(lines)


def export_filtered_notes_as_text(
    notes: list[Note], query: str | None = None, tag: str | None = None
) -> str:
    """
    Apply optional filtering (search query and/or tag) to the notes and
    return their text export. If the resulting list is empty, an empty
    string is returned.
    """
    filtered = notes

    if query:
        filtered = search_notes(filtered, query)

    if tag:
        filtered = filter_by_tag(filtered, tag)

    if not filtered:
        return ""

    return export_notes_as_text(filtered)
