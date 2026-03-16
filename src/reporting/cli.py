import argparse

from src.notebook.storage import load_notes
from src.reporting.summary import (
    count_notes,
    count_notes_by_tag,
    count_notes_without_tags,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reporting CLI")
    parser.add_argument("--file", required=True, help="Path to notes json file")
    args = parser.parse_args()

    notes = load_notes(args.file)

    print(f"total={count_notes(notes)}")

    tag_stats = count_notes_by_tag(notes)
    for tag in sorted(tag_stats):
        print(f"{tag}={tag_stats[tag]}")

    print(f"without_tags={count_notes_without_tags(notes)}")


if __name__ == "__main__":
    main()
