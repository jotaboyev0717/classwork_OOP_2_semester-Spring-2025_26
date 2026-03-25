class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}!")
        

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed
    
    def info(self):
        print(f"{self.name} is a {self.breed}")
        
dog = Dog("Buddy", "Labrador")
dog.speak()
dog.info()