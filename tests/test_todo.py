import json
import subprocess
import sys
from pathlib import Path

import pytest

from src.todo import storage, models


@pytest.fixture
def temp_tasks_file(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "TASKS_FILE", file_path)
    # Ensure clean state
    if file_path.exists():
        file_path.unlink()
    yield file_path
    # Cleanup
    if file_path.exists():
        file_path.unlink()


def test_add_and_list_tasks(temp_tasks_file):
    # Initially empty
    assert storage.list_tasks() == []

    # Add first task
    task1 = storage.add_task("First task")
    assert task1.id == 1
    assert task1.text == "First task"

    # Add second task
    task2 = storage.add_task("Second task")
    assert task2.id == 2
    assert task2.text == "Second task"

    # List tasks
    tasks = storage.list_tasks()
    assert len(tasks) == 2
    assert tasks[0] == task1
    assert tasks[1] == task2


def test_remove_task(temp_tasks_file):
    storage.add_task("Task to keep")
    task_to_remove = storage.add_task("Task to delete")
    assert len(storage.list_tasks()) == 2

    removed = storage.remove_task(task_to_remove.id)
    assert removed is True
    remaining = storage.list_tasks()
    assert len(remaining) == 1
    assert remaining[0].text == "Task to keep"

    # Removing non‑existent id should return False
    assert storage.remove_task(999) is False


def test_cli_add_list_remove(temp_tasks_file):
    # Use subprocess to invoke the module as a script
    def run_cmd(*args):
        result = subprocess.run(
            [sys.executable, "-m", "src.todo"] + list(args),
            cwd=Path.cwd(),
            capture_output=True,
            text=True,
            check=False,
        )
        return result

    # Add a task
    res_add = run_cmd("add", "CLI task")
    assert res_add.returncode == 0
    assert "Added task 1" in res_add.stdout

    # List tasks
    res_list = run_cmd("list")
    assert res_list.returncode == 0
    assert "1: CLI task" in res_list.stdout

    # Remove the task
    res_remove = run_cmd("remove", "1")
    assert res_remove.returncode == 0
    assert "Removed task 1" in res_remove.stdout

    # List again should be empty
    res_list2 = run_cmd("list")
    assert res_list2.returncode == 0
    assert "No tasks." in res_list2.stdout

    # Verify the JSON file content matches expectations
    data = json.loads(temp_tasks_file.read_text())
    assert data == []
