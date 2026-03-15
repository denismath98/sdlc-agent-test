# src/todo/storage.py
import json
from pathlib import Path
from typing import List

from .models import Task

# Path to the JSON file storing tasks. Can be monkey‑patched in tests.
TASKS_FILE: Path = Path(__file__).with_name("tasks.json")


def _ensure_file_exists() -> None:
    if not TASKS_FILE.exists():
        TASKS_FILE.write_text("[]", encoding="utf-8")


def load_tasks() -> List[Task]:
    """Load tasks from the JSON file."""
    _ensure_file_exists()
    try:
        data = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        data = []
    return [Task(**item) for item in data]


def save_tasks(tasks: List[Task]) -> None:
    """Save the list of tasks to the JSON file."""
    data = [task.__dict__ for task in tasks]
    TASKS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add_task(text: str) -> Task:
    """Add a new task and return it."""
    tasks = load_tasks()
    next_id = max((task.id for task in tasks), default=0) + 1
    new_task = Task(id=next_id, text=text)
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def list_tasks() -> List[Task]:
    """Return the list of all tasks."""
    return load_tasks()


def remove_task(task_id: int) -> None:
    """Remove a task by its ID. Raises ValueError if not found."""
    tasks = load_tasks()
    filtered = [task for task in tasks if task.id != task_id]
    if len(filtered) == len(tasks):
        raise ValueError(f"Task with id {task_id} not found")
    save_tasks(filtered)
