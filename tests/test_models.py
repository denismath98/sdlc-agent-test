from datetime import datetime, timedelta

import pytest

from src.tasktracker.models import Task


def test_task_creation():
    now = datetime.utcnow()
    task = Task(id=1, text="Sample", created_at=now)
    assert task.id == 1
    assert task.text == "Sample"
    assert task.completed is False
    assert task.created_at == now


def test_task_serialization():
    task = Task(id=2, text="Serialize", completed=True, created_at=datetime.utcnow())
    d = task.to_dict()
    restored = Task.from_dict(d)
    assert restored == task


def test_task_equality():
    t1 = Task(id=1, text="A", completed=False, created_at=datetime.utcnow())
    t2 = Task(id=1, text="A", completed=False, created_at=t1.created_at)
    assert t1 == t2
