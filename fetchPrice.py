from ticker import Ticker

class APIPrice:
    @staticmethod
    def fetchPrice(stock: Ticker):
        print(f"Fetching Price for {stock.getSymbol()}")
        # updatePrice = APIPrice.apiCall(stock.getSymbol())
        # stock.updatePrice(updatePrice)
        # return updatePrice