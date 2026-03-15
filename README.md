# README.md
# Todo CLI

A minimal todo list manager that stores tasks in a JSON file.

## Installation

```bash
pip install .
```

## Usage

Run the CLI as a module:

```bash
python -m src.todo add "Buy milk"
python -m src.todo list
python -m src.todo remove 1
```

Or use the installed console script:

```bash
todo add "Buy milk"
todo list
todo remove 1
```
