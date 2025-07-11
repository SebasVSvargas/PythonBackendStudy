from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass

class IvaStrategy(TaxStrategy):
    def calculate(self, amount: float) -> float:
        return amount*0.16
    
class RentaStrategy(TaxStrategy):
    def calculate(self, amount: float) -> float:
        return amount*0.30
    
class TaxCalculator:
    def __init__(self, strategy : TaxStrategy):
        self.__strategy = strategy

    def set_strategy(self, strategy: TaxStrategy):
        self.__strategy = strategy

    def calculate(self, amounts : list[float]) -> list[float]:
        taxes = []
        for amount in amounts:
            taxes.append(self.__strategy.calculate(amount))
        return taxes


amounts = [100,135,1654,354,678]            
iva_calculator = IvaStrategy()
renta_calculator = RentaStrategy()

tax_calculator = TaxCalculator(iva_calculator)

result = tax_calculator.calculate(amounts)
print(result)

tax_calculator.set_strategy(renta_calculator)
print(tax_calculator.calculate(amounts))