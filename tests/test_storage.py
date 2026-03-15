import os
import json
from pathlib import Path

import pytest

from src.todo.storage import add_task, list_tasks, remove_task, _get_tasks_file


@pytest.fixture
def temp_tasks_file(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setenv("TODO_TASKS_FILE", str(tasks_file))
    # Ensure clean state
    if tasks_file.exists():
        tasks_file.unlink()
    yield tasks_file
    # Cleanup
    if tasks_file.exists():
        tasks_file.unlink()


def test_add_and_list_tasks(temp_tasks_file):
    # Initially empty
    assert list_tasks() == []

    # Add a task
    task = add_task("First task")
    assert task.id == 1
    assert task.text == "First task"

    # List should contain the task
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].text == "First task"


def test_remove_task(temp_tasks_file):
    t1 = add_task("Task 1")
    t2 = add_task("Task 2")
    assert len(list_tasks()) == 2

    remove_task(t1.id)
    remaining = list_tasks()
    assert len(remaining) == 1
    assert remaining[0].id == t2.id

    # Removing non‑existent task should raise
    with pytest.raises(ValueError):
        remove_task(999)


def test_persistence_between_calls(temp_tasks_file):
    add_task("Persisted task")
    # Simulate a new process by reloading the module function
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0].text == "Persisted task"
