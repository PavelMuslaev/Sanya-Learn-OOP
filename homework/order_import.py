"""Импорт заказов из разных источников."""

from typing import Protocol


class Order:
    """Представляет заказ."""

    def __init__(
        self,
        order_id: int,
        customer: str,
        amount: float,
    ) -> None:
        self.order_id = order_id
        self.customer = customer
        self.amount = amount

    def __str__(self) -> str:
        """Возвращает пользовательское представление заказа."""
        return f"Заказ №{self.order_id}: " f"{self.customer} — {self.amount:.2f} руб."

    def __repr__(self) -> str:
        """Возвращает подробное представление заказа."""
        return (
            f"Order(order_id={self.order_id!r}, "
            f"customer={self.customer!r}, "
            f"amount={self.amount!r})"
        )


class OrderReaderProtocol(Protocol):
    """Описывает интерфейс чтения заказов."""

    def read(self) -> list[str]:
        """Возвращает записи заказов в строковом формате."""
        ...


class TextOrderReader:
    """Читает заказы из списка строк."""

    def __init__(self, records: list[str]) -> None:
        self._records = records

    def read(self) -> list[str]:
        """Возвращает переданные записи."""
        return self._records


class LegacyOrderSource:
    """Хранит заказы в устаревшем формате."""

    def __init__(
        self,
        records: list[tuple[int, str, float]],
    ) -> None:
        self._records = records

    def load_orders(self) -> list[tuple[int, str, float]]:
        """Возвращает заказы в исходном формате."""
        return self._records


class LegacyOrderReaderAdapter:
    """Преобразует старый источник в интерфейс чтения строк."""

    def __init__(self, source: LegacyOrderSource) -> None:
        self._source = source

    def read(self) -> list[str]:
        """Преобразует кортежи заказов в строки."""
        orders = self._source.load_orders()

        return [
            f"{order_id};{customer};{amount}" for order_id, customer, amount in orders
        ]


class InvalidOrderDataError(Exception):
    """Ошибка некорректных данных заказа."""


def parse_order(record: str) -> Order:
    """Преобразует строку в объект заказа."""
    parts = record.split(";")

    if len(parts) != 3:
        raise InvalidOrderDataError(f"Неверный формат записи заказа: {record!r}")

    try:
        order_id = int(parts[0])
        amount = float(parts[2])
    except ValueError as error:
        raise InvalidOrderDataError(
            f"Некорректный идентификатор или сумма: {record!r}"
        ) from error

    customer = parts[1]
    return Order(order_id, customer, amount)


def import_orders(reader: OrderReaderProtocol) -> list[Order]:
    """Импортирует заказы из источника."""
    records = reader.read()
    return [parse_order(record) for record in records]


def find_cheapest_order(orders: list[Order]) -> Order:
    """Возвращает заказ с минимальной суммой."""
    if not orders:
        raise ValueError("Список заказов пуст.")

    min_amount = float("inf")
    cheapest_order = orders[0]

    for order in orders:
        if order.amount < min_amount:
            min_amount = order.amount
            cheapest_order = order

    return cheapest_order


if __name__ == "__main__":
    valid_records: list[str] = [
        "1001;Анна;2490.50",
        "1002;Иван;799.00",
    ]

    invalid_records: list[str] = [
        "1003;Мария;не число",
        "неправильная строка",
    ]

    legacy_records: list[tuple[int, str, float]] = [
        (1004, "Олег", 1500.00),
        (1005, "Елена", 3200.50),
    ]

    print("=== Импорт обычных заказов ===")

    valid_reader = TextOrderReader(valid_records)
    valid_orders = import_orders(valid_reader)

    for order in valid_orders:
        print(str(order))
        print(repr(order))

    print("Самый дешёвый заказ:", find_cheapest_order(valid_orders))

    print("\n=== Импорт через адаптер ===")

    legacy_source = LegacyOrderSource(legacy_records)
    legacy_reader = LegacyOrderReaderAdapter(legacy_source)
    legacy_orders = import_orders(legacy_reader)

    for order in legacy_orders:
        print(str(order))
        print(repr(order))

    print("Самый дешёвый заказ:", find_cheapest_order(legacy_orders))

    print("\n=== Импорт некорректных данных ===")

    invalid_reader = TextOrderReader(invalid_records)

    try:
        invalid_orders = import_orders(invalid_reader)
    except InvalidOrderDataError as error:
        print(f"Ошибка импорта: {error}")
    else:
        for order in invalid_orders:
            print(order)
    finally:
        print("Попытка импорта завершена.")
