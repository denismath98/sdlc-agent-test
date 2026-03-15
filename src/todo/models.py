# src/todo/models.py
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    text: str
