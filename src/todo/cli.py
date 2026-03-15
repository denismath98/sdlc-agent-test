import argparse
import sys

from . import storage


def _cmd_add(args):
    task = storage.add_task(args.text)
    print(f"Added task {task.id}: {task.text}")


def _cmd_list(args):
    tasks = storage.list_tasks()
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task.id}: {task.text}")


def _cmd_remove(args):
    success = storage.remove_task(args.id)
    if success:
        print(f"Removed task {args.id}.")
    else:
        print(f"Task {args.id} not found.", file=sys.stderr)
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Simple TODO manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("text", help="Task description")
    parser_add.set_defaults(func=_cmd_add)

    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.set_defaults(func=_cmd_list)

    parser_remove = subparsers.add_parser("remove", help="Remove a task by ID")
    parser_remove.add_argument("id", type=int, help="ID of the task to remove")
    parser_remove.set_defaults(func=_cmd_remove)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
