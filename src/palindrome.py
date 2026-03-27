def is_palindrome(text: str) -> bool:
    """
    Return True if the given text is a palindrome, ignoring case and spaces.
    """
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]
