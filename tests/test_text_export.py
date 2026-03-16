from src.notebook.models import Note
from src.exporting.text_export import (
    export_notes_as_text,
    export_filtered_notes_as_text,
)


def build_notes():
    return [
        Note(id=1, title="A", text="x", tags=["work"]),
        Note(id=2, title="B", text="y", tags=["home"]),
        Note(id=3, title="C", text="z", tags=["work", "draft"]),
        Note(id=4, title="D", text="no tags", tags=[]),
    ]


def test_export_all_notes():
    notes = build_notes()[:3]  # first three have tags
    result = export_notes_as_text(notes)
    expected = "\n".join(
        [
            "[1] A :: work :: x",
            "[2] B :: home :: y",
            "[3] C :: work,draft :: z",
        ]
    )
    assert result == expected


def test_export_note_without_tags():
    notes = [build_notes()[3]]
    result = export_notes_as_text(notes)
    assert result == "[1] D ::  :: no tags"


def test_export_filtered_by_query():
    notes = build_notes()
    result = export_filtered_notes_as_text(notes, query="report")
    # No note contains "report" in title or text, expect empty string
    assert result == ""


def test_export_filtered_by_tag():
    notes = build_notes()
    result = export_filtered_notes_as_text(notes, tag="work")
    expected = "\n".join(
        [
            "[1] A :: work :: x",
            "[2] C :: work,draft :: z",
        ]
    )
    assert result == expected


def test_export_filtered_by_query_and_tag():
    notes = [
        Note(id=1, title="Alpha", text="beta", tags=["t1"]),
        Note(id=2, title="Gamma", text="delta report", tags=["t2"]),
        Note(id=3, title="Report", text="epsilon", tags=["t2"]),
    ]
    result = export_filtered_notes_as_text(notes, query="Report", tag="t2")
    expected = "[1] Report :: t2 :: epsilon"
    assert result == expected


def test_export_filtered_empty_result():
    notes = build_notes()
    result = export_filtered_notes_as_text(notes, query="nonexistent")
    assert result == ""
