# tests/test_cli.py
import subprocess
import sys
from pathlib import Path


def run_cli(args, cwd):
    return subprocess.run(
        [sys.executable, "-m", "src.todo"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def test_cli_flow(tmp_path: Path):
    # Ensure the package uses a temporary tasks file by setting env var
    # We'll monkey‑patch the TASKS_FILE path via a sitecustomize trick:
    # Create a sitecustomize that modifies src.todo.storage.TASKS_FILE
    sitecustomize = tmp_path / "sitecustomize.py"
    sitecustomize.write_text(
        "import importlib, pathlib; "
        "mod = importlib.import_module('src.todo.storage'); "
        "mod.TASKS_FILE = pathlib.Path(__file__).parent / 'tasks.json'"
    )
    env = {
        "PYTHONPATH": str(Path.cwd()),
        "PYTHONPATH": str(Path.cwd()),
        "PYTHONPATH": str(Path.cwd()),
        "PYTHONPATH": str(Path.cwd()),
        "PYTHONPATH": str(Path.cwd()),
    }
    # Ensure sitecustomize is importable
    env["PYTHONPATH"] = str(tmp_path) + ":" + env["PYTHONPATH"]
    # Add first task
    result = run_cli(["add", "CLI task"], cwd=tmp_path)
    assert result.returncode == 0
    assert "Added task 1" in result.stdout

    # List tasks
    result = run_cli(["list"], cwd=tmp_path)
    assert result.returncode == 0
    assert "1: CLI task" in result.stdout

    # Remove task
    result = run_cli(["remove", "1"], cwd=tmp_path)
    assert result.returncode == 0
    assert "Removed task 1" in result.stdout

    # List again should be empty
    result = run_cli(["list"], cwd=tmp_path)
    assert result.returncode == 0
    assert "No tasks." in result.stdout
