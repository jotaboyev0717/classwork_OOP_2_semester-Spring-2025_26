from enum import Enum
from abc import ABC, abstractmethod
class DrinkType(Enum):
    COFFEE = 1
    TEA = 2
    JUICE = 3
    

class Drink(ABC):
    def __init__(self, size):
        self.size = size
        
    @abstractmethod
    def prepare(self):
        pass
    
class Coffee(Drink):
    def prepare(self):
        print(f"Brewing {self.size} coffee ☕")
        
class Tea(Drink):
    def prepare(self):
        print(f"Steeping {self.size} tea 🍵")
        
class Juice(Drink):
    def prepare(self):
        print(f"Squeezing {self.size} juice 🧃")
        
class DrinkFactory:
    _types = {
        DrinkType.COFFEE: Coffee,
        DrinkType.TEA: Tea,
        DrinkType.JUICE: Juice,
    }
    
    @staticmethod
    def create(kind, size):
        if kind not in DrinkFactory._types:
            raise ValueError(f"Unknown drink: {kind}")
        cls = DrinkFactory._types[kind]
        obj = cls(size)
        return obj 
    
orders = [
    (DrinkType.COFFEE, "large"),
    (DrinkType.TEA, "small"),
    (DrinkType.JUICE, "medium"),
    (DrinkType.COFFEE, "small"),
]

for kind, size in orders:
    drink = DrinkFactory.create(kind, size)
    drink.prepare()
