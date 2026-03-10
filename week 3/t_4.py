class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} (age: {self.age})"
    
    def __ge__(self, other):
        if isinstance(other, User):
            return self.age >= other.age
        return NotImplemented
u1 = User("Alisher", 20)
u2 = User("Bobur", 17)
u3 = User("Charos", 20)
print(u1 >= u2)
print(u2 >= u1)
print(u1 >= u3)