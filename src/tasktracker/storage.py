import json
from pathlib import Path
from typing import List
from .models import Task


class JSONStorage:
    def __init__(self, file_path: Path | str = "tasks.json"):
        self.file_path = Path(file_path)
        if not self.file_path.parent.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def load_tasks(self) -> List[Task]:
        try:
            raw = self.file_path.read_text(encoding="utf-8")
            data = json.loads(raw)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
        return [Task.from_dict(item) for item in data]

    def save_tasks(self, tasks: List[Task]) -> None:
        data = [task.to_dict() for task in tasks]
        self.file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
