import os
import subprocess
import sys
import json
from pathlib import Path

import pytest

from src.todo import storage, models


@pytest.fixture
def temp_tasks_file(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    monkeypatch.setenv("TODO_TASKS_FILE", str(file_path))
    # Ensure storage module picks up the new env var
    import importlib
    import src.todo.storage as storage_mod

    importlib.reload(storage_mod)
    return file_path


def test_add_list_remove_functions(temp_tasks_file):
    # Initially empty
    assert storage.list_tasks() == []

    # Add a task
    task = storage.add_task("First task")
    assert task.id == 1
    assert task.text == "First task"

    # List returns the added task
    tasks = storage.list_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task

    # Remove the task
    removed = storage.remove_task(task.id)
    assert removed is True
    assert storage.list_tasks() == []


def run_cli(args, env=None):
    cmd = [sys.executable, "-m", "src.todo"] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    return result


def test_cli_add_list_remove(temp_tasks_file):
    env = os.environ.copy()
    env["TODO_TASKS_FILE"] = str(temp_tasks_file)

    # Add via CLI
    res = run_cli(["add", "CLI task"], env=env)
    assert res.returncode == 0
    assert "Added task 1" in res.stdout

    # List via CLI
    res = run_cli(["list"], env=env)
    assert res.returncode == 0
    assert "1: CLI task" in res.stdout

    # Remove via CLI
    res = run_cli(["remove", "1"], env=env)
    assert res.returncode == 0
    assert "Removed task 1" in res.stdout

    # Verify file is empty after removal
    with temp_tasks_file.open() as f:
        data = json.load(f)
    assert data == []
