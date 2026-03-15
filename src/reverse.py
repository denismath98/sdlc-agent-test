import sys


def reverse_string(text: str) -> str:
    return text[::-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m src.reverse <text>")
        sys.exit(1)
    print(reverse_string(sys.argv[1]))
