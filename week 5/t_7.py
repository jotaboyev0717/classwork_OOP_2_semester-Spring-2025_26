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
        self.location = "Hangar"
        
    def warp(self, destination):
        self.location = destination
        print(f"{self.name} warps to {destination}.")
    
    def fire(self, target):
        target.health = max(target.health - 30, 0)
        print(f"{self.name} fires at {target.name}! (-30 HP)")
        
class MedicalCruiser(Moveable, Healer):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.location = "Hangar"
        
    def warp(self, destination):
        self.location = destination
        print(f"{self.name} warps to {destination}.")
    
    def repair(self, target):
        target.health += 20
        print(f"{self.name} repairs {target.name}. (+25 HP)")
        
        
class DefensePlatform(Attacker):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.location = "Hangar"
        
    def fire(self, target):
        target.health = max(target.health -50, 0)
        print(f"{self.name} fires at {target.name}! (-50 HP)")
        
class AlienDrone(Attacker):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.location = "Unknown"
        
    def fire(self, target):
        target.health = max(target.health -20, 0)
        print(f"{self.name} fires at {target.name}! (-20 HP)")
        
class EnemyShip:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class Fleet:
    def __init__(self):
        self.ships = []
    
    def add_ship(self, ship):
        self.ships.append(ship)
    
    def move_fleet(self, destination):
        for ship in self.ships:
            if hasattr(ship, "warp"):
                ship.warp(destination)
            else:
                print(f"{ship.name} cannot move!")

    def support(self, target):
        for ship in self.ships:
            if hasattr(ship, "repair"):
                ship.repair(target)

    def all_out_attack(self, target):
        for ship in self.ships:
            if hasattr(ship, "fire"):
                ship.fire(target)

fleet = Fleet()
fighter = Fighter("X-Wing", 100)
medic = MedicalCruiser("Rescue-1", 80)
platform = DefensePlatform("Alpha Station", 200)
drone = AlienDrone("Bzzz-7", 60)

fleet.add_ship(fighter)
fleet.add_ship(medic)
fleet.add_ship(platform)
fleet.add_ship(drone)

fighter.health = 50  # damaged in earlier battle

print("--- Moving Fleet ---")
fleet.move_fleet("Sector 7")
print(f"X-Wing location: {fighter.location}")
print(f"Rescue-1 location: {medic.location}")
print(f"Alpha Station location: {platform.location}")
print(f"Bzzz-7 location: {drone.location}")

print("\n--- Supporting ---")
fleet.support(fighter)
print(f"X-Wing health: {fighter.health}")

print("\n--- All Out Attack ---")
enemy = EnemyShip("Borg Cube", 150)
fleet.all_out_attack(enemy)
print(f"Borg Cube health: {enemy.health}")