"""
Инструменты проверки качества кода.

Установка зависимостей:
    uv add black mypy pylint ruff

Black — форматировщик:
    uv run black homework/name_file.py
    uv run black --check homework/name_file.py

Ruff — быстрый линтер:
    uv run ruff check homework/name_file.py

Pylint — строгий анализатор качества:
    uv run pylint homework/name_file.py

mypy — статический анализатор аннотаций типов:
    uv run mypy homework/name_file.py

Команды выполняются из корня репозитория. Вместо homework/name_file.py
указывай точный путь только к модулю текущей задачи. Не используй ".",
"*.py", целые папки homework/ и lessons/ и не запускай инструменты
для остальных учебных модулей.
"""


def add(a: int, b: int, c: int) -> str:
    return a + b


add(1, 2)
add(1, "2")
add(1,)
