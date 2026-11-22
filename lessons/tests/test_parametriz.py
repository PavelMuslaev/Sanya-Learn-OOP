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
            (5, 10, 15),
            (15, 100, 115),
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



@pytest.fixture 
def user_profile_factory(): 
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












