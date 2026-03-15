import sys


def reverse_string(text: str) -> str:
    """Return the given string reversed."""
    return text[::-1]


if __name__ == "__main__":
    # Expect the string to reverse as the first command‑line argument.
    # Let Python raise an IndexError if the argument is missing.
    print(reverse_string(sys.argv[1]))
