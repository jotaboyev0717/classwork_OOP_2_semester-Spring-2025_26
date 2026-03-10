class ShoppingCart:
    def __init__(self):  
        self.lists = {}
        
    def add(self, name, price):
        self.lists[name] = price
        
    def __len__(self):
        return len(self.lists)
        
    def __getitem__(self, index):
        items = list(self.lists.items())
        name, price = items[index]
        return f"{name}: ${price:.2f}"
    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            new_cart = ShoppingCart()
            for name, price in self.lists.items():
                new_cart.add(name, price)
            for name, price in other.lists.items():
                new_cart.add(name, price)
            return new_cart
    
    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return self.total_price() == other.total_price()
        return False
    
    def total_price(self):
        return sum(self.lists.values())
    
    def __str__(self):
        return f"Cart has {len(self)} items, Total: ${self.total_price():.2f}"
    
    def __bool__(self):
        return len(self.lists) > 0
    
cart1 = ShoppingCart()
cart1.add("Apple", 2.50)
cart1.add("Bread", 3.00)

cart2 = ShoppingCart()
cart2.add("Milk", 4.50)
cart2.add("Eggs", 1.00)

print(len(cart1))
print(cart1[0])
print(cart1)

cart3 = cart1 + cart2
print(cart3)
print(len(cart3))

print(cart1 == cart2)

empty = ShoppingCart()
if not empty:
    print("Cart is empty")