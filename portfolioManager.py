from user import User
from ticker import Ticker
from queue import Queue
from threading import Lock


class PortfolioManager:
    _instance = None

    def __init__(self) -> None:
        if PortfolioManager._instance is not None:
            raise Exception("Singleton Class!")
        self.users = {}
        self.stocks = {}
        self.orders = []
        self.queue = Queue()
        self.lock = Lock()

    @staticmethod
    def getInstance():
        if PortfolioManager._instance is None:
            PortfolioManager._instance = PortfolioManager()
        return PortfolioManager._instance

    def addUser(self, user: User):
        self.users[user.getID()] = user

    def addStock(self, stock: Ticker):
        self.stocks[stock.getSymbol()] = stock

    def removeStock(self, stockName: str):
        if stockName not in self.stocks:
            print("No such stock exists!")
            return
        del self.stocks[stockName]

    def placeOrder(self, order):
        with self.lock:
            self.queue.put(order)

    def executeOrder(self):
        while not self.queue.empty():
            order = self.queue.get()
            order.execute()

    def getReturns(self, user: User):
        return user.getPortfolio().fetchReturns()

    def getHoldings(self, user: User):
        return user.getPortfolio().fetchHoldings()
