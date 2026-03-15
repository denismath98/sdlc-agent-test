def search_notes(notes, query):
    """
    Search for notes containing the query string, case-insensitively.

    Parameters
    ----------
    notes : list of str
        List of note strings to search within.
    query : str
        Query string to search for.

    Returns
    -------
    list of str
        Subset of `notes` that contain `query` (case‑insensitive), preserving original case.
    """
    query_lower = query.lower()
    return [note for note in notes if query_lower in note.lower()]
