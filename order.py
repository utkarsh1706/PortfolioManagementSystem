from abc import ABC, abstractmethod
from ticker import Ticker
from user import User
import uuid
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    FAILED = 2
    EXECUTED = 3

class Order(ABC):
    def __init__(self, price, quantity, stock: Ticker, user: User) -> None:
        self.orderID = self.generateOrderID()
        self.price = price
        self.quantity = quantity
        self.stock = stock
        self.user = user
        self.status = OrderStatus.PENDING

    def generateOrderID():
        return str(uuid.uuid4).replace('-', '')[:8]
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity
    
    @abstractmethod
    def execute(self):
        pass
