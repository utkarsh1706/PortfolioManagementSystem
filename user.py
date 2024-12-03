from portfolio import Portfolio
from account import Account

class User:
    def __init__(self, name, pan, id) -> None:
        self.id = id
        self.name = name
        self.pan = pan
        self.portfolio = Portfolio(self)
        self.account = Account(self)
        return
    
    def getPortfolio(self):
        return self.portfolio
    
    def getID(self):
        return self.id