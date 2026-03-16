# Добавить поддержку фильтрации заметок без тегов в notebook CLI и reporting CLI

## Задача

Добавить поддержку фильтрации заметок без тегов в notebook CLI и reporting CLI.

## Контекстные файлы

- `src/notebook/cli.py`
- `src/notebook/search.py`
- `src/reporting/summary.py`
- `src/reporting/cli.py`
- `src/notebook/models.py`
- `tests/test_notebook_cli.py`
- `tests/test_reporting.py`
- `tests/test_reporting_cli.py`

## Требования

- в `src/notebook/cli.py` добавить флаг `--without-tags`
- при использовании `--without-tags` выводить только заметки, у которых `tags == []`
- в `src/reporting/summary.py` использовать ту же логику для подсчёта заметок без тегов
- `src/reporting/cli.py` должен печатать строку `without_tags=<n>`
- обновить тесты notebook CLI, reporting и reporting CLI
- не менять существующие сигнатуры функций без необходимости

## Ограничения

- не менять формат уже существующего вывода
- не менять модель `Note`
- не удалять существующие функции
- изменения должны быть минимальными и совместимыми с существующим кодом

Generated: 2026-03-16 18:21:31.772166