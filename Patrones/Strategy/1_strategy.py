from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        """Method to execute the strategy with given parameters."""
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        """Adds two numbers."""
        return a + b
    
class SubtractStrategy(Strategy):
    def execute(self, a, b):
        """Subtracts second number from first."""
        return a - b
    
class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        """Multiplies two numbers."""
        return a * b
    

class Operation:
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def calculate(self, a, b):
        return self.__strategy.execute(a,b)
    
    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy


add_strategy = AddStrategy()
sustract_strategy = SubtractStrategy()
multiply_strategy = MultiplyStrategy()

operation = Operation(add_strategy)
print(operation.calculate(5,7))

operation.set_strategy(sustract_strategy)
print(operation.calculate(5,7))

operation.set_strategy(multiply_strategy)
print(operation.calculate(5,7))