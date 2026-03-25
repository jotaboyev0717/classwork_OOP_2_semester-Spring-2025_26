class Potion:
    def __init__(self, name):
        self.name = name
        self.name_q = {}
        
    def add(self, ingredient, quantity):
        self.name_q[ingredient] = quantity
        
    def __len__(self):
        return len(self.name_q)
    
    def __getitem__(self, ingredient):
        if ingredient not in self.name_q:
            raise KeyError("Ingredient Not found")
        return self.name_q[ingredient]
    
    def __delitem__(self, ingredient):
        if ingredient not in self.name_q:
            raise KeyError("Not found")
        del self.name_q[ingredient]
        
    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_potion = Potion(self.name)
        
        for ingredient, qty in self.name_q.items():
            new_potion.name_q[ingredient] = n * qty
        return new_potion 
    
    def __add__(self, other):
        if not isinstance(other, Potion):
            return NotImplemented
        
        new_potion = Potion(self.name)
        
        for ingredient, qty in self.name_q.items():
            new_potion.name_q[ingredient] = qty
        
        for ingredient, qty in other.name_q.items():
            if ingredient in new_potion.name_q:
                new_potion.name_q[ingredient] += qty
            else:
                new_potion.name_q[ingredient] = qty
        return new_potion
    
    def __str__(self):
        count = len(self.name_q)
        total = sum(self.name_q.values())
        return f"Potion '{self.name}': {count} ingredients, total quantity {total}"
    
    def __repr__(self):
        count = len(self.name_q)
        return f"Potion('{self.name}', {count} ingredients)"
    
    def __eq__(self, value):
        if not isinstance(value, Potion):
            return NotImplemented
        
        return self.name_q == value.name_q
    
    def __bool__(self):
        return len(self.name_q) > 0
    
    def brew(self):
        if not self.name_q:
            return "Nothing to brew!"
        return f"Brewing {self.name} with {len(self.name_q)} ingredients..."
    
    def needed(self, other):
        return sorted([ingredient for ingredient in other.name_q if ingredient not in self.name_q])
    
p1 = Potion("Polyjuice")
p1.add("Lacewing Flies", 3)
p1.add("Leeches", 4)
p1.add("Bicorn Horn", 1)
p1.add("Boomslang Skin", 2)

print(len(p1))
print(p1["Lacewing Flies"])

del p1["Leeches"]
print(len(p1))

p2 = p1 * 2
print(p2["Lacewing Flies"])
print(p2["Boomslang Skin"])

p3 = Potion("Felix Felicis")
p3.add("Ashwinder Egg", 1)
p3.add("Squill Bulb", 2)
p3.add("Boomslang Skin", 3)

p4 = p1 + p3
print(len(p4))
print(p4["Boomslang Skin"])

print(p1)
print(repr(p1))

p5 = Potion("Test")
p5.add("Lacewing Flies", 3)
p5.add("Bicorn Horn", 1)
p5.add("Boomslang Skin", 2)
print(p1 == p5)
print(p1 == p3)

empty = Potion("Water")
if not empty:
    print("No ingredients")

print(p1.brew())
print(empty.brew())

print(p1.needed(p3))