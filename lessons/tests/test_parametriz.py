"""
Нам часто требуется проверить одну и туже функцию на 
разных наборах данных, и чтобы не создавать тысячу однотипных 
фикстур или не прокидывать вручную бесконечные assert-ы с 
прямым вызовом функций, существует параметризация, которая 
реализуется с помощью декортора pytest.mark.parametrize: 
"""



import pytest 
from typing import Callable
 
class Calculator: 
    @staticmethod
    def divide(x: int | float, y: int | float) -> int | float: 
        return x / y 

    @staticmethod
    def add(x: int | float, y: int | float) -> int | float: 
        return x + y

class TestCalculator:
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (10, 20, 30),
            pytest.param(5, 10, 15, id="999"),
            pytest.param(15, 100, 115, id="Final Test"),
        ]
    )
    def test_add_positive(self, num1, num2, result):
        assert Calculator.add(num1, num2) == result

    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (-1, -2, -3),
            (-2, -4, -6),
            (-3, -5, -8),
        ]
    )
    def test_add_negative(self, num1, num2, result):
        assert Calculator.add(num1, num2) == result

    @pytest.mark.parametrize(
            "num1, num2, res",
            [
                (1, "0", TypeError),
                pytest.param(-2, 0, ZeroDivisionError, id="DIVIDE ON 0 IS BAD!"),
                ("3", 10, TypeError),
            ]
        )
    def test_divide_error(self, num1, num2, res):
        with pytest.raises(res):
            assert Calculator.divide(num1, num2)


@pytest.fixture 
def user_profile_factory(): 
    # Фабрика (Фабричная функция)
    def _create_user_profile(name, role="viewer"): 
        return {"username": name, "role": role, "permissions": []} 
 
    return _create_user_profile

@pytest.mark.parametrize( 
    "role_to_assign, expected_permissions_count", 
    [ 
        ("admin", 5), 
        ("editor", 3), 
        ("viewer", 1), 
    ] 
) 
def test_user_permissions_after_role_assignment( 
    print_end_start_session: Callable,
    user_profile_factory: Callable, 
    role_to_assign: str, 
    expected_permissions_count: int,
): 
    profile = user_profile_factory(name="testuser")

    # Имитируем логику присвоения прав в зависимости от роли 
    if role_to_assign == "admin": 
        profile["permissions"] = ["read", "write", "delete", "manage_user", "publish"] 
    elif role_to_assign == "editor": 
        profile["permissions"] = ["read", "write", "publish"] 
    elif role_to_assign == "viewer": 
        profile["permissions"] = ["read"]

    profile["role"] = role_to_assign 

    assert profile["role"] == role_to_assign 
    assert len(profile["permissions"]) == expected_permissions_count












