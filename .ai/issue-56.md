# Экспорт заметок в текстовый формат

## Задача

Добавить новый пакет `src/exporting`, который позволяет экспортировать заметки в текстовый формат и использовать существующую логику проекта без нарушения совместимости.

## Контекстные файлы

- `src/notebook/models.py`
- `src/notebook/storage.py`
- `src/notebook/search.py`
- `src/notebook/cli.py`
- `src/reporting/summary.py`
- `src/reporting/cli.py`
- `tests/test_storage.py`
- `tests/test_search.py`
- `tests/test_notebook_cli.py`
- `tests/test_reporting.py`
- `tests/test_reporting_cli.py`

## Новая структура

Нужно добавить:

- `src/exporting/__init__.py`
- `src/exporting/text_export.py`
- `src/exporting/cli.py`
- `tests/test_text_export.py`
- `tests/test_exporting_cli.py`

## Требования

### 1. Экспорт заметок в текст
В `src/exporting/text_export.py` реализовать функцию:

`export_notes_as_text(notes: list[Note]) -> str`

Формат вывода строго такой:

```text
[1] A :: work :: x
[2] B :: home :: y
[3] C :: work,draft :: z
```

Правила:
- одна заметка на строку
- формат строки должен совпадать с форматом, который уже используется в notebook CLI
- если тегов нет, середина должна быть пустой:
  `[4] D ::  :: no tags`
- порядок заметок должен сохраняться

### 2. Фильтрация перед экспортом
В `src/exporting/text_export.py` реализовать функцию:

`export_filtered_notes_as_text(notes: list[Note], query: str | None = None, tag: str | None = None) -> str`

Правила:
- если передан `query`, использовать существующую логику `search_notes`
- если передан `tag`, использовать существующую логику `filter_by_tag`
- если переданы оба параметра, сначала выполнять `query`, затем `tag`
- если после фильтрации заметок нет, вернуть пустую строку
- не дублировать уже существующую бизнес-логику поиска и фильтрации, если можно использовать существующие функции проекта

### 3. Новый CLI
В `src/exporting/cli.py` реализовать CLI:

```bash
python -m src.exporting.cli --file notes.json
python -m src.exporting.cli --file notes.json --query report
python -m src.exporting.cli --file notes.json --tag work
python -m src.exporting.cli --file notes.json --query report --tag work
```

Поведение:
- загружать заметки через существующую функцию `load_notes`
- использовать `export_filtered_notes_as_text`
- печатать результат в stdout
- если заметок нет, stdout должен быть пустым
- exit code 0

### 4. Совместимость
Очень важно:
- не менять модель `Note`
- не менять сигнатуры существующих функций в `notebook` и `reporting`
- не ломать существующие тесты
- не переносить существующую бизнес-логику в CLI-модули
- не импортировать бизнес-логику из одного CLI-модуля в другой CLI-модуль
- если нужно переиспользовать форматирование заметки, сделать это архитектурно корректно

### 5. Тесты
Добавить тесты, которые проверяют:
- экспорт всех заметок
- экспорт заметок без тегов
- фильтрацию по query
- фильтрацию по tag
- фильтрацию по query + tag
- пустой результат
- работу CLI

## Ограничения

- новый код должен быть совместим с существующей кодовой базой
- изменения в существующих пакетах допускаются только если это действительно необходимо для переиспользования логики
- не переписывать существующие модули без необходимости
- если требуется общий вспомогательный код, его нужно вынести в подходящий не-CLI модуль

Generated: 2026-03-16 18:34:28.292243