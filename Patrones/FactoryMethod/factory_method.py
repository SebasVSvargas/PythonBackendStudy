'''
Factory Method pattern
This pattern defines an interface for creating an object, but it is the responsibility of 
the derived classes to implement the method and instantiate the appropriate class.
'''

from abc import ABC, abstractmethod

class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod    
    def price(self) -> float:
        pass

class Product(Concept):
    def __init__(self, amount: float, tax: float):
        self.__amount = amount
        self.__tax = tax

    def description(self) -> str:
        return "This is a product."

    def price(self) -> float:
        return self.__amount + (self.__amount * self.__tax / 100)

class Service(Concept):
    def __init__(self, amount: float):
        self.__amount = amount

    def description(self) -> str:
        return "This is a service."
    
    def price(self) -> float:
        return self.__amount

# Factory interface
class ConceptFactory(ABC):
    def __init__(self, *args):
        self._args = args

    @abstractmethod
    def create_concept(self) -> Concept:
        pass

class ProductFactory(ConceptFactory):
    def create_concept(self) -> Concept:
        return Product(self._args[0], self._args[1])

class ServiceFactory(ConceptFactory):
    def create_concept(self) -> Concept:
        return Service(self._args[0])

def show_info(concept: Concept):
    print(f"The concept is: {concept.description()}")

    
# initial creation
product_factory = ProductFactory(100.0, 15.0)
service_factory = ServiceFactory(200.0)

# creation of many concepts based on the same factory
concept1 = product_factory.create_concept()
concept2 = service_factory.create_concept()
concept3 = service_factory.create_concept()
concept4 = product_factory.create_concept()

show_info(concept1)
show_info(concept2)

print(f"The price is: {concept1.price()}")
print(f"The price is: {concept2.price()}")
print(f"The price is: {concept3.price()}")
print(f"The price is: {concept4.price()}")
