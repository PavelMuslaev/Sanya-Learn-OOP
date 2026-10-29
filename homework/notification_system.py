from abc import ABC, abstractmethod

class NotificationChannel(ABC):

    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        ...

class EmailChannel(NotificationChannel):

    def send(self, recipient: str, message: str) -> str:
        return f"Email для {recipient}: {message}"

class SmsChannel(NotificationChannel):

    def send(self, recipient: str, message: str) -> str:
        return f"SMS для {recipient}: {message}"

class MessageFormatter:
    """
    Форматирует итоговое сообщение из темы и текста.
    """

    def format(self, subject: str, text: str) -> str:

        parts = [part for part in (subject, text) if part]
        return " ".join(parts)

class NotificationService:
    """
    Сервис рассылки уведомлений через список каналов.

    Каналы передаются извне (агрегация), а форматтер создаётся
    внутри сервиса (композиция).
    """

    def __init__(self, channels: list[NotificationChannel]) -> None:

        self._channels = channels
        self._formatter = MessageFormatter()

    def notify_all(self, recipient: str, subject: str, text: str) -> list[str]:
        """
        Отправить уведомление через все каналы.

        Args:
            recipient: Получатель сообщения.
            subject: Тема сообщения.
            text: Текст сообщения.

        Returns:
            Список строк с результатами отправки от каждого канала.
        """
        message = self._formatter.format(subject, text)
        results = []
        for channel in self._channels:
            results.append(channel.send(recipient, message))
        return results


if __name__ == "__main__":
    # Демонстрация работы
    email_channel = EmailChannel()
    sms_channel = SmsChannel()
    channels = [email_channel, sms_channel]

    service = NotificationService(channels)
    results = service.notify_all(
        recipient="student@example.com",
        subject="Ваш заказ",
        text="готов"
    )

    for result in results:
        print(result)


