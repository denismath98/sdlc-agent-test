import json
from pathlib import Path
from typing import List

from .models import Task

# Default location of the tasks JSON file.
TASKS_FILE = Path.cwd() / "tasks.json"


def _load_tasks() -> List[Task]:
    if not TASKS_FILE.exists():
        return []
    try:
        data = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return [Task(**item) for item in data]


def _save_tasks(tasks: List[Task]) -> None:
    data = [task.__dict__ for task in tasks]
    TASKS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


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
