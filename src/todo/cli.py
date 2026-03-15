import argparse
import sys

from .storage import add_task, list_tasks, remove_task


def _cmd_add(args):
    task = add_task(args.text)
    print(f"Added task {task.id}")


def _cmd_list(args):
    tasks = list_tasks()
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        print(f"{task.id}: {task.text}")


def _cmd_remove(args):
    try:
        remove_task(args.id)
        print(f"Removed task {args.id}")
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("text", help="Task description")
    parser_add.set_defaults(func=_cmd_add)

    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.set_defaults(func=_cmd_list)

    parser_remove = subparsers.add_parser("remove", help="Remove a task by id")
    parser_remove.add_argument("id", type=int, help="Task ID")
    parser_remove.set_defaults(func=_cmd_remove)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
