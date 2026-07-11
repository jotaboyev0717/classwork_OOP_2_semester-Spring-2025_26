class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age}"
    
    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old!"
    
a = Pet("Puddy", "Dog", 3)
print(a)
b = Pet("Whiskers", "Cat", 2)
print(b.birthday())