def search_notes(notes, query):
    """
    Search for notes containing the query string, case‑insensitively.
    Returns a list of notes that contain the query, preserving the original
    note objects.
    """
    lowered_query = query.lower()
    result = []
    for note in notes:
        # Assume each note has a 'text' attribute containing its content.
        if lowered_query in note.text.lower():
            result.append(note)
    return result
