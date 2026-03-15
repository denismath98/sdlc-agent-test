from typing import List

from .models import Task
from .storage import get_storage

_storage = get_storage()


def create_task(text: str) -> Task:
    task_id = _storage.generate_id()
    task = Task(id=task_id, text=text)
    tasks = _storage.get_all()
    tasks.append(task)
    _storage.save_all(tasks)
    return task


def complete_task(task_id: int) -> Task:
    tasks = _storage.get_all()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            _storage.save_all(tasks)
            return task
    raise ValueError(f"Task with id {task_id} not found")


def list_tasks() -> List[Task]:
    return _storage.get_all()


def delete_task(task_id: int) -> None:
    tasks = _storage.get_all()
    new_tasks = [t for t in tasks if t.id != task_id]
    if len(new_tasks) == len(tasks):
        raise ValueError(f"Task with id {task_id} not found")
    _storage.save_all(new_tasks)
