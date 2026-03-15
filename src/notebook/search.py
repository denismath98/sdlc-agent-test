"""
Search utilities for notebook notes.

Provides a case‑insensitive search over a collection of note objects.
"""

from typing import Iterable, List, Any


def _get_note_text(note: Any) -> str:
    """
    Retrieve the textual representation of a note.

    The function first tries to access a ``text`` attribute; if it does not exist,
    it falls back to ``str(note)``.
    """
    return getattr(note, "text", str(note))


def search_notes(notes: Iterable[Any], query: str) -> List[Any]:
    """
    Return a list of notes whose text contains the given query, case‑insensitively.

    Parameters
    ----------
    notes : iterable
        Collection of note objects.
    query : str
        Search string.

    Returns
    -------
    list
        Notes that match the query.
    """
    query_lower = query.lower()
    matched: List[Any] = []
    for note in notes:
        note_text = _get_note_text(note)
        if query_lower in note_text.lower():
            matched.append(note)
    return matched
