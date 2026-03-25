from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass
    
class SurvivalGear(ABC):
    @abstractmethod
    def use(self, user):
        pass
    
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class M60MachineGun(Weapon):
    def attack(self, target):
        if target.health - 40 >= 0:
            target.health -= 40
        else:
            target.health = 0        
        print(f"Rambo sprays bullets at {target.name}! (-40 HP)")
        
class Medkit(SurvivalGear):
    def use(self, user):
        user.health += 50
        print(f"Rambo bandages his wounds. (+50 HP)")
        
class ExplosiveArrow(SurvivalGear, Weapon):
    def attack(self, target):
        if target.health - 60 >= 0:
            target.health -= 60
        else:
            target.health = 0
        print(f"Rambo fires an explosive arrow at {target.name}!! BOOM! (-60 HP)")
        
    def use(self, user):
        user.health += 20
        print(f"Rambo uses the arrow powder to start a campfire. (+20 HP)")
        
class Rambo:
    def __init__(self):
        self.health = 100
        self.inventory = []
        
    def pick_up(self, item):
        self.inventory.append(item)
    
    def engage(self, target):
        for item in self.inventory:
            if isinstance(item, Weapon):
                item.attack(target)
            
    def survive(self):
        for item in self.inventory:
            if isinstance(item, SurvivalGear):
                item.use(self)
    
            
rambo = Rambo()
enemy = Enemy("Sheriff Teasle", 100)

rambo.pick_up(M60MachineGun())
rambo.pick_up(Medkit())
rambo.pick_up(ExplosiveArrow())

rambo.engage(enemy)
print(f"Sheriff Teasle's Health: {enemy.health}")
print("---")
rambo.survive()
print(f"Rambo's Health: {rambo.health}")