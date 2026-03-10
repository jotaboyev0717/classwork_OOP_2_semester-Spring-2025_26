class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, name, value):
        self.items.append({"name": name, "value": value})

    def total_gold(self):
        total = 0
        for item in self.items:
            total += item["value"]
        return total

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        item = self.items[index]
        return f"{item['name']} ({item['value']} gold)"

    def __str__(self):
        return f"Inventory '{self.owner}': {len(self)} items, total {self.total_gold()} gold"

    def __repr__(self):
        return f"Inventory('{self.owner}', {len(self)} items)"

    def __add__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented

        new_inventory = Inventory(self.owner)

        for item in self.items:
            new_inventory.add(item["name"], item["value"])

        existing_names = []
        for item in new_inventory.items:
            existing_names.append(item["name"])

        for item in other.items:
            if item["name"] not in existing_names:
                new_inventory.add(item["name"], item["value"])
                existing_names.append(item["name"])

        return new_inventory

    def __sub__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented

        new_inventory = Inventory(self.owner)

        other_names = []
        for item in other.items:
            other_names.append(item["name"])

        for item in self.items:
            if item["name"] not in other_names:
                new_inventory.add(item["name"], item["value"])

        return new_inventory

    def __eq__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented
        return self.total_gold() == other.total_gold()

    def __gt__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented
        return self.total_gold() > other.total_gold()

    def __bool__(self):
        return len(self.items) > 0
    
inv1 = Inventory("Hero")
inv1.add("Sword", 50)
inv1.add("Shield", 30)
inv1.add("Potion", 10)

inv2 = Inventory("Merchant")
inv2.add("Shield", 30)
inv2.add("Bow", 40)

print(len(inv1))
print(inv1[0])
print(inv1)
print(repr(inv1))

inv3 = inv1 + inv2
print(len(inv3))

inv4 = inv1 - inv2
print(len(inv4))
print(inv4[0])

print(inv1 > inv2)

inv5 = Inventory("Traveler")
inv5.add("Ring", 20)
inv5.add("Bow", 50)
print(inv2 == inv5)

empty = Inventory("Goblin")
if not empty:
    print("Inventory is empty")