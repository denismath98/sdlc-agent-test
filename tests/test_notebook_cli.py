import json
import subprocess
import sys


def write_notes(path):
    data = [
        {"id": 1, "title": "Work plan", "text": "Prepare report", "tags": ["work"]},
        {"id": 2, "title": "Shopping", "text": "Buy milk", "tags": ["home"]},
        {
            "id": 3,
            "title": "Ideas",
            "text": "Project report draft",
            "tags": ["work", "draft"],
        },
    ]
    path.write_text(json.dumps(data), encoding="utf-8")


def test_notebook_cli_query(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.notebook.cli",
            "--file",
            str(path),
            "--query",
            "report",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert len(lines) == 2
    assert "[1] Work plan" in lines[0]
    assert "[3] Ideas" in lines[1]


def test_notebook_cli_tag(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.notebook.cli",
            "--file",
            str(path),
            "--tag",
            "home",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert len(lines) == 1
    assert "[2] Shopping" in lines[0]


def test_notebook_cli_sort_title(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.notebook.cli",
            "--file",
            str(path),
            "--sort-title",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert len(lines) == 3
    # Expected order: Ideas, Shopping, Work plan
    assert lines[0].startswith("[3] Ideas")
    assert lines[1].startswith("[2] Shopping")
    assert lines[2].startswith("[1] Work plan")
