import json
from datetime import datetime, timedelta
from src.tasktracker.models import Task


def test_task_serialization():
    now = datetime.now()
    task = Task(id=1, text="Test", completed=False, created_at=now)
    d = task.to_dict()
    assert d["id"] == 1
    assert d["text"] == "Test"
    assert d["completed"] is False
    assert d["created_at"] == now.isoformat()

    restored = Task.from_dict(d)
    assert restored == task


def test_task_equality():
    t1 = Task(id=1, text="A", completed=False, created_at=datetime.now())
    t2 = Task(id=1, text="A", completed=False, created_at=t1.created_at)
    assert t1 == t2
