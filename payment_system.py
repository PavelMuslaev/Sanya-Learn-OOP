"""Модуль для демонстрации полиморфной обработки платежей."""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Абстрактный способ оплаты."""

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Оплатить указанную сумму и вернуть описание операции."""
        ...


class CardPayment(PaymentMethod):
    """Оплата банковской картой."""

    def pay(self, amount: float) -> str:
        """Оплатить картой."""
        return f"Оплачено картой: {amount:.2f} руб."


class CashPayment(PaymentMethod):
    """Оплата наличными."""

    def pay(self, amount: float) -> str:
        """Оплатить наличными."""
        return f"Оплачено наличными: {amount:.2f} руб."


class SbpPayment(PaymentMethod):
    """Оплата через СБП."""

    def pay(self, amount: float) -> str:
        """Оплатить через СБП."""
        return f"Оплачено через СБП: {amount:.2f} руб."


class GiftCertificate:
    """Подарочный сертификат, совместимый по методу pay."""

    def pay(self, amount: float) -> str:
        """Оплатить сертификатом."""
        return f"Оплачено подарочным сертификатом: {amount:.2f} руб."


def process_payment(payment, amount: float) -> str:
    """Обработать оплату через любой объект с методом pay()."""
    return payment.pay(amount)


if __name__ == "__main__":
    payments: list = [
        CardPayment(),
        CashPayment(),
        SbpPayment(),
        GiftCertificate(),
    ]

    total = 1500.00
    for payment in payments:
        print(process_payment(payment, total))
