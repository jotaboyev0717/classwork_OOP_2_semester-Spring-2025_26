class Package:
    def __init__(self, weight):
        self.weight = weight
    
    def __str__(self):
        return f"Package({self.weight}kg)"
    
    def __le__(self, other):
        if isinstance(other, Package):
            return self.weight <= other.weight
        return NotImplemented
    
p1 = Package(5)
p2 = Package(10)
p3 = Package(5)
print(p1 <= p2)
print(p2 <= p1)
print(p1 <= p3)