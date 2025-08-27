from abc import ABC, abstractmethod

# Interfaz de estado
class CoffeeMachineState(ABC):
    @abstractmethod
    def handle(self, context):
        ...

# Estados concretos
class NoCoinState(CoffeeMachineState):
    def handle(self, context):
        print("Insertando moneda...")
        context.state = HasCoinState()

class HasCoinState(CoffeeMachineState):
    def handle(self, context):
        print("Preparando café...")
        context.state = DispensingState()

class DispensingState(CoffeeMachineState):
    def handle(self, context):
        print("Café servido. Retirando moneda...")
        context.state = NoCoinState()

# Contexto
class CoffeeMachine:
    def __init__(self):
        self.state: CoffeeMachineState = NoCoinState()

    def request(self):
        self.state.handle(self)

print("\n-------------Ejm 1----------------\n")

# Uso
machine = CoffeeMachine()
machine.request()  # Insertando moneda...
machine.request()  # Preparando café...
machine.request()  # Café servido...
machine.request()  # Insertando moneda.


print("\n-------------Ejm 2----------------\n")

# ---Ejm 2----

class DeliverableState(ABC):
    @abstractmethod
    def approve(self, context): ...
    @abstractmethod
    def reject(self, context): ...

class PendingReview(DeliverableState):
    def approve(self, context):
        print("Pasando a estado Aprobado")
        context.state = Approved()
    def reject(self, context):
        print("Pasando a estado Rechazado")
        context.state = Rejected()

class Approved(DeliverableState):
    def approve(self, context):
        print("Ya está aprobado")
    def reject(self, context):
        print("No se puede rechazar un entregable aprobado")

class Rejected(DeliverableState):
    def approve(self, context):
        print("Revisar antes de aprobar")
        context.state = PendingReview()
    def reject(self, context):
        print("Ya está rechazado")

class Deliverable:
    def __init__(self):
        self.state: DeliverableState = PendingReview()

    def approve(self):
        self.state.approve(self)

    def reject(self):
        self.state.reject(self)

# Uso
doc = Deliverable()
doc.approve()  # Aprobado
doc.approve()  # Aprobado
doc.reject()  # No se puede rechazar


print("\n-------------Ejm 3----------------\n")


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ProcessContext:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state:State):
        self._state = state

    def request(self):
        self._state.handle(self)    

class StartState(State):
    def handle(self, context: ProcessContext):
        print("Estado: Inicial. Pasando a Ejecución")
        context.set_state(ExecutionState())

class ExecutionState(State):
    def handle(self, context: ProcessContext):
        print("Estado: Procesando. Pasando a Finalización")
        context.set_state(EndState())

class EndState(State):
    def handle(self, context: ProcessContext):
        print("Estado: Finalizado")


# uso
process = ProcessContext(StartState())
process.request()
process.request()
process.request()
process.request()

