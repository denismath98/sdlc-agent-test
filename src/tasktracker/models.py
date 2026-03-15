from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any


@dataclass
class Task:
    id: int
    text: str
    completed: bool
    created_at: datetime

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["created_at"] = self.created_at.isoformat()
        return data

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Task":
        return Task(
            id=data["id"],
            text=data["text"],
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"]),
        )
