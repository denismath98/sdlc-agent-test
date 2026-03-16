# Добавить в CLI поддержку флага `--exact-title`

## Задача

Добавить в `src/notebook/cli.py` поддержку флага `--exact-title`.

## Контекстные файлы

- `src/notebook/cli.py`
- `src/notebook/search.py`
- `src/notebook/models.py`
- `tests/test_search.py`
- `tests/test_notebook_cli.py`

## Требования

- если передан `--exact-title VALUE`, CLI должен использовать поиск по точному совпадению заголовка
- для поиска использовать функцию `find_by_exact_title`
- сохранить текущую поддержку `--query` и `--tag`
- не удалять существующую логику CLI
- обновить тесты CLI и search
- не менять остальные модули без необходимости

## Ограничения

- не менять формат вывода `format_note_line`
- не менять модель `Note`
- не менять существующие публичные функции без необходимости

Generated: 2026-03-16 18:06:26.457465