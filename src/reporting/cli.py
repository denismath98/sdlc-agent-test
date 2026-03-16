import argparse

from src.notebook.storage import load_notes
from src.notebook.cli import _sort_by_title
from src.reporting.summary import count_notes, count_notes_by_tag


def main() -> None:
    parser = argparse.ArgumentParser(description="Reporting CLI")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    parser.add_argument(
        "--sort-title",
        action="store_true",
        help="Sort notes by title in ascending order before reporting",
    )
    args = parser.parse_args()

    notes = load_notes(args.file)

    if args.sort_title:
        notes = _sort_by_title(notes)

    print(f"total={count_notes(notes)}")

    tag_stats = count_notes_by_tag(notes)
    for tag in sorted(tag_stats):
        print(f"{tag}={tag_stats[tag]}")


if __name__ == "__main__":
    main()
