import tempfile
import shutil
from pathlib import Path

import pytest

from src.tasktracker.storage import JSONStorage, get_storage


@pytest.fixture(autouse=True)
def isolated_storage(tmp_path_factory):
    """Replace the default storage file with a temporary one for each test."""
    temp_dir = tmp_path_factory.mktemp("tasktracker")
    storage_path = temp_dir / "tasks.json"
    # Re‑initialize the singleton with the temporary path
    JSONStorage._instance = None  # type: ignore
    storage = get_storage(storage_path)
    yield
    # Cleanup
    if storage_path.exists():
        storage_path.unlink()
