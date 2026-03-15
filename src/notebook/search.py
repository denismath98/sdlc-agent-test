"""
Search utilities for notebook notes.

Provides a case‑insensitive search over an iterable of notes.
"""

from typing import Iterable, List, Any


def search_notes(notes: Iterable[Any], query: str) -> List[Any]:
    """
    Return a list of notes that contain the ``query`` string,
    performing a case‑insensitive match.

    Parameters
    ----------
    notes : Iterable[Any]
        Collection of notes. Each note is converted to ``str`` for matching.
    query : str
        Substring to search for.

    Returns
    -------
    List[Any]
        List of original note objects that match the query.
    """
    query_lower = query.lower()
    return [note for note in notes if query_lower in str(note).lower()]
