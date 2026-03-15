from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(eq=True, frozen=False)
class Task:
    id: int
    text: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
        }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Task":
        return Task(
            id=data["id"],
            text=data["text"],
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"]),
        )
