import argparse
import sys

from src.notebook.storage import load_notes
from src.exporting.text_export import export_filtered_notes_as_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Export notes as text")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    parser.add_argument("--query", help="Search query")
    parser.add_argument("--tag", help="Filter by tag")
    args = parser.parse_args()

    notes = load_notes(args.file)

    output = export_filtered_notes_as_text(notes, args.query, args.tag)

    if output:
        # print adds a trailing newline which is acceptable for non‑empty output
        print(output)


if __name__ == "__main__":
    main()
