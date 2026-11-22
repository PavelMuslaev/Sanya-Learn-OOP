# pytest .

import pytest

def add(num1, num2):
    return num1 + num2


def test_add_positive():
    assert add(10, 20) == 30
    assert add(5, 20) == 25

def test_add_negative():
    assert add(-10, -20) == -30
    assert add(-5, -20) == -25




""" Фикстура в тестирование - это функция, которая выполняется 
перед (или иногда после) теста и предоставляет ему данные или 
ресурсы. Она позволяет избежать дублирования кода и обеспечивает 
более чистый и структурированный код. Фикстуры могут 
использоваться для создания тестовых данных, настройки 
соединений с базами данных и очистки ресурсов после 
тестирования. """

from typing import Any

def is_check_student(student: dict[str, Any]) -> bool:
    is_student = student.get("is_student")
    return False if is_student is None else is_student

@pytest.fixture
def student():
    return {"name": "Pavel", "is_student": True}

@pytest.fixture
def not_student():
    return {"name": "Pavel", "is_student": False}

def test_is_student_true(student):
    assert is_check_student(student) == True
    del student["name"]
    assert "name" not in student

def test_is_student_false(not_student):
    assert is_check_student(not_student) == False

    







@pytest.fixture 
def sample_list(): 
    print("\nВыполняется фикстура sample_list: создаю список.") 
    return [1, 2, 3, 4, 5] 

@pytest.fixture 
def sample_dict(): 
    print("\nВыполняется фикстура sample_dict: создаю словарь.") 
    return dict(name="Bob", age=24) 

def test_list_length(sample_list):  # Здесь мы передаём имя фикстуры как параметр 
    print("\n###--- run test: test_list_length") 
    assert len(sample_list) == 5 

def test_dict_has_key(sample_dict):  # Здесь мы передаём имя фикстуры как параметр 
    print("\n###--- run test: test_dict_has_key") 
    assert "name" in sample_dict 
    assert "age" in sample_dict 

def test_list_and_dict_usage(sample_list, sample_dict): 
    print("\n###--- run test: test_list_and_dict_usage") 
    assert sample_list == [1, 2, 3, 4, 5] 
    assert sample_dict == {"name": "Bob", "age": 24} 


# Чтобы увидеть выводы print, нужно выполнить команду: 
# pytest -v -s



import os 

@pytest.fixture
def temp_file_fix(): 
    print("\nВыполняется фикстура temp_file_fix: создаю файл.") 
    file_path = "example.txt" 
    with open(file_path, 'w',) as f: 
        f.write("Hello World")
 
    # ОЧЕНЬ ВАЖНО НЕ ЗАБЫТЬ УКАЗАТЬ, ЧТО ПРОКИДЫВАЕТ YIELD 
    yield file_path 
 
    # ЧТОБЫ ЛУЧШЕ ПОНЯТЬ ЗДЕСЬ ПРИНЦИП РАБОТЫ YIELD 
    # ЗАМЕНИТЕ ЕГО НА return 
 
    # Удаляем файл. 
    print("\nЗавершается фикстура temp_file_fix: удаляю файл.") 
    os.remove(file_path) 


def test_read_temp_file(temp_file_fix): 
    print("\nЗапуск теста test_read_temp_file.") 
    file = temp_file_fix 
 
    with open(file, 'r') as f: 
        content = f.read() 
 
    assert content == "Hello World" 
    print("\nКонец теста test_read_temp_file.")



@pytest.fixture(scope='session') 
def session_db_connection(): 
    print("\nФикстура session_db_connection: устанавливаю соединение" 
          " с БД - ОДИН РАЗ ЗА СЕССИЮ.") 
    connection = {"status": "connected",} # Имитация соединения 
    yield connection 
    print("\nФикстура session_db_connection: закрываю соединение" 
          " с БД - ОДИН РАЗ ЗА СЕССИЮ.") 
 
@pytest.fixture(scope='module') 
def module_data_setup(session_db_connection): 
    # Эта фикстура зависит от session_db_connection 
    assert session_db_connection["status"] == "connected" 
    print("\nФикстура session_db_module: настраиваю данные модуля" 
          " - ОДИН РАЗ ЗА МОДУЛЬ.") 
    data = {"name": "Pavel", "age": 25} 
    yield data 
    print("\nФикстура session_db_modul")


class TestOperationDB: 
    def test_create_user(self, module_data_setup, session_db_connection): 
        print("\nТест test_create_user") 
        assert session_db_connection["status"] == "connected" 
        assert module_data_setup["name"] == "Pavel" 
        # module_data_setup.clear() # Показать, что происходит с данными  
 
    def test_user_view(self, module_data_setup, session_db_connection): 
        print("\nТест test_user_view") 
        assert session_db_connection["status"] == "connected" 
        assert module_data_setup["age"] == 25 





