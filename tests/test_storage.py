# tests/test_storage.py
import os
from pathlib import Path

import pytest

from src.todo import storage

def test_add_and_list(tmp_path, monkeypatch):
    # Use a temporary tasks file
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setenv(storage.TASKS_FILE_ENV, str(tasks_file))

    # Ensure clean start
    if tasks_file.exists():
        tasks_file.unlink()

    task = storage.add_task("First task")
    assert task.id == 1
    assert task.text == "First task"

    tasks = storage.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].text == "First task"

def test_remove_task(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setenv(storage.TASKS_FILE_ENV, str(tasks_file))

    storage.add_task("Task 1")
    storage.add_task("Task 2")
    tasks_before = storage.list_tasks()
    assert len(tasks_before) == 2

    storage.remove_task(1)
    tasks_after = storage.list_tasks()
    assert len(tasks_after) == 1
    assert tasks_after[0].id == 2
    assert tasks_after[0].text == "Task 2"

def test_remove_nonexistent_raises(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setenv(storage.TASKS_FILE_ENV, str(tasks_file))

    storage.add_task("Only task")
    with pytest.raises(ValueError):
        storage.remove_task(999)

def test_default_location(tmp_path, monkeypatch):
    # Ensure the env var is not set
    monkeypatch.delenv(storage.TASKS_FILE_ENV, raising=False)

    # Use a temporary copy of the package to avoid interfering with real repo
    temp_pkg = tmp_path / "src" / "todo"
    temp_pkg.mkdir(parents=True)
    # Copy storage.py and models.py into the temp package
    import shutil, importlib.util, sys
    src_dir = Path(__file__).resolve().parents[1] / "src" / "todo"
    shutil.copy(src_dir / "models.py", temp_pkg / "models.py")
    shutil.copy(src_dir / "storage.py", temp_pkg / "storage.py")
    # Create an __init__.py
    (temp_pkg / "__init__.py").write_text("# temp package")

    # Add temp directory to sys.path and import the temporary storage module
    sys.path.insert(0, str(tmp_path))
    spec = importlib.util.spec_from_file_location("temp_todo.storage", temp_pkg / "storage.py")
    temp_storage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(temp_storage)

    # Ensure no tasks file exists initially
    default_path = temp_storage.DEFAULT_TASKS_FILE
    if default_path.is_file():
        default_path.unlink()
    assert not default_path.exists()

    # Add a task, which should create the default file
    temp_storage.add_task("Temp task")
    assert default_path.is_file()

    # Clean up sys.path
    sys.path.pop(0)
