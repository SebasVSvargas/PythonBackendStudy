
from abc import ABC, abstractmethod

# ABC: convierte la clase en abstracta.
# @abstractmethod: indica que este método debe ser implementado por cualquier subclase.

class Drink(ABC):
    @abstractmethod
    def get_quantity(): # No requiere self porque es un método abstracto
        """Método abstracto que debe ser implementado por las subclases para obtener la cantidad de bebida."""
        pass

    def description(self):
        return "This is a drink."

# Clase concreta que hereda de Drink y debe implementar el método abstracto get_quantity
class Beer(Drink):
    def __init__(self, quantity):
        self.__quantity = quantity # Private attribute

    def get_quantity(self): #metodo que debe definirse porque hereda de Drink que es abstracta
        return f"Beer quantity: {self.__quantity}ml"
    
beer = Beer(500)
print(beer.get_quantity())  # Output: Beer quantity: 500ml

