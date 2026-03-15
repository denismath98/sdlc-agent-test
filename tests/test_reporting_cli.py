import json
import subprocess
import sys


def write_notes(path):
    data = [
        {"id": 1, "title": "A", "text": "x", "tags": ["work"]},
        {"id": 2, "title": "B", "text": "y", "tags": ["home"]},
        {"id": 3, "title": "C", "text": "z", "tags": ["work", "draft"]},
    ]
    path.write_text(json.dumps(data), encoding="utf-8")


def test_reporting_cli(tmp_path):
    path = tmp_path / "notes.json"
    write_notes(path)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.reporting.cli",
            "--file",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    assert lines == [
        "total=3",
        "draft=1",
        "home=1",
        "work=2",
    ]