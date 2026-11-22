import pytest

@pytest.fixture(scope="session", autouse=True) 
def print_end_start_session():
    print("-" * 10, "ТЕСТОВАЯ ССЕСИЯ НАЧАЛАСЬ!", "-" * 10)
    yield
    print("-" * 10, "ТЕСТОВАЯ ССЕСИЯ ЗАКОНЧИЛАСЬ!", "-" * 10)
    
# @pytest.fixture(autouse=True) 
# def print_end_start_function():
#     print("-" * 10, "ТЕСТОВАЯ ФУНКЦИЯ НАЧАЛАСЬ!", "-" * 10)
#     yield
#     print("-" * 10, "ТЕСТОВАЯ ФУНКЦИЯ ЗАКОНЧИЛАСЬ!", "-" * 10)


@pytest.fixture(scope="function", autouse=True) 
def track_test_duration(): 
    import time 
    start_time = time.time() 
    yield 
    result = time.time() - start_time 
    print(f"Тест выполнился: {result:.4f} сек.")


