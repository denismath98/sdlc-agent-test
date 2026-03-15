def search_notes(notes, query):
    """
    Return a list of notes that contain the query string, case‑insensitively.

    Parameters
    ----------
    notes : iterable of str
        The collection of note strings to search through.
    query : str
        The substring to look for.

    Returns
    -------
    list of str
        Notes that contain the query, preserving the original note order.
    """
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    lowered_query = query.lower()
    result = []
    for note in notes:
        if not isinstance(note, str):
            continue
        if lowered_query in note.lower():
            result.append(note)
    return result
