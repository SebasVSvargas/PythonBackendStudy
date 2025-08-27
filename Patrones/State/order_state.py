
from abc import ABC, abstractmethod

# this is the state interface
class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass

# this is the context class
class Order:
    def __init__(self, state: OrderState):
        self.state = state

    def set_state(self, state: OrderState):
        self.state = state

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def deliver(self):
        self.state.deliver(self)


# concrete states
class PendingState(OrderState):
    def pay(self, order):
        print("Payment received.")
        order.set_state(ShippedState())

    def ship(self, order):
        print("Order is still pending.")

    def deliver(self, order):
        print("Order is still pending.")

class ShippedState(OrderState):
    def pay(self, order):
        print("Order is already paid.")

    def ship(self, order):
        print("Order has been shipped.")
        order.set_state(DeliveredState())

    def deliver(self, order):
        print("Order is still in transit.")

class DeliveredState(OrderState):
    def pay(self, order):
        print("Order is already paid.")

    def ship(self, order):
        print("Order is already shipped.")

    def deliver(self, order):
        print("Order has been delivered.")

order = Order(PendingState())
order.ship()   # Order is still pending.
order.pay()    # Payment received.
order.pay()    # Order is already paid.
order.deliver()  # Order is still in transit.

order.ship()   # Order has been shipped.
order.ship()   # Order is already shipped.

order.deliver()  # Order has been delivered.
order.deliver()  # Order is already delivered.