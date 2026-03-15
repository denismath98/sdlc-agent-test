import os
import subprocess
import sys
from pathlib import Path

import pytest


def run_cli(args, env):
    """Run the todo CLI as a subprocess."""
    cmd = [sys.executable, "-m", "src.todo"] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    return result


@pytest.fixture
def cli_env(tmp_path, monkeypatch):
    # Ensure the package can be imported
    pythonpath = f"{Path.cwd()}:{tmp_path}"
    env = os.environ.copy()
    env["PYTHONPATH"] = pythonpath
    # Redirect tasks file to a temporary location
    env["TODO_TASKS_FILE"] = str(tmp_path / "tasks.json")
    return env


def test_cli_add_and_list(cli_env):
    # Add a task
    add_res = run_cli(["add", "CLI task"], env=cli_env)
    assert add_res.returncode == 0
    assert "Added task" in add_res.stdout

    # List tasks
    list_res = run_cli(["list"], env=cli_env)
    assert list_res.returncode == 0
    assert "1: CLI task" in list_res.stdout


def test_cli_remove_success(cli_env):
    # Add a task to remove
    run_cli(["add", "To be removed"], env=cli_env)

    # Remove it
    rm_res = run_cli(["remove", "1"], env=cli_env)
    assert rm_res.returncode == 0
    assert "Removed task 1" in rm_res.stdout

    # Verify it's gone
    list_res = run_cli(["list"], env=cli_env)
    assert list_res.returncode == 0
    assert "No tasks." in list_res.stdout


def test_cli_remove_nonexistent(cli_env):
    # Attempt to remove a task that doesn't exist
    rm_res = run_cli(["remove", "42"], env=cli_env)
    assert rm_res.returncode != 0
    assert "does not exist" in rm_res.stderr
