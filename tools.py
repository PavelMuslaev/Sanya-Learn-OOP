"""
Инструменты проверки качества кода.

Установка зависимостей:
    uv add black mypy pylint ruff

Black — форматировщик:
    uv run black name_file.py
    uv run black --check name_file.py

Ruff — быстрый линтер:
    uv run ruff check name_file.py

Pylint — строгий анализатор качества:
    uv run pylint name_file.py

mypy — статический анализатор аннотаций типов:
    uv run mypy name_file.py

В домашних заданиях вместо name_file.py указывай только модуль,
который разрабатываешь в текущей задаче. Не используй ".", "*.py"
и не запускай инструменты для остальных учебных модулей.
"""


def add(a: int, b: int, c: int) -> str:
    return a + b


add(1, 2)
add(1, "2")
add(1,)
