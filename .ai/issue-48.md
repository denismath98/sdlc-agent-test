# Добавить функцию подсчета заметок не содержащих тэга

## Задача

Добавить в `src/reporting/summary.py` функцию `count_notes_without_tags(notes)` и вывести это значение в `src/reporting/cli.py`.

## Контекстные файлы

- `src/reporting/summary.py`
- `src/reporting/cli.py`
- `src/notebook/models.py`
- `src/notebook/storage.py`
- `tests/test_reporting.py`
- `tests/test_reporting_cli.py`

## Требования

- реализовать функцию `count_notes_without_tags(notes) -> int`
- функция должна считать количество заметок, у которых список `tags` пустой
- CLI должен печатать строку:
  `without_tags=<n>`
- сохранить текущий вывод `total=...` и статистику по тегам
- обновить тесты reporting
- не менять остальные модули без необходимости

## Ограничения

- не менять формат уже существующих строк вывода
- не изменять структуру `Note`
- не удалять существующие функции в `summary.py`

Generated: 2026-03-16 18:11:59.423701