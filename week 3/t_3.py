class Dish:
    def __init__(self, name, spice_level):
        self.name = name
        self.spice_level = spice_level
        
    def __str__(self):
        return f"{self.name} (spice: {self.spice_level})"
    
    def __gt__(self, other):
        if isinstance(other, Dish):
            return self.spice_level > other.spice_level
        return NotImplemented
d1 = Dish("Pizza", 3)
d2 = Dish("Curry", 8)
print(d1 > d2)
print(d2 > d1)
print(d1)