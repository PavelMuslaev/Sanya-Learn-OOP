"""
Что такое self?
self - это некий конкретный экземпляр класса,
    т.е. self нужен для связи с объектом класса.
В конструкции:
    dog_barbos = Dog('Барбос', 21), передача на самом  деле
происходит следующим образом:
    dog_barbos = Dog(dog_barbos, 'Барбос', 21),
а вот это:
    dog2.sit() превращается в вот это:
    sit(dog2)


Из чего состоит класс?
Две ключевых основы класса:
    1) Свойства - это атрибуты класса;
    2) Поведение - это методы класса.


Два вида атрибутов:
    1) Атрибуты уровня класса (Общий для всех,
                    обращение происходит через имя класса,
                    но также остаётся возможность взаимодействия
                    через экземпляр класса.);
    2) Атрибуты уровня экземпляра.


Виды методов:
    1) Метод экземпляра (обычные методы) -
        это вид методов, которые напрямую взаимодействуют
        через self.;
    2) Специальные (магические, дандер) методы — это методы с именами,
        начинающимися и заканчивающимися двойными подчеркиваниями
        (например, __init__). Они имеют специальное значение в Python и
        часто используются для перегрузки операторов или определения
        стандартного поведения объектов.
    3) Методы класса - это методы, которые принимают класс
        (а не экземпляр) в качестве первого параметра,
        обычно называемого cls. Они декорируются с помощью @classmethod
        и обычно используются для создания альтернативных конструкторов
        или для работы с атрибутами класса.
    4) Статические методы — это методы, которые не принимают
        ни self, ни cls. Они декорируются с помощью @staticmethod и
        обычно используются для вспомогательных функций, логически
        связанных с классом, но не требующих доступа к состоянию класса
        или экземпляра.
    5) Абстрактные методы - В Python абстрактные методы — это методы, которые объявлены в классе,
        но не имеют реализации и обязаны быть переопределены в подклассах.
        Они используются для создания абстрактных классов — классов,
        которые нельзя напрямую инстанцировать, а можно только наследовать.


    ВСЁ В PYTHON - ЭТО ОБЪЕКТ, ТАК КАК ВСЁ В PYTHON БАЗИРУЕТСЯ НА КЛАССАХ:
    1) ВСТРОЕННЫЕ КЛАССЫ (ТИПЫ ДАННЫХ) В PYTHON:
        - str;
        - int;
        - float;
        - bool;
        - list;
        - tuple;
        - set;
        - dict;
        - None;
        и д.р.
    2) КАСТОМНЫЕ ТИПЫ ДАННЫХ (ЭТО НАШИ ПОЛЬЗОВАТЕЛЬСКИЕ КЛАССЫ).


    ПРАВИЛА ООП: 💎💎💎💎💎💎💎💎💎
    1) НАСЛЕДОВАНИЕ - Наследование – это такой тип отношений когда объект
        «является» специализацией другого класса. (Всё в Python наследуется от класса object);
    2) АБСТРАКЦИЯ - это "чертёж" или "шаблон" для других классов.
        Он описывает что должно быть сделано, но не как это делать.
    3) ИНКАПСУЛЯЦИЯ в Python - это принцип, при котором данные (переменные) 
        и методы (функции), работающие с этими данными, 
        объединяются в единый компонент - класс. 
        При этом доступ к внутренней реализации
        объекта ограничивается снаружи.
        Инкапсуляция - это скрытие реализации, за удобным интерфейсом.
        Пользователю не надо знать, как работает пульт, чтобы пользоваться
            пультом.

    4) ПОЛИМОРФИЗМ — позволяет одному и тому же коду работать с объектами разных типов, 
        и в зависимости от типа объекта метод выполняет разную логику. 
        Проще говоря: вы вызываете один и тот же метод для разных объектов, и каждый из них «отвечает» по-своему. 
        
        Полиморфизм - это способность объектов разных классов реагировать на одинаковые методы или операции по-разному.
        В переводе с греческого "полиморфизм" означает "много форм".


    Python использует MRO (Method Resolution Order) (Порядок разрешения метода) -
    специальный порядок поиска методов, чтобы не было конфликтов "чей метод вызывать,
    если у родителей есть одинаковые методы".


    # uv init
    # uv venv
    # uv tree
    # uv add
    # uv remove
    # uv sync
    # uv help
"""

class Dog:
    """Модель собаки"""

    def __init__(self, name: str, age: int) -> None:
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} сядь!")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} перекатись!")


# Экземпляр (объект) класса Dog
dog_barbos = Dog("Барбос", 21)
print(f"Мою собаку зовут {dog_barbos.name}.")
print(f"Ей {dog_barbos.age} лет.")

dog2 = Dog("Рэкс", 20)
dog2.sit()
dog2.roll_over()
print("\n")


class Student:
    name_organization = "МАИ"  # Атрибут уровня класса

    def __init__(self, name, age):
        self.name = name  # атрибут уровня экземпляра
        self.age = age  # атрибут уровня экземпляра

    def hello(self):
        return "Привет, " + self.name + "!"


print(Student.name_organization)

pavel = Student("Pavel", 21)
miron = Student("Miron", 21)
print(f"Паша учится в: {pavel.name_organization}")

Student.name_organization = "МГУ"
print(f"Паша учится в: {pavel.name_organization}")
print(f"Мирон учится в: {miron.name_organization}")

pavel.name_organization = "МАИ"
print(f"Паша учится в: {pavel.name_organization}")
print(f"Мирон учится в: {miron.name_organization}")
print("\n\n")


def counter(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        return counter, func(*args, **kwargs)

    return wrapper


from time import time as t


@counter
def time():
    return t()


print(time())
print("\n")


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_str(cls, date: str):
        day, month, year = map(int, date.split("."))
        return cls(day, month, year)

    @counter
    def display(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"


current_date = Date(12, 12, 2022)
print(current_date.display())

date2 = Date.date_str("25.12.2023")
print(date2.display())
print("\n")


class Calculator:
    @staticmethod
    def add(*args) -> int:
        return sum(args)

    @staticmethod
    def sub(num1, num2) -> int:
        return num1 - num2


print(Calculator.sub(5, 6))
print(Calculator.add(5, 6, 2, 4, 5, 6))
print(Calculator.add(11, 22))
print("\n")


class Vector2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other: Vector2D) -> Vector2D:
        # Перегрузка оператора +
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: int) -> Vector2D:
        # Перегрузка оператора *
        return Vector2D(self.x * scalar, self.y * scalar)

    def display(self) -> str:
        return f"x: {self.x}, y: {self.y}"


vec = Vector2D(2, 3)
vec2 = Vector2D(10, 2)
print(f"У меня есть вектор: {vec}")  # У меня есть вектор: x: 2, y: 3
print(vec)  # x: 2, y: 3
print(vec.display())  # x: 2, y: 3

total_vec = vec + vec2
print(total_vec)  # x: 12, y: 5

print(total_vec * 2)

a = 5
b = 7

c = a + b

print(type(a))  # <class 'int'>
print(type(vec))  # <class '__main__.Vector2D'>
print("\n")


# РОДИТЕЛЬСКИЙ/БАЗОВЫЙ/СУПЕРКЛАСС КЛАСС
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Какие-то звуки!"


# ДОЧЕРНИЙ/ПРОИЗВОДНЫЙ/ПОДКЛАСС КЛАСС
class Cat(Animal):  # КЛАСС CAT НАСЛЕДУЕТСЯ ОТ ANIMAL
    def speak(self):
        return f"Кот: {self.name}, говорит мяу!"


class Dog(Animal):
    def speak(self):
        return f"Собака: {self.name}, говорит гав!"


# Создаем экземпляры класса
animal = Animal("Существо", 15)
cat = Cat("Нестор", 11)

print(animal.speak())
print(cat.speak())  # вызываем переопределенный метод
print(cat.name)  # используем унаследованный атрибут
print("\n")


# Функция super() в Python нужна для корректного и безопасного вызова методов родительского
# класса при наследовании. Она упрощает работу с иерархией классов и гарантирует,
# что методы вызываются в правильном порядке, особенно при множественном наследовании.


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"{self.name.capitalize()} {self.age} лет."


class Cat(Animal):
    def __init__(self, name, age, count_life):
        super().__init__(name, age)
        self.count_life = count_life

    def info(self) -> str:
        return super().info() + f"\nCount life: {self.count_life}."


cat = Cat("dina", 10, 9)
print(cat.info())
print("\n")


# ЦЕПОЧКА НАСЛЕДОВАНИЯ
class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Human):
    def __init__(self, name: str, age: int, salary: float) -> None:
        super().__init__(name, age)
        self.salary = salary

    def info(self) -> str:
        return f"{super().info()}, Salary: {self.salary}"


class Director(Employee):
    def __init__(self, name: str, age: int, salary: float, office: int) -> None:
        super().__init__(name, age, salary)
        self.office = office

    def info(self) -> str:
        return f"{super().info()}, Office: {self.office}"


human = Human("Павел", 21)
print(human.info())

employee = Employee("Павел", 21, 150_000)
print(employee.info())

director = Director("Павел", 21, 150_000, 300)
print(director.info())
print("\n")


# ISINSTANCE() И ISSUBCLASS()
# Является ли director экземпляром класса Director
print(isinstance(director, Director))  # True

# Является ли director экземпляром класса Employee (через наследование)
print(isinstance(director, Employee))  # True

# Является ли director экземпляром класса Human (через наследование)
print(isinstance(director, Human))  # True

# Является ли director экземпляром класса object (через наследование)
print(isinstance(director, object))  # True

# Является ли 10 экземпляром класса int (через наследование)
print(isinstance(10, int))  # True

# Является ли employee экземпляром класса Director (через наследование)
print(isinstance(employee, Director))  # False

# Является ли "10" экземпляром класса int (через наследование)
print(isinstance("10", (int, bool)))  # False

# Является ли класс Director подклассом Employee
print(issubclass(Director, Employee))  # True

# Является ли класс Employee подклассом Director
print(issubclass(Employee, Director))  # False

# ЖЕСТКОЕ СРАВНЕНИЕ ТИПОВ (БЕЗ УЧЕТА НАСЛЕДОВАНИЯ)
print(10 is int)        # False
print(type(10) is int)  # True
print(None is None)     # True
print("\n")


# TODO: ОТ СЮДА НАЧАЛИ
# АБСТРАКТНЫЕ КЛАССЫ
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def info() -> str:
        return "This is Shape!"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * self.width + self.height


rectangle = Rectangle(100, 200)
print(rectangle.perimeter())
print("\n")


# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
class MyBaseClass:
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


child = MyChildClass()
print(child.value)
print("\n")


class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesTwo:
    def __init__(self):
        self.value *= 2

class PlusFive:
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print("First ordering value is (5 * 2) + 5 =", foo.value)
print("\n")


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

bar = AnotherWay(5)
print("Second ordering should be (5 + 5) * 2, but is", bar.value)
print("\n")


class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = ThisWay(5)
print("Should be (5 * 7) + 9 = 44 but is", foo.value)
print("\n")

"""
    Для решения этих проблем в Python есть встроенная функция super и стандартный порядок
    разрешения методов (MRO). super гарантирует,
    что общие суперклассы в ромбовидных иерархиях выполняются только один раз. 
"""

class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesSeven(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class ThisWay(PlusNine, TimesSeven):
    def __init__(self, value):
        super().__init__(value)

print(ThisWay.__mro__)

foo = ThisWay(5)
print("Should be 9 + 7 * 5 = 44 and is", foo.value)
print("\n\n")




"""
    Композиция и агрегация — это два типа отношений «часть-целое» между классами в ООП. 
    Они показывают, как объекты связаны друг с другом,
    но различаются по силе связи и жизненному циклу включаемого объекта.

    Агрегация — это более слабая связь, при которой один объект (контейнер) содержит
    другой объект в качестве своей части, но при этом часть может существовать независимо от контейнера.
    Если контейнер уничтожается, его часть остаётся в памяти и может использоваться дальше.

    Композиция — это более жёсткая связь, частный случай агрегации.
    Здесь объект-часть не может существовать отдельно от контейнера.
    Контейнер полностью контролирует жизненный цикл объекта-части: он создаётся вместе с ним и уничтожается вместе с ним.
"""
# КОМПОЗИЦИЯ И АГРЕГАЦИЯ
class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Point2D) -> Point2D:
        return Point2D(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __eq__(self, other: Point2D) -> bool:
        return self.x == other.x and self.y == other.y


class Vector2D:
    def __init__(self, point1: Point2D, point2: Point2D) -> None:
        self.point1 = point1
        self.point2 = point2

    def __str__(self) -> str:
        return f"Point1({self.point1}); Point2({self.point2})"

    def __add__(self, other: Vector2D) -> Vector2D:
        # Перегрузка оператора +
        new_point1 = self.point1 + other.point1
        new_point2 = self.point2 + other.point2
        return Vector2D(new_point1, new_point2)

    def __eq__(self, other: Vector2D) -> bool:
        if self.point1 == other.point1 and self.point2 == other.point2:
            return True
        return False


vec1 = Vector2D(Point2D(10, 10), Point2D(5, 5))
vec2 = Vector2D(Point2D(10, 10), Point2D(5, 5))
print(vec1)

vec3 = vec1 + vec2
print(vec3)


print(vec1 == vec2)
print("\n\n")


# УРОВНИ ДОСТУПА
"""
1) без префикса — публичный (public), доступен отовсюду; 
2) одно подчеркивание — защищенный (protected),
    не следует использовать вне класса и его подклассов;
3) двойное подчеркивание — приватный (private),
    не следует использовать вне класса.
"""

class User: # ПУБЛИЧНЫЙ ЮЗЕР
    def __init__(self, login, password):
        self.login = login
        self.password = password


user1 = User("PavelCool", "super_secret_password")
print(user1.login)
print(user1.password)
print("\n\n")


class User: # ЗАЩИЩЕННЫЙ ЮЗЕР
    def __init__(self, login, password):
        self._login = login         # защищенный арибут
        self._password = password   # защищенный арибут

class SuperUser(User):
    def __init__(self, login, password, super_key):
        super().__init__(login, password)
        self._super_key = super_key # защищенный арибут

    def __str__(self) -> str:
        return f"Имя: {self._login}, Ключ: {self._super_key}"

    
user1 = User("PavelCool", "super_secret_password")
print(user1._login)
print(user1._password)
print(user1.__dict__)
print("\n\n")

class User: # ПРИВАТНЫЙ ЮЗЕР
    def __init__(self, login, password):
        self.__login = login         # приватный арибут
        self.__password = password   # приватный арибут

class SuperUser(User):
    def __init__(self, login, password, super_key):
        super().__init__(login, password)
        self._super_key = super_key # защищенный арибут

    def __str__(self) -> str:
        return f"Ключ: {self._super_key}"

    
user1 = User("PavelCool", "super_secret_password")
print(user1._User__login)
print(user1._User__password)
print(user1.__dict__)
print("\n\n")


# ИНКАПСУЛЯЦИЯ
class User:
    def __init__(self, login, password):
        self.login = login          # 
        self.password = password

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, new_login: str) -> None:
        if not isinstance(new_login, str):
            print("Логин должен быть строкой")
            return
        if len(new_login.strip()) < 4:
            print("Длина логина должна быть больше 4")
            return
        
        self._login = new_login.strip()

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, new_password) -> None:
        if not isinstance(new_password, str):
            print("Пароль должен быть строкой")
            return
        if len(new_password.strip()) < 4:
            print("Длина пароля должна быть больше 4")
            return
        self._password = new_password.strip()


user1 = User("pavel", "supersecret_password")
print(user1.login)
user1.login = " pa "
print(user1.login)

print(user1._login)
print(user1.login)

user1._login = " pa "
print(user1.password)
print("\n\n")





# Полиморфизм
# ВСТРОЕННЫЙ ПОЛИМОРФИЗМ
def add(a, b):
    return a + b

print(add(1, 2))
print(add('Hello ', 'world!'))

print(len([1, 2, 3, 4, 5]))
print(len('Павел'))
print(len((1, 2, 3, 4, 5)))
print("\n\n")

# ПОЛИМОРФИЗМ ПРИ НАСЛЕДОВАНИИ
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def info(self):
        return f"Имя: {self.name}, звук: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return 'Мяу!'






import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def info(self):
        return f'Площадь: {self.area()}, периметр: {self.perimeter()}.'

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

shapes = [Rectangle(10, 2), Circle(8)]

print('\n'.join(shape.info() for shape in shapes))
print("\n\n")



# ПРИНЦИП УТКИ
"""
    Утиная типизация (принцип утки) - это правило Python, которое звучит так – 
    «Если что-то движется и говорит как утка, значит, это утка». 
    Теперь, рассмотрим следующий пример:
"""
class Duck:
    def eat(self):
        return 'Утка кушает.'

    def speak(self):
        return 'Кря!'

class Horse:
    def eat(self):
        return 'Лошадь ест.'

    def speak(self):
        return 'Звук лошади!'

class Fish:
    def swim(self):
        return 'Плыву'

    def eat(self):
        return 'Рыбка ест.'

def handler_animal(animal) -> None:
    """
    Выводит информацию о животном.

    :param animal: объект животного ОБЯЗАТЕЛЬНО 
        animal.eat() и animal.speak()
    """
    print(f'Еда: {animal.eat()}')
    print(f'Звук: {animal.speak()}')

duck = Duck()
horse = Horse()
fish = Fish()

handler_animal(duck)
handler_animal(horse)
# handler_animal(fish) # не сработает!



# Пример из реальной жизни - обработка разных файлов
class CSVReader:
    def read(self):
        return "Читаю CSV"

class JSONReader:
    def read(self):
        return "Читаю JSON"

def process_file(reader):
    return reader.read()  # Единый интерфейс
