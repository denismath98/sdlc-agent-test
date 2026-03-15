import click
from .service import create_task, complete_task, list_tasks, delete_task
from .models import Task


def _format_task(task: Task) -> str:
    status = "✔" if task.completed else "✘"
    return f"[{task.id}] {status} {task.text} (created: {task.created_at.isoformat()})"


@click.group()
def cli() -> None:
    """Task Tracker CLI."""
    pass


@cli.command()
@click.argument("text", nargs=-1, required=True)
def create(text):
    """Create a new task."""
    task_text = " ".join(text)
    task = create_task(task_text)
    click.echo(f"Created task {task.id}")


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Mark a task as completed."""
    try:
        task = complete_task(task_id)
        click.echo(f"Task {task.id} marked as completed")
    except ValueError as e:
        click.echo(str(e), err=True)


@cli.command(name="list")
def list_cmd():
    """List all tasks."""
    tasks = list_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for task in tasks:
        click.echo(_format_task(task))


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task."""
    try:
        delete_task(task_id)
        click.echo(f"Task {task_id} deleted")
    except ValueError as e:
        click.echo(str(e), err=True)


if __name__ == "__main__":
    cli()
