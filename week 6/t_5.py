class Package:
    def __init__(self, name, weight_kg):
        self.name = name
        self.weight_kg = weight_kg
    
    @classmethod
    def from_string(cls, data):
        name, weight_kg = data.split(':')
        weight_kg = float(weight_kg)
        return cls(name, weight_kg)
    
    @classmethod
    def from_pounds(cls, name, weight_lb):
        weight_lb = round(weight_lb / 2.205, 2)
        return cls(name, weight_lb)
    
    def label(self):
        return f"Package '{self.name}' — {self.weight_kg} kg"
    
p1 = Package("Electronics", 1.2)
p2 = Package.from_string("Books:3.5")
p3 = Package.from_pounds("Clothes", 11)

print(p1.label())
print(p2.label())
print(p3.label())