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
