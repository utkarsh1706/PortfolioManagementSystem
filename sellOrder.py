from order import Order, OrderStatus
from ticker import Ticker
from user import User

class SellOrder(Order):
    def __init__(self, price, quantity, stock: Ticker, user: User) -> None:
        super().__init__(price, quantity, stock, user)
        return
    
    def execute(self):
        currHolding = self.user.portfolio.getHolding(self.stock)
        currQuantity = currHolding.get("Quantity")
        if currQuantity < self.quantity:
            print("Not enough quantity present!")
            self.status = OrderStatus.FAILED
            return
        
        self.user.portfolio.removeHolding(self.stock, self)
        self.user.account.addBalance(self.price*self.quantity)
        self.status = OrderStatus.EXECUTED
        return