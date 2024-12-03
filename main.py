from portfolioManager import PortfolioManager
from user import User
from ticker import Ticker
from buyOrder import BuyOrder
from sellOrder import SellOrder

class PortfolioManagementSystem:
    @staticmethod
    def run():
        portfolioManagement = PortfolioManager.getInstance()

        user1 = User("Utkarsh", "123", 1)
        stock1 = Ticker(1, "TCS", 1840)
        stock2 = Ticker(2, "WIPRO", 300)

        portfolioManagement.addUser(user1)
        portfolioManagement.addStock(stock1)
        portfolioManagement.addStock(stock2)

        order1 = BuyOrder(1850, 1, stock1, user1)
        order2 = BuyOrder(400, 2, stock2, user1)

        portfolioManagement.placeOrder(order1)
        portfolioManagement.placeOrder(order2)

        portfolioManagement.getReturns(user1)
        portfolioManagement.getHoldings(user1)


if __name__ == "__main__":
    PortfolioManagementSystem.run()