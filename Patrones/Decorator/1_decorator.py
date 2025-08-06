from abc import ABC, abstractmethod

class Taco(ABC):
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def description(self):
        pass

class BasicTaco(Taco):
    def price(self):
        return 5
    def description(self):
        return "Taco simple "

class TacoDecorator(Taco):
    def __init__(self, taco:Taco):
        self._taco = taco

    def price(self):
        return self._taco.price()
    def description(self):
        return self._taco.description() + "Extra "
    
class DoubleMeatTaco(TacoDecorator):
    def price(self):
        return self._taco.price() + 4
    def description(self):
        return super().description() + "Doble Carne "
    
class CheeseTaco(TacoDecorator):
    def price(self):
        return super().price() + 2
    def description(self):
        return super().description() + "Quesillo "
    
taco = BasicTaco()
print(f"Taco sencillo: ${taco.price()}")
print(f"Descripción: {taco.description()}")
print("--------------------------------------------")

double_meat_taco = DoubleMeatTaco(
                        CheeseTaco(
                            BasicTaco()
                        )
                    )

print(f"taco doble carne: ${double_meat_taco.price()}")
print(f"Descripción: {double_meat_taco.description()}")
print("--------------------------------------------")

cheese_taco = CheeseTaco(BasicTaco())
print(f"Taco con queso: ${cheese_taco.price()}")
print(f"Descripción: {cheese_taco.description()}")
print("--------------------------------------------")

triple_meat_taco = DoubleMeatTaco(double_meat_taco)
print(f"Taco triple carne: ${triple_meat_taco.price()}")
print(f"Descripción: {triple_meat_taco.description()}")
print("--------------------------------------------")

# ------------------------------------- 

# Componente base
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# Componente concreto
class NotificadorBase(Notificador):
    def enviar(self, mensaje):
        print(f" Notificando: {mensaje}")

# Decorador base
class DecoradorNotificador(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensaje):
        self._notificador.enviar(mensaje)

# Decorador concreto: Email
class NotificadorEmail(DecoradorNotificador):
    def enviar(self, mensaje):
        super().enviar(mensaje)
        print(f" Enviando email con mensaje: {mensaje}")

# Decorador concreto: SMS
class NotificadorSMS(DecoradorNotificador):
    def enviar(self, mensaje):
        super().enviar(mensaje)
        print(f" Enviando SMS con mensaje: {mensaje}")


notificador = NotificadorSMS(
                NotificadorEmail(
                    NotificadorBase()
                )
            )

notificador.enviar("¡Tu patrón Decorator funciona!")
