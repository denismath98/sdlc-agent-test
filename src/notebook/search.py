def search_notes(notes, query):
    """
    Search for notes containing the given query string, case‑insensitively.

    Parameters
    ----------
    notes : iterable of str
        Collection of note texts to search through.
    query : str
        Substring to look for within each note.

    Returns
    -------
    list of str
        List of notes that contain the query, preserving the original order.
    """
    lowered_query = query.lower()
    matching_notes = []
    for note in notes:
        if lowered_query in note.lower():
            matching_notes.append(note)
    return matching_notes
