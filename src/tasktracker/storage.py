import json
from pathlib import Path
from threading import Lock
from typing import List

from .models import Task

DEFAULT_STORAGE_FILE = Path("tasks.json")


class JSONStorage:
    _instance = None
    _lock = Lock()

    def __new__(cls, file_path: Path | None = None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._init(file_path or DEFAULT_STORAGE_FILE)
            return cls._instance

    def _init(self, file_path: Path) -> None:
        self.file_path = file_path
        self._file_lock = Lock()
        # Ensure the file exists
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def _load(self) -> List[Task]:
        with self._file_lock:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            return [Task.from_dict(item) for item in data]

    def _save(self, tasks: List[Task]) -> None:
        with self._file_lock:
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)

    def get_all(self) -> List[Task]:
        return self._load()

    def save_all(self, tasks: List[Task]) -> None:
        self._save(tasks)

    def generate_id(self) -> int:
        tasks = self._load()
        if not tasks:
            return 1
        return max(t.id for t in tasks) + 1


def get_storage(file_path: Path | None = None) -> JSONStorage:
    return JSONStorage(file_path)
