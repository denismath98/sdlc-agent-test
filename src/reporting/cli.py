import argparse

from src.notebook.storage import load_notes
from src.notebook.cli import format_note_line
from src.reporting.summary import count_notes, count_notes_by_tag, group_notes_by_tag


def main() -> None:
    parser = argparse.ArgumentParser(description="Reporting CLI")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    parser.add_argument(
        "--show-grouped",
        action="store_true",
        help="Show notes grouped by tags after the summary",
    )
    args = parser.parse_args()

    notes = load_notes(args.file)

    print(f"total={count_notes(notes)}")

    tag_stats = count_notes_by_tag(notes)
    for tag in sorted(tag_stats):
        print(f"{tag}={tag_stats[tag]}")

    if args.show_grouped:
        groups = group_notes_by_tag(notes)

        print()
        sorted_tags = sorted(groups)
        for idx, tag in enumerate(sorted_tags):
            print(f"[group:{tag}]")
            for note in groups[tag]:
                print(format_note_line(note))
            if idx != len(sorted_tags) - 1:
                print()  # blank line between groups


if __name__ == "__main__":
    main()
