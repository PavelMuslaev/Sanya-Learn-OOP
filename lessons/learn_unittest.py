"""
TDD (Test-Driven Development) - это стиль разработки, при 
    котором вы сначала пишете тест (он падает, потому что 
    функциональности ещё нет), потом пишете минимальный код, 
    чтобы тест прошёл, потом рефакторите. Красный-зелёный
    рефакторинг. Это дисциплинирует и заставляет проектировать 
    интерфейсы до реализации. 

BDD (Behavior-Driven Development) - развитие TDD, где тесты 
    пишутся на почти естественном языке (given-when-then). 
    Инструменты типа pytest-bdd позволяют описывать поведение 
    системы понятным для бизнеса языком, а потом автоматизировать 
    эти сценарии.
"""

"""
Тесты можно классифицировать по уровню детализации и цели: 
• Юнит-тесты (модульные) - проверяют одну маленькую 
единицу кода в изоляции: функцию, метод класса. Они 
быстрые и пишутся в большом количестве. 

• Интеграционные тесты - проверяют, как разные модули 
работают вместе: например, ваша функция, которая ходит в 
базу данных, и сама база. Они уже медленнее. 

• Функциональные тесты (или сквозные) - проверяют сценарий 
целиком глазами пользователя. Для консольного приложения 
это может быть запуск скрипта с определёнными аргументами 
и проверка вывода. 

• Регрессионные тесты - не отдельный вид, а цель: убедиться, 
что новое изменение не сломало старое поведение. Обычно 
регрессионные тесты пишут, когда нашли баг: сначала тест, 
который воспроизводит баг, потом его исправление. 

Все эти виды образуют пирамиду тестирования. 
В основании - много юнит-тестов (они дёшевы и быстры), 
выше - меньше интеграционных, 
на вершине - совсем мало функциональных/сквозных. 

Такой баланс позволяет быстро 
получать обратную связь и при этом быть уверенным, 
что система работает. 
"""



def add(num1: int | float, num2: int | float) -> int | float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError

    return num1 + num2


import unittest

class TestCalc(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        cls.num1 = 10
        cls.num2 = 30

    def setUp(self): 
        # Создание тестовых данных 
        self.user_data = {"id": 1, "name": "Test User"}

    def test_positive_add(self):
        self.assertEqual(add(self.num1, self.num2), 30)

    def test_negative_add(self):
        self.assertEqual(add(10, 20), 30)


class TestDatabaseOperations(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Подключение к тестовой БД 
        cls.db_connection = "< simulated_db_connection >" 
    
    @classmethod 
    def tearDownClass(cls): 
        # Закрытие подключение к БД 
        cls.db_connection = None 

    def setUp(self): 
        # Создание тестовых данных 
        self.user_data = {"id": 1, "name": "Test User"} 

    def tearDown(self): 
        # Удаление тестовых данных 
        self.user_data = None 

    def test_user_creation(self): 
        self.assertIn('name', self.user_data) 
        self.assertTrue(self.db_connection)

    def test_user_property_access(self): 
        self.assertEqual(self.user_data['name'], 'Test User') 
        self.assertEqual(self.user_data['id'], 1) 


"""
Модуль unittest - это встроенный инструмент для написания 
автоматических тестов. Его ключевые элементы: 
• классы, наследующие TestCase, 
• методы setUp/tearDown для фикстур, 
• богатый набор assert-методов, 
• запуск через командную строку или unittest.main(). 

Однако для повседневной разработки на Python мы почти 
всегда выбираем pytest - он проще, выразительнее и мощнее. 
Поэтому, познакомившись с unittest, мысленно поблагодарим его за 
вклад и смело перейдём к следующей главе, где нас ждёт настоящая 
магия тестирования. 
"""
