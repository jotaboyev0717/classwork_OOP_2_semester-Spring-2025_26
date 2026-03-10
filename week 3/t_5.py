class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self):
        return f"Color({self.r},{self.g},{self.b})"
    
    def __ne__(self, other):
        if isinstance(other, Color):
            return self.r != other.r or self.g != other.g or self.b != other.b
        return NotImplemented

    
c1 = Color(255, 0, 0)
c2 = Color(0, 0, 255)
c3 = Color(255, 0, 0)
print(c1 != c2)
print(c1 != c3)
print(c1)
