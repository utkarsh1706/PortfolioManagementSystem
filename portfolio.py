from fetchPrice import APIPrice
from ticker import Ticker

class Portfolio:
    def __init__(self, user) -> None:
        self.user = user
        self.holdings = {}
    
    def addHolding(self, stock: Ticker, order):
        stockSymbol = stock.getSymbol()
        if stockSymbol not in self.holdings:
            self.holdings[stockSymbol] = {"Price": 0, "Quantity": 0}
        self.updateHolding(self.holdings[stockSymbol], order)
    
    def removeHolding(self, stock: Ticker, order):
        stockSymbol = stock.getSymbol()
        initialHolding = self.holdings.get(stockSymbol)
        if not initialHolding:
            print("No such holding present!")
            return
        initialHolding["Quantity"] -= order.getQuantity()
        if initialHolding["Quantity"] <= 0:
            del self.holdings[stockSymbol]
    
    def updateHolding(self, holding, order):
        initialPrice = holding.get("Price", 0)
        initialQuantity = holding.get("Quantity", 0)
        currPrice = order.getPrice()
        currQuantity = order.getQuantity()

        if currQuantity == 0:
            return
        
        newPrice = (initialPrice * initialQuantity + currPrice * currQuantity) / (currQuantity + initialQuantity)
        newQuantity = currQuantity + initialQuantity
        holding["Price"] = newPrice
        holding["Quantity"] = newQuantity
    
    def getHolding(self, stock: Ticker):
        return self.holdings.get(stock.getSymbol())
    
    def fetchHoldings(self):
        return self.holdings
    
    def fetchReturns(self):
        finalReturns = 0
        for stockSymbol, holding in self.holdings.items():
            currReturn = self.calculateReturn(stockSymbol, holding)
            finalReturns += currReturn
        return finalReturns
    
    def calculateReturn(self, stockSymbol, holding):
        avgPrice = holding.get("Price")
        quantity = holding.get("Quantity")
        lastTradedPrice = APIPrice.getLastPrice(stockSymbol) 
        returnsHolding = (lastTradedPrice - avgPrice) * quantity
        return returnsHolding
