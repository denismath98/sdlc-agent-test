import os
import json
import yaml
from typing import Dict


def load_config(path: str) -> Dict:
    """
    Load a configuration file in JSON or YAML format.

    Args:
        path: Path to the configuration file.

    Returns:
        A dictionary representing the configuration.

    Raises:
        ValueError: If the file does not exist or has an unsupported extension.
    """
    if not os.path.isfile(path):
        raise ValueError(f"Configuration file not found: {path}")

    _, ext = os.path.splitext(path.lower())
    with open(path, "r", encoding="utf-8") as f:
        if ext == ".json":
            data = json.load(f)
        elif ext in {".yaml", ".yml"}:
            data = yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported configuration file type: {ext}")

    if not isinstance(data, dict):
        raise ValueError(
            "Configuration file must contain a JSON/YAML object at the top level."
        )
    return data
