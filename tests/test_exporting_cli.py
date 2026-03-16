import json
import subprocess
import sys
from pathlib import Path


def write_notes(path: Path):
    data = [
        {"id": 1, "title": "A", "text": "x", "tags": ["work"]},
        {"id": 2, "title": "B", "text": "y", "tags": ["home"]},
        {"id": 3, "title": "C", "text": "z", "tags": ["work", "draft"]},
        {"id": 4, "title": "D", "text": "no tags", "tags": []},
    ]
    path.write_text(json.dumps(data), encoding="utf-8")


def test_cli_export_all(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.exporting.cli",
            "--file",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert lines == [
        "[1] A :: work :: x",
        "[2] B :: home :: y",
        "[3] C :: work,draft :: z",
        "[4] D ::  :: no tags",
    ]


def test_cli_export_with_query(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.exporting.cli",
            "--file",
            str(path),
            "--query",
            "x",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert lines == ["[1] A :: work :: x"]


def test_cli_export_with_tag(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.exporting.cli",
            "--file",
            str(path),
            "--tag",
            "draft",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert lines == ["[1] C :: work,draft :: z"]


def test_cli_export_with_query_and_tag(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.exporting.cli",
            "--file",
            str(path),
            "--query",
            "z",
            "--tag",
            "draft",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert lines == ["[1] C :: work,draft :: z"]


def test_cli_export_empty_result(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.exporting.cli",
            "--file",
            str(path),
            "--query",
            "nonexistent",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # stdout should be empty (no trailing newline)
    assert result.stdout == ""
