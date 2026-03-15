import sys
from click.testing import CliRunner
from src.tasktracker import cli


def test_cli_create_and_list(monkeypatch, tmp_path):
    # Redirect storage to temporary file
    from src.tasktracker.service import _storage as original_storage
    from src.tasktracker.storage import JSONStorage

    temp_storage = JSONStorage(tmp_path / "tasks.json")
    monkeypatch.setattr("src.tasktracker.service._storage", temp_storage)

    runner = CliRunner()
    result = runner.invoke(cli.main, ["create", "Demo task"])
    assert result.exit_code == 0
    assert "Demo task" in result.output

    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0
    assert "Demo task" in result.output


def test_cli_complete_and_delete(monkeypatch, tmp_path):
    from src.tasktracker.service import _storage as original_storage
    from src.tasktracker.storage import JSONStorage

    temp_storage = JSONStorage(tmp_path / "tasks.json")
    monkeypatch.setattr("src.tasktracker.service._storage", temp_storage)

    runner = CliRunner()
    # create
    create_res = runner.invoke(cli.main, ["create", "Task to complete"])
    assert create_res.exit_code == 0
    # extract id from output
    line = create_res.output.splitlines()[0]
    task_id = int(line.split("]")[0].strip("["))

    # complete
    comp_res = runner.invoke(cli.main, ["complete", str(task_id)])
    assert comp_res.exit_code == 0
    assert "✅" in comp_res.output

    # delete
    del_res = runner.invoke(cli.main, ["delete", str(task_id)])
    assert del_res.exit_code == 0
    assert "deleted" in del_res.output.lower()
