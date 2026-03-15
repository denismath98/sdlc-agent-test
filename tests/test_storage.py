# tests/test_storage.py
import json
from pathlib import Path

import pytest

from src.todo import storage


def test_add_list_remove(tmp_path: Path):
    # Redirect storage to a temporary file
    storage.TASKS_FILE = tmp_path / "tasks.json"

    # Initially empty
    assert storage.list_tasks() == []

    # Add a task
    task = storage.add_task("First task")
    assert task.id == 1
    assert task.text == "First task"

    # List should contain the task
    tasks = storage.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].text == "First task"

    # Add another task
    task2 = storage.add_task("Second task")
    assert task2.id == 2

    # Remove first task
    storage.remove_task(1)
    remaining = storage.list_tasks()
    assert len(remaining) == 1
    assert remaining[0].id == 2
    assert remaining[0].text == "Second task"

    # Removing non‑existent task raises
    with pytest.raises(ValueError):
        storage.remove_task(999)


def test_persistence(tmp_path: Path):
    storage.TASKS_FILE = tmp_path / "tasks.json"
    storage.add_task("Persisted task")
    # Reload module state by reading file directly
    data = json.loads(storage.TASKS_FILE.read_text())
    assert data == [{"id": 1, "text": "Persisted task"}]
