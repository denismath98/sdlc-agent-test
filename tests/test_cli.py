import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from src.tasktracker.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_create_and_complete_and_delete(runner):
    # Create a task
    result = runner.invoke(cli, ["create", "Demo task"])
    assert result.exit_code == 0
    # Expect output like "[1] Demo task"
    assert "[1]" in result.output
    assert "Demo task" in result.output
    # Parse the id
    task_id = int(result.output.split("[")[1].split("]")[0])

    # Complete the task
    result = runner.invoke(cli, ["complete", str(task_id)])
    assert result.exit_code == 0
    assert "✅" in result.output
    assert f"[{task_id}]" in result.output

    # List tasks and verify completed status
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert f"[
