class Account:
    def __init__(self, user) -> None:
        self.user = user
        self.balance = 0
        return
    
    def getBalance(self):
        return self.balance
    
    def addBalance(self, balance):
        self.balance += balance
        return
    
    def reduceBalance(self, balance):
        self.balance -= balance
        return