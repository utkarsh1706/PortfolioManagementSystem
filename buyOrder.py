from order import Order, OrderStatus
from ticker import Ticker
from user import User

class BuyOrder(Order):
    def __init__(self, price, quantity, stock: Ticker, user: User) -> None:
        super().__init__(price, quantity, stock, user)
        return
    
    def execute(self):
        currBalance = self.user.account.getBalance()
        if self.price * self.quantity > currBalance:
            print("Not enough Balance!")
            self.status = OrderStatus.FAILED
            return
        
        self.user.portfolio.addHolding(self.stock, self)
        self.user.account.reduceBalance(self.price*self.quantity)
        self.status = OrderStatus.EXECUTED
        return