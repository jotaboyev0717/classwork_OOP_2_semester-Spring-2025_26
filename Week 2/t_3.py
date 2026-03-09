class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self.__price = value
    
    @property
    def quantity(self):
        return self.__quantity        
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = value
            
    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
        else:
            raise ValueError("Restock amount must be positive")
    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Sell amount must be positive")
            
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("Insufficient stock")
            
    def total_value(self):
        return self.price * self.quantity
    
p = Product("Laptop", 999.99, 10)
print(p.name)
print(p.price)
print(p.quantity)
print(p.total_value())

p.price = 899.99
p.restock(5)
print(p.quantity)
print(p.total_value())

p.sell(3)
print(p.quantity)

try:
    p.price = -50
except ValueError as e:
    print(e)

try:
    p.sell(100)
except ValueError as e:
    print(e)

try:
    p.name = "Tablet"
except AttributeError:
    print("Cannot change product name")

