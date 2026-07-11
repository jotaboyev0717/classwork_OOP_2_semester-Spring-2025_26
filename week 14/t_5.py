from abc import abstractmethod, ABC
class TradingStrategy(ABC):
    @abstractmethod
    def decide(self, price):
        BUY = 1
        SELL = 2
        HOLD = 3
        pass
    
class BuyLowStrategy(TradingStrategy):
    def __init__(self, threshold):
            self.threshold = threshold

    def decide(self, price):
        if price < self.threshold:
            return self.BUY
        else:
            return self.HOLD
        
class SellHighStrategy(TradingStrategy):
    def __init__(self, threshold):
        self.threshold = threshold

    def decide(self, price):
        if price > self.threshold:
            return self.SELL
        else:
            return self.HOLD

class AlwaysHoldStrategy(TradingStrategy):
    def decide(self, price):
        return self.HOLD
    
class Observer:
    @abstractmethod
    def update(price):
        pass
    
class Trader(Observer):
    def __init__(self, name):
        self.name = name
        self.strategy = TradingStrategy()
        
    def update(self, price):
        action = self.strategy.decide(price)
        print(f"{self.name}: {action} at ${price}")
        
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        