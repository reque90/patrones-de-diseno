from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"[EMAIL] Enviando correo: {message}")


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"[SMS] Enviando SMS: {message}")


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass


class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


def notify_user(factory: NotificationFactory, message: str) -> None:
    notification = factory.create_notification()
    notification.send(message)


if __name__ == "__main__":
    notify_user(EmailFactory(), "Tu pedido ha sido enviado.")
    notify_user(SMSFactory(), "Tu código OTP es 4921.")
