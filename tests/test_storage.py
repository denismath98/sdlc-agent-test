import json
import os
import tempfile
from pathlib import Path
from src.tasktracker.models import Task
from src.tasktracker.storage import JSONStorage
from datetime import datetime


def test_storage_create_and_load(tmp_path: Path):
    file_path = tmp_path / "tasks.json"
    storage = JSONStorage(file_path)

    # initially empty
    tasks = storage.load_tasks()
    assert tasks == []

    # save a task
    task = Task(id=1, text="Sample", completed=False, created_at=datetime.now())
    storage.save_tasks([task])

    # load again
    loaded = storage.load_tasks()
    assert len(loaded) == 1
    assert loaded[0].id == task.id
    assert loaded[0].text == task.text

    # file content is valid JSON
    content = file_path.read_text()
    data = json.loads(content)
    assert isinstance(data, list)
    assert data[0]["id"] == 1


def test_storage_handles_corrupt_file(tmp_path: Path):
    file_path = tmp_path / "bad.json"
    file_path.write_text("not json", encoding="utf-8")
    storage = JSONStorage(file_path)
    tasks = storage.load_tasks()
    assert tasks == []
