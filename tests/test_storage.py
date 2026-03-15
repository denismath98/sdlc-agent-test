import json
from pathlib import Path

import pytest

from src.tasktracker.storage import JSONStorage, get_storage


def test_storage_initialization(tmp_path):
    storage_path = tmp_path / "mytasks.json"
    storage = get_storage(storage_path)
    assert storage.file_path == storage_path
    assert storage.file_path.read_text() == "[]"


def test_save_and_load(tmp_path):
    storage_path = tmp_path / "tasks.json"
    storage = get_storage(storage_path)
    task_data = [
        {"id": 1, "text": "A", "completed": False, "created_at": "2023-01-01T00:00:00"}
    ]
    storage._save(task_data)  # type: ignore
    loaded = storage._load()  # type: ignore
    assert loaded[0].id == 1
    assert loaded[0].text == "A"


def test_generate_id(tmp_path):
    storage_path = tmp_path / "tasks.json"
    storage = get_storage(storage_path)
    assert storage.generate_id() == 1
    storage._save(
        [  # type: ignore
            {
                "id": 1,
                "text": "A",
                "completed": False,
                "created_at": "2023-01-01T00:00:00",
            }
        ]
    )
    assert storage.generate_id() == 2
