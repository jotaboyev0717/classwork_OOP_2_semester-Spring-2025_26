from abc import ABC, abstractmethod

class Moveable(ABC):
    @abstractmethod
    def warp(self, destination):
        pass
    
class Attacker(ABC):
    @abstractmethod
    def fire(self, target):
        pass
    
class Healer(ABC):
    @abstractmethod
    def repair(self, target):
        pass
    
class Fighter(Moveable, Attacker):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def warp(self, destination):
        print(f"{self.name} warps to {destination}.")
    
    def fire(self, target):
        target.health = max(target.health - 30, 0)
        print(f"{self.name} fires at {target.name}! (-30 HP)")
        
class MedicalCruiser(Moveable, Healer):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def warp(self, destination):
        return super().warp(destination)
    
    def repair(self, target):
        target.health += 20
        print(f"{self.name} repairs {target.name}. (+25 HP)")
        
        
class DefensePlatform(Attacker):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def fire(self, target):
        target.health -= 50
        
class AlienDrone(Attacker):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def fire(self, target):
        self.health -= 20
        
# class EnemyShip:
#     def __init__(self):