# Todo storage

Создать пакет src/todo.

Структура:

src/todo/models.py
src/todo/storage.py
src/todo/cli.py

Функциональность:

add_task(text)
list_tasks()
remove_task(id)

Хранение задач в JSON файле tasks.json.

CLI:

python -m src.todo add "task"
python -m src.todo list
python -m src.todo remove 1

Добавить тесты.

Generated: 2026-03-15 13:33:41.412527