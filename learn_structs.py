"""
    Отладка - процесс поиска и устранения ошибок.

    Режим Дебаг - инструмент для анализа кодовой базы.

    Bug - (баг/жук).

    Стек - адресное пространство нашей программа.
        Стек состоит из кадров (Вызовы функций, по умолчанию есть глобальный кадр). 

    Метаданные - данные о данных.
"""



from dataclasses import dataclass, field

"""
    @dataclass — это декоратор в Python из модуля dataclasses, 
    который автоматически генерирует специальные методы для классов, 
    предназначенных в основном для хранения данных. Он появился в Python 3.7.
    
    Автоматически создает методы:
    __init__() — инициализатор с аргументами для всех полей 
    __repr__() — читаемое строковое представление
    __eq__() — сравнение по значению полей
    
    (опционально) __hash__(), __lt__() и другие
"""

@dataclass(frozen=True)
class User:
    name: str
    surname: str
    age: int = 0
    gender: str = field(default="male", kw_only=True, doc="Это пол пользователя.")

    def __post_init__(self): # Проверка атрибутов
        """Он выполняется после того, как переменной было присвоено значение."""
        if not isinstance(self.name, str):
            raise ValueError
        if not isinstance(self.surname, str):
            raise ValueError

        

user1 = User("Денис", "Лебедев", 22)
user2 = User("Денис", "Лебедев", 22)

# user1.name = "Буба" # frozen=True запрещает изменять
print(user1) # User(name='Денис', surname='Лебедев', age=22)

print(user1 == user2)
print()

from enum import StrEnum, IntEnum, Enum

class CodeError(Enum):
    FATAL = 12
    BUG = 100

class Device(StrEnum):
    LAPTOP = "LAPTOP :)"
    PHONE = "phone"

print(Device.LAPTOP == "LAPTOP :)")

month = 12

match month:
    case 12:
        print(1)
    case 11:
        print(2)
    case _:
        print(3)

user_code = 12
if user_code == CodeError.FATAL:
    pass


user = ("Павел", 22, "муж.")

match user:
    case name, age, "муж.":
        print("aidjsaoj")
    case _, _, "жен.":
        print("aidjsaoj")


