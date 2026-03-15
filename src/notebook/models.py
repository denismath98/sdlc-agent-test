from dataclasses import dataclass, field


@dataclass
class Note:
    id: int
    title: str
    text: str
    tags: list[str] = field(default_factory=list)
