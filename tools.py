"""
uv add black - форматировщик
1) black команды:
    black --help
    black name_file (.)

uv add mypy - статический анализатор
1) mypy команды:
    mypy --help
    mypy name_file (.)

uv add pylint - линтер (строгий анализатор)
1) pylint команды:
    pylint --help
    pylint name_file (.)

uv add ruff (форматировщик + линтер)
1) ruff команды:
    ruff --help
    ruff name_file (.)
"""


def add(a: int, b: int, c: int) -> str:
    return a + b


add(1, 2)
add(1, "2")
add(1,)
