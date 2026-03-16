import argparse

from src.notebook.search import filter_by_tag, filter_without_tags, search_notes
from src.notebook.storage import load_notes


def format_note_line(note) -> str:
    tags = ",".join(note.tags)
    return f"[{note.id}] {note.title} :: {tags} :: {note.text}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Notebook CLI")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    parser.add_argument("--query", help="Search query")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument(
        "--without-tags",
        action="store_true",
        default=False,
        help="Show only notes without tags",
    )
    args = parser.parse_args()

    notes = load_notes(args.file)

    if args.query:
        notes = search_notes(notes, args.query)

    if args.tag:
        notes = filter_by_tag(notes, args.tag)

    if args.without_tags:
        notes = filter_without_tags(notes)

    for note in notes:
        print(format_note_line(note))


if __name__ == "__main__":
    main()
