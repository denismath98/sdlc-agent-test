import os
from pathlib import Path
from src.tasktracker.service import create_task, complete_task, list_tasks, delete_task
from src.tasktracker.storage import JSONStorage
from src.tasktracker.models import Task
from datetime import datetime


def test_full_flow(tmp_path: Path, monkeypatch):
    # Use a temporary storage file
    storage_path = tmp_path / "tasks.json"
    monkeypatch.setattr("src.tasktracker.service._storage", JSONStorage(storage_path))

    # Create tasks
    t1 = create_task("First")
    t2 = create_task("Second")
    assert t1.id != t2.id
    assert not t1.completed

    # Complete one
    completed = complete_task(t1.id)
    assert completed.completed is True

    # List pending
    pending = list_tasks(completed=False)
    assert len(pending) == 1
    assert pending[0].id == t2.id

    # Delete completed
    delete_task(t1.id)
    remaining = list_tasks()
    assert len(remaining) == 1
    assert remaining[0].id == t2.id


def test_errors(monkeypatch, tmp_path):
    storage_path = tmp_path / "tasks.json"
    monkeypatch.setattr("src.tasktracker.service._storage", JSONStorage(storage_path))

    # Deleting non‑existent task raises
    try:
        delete_task(999)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    # Completing non‑existent task raises
    try:
        complete_task(999)
        assert False, "Expected ValueError"
    except ValueError:
        pass
