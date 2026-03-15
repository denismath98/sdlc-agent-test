# tests/test_cli.py
import os
import subprocess
import sys
from pathlib import Path

def run_cli(args, env):
    result = subprocess.run(
        [sys.executable, "-m", "src.todo"] + args,
        env=env,
        capture_output=True,
        text=True,
    )
    return result

def test_cli_add_list_remove(tmp_path):
    tasks_file = tmp_path / "tasks.json"
    env = os.environ.copy()
    env["TODO_TASKS_FILE"] = str(tasks_file)

    # Add a task
    res_add = run_cli(["add", "CLI task"], env)
    assert res_add.returncode == 0
    assert "Added task 1" in res_add.stdout

    # List tasks
    res_list = run_cli(["list"], env)
    assert res_list.returncode == 0
    assert "1: CLI task" in res_list.stdout

    # Remove task
    res_remove = run_cli(["remove", "1"], env)
    assert res_remove.returncode == 0
    assert "Removed task 1" in res_remove.stdout

    # List again, should be empty
    res_list2 = run_cli(["list"], env)
    assert res_list2.returncode == 0
    assert "No tasks." in res_list2.stdout
