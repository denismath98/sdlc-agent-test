import json
import os
from pathlib import Path
from typing import List

from .models import Task

# Configurable path for the tasks JSON file
TASKS_FILE = Path(os.getenv("TODO_TASKS_FILE", Path.cwd() / "tasks.json"))


def _load_tasks() -> List[Task]:
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return [Task(**item) for item in data]
    except json.JSONDecodeError:
        # Corrupted file – start fresh
        return []


def _save_tasks(tasks: List[Task]) -> None:
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump([task.__dict__ for task in tasks], f, ensure_ascii=False, indent=2)


def add_task(text: str) -> Task:
    tasks = _load_tasks()
    next_id = max((task.id for task in tasks), default=0) + 1
    new_task = Task(id=next_id, text=text)
    tasks.append(new_task)
    _save_tasks(tasks)
    return new_task


def list_tasks() -> List[Task]:
    return _load_tasks()


def remove_task(task_id: int) -> bool:
    tasks = _load_tasks()
    filtered = [task for task in tasks if task.id != task_id]
    if len(filtered) == len(tasks):
        return False  # No task removed
    _save_tasks(filtered)
    return True
