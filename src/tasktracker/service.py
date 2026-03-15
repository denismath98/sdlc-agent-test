from typing import List, Optional
from pathlib import Path
from .models import Task
from .storage import JSONStorage

_storage = JSONStorage()


def _get_next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1


def create_task(text: str) -> Task:
    tasks = _storage.load_tasks()
    new_task = Task(
        id=_get_next_id(tasks),
        text=text,
        completed=False,
        created_at=datetime.now(),
    )
    tasks.append(new_task)
    _storage.save_tasks(tasks)
    return new_task


def complete_task(task_id: int) -> Task:
    tasks = _storage.load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            _storage.save_tasks(tasks)
            return task
    raise ValueError(f"Task with id {task_id} not found")


def list_tasks(completed: Optional[bool] = None) -> List[Task]:
    tasks = _storage.load_tasks()
    if completed is None:
        return tasks
    return [task for task in tasks if task.completed == completed]


def delete_task(task_id: int) -> None:
    tasks = _storage.load_tasks()
    new_tasks = [task for task in tasks if task.id != task_id]
    if len(new_tasks) == len(tasks):
        raise ValueError(f"Task with id {task_id} not found")
    _storage.save_tasks(new_tasks)
