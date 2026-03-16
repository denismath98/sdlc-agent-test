import argparse

from src.notebook.search import filter_by_tag, search_notes, find_by_exact_title
from src.notebook.storage import load_notes


def format_note_line(note) -> str:
    tags = ",".join(note.tags)
    return f"[{note.id}] {note.title} :: {tags} :: {note.text}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Notebook CLI")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    parser.add_argument("--query", help="Search query")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--exact-title", help="Exact title match")
    args = parser.parse_args()

    notes = load_notes(args.file)

    if args.exact_title is not None:
        notes = find_by_exact_title(notes, args.exact_title)
    else:
        if args.query:
            notes = search_notes(notes, args.query)

        if args.tag:
            notes = filter_by_tag(notes, args.tag)

    for note in notes:
        print(format_note_line(note))


if __name__ == "__main__":
    main()
