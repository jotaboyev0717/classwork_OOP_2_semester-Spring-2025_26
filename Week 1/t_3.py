class ShoppingCart:
    store_name = "Online Bazar"
    tax_rate = 0.08
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        
    def add_item(self, item_name, price):
        if price <= 0:
            print("Invalid price. Must be greater than 0")
        else:
            self.items.append({"name": item_name, "price": price})
            print(f"Added {item_name} (${price}) to cart")
            
    def remove_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                print(f'Removed {item_name} from cart')
                return
        print(f"Item '{item_name}' not found in cart")
                
    def get_subtotal(self):
        total_sum = 0
        for item in self.items:
            total_sum += item['price']
        return total_sum
    
    def get_total(self):
        sub = self.get_subtotal()
        return sub + (sub * self.tax_rate)
    
    def display_cart(self):
        print(f"Cart for {self.customer_name} at {self.store_name}:")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']}")
        sub = self.get_subtotal()
        total = self.get_total()
        print(f"Subtotal: ${sub}")
        print(f"Total(with tax): ${total}")
    
cart = ShoppingCart("Dilshod")
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 25.50)
cart.add_item("Keyboard", 75.00)

cart.remove_item("Mouse")

cart.display_cart()

print(cart.get_subtotal())
print(cart.get_total())