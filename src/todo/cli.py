# src/todo/cli.py
import argparse
import sys

from .storage import add_task, list_tasks, remove_task


def _cmd_add(args: argparse.Namespace) -> None:
    task = add_task(args.text)
    print(f"Added task {task.id}: {task.text}")


def _cmd_list(_: argparse.Namespace) -> None:
    tasks = list_tasks()
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task.id}: {task.text}")


def _cmd_remove(args: argparse.Namespace) -> None:
    try:
        remove_task(args.id)
        print(f"Removed task {args.id}")
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="todo", description="Simple todo CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("text", help="Task description")
    parser_add.set_defaults(func=_cmd_add)

    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.set_defaults(func=_cmd_list)

    parser_remove = subparsers.add_parser("remove", help="Remove a task by ID")
    parser_remove.add_argument("id", type=int, help="ID of the task to remove")
    parser_remove.set_defaults(func=_cmd_remove)

    args = parser.parse_args(argv)
    args.func(args)
