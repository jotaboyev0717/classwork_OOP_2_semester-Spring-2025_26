class ShoppingCart:
    def __init__(self, customer_name, discount_code):
        self._customer_name = customer_name
        self.__discount_code = discount_code
        self.__discount_applied = False
        self.items = []
        
    @property
    def customer_name(self):
        return self._customer_name
    
    def add_item(self, name, price, quantity):
        if price <= 0:
            raise ValueError('Price must be positive')
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        for existing_item in self.items:
            if existing_item['name'] == name:
                existing_item["quantity"] += quantity
                return
        item = {
            "name":name,
            "price" : price,
            "quantity" : quantity
        }
        self.items.append(item)
    def remove_item(self, name):
        for i in range(len(self.items)):
            if self.items[i]["name"] == name:
                self.items.pop(i)
                return
        raise ValueError("Item not found")
    @property
    def item_count(self):
        total_quantity = sum(item["quantity"] for item in self.items)
        return total_quantity
    
    @property
    def subtotal(self):
        total = sum(item["quantity"] * item["price"] for item in self.items)
        return round(total, 2)
    
    def apply_discount(self, code):
        if self.__discount_applied:
            raise ValueError("Discount already applied")
        if code != self.__discount_code:
            raise ValueError("Invalid discount code")
        
        self.__discount_applied = True
    
    @property
    def total(self):
        current_total = self.subtotal
        if self.__discount_applied:
            current_total *= 0.9
        return round(current_total, 2)
    
    def summary(self):
        return f'{self._customer_name}:{self.item_count} items, total: ${self.total:.2f}'
    
cart = ShoppingCart("Nodira", "SAVE10")

cart.add_item("Notebook", 12.99, 3)
cart.add_item("Pen", 1.50, 10)
cart.add_item("Notebook", 12.99, 2)

print(cart.customer_name)
print(cart.item_count)
print(cart.subtotal)
print(cart.total)
print(cart.summary())

cart.apply_discount("SAVE10")
print(cart.total)
print(cart.summary())

cart.remove_item("Pen")
print(cart.item_count)
print(cart.total)

try:
    cart.add_item("Eraser", -5, 1)
except ValueError as e:
    print(e)

try:
    cart.remove_item("Marker")
except ValueError as e:
    print(e)

try:
    cart.apply_discount("SAVE10")
except ValueError as e:
    print(e)

try:
    cart.apply_discount("WRONG")
except ValueError as e:
    print(e)

try:
    cart.customer_name = "Someone"
except AttributeError:
    print("Cannot change customer name")

try:
    print(cart.__discount_code)
except AttributeError:
    print("Cannot access private discount code")