import sys
from typing import List

import click

from .service import create_task, complete_task, delete_task, list_tasks
from .models import Task


@click.group()
def cli() -> None:
    """Task Tracker CLI."""
    pass


@cli.command(name="create")
@click.argument("text", nargs=-1)
def create_command(text: List[str]) -> None:
    """Create a new task."""
    task_text = " ".join(text).strip()
    if not task_text:
        click.echo("Error: task text cannot be empty", err=True)
        sys.exit(1)
    task = create_task(task_text)
    click.echo(f"[{task.id}] {task.text}")


@cli.command(name="complete")
@click.argument("task_id", type=int)
def complete_command(task_id: int) -> None:
    """Mark a task as completed."""
    try:
        task = complete_task(task_id)
        click.echo(f"✅ Task [{task.id}] marked as completed")
    except ValueError as e:
        click.echo(str(e), err=True)
        sys.exit(1)


@cli.command(name="list")
def list_command() -> None:
    """List all tasks."""
    tasks: List[Task] = list_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for task in tasks:
        status = "✅" if task.completed else "❌"
        click.echo(f"[{task.id}] {task.text} {status}")


@cli.command(name="delete")
@click.argument("task_id", type=int)
def delete_command(task_id: int) -> None:
    """Delete a task."""
    try:
        delete_task(task_id)
        click.echo(f"Deleted task [{task_id}]")
    except ValueError as e:
        click.echo(str(e), err=True)
        sys.exit(1)
