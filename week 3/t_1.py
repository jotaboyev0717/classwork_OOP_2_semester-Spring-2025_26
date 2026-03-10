class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    def __str__(self):
        return f"{self.celsius}°C"
    
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        return NotImplemented
t1 = Temperature(15)
t2 = Temperature(30)
print(t1 < t2)
print(t2 < t1)
print(t1)