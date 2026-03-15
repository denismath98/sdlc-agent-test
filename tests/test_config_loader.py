import json
import yaml
import pytest
from src.config_loader import load_config


def test_load_json_config(tmp_path):
    config_data = {"key": "value", "number": 42}
    json_file = tmp_path / "config.json"
    json_file.write_text(json.dumps(config_data), encoding="utf-8")

    loaded = load_config(str(json_file))
    assert loaded == config_data


def test_load_yaml_config(tmp_path):
    config_data = {"name": "example", "list": [1, 2, 3]}
    yaml_file = tmp_path / "config.yaml"
    yaml_file.write_text(yaml.safe_dump(config_data), encoding="utf-8")

    loaded = load_config(str(yaml_file))
    assert loaded == config_data


def test_load_yaml_with_yml_extension(tmp_path):
    config_data = {"a": 1}
    yml_file = tmp_path / "config.yml"
    yml_file.write_text(yaml.safe_dump(config_data), encoding="utf-8")

    loaded = load_config(str(yml_file))
    assert loaded == config_data


def test_nonexistent_file_raises(tmp_path):
    nonexistent = tmp_path / "does_not_exist.json"
    with pytest.raises(ValueError) as excinfo:
        load_config(str(nonexistent))
    assert "Configuration file not found" in str(excinfo.value)


def test_unsupported_extension_raises(tmp_path):
    txt_file = tmp_path / "config.txt"
    txt_file.write_text("just some text", encoding="utf-8")
    with pytest.raises(ValueError) as excinfo:
        load_config(str(txt_file))
    assert "Unsupported configuration file type" in str(excinfo.value)
