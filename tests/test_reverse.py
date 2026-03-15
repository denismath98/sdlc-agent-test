import subprocess
import sys

import pytest

from src.reverse import reverse_string


def test_reverse_abc():
    assert reverse_string("abc") == "cba"


def test_reverse_empty():
    assert reverse_string("") == ""


def test_reverse_single_char():
    assert reverse_string("a") == "a"


def test_cli_output():
    # Run the module as a script using the -m flag.
    result = subprocess.run(
        [sys.executable, "-m", "src.reverse", "hello"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "olleh"
