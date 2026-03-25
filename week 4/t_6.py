class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

    def cost(self):
        return self.price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def __eq__(self, other):
        return isinstance(other, Item) and self.name == other.name


class DiscountedItem(Item):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def cost(self):
        return self.price * (1 - self.discount)

    def __str__(self):
        percent = int(self.discount * 100)
        return f"{self.name}: ${self.price:.2f} -> ${self.cost():.2f} (-{percent}%)"


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart

    def total(self):
        total = 0
        for item in self.items:
            total += item.cost()
        return total

    def summary(self):
        for item in self.items:
            print(item)
        print(f"Total: ${self.total():.2f} ({len(self)} items)")


def load_cart(data):
    cart = Cart()

    for d in data:
        try:
            if "discount" in d:
                item = DiscountedItem(d["name"], d["price"], d["discount"])
            else:
                item = Item(d["name"], d["price"])
            cart.add(item)
        except ValueError as e:
            print("Skipped:", e)

    return cart


data1 = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": -50},
    {"name": "Keyboard", "price": 75, "discount": 0.2},
]

data2 = [
    {"name": "Monitor", "price": 300, "discount": 0.1},
]

cart1 = load_cart(data1)
cart2 = load_cart(data2)

merged = cart1 + cart2
merged.summary()