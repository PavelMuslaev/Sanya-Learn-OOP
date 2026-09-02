class Product:
    """Товар в магазине."""

    def __init__(self, sku: str, name: str, price: float, stock: int, discount: float = 0) -> None:
        self.sku = sku
        self.__name = "Default"
        self.__price = 1.0
        self.__stock = 0
        self._discount = 0
        self.name = name
        self.price = price
        self.stock = stock
        self.discount = discount

# Если какой-то аргумент некорректен, сеттер выведет сообщение и оставит значение по умолчанию
    @property
    def name(self) -> str:
        """Название товара."""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            print("Ошибка: название должно быть строкой.")
            return
        stripped = new_name.strip()
        if not stripped:
            print("Ошибка: название не может быть пустым.")
            return
        if len(stripped) < 3:
            print("Ошибка: название должно содержать минимум 3 символа.")
            return
        self.__name = stripped

    @property
    def price(self) -> float:
        """Цена товара (положительное число)."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if not isinstance(new_price, (int, float)):
            print("Ошибка: цена должна быть числом.")
            return
        if new_price <= 0:
            print("Ошибка: цена должна быть строго больше нуля.")
            return
        self.__price = float(new_price)

    @property
    def stock(self) -> int:
        """Остаток товара на складе (неотрицательное целое число)."""
        return self.__stock

    @stock.setter
    def stock(self, new_stock: int) -> None:
        if not isinstance(new_stock, int):
            print("Ошибка: количество должно быть целым числом.")
            return
        if new_stock < 0:
            print("Ошибка: количество не может быть отрицательным.")
            return
        self.__stock = new_stock

    @property
    def discount(self) -> float:
        """Скидка в процентах (от 0 до 50)."""
        return self._discount

    @discount.setter
    def discount(self, new_discount: float) -> None:
        if not isinstance(new_discount, (int, float)):
            print("Ошибка: скидка должна быть числом.")
            return
        if not (0 <= new_discount <= 50):
            print("Ошибка: скидка должна быть от 0 до 50 процентов.")
            return
        self._discount = float(new_discount)

    @property
    def final_price(self) -> float:
        """Итоговая цена с учётом скидки (только для чтения)."""
        return self.__price * (1 - self._discount / 100)

if __name__ == "__main__":
    # создание товара с корректными значениями
    product = Product(sku="B123", name="Телефон", price=50000, stock=10, discount=10)

    # чтение всех свойств
    print("Начальные значения:")
    print(f"sku: {product.sku}")
    print(f"name: {product.name}")
    print(f"price: {product.price}")
    print(f"stock: {product.stock}")
    print(f"discount: {product.discount}")
    print(f"final_price: {product.final_price}")

    # корректные изменения
    print("\nКорректные изменения:")
    product.price = 55000
    product.stock = 8
    product.discount = 15
    print(f"price: {product.price}")
    print(f"stock: {product.stock}")
    print(f"discount: {product.discount}")
    print(f"final_price: {product.final_price}")

    # некорректные присваивания (минимум 2)
    print("\nНекорректные присваивания:")
    print("Попытка установить name = 'AB' (слишком короткое):")
    product.name = "AB"
    print(f"Текущее name: {product.name}")

    print("Попытка установить price = -100:")
    product.price = -100
    print(f"Текущее price: {product.price}")

    print("Попытка установить stock = -5:")
    product.stock = -5
    print(f"Текущее stock: {product.stock}")

    print("Попытка установить discount = 75:")
    product.discount = 75
    print(f"Текущее discount: {product.discount}")

    # итоговые значения после неудачных попыток
    print("\nИтоговые значения после некорректных попыток:")
    print(f"name: {product.name}")
    print(f"price: {product.price}")
    print(f"stock: {product.stock}")
    print(f"discount: {product.discount}")
    print(f"final_price: {product.final_price}")

    # name mangling: показываем содержимое __dict__
    print("\nСодержимое product.__dict__:")
    print(product.__dict__)
