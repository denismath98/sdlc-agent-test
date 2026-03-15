import argparse
import sys
from . import search_in_files


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Search for a pattern in files recursively."
    )
    parser.add_argument("directory", help="Directory to search")
    parser.add_argument("pattern", help="Pattern to search for")
    args = parser.parse_args(argv)

    matches = search_in_files(args.directory, args.pattern)
    for file_path, line_no, line_text in matches:
        # Strip trailing newline for cleaner output
        print(f"{file_path}:{line_no}: {line_text.rstrip()}")


if __name__ == "__main__":
    sys.exit(main())
