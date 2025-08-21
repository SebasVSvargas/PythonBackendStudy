from abc import ABC, abstractmethod
from typing import List


# Sujeto
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Observador
class Observer:
    def update(self, message):
        print(f"Recibido: {message}")

# Uso
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("El estado ha cambiado!")


# ---------------

# Ejemplo 2

class Observer2(ABC):
    @abstractmethod
    def refresh(self, ticker_number: int):
        pass

class Subject2():
    def __init__(self):
        self._observers: List[Observer2] = []
        self._tickets = 1

    def suscribe(self, observer: Observer2):
        if observer not in self._observers:
            self._observers.append(observer)

    def desuscribe(self, observer: Observer2):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("No existe el observador especificado")

    def notify(self):
        for observer in self._observers:
            observer.refresh(self._tickets)

    def sell(self):
        self.notify()
        self._tickets += 1


class SendMail(Observer2):
    def refresh(self, ticket_number):
        print(f"Se envía un correo al gerente: {ticket_number}")

class Invoice(Observer2):
    def refresh(self, ticket_number):
        print(f"Se envía factura: {ticket_number}")


send_mail = SendMail()
invoice = Invoice()

subject2 = Subject2()
subject2.suscribe(send_mail)
subject2.suscribe(invoice)
subject2.sell()
subject2.sell()
print("----------Se desuscribe el invoice------------")
subject2.desuscribe(invoice)
subject2.notify()