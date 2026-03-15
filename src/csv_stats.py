import csv
import json
import argparse
import sys
from typing import Dict, Any

__all__ = ["compute_column_stats"]


def compute_column_stats(path: str) -> Dict[str, Dict[str, Any]]:
    """
    Compute min, max and mean for each numeric column in a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        A dictionary mapping column names to a dict with keys "min", "max", "mean".
    """
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                return {}

            # Assume all columns are numeric until proven otherwise
            numeric_cols = set(reader.fieldnames)
            stats: Dict[str, Dict[str, Any]] = {
                col: {"sum": 0.0, "count": 0, "min": None, "max": None}
                for col in numeric_cols
            }

            for row in reader:
                # Iterate over a copy because we may modify numeric_cols during loop
                for col in list(numeric_cols):
                    value = row.get(col, "")
                    try:
                        num = float(value)
                    except (ValueError, TypeError):
                        # Column is not numeric; discard it
                        numeric_cols.remove(col)
                        stats.pop(col, None)
                        continue

                    col_stats = stats[col]
                    col_stats["sum"] += num
                    col_stats["count"] += 1
                    if col_stats["min"] is None or num < col_stats["min"]:
                        col_stats["min"] = num
                    if col_stats["max"] is None or num > col_stats["max"]:
                        col_stats["max"] = num

            # Build final result
            result: Dict[str, Dict[str, Any]] = {}
            for col, col_stats in stats.items():
                if col_stats["count"] == 0:
                    continue
                mean = col_stats["sum"] / col_stats["count"]
                result[col] = {
                    "min": col_stats["min"],
                    "max": col_stats["max"],
                    "mean": mean,
                }
            return result

    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path}") from e
    except csv.Error as e:
        raise csv.Error(f"Error reading CSV file: {e}") from e


def _main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute numeric column statistics for a CSV file."
    )
    parser.add_argument("csv_path", help="Path to the CSV file")
    args = parser.parse_args()

    try:
        stats = compute_column_stats(args.csv_path)
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except csv.Error as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    _main()
