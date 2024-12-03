from fetchPrice import APIPrice

class Ticker:
    def __init__(self, id, symbol, price) -> None:
        self.tickerID = id
        self.symbol = symbol
        self.stockPrice = price
        self.apiPrice = APIPrice(self)
        return
    
    def getPrice(self):
        return self.stockPrice
    
    def getSymbol(self):
        return self.symbol
    
    def updatePrice(self):
        self.stockPrice = self.apiPrice.fetchPrice()
        return