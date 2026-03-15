import argparse
import sys
from .service import create_task, complete_task, list_tasks, delete_task
from .models import Task
from typing import List


def _print_task(task: Task) -> None:
    status = "✅" if task.completed else "❌"
    print(f"[{task.id}] {status} {task.text} (created: {task.created_at.isoformat()})")


def _print_tasks(tasks: List[Task]) -> None:
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        _print_task(task)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="tasktracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new task")
    create_parser.add_argument("text", help="Task description")

    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID")

    list_parser = subparsers.add_parser("list", help="List tasks")
    group = list_parser.add_mutually_exclusive_group()
    group.add_argument(
        "--completed", action="store_true", help="Show only completed tasks"
    )
    group.add_argument("--pending", action="store_true", help="Show only pending tasks")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args(argv)

    try:
        if args.command == "create":
            task = create_task(args.text)
            _print_task(task)
        elif args.command == "complete":
            task = complete_task(args.id)
            _print_task(task)
        elif args.command == "list":
            if args.completed:
                tasks = list_tasks(completed=True)
            elif args.pending:
                tasks = list_tasks(completed=False)
            else:
                tasks = list_tasks()
            _print_tasks(tasks)
        elif args.command == "delete":
            delete_task(args.id)
            print(f"Task {args.id} deleted.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
