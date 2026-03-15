# src/todo/storage.py
import json
import os
from pathlib import Path
from typing import List

from .models import Task

# Environment variable to override tasks file location
TASKS_FILE_ENV = "TODO_TASKS_FILE"

# Default tasks file location (next to this file)
DEFAULT_TASKS_FILE = Path(__file__).with_name("tasks.json")

def _get_tasks_file() -> Path:
    path = os.getenv(TASKS_FILE_ENV)
    if path:
        return Path(path)
    return DEFAULT_TASKS_FILE

def load_tasks() -> List[Task]:
    tasks_file = _get_tasks_file()
    if not tasks_file.is_file():
        return []
    with tasks_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task(**item) for item in data]

def save_tasks(tasks: List[Task]) -> None:
    tasks_file = _get_tasks_file()
    tasks_file.parent.mkdir(parents=True, exist_ok=True)
    with tasks_file.open("w", encoding="utf-8") as f:
        json.dump([task.__dict__ for task in tasks], f, ensure_ascii=False, indent=2)

def add_task(text: str) -> Task:
    tasks = load_tasks()
    new_id = max((task.id for task in tasks), default=0) + 1
    new_task = Task(id=new_id, text=text)
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def list_tasks() -> List[Task]:
    return load_tasks()

def remove_task(task_id: int) -> None:
    tasks = load_tasks()
    filtered = [task for task in tasks if task.id != task_id]
    if len(filtered) == len(tasks):
        raise ValueError(f"Task with id {task_id} does not exist")
    save_tasks(filtered)
