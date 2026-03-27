import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Import the function to be tested
from src.search import search_in_files


class TestSearchInFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory with a known structure
        self.temp_dir = tempfile.TemporaryDirectory()
        base = Path(self.temp_dir.name)

        # File 1
        (base / "file1.txt").write_text("first line\nTODO: fix this\nlast line\n")
        # File 2
        (base / "subdir").mkdir()
        (base / "subdir" / "file2.py").write_text(
            "# TODO implement feature\nprint('hello')\n"
        )
        # File 3 (no match)
        (base / "file3.md").write_text("nothing to see here\n")

        self.base_path = str(base)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_search_todo(self):
        pattern = "TODO"
        results = search_in_files(self.base_path, pattern)
        # Normalize paths for comparison
        results_set = {
            (Path(p).relative_to(self.base_path).as_posix(), ln, txt)
            for p, ln, txt in results
        }
        expected = {
            ("file1.txt", 2, "TODO: fix this\n"),
            ("subdir/file2.py", 1, "# TODO implement feature\n"),
        }
        self.assertEqual(results_set, expected)

    def test_search_nonexistent(self):
        pattern = "NONEXISTENT"
        results = search_in_files(self.base_path, pattern)
        self.assertEqual(results, [])

    def test_cli_output(self):
        pattern = "TODO"
        cmd = [sys.executable, "-m", "src.search", self.base_path, pattern]
        completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output_lines = completed.stdout.strip().splitlines()
        # Expected lines (order may vary)
        expected_lines = {
            f"{Path(self.base_path) / 'file1.txt'}:2: TODO: fix this",
            f"{Path(self.base_path) / 'subdir' / 'file2.py'}:1: # TODO implement feature",
        }
        self.assertEqual(set(output_lines), expected_lines)


if __name__ == "__main__":
    unittest.main()
