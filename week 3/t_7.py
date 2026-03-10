class Duration:
    def __init__(self, time):
        self.time = time
        
    def __str__(self):
        return f"{self.time//60}h {self.time%60}m"
    
    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(self.time + other.time)
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Duration):
            return self.time > other.time
        return NotImplemented
    def __bool__(self):
        return self.time != 0
d1 = Duration(90)
d2 = Duration(45)
d3 = d1 + d2
print(d1)
print(d2)
print(d3)
print(d1 > d2)
d4 = Duration(0)
if not d4:
    print("No time left")
