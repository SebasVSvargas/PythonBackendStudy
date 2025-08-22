from abc import ABC, abstractmethod
# Dependency Injection (DI) is a design pattern used to implement IoC (Inversion of Control), allowing for better separation of concerns and easier testing.

# benefits
# - Improved code maintainability
# - Enhanced testability
# - Reduced coupling between components
# - Increased flexibility and scalability

#example

class EmailNotification:
    def __init__(self, user, pwd, url):
        self._user = user
        self._pwd = pwd
        self._url = url

    def send(self, message):
        print(f"Sending email with message: {message}")

# lets see how we must not use it
# This tightly couples NotificationManager to EmailNotification, making it hard to change the notification method or test it.
class NotificationManager:
    def __init__(self):
        self._notification = EmailNotification("user", "pwd", "url")

    def send_notification(self, message):
        self._notification.send(message)


# A better approach is to use Dependency Injection to decouple these classes.
# DESACOPLAR será clave

# first we create an abstract class for notifications, 
# this will allow us to define a common interface and implementation for different notification methods.
class Notification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

# second, we create a concrete implementation for notifications
class EmailNotification(Notification):
    def __init__(self, user, pwd, url):
        self._user = user 
        self._pwd = pwd
        self._url = url

    def send_notification(self, message):
        print(f"Sending email with message: {message}")

class SMSNotification(Notification):
    def __init__(self, phone_number):
        self._phone_number = phone_number

    def send_notification(self, message):
        print(f"Sending SMS to {self._phone_number} with message: {message}")


# Third, we create a NotificationManager that uses the Notification interface
class NotificationManager2():
    def __init__(self, notification: Notification):
        self._notification = notification

    def notify_user(self, message):
        self._notification.send_notification(message)


# create implementations
email_notification= EmailNotification("user", "pwd", "url")        
sms_notification= SMSNotification("123-456-7890")

manager = NotificationManager2(email_notification)
manager.notify_user("Hello via Email!")

print("-------------Changing notification method----------------")

manager = NotificationManager2(sms_notification)
manager.notify_user("Hello via SMS!")