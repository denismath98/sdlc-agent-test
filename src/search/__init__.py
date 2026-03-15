import os
from pathlib import Path
from typing import List, Tuple


def search_in_files(directory: str, pattern: str) -> List[Tuple[str, int, str]]:
    """
    Recursively search for lines containing `pattern` in all files under `directory`.

    Returns:
        List of tuples (file_path, line_number, line_text) where:
            - file_path is the absolute path to the file,
            - line_number is 1‑based,
            - line_text is the original line (including newline).
    """
    results: List[Tuple[str, int, str]] = []
    base_path = Path(directory).resolve()

    for root, _, files in os.walk(base_path):
        for file_name in files:
            file_path = Path(root) / file_name
            try:
                with file_path.open("r", encoding="utf-8", errors="ignore") as f:
                    for idx, line in enumerate(f, start=1):
                        if pattern in line:
                            results.append((str(file_path), idx, line))
            except (OSError, UnicodeDecodeError):
                # Skip files that cannot be read
                continue
    return results
