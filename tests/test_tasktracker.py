import json
import os
from pathlib import Path
from datetime import datetime

import pytest
from freezegun import freeze_time
from click.testing import CliRunner

from tasktracker import service, cli, models


@pytest.fixture
def temp_storage(tmp_path, monkeypatch):
    temp_file = tmp_path / "tasks.json"
    storage = service.JSONStorage(file_path=temp_file)
    monkeypatch.setattr(service, "_storage", storage)
    yield storage
    # restore original storage
    monkeypatch.setattr(service, "_storage", service.JSONStorage())


def test_create_task(temp_storage):
    with freeze_time("2023-01-01 12:00:00"):
        task = service.create_task("Test task")
    assert task.id == 1
    assert task.text == "Test task"
    assert task.completed is False
    assert task.created_at == datetime(2023, 1, 1, 12, 0, 0)
    # verify persisted
    data = json.loads(Path(temp_storage.file_path).read_text())
    assert data[0]["id"] == 1
    assert data[0]["text"] == "Test task"


def test_complete_task(temp_storage):
    task = service.create_task("Another task")
    completed = service.complete_task(task.id)
    assert completed.completed is True
    loaded = service.list_tasks()[0]
    assert loaded.completed is True


def test_list_tasks(temp_storage):
    service.create_task("Task 1")
    service.create_task("Task 2")
    tasks = service.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].text == "Task 1"
    assert tasks[1].text == "Task 2"


def test_delete_task(temp_storage):
    t1 = service.create_task("To delete")
    service.delete_task(t1.id)
    assert service.list_tasks() == []


def test_cli_create_and_list(monkeypatch, tmp_path):
    runner = CliRunner()
    storage_path = tmp_path / "cli_tasks.json"
    storage = service.JSONStorage(file_path=storage_path)
    monkeypatch.setattr(service, "_storage", storage)

    result = runner.invoke(cli.cli, ["create", "CLI", "task"])
    assert result.exit_code == 0
    assert "Created task" in result.output

    result = runner.invoke(cli.cli, ["list"])
    assert result.exit_code == 0
    assert "CLI task" in result.output
