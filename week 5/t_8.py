from abc import ABC, abstractmethod

class Interactable(ABC):
    @abstractmethod
    def interact(self, character):
        pass
        

class Fightable(ABC):
    @abstractmethod
    def take_hit(self, damage):
        pass
    
class Potion(Interactable):
    def __init__(self, power):
        self.power = power
    
    def interact(self, character):
        character.health += self.power 
        return f"Healed {self.power} HP"
    
class Sword(Interactable):
    def __init__(self, bonus):
        self.bonus = bonus
        
    def interact(self, character):
        character.attack += self.bonus
        return f"Attack +{self.bonus}"
    
class Mimic:
    def interact(self, character):
        character.health = max(character.health-15, 0)
        return "It's a Mimic! -15 HP"
    
    
class Monster(Fightable):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def take_hit(self, damage):
        self.health = max(0, self.health - damage)
        return self.health > 0
        
class Hero(Fightable):
    def __init__(self, name):
        self.health = 100
        self.attack = 10
        self.name = name
        self.inventory = []
    
    def take_hit(self, damage):
        self.health = max(0, self.health - damage)
        return self.health > 0
    
    def pick_up(self, item):
        self.inventory.append(item)
        return item.interact(self)
    
    def fight(self, monster):
        while True:
            print(f"{self.name} hits {monster.name} for {self.attack} damage.")
            alive = monster.take_hit(self.attack)
            if not alive:
                print(f"{monster.name} has been defeated.")
                break

            print(f"{monster.name} hits {self.name} for {monster.attack} damage.")
            alive = self.take_hit(monster.attack)
            if not alive:
                print(f"{self.name} has been defeated.")
                break
            

class Room:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.monster = None

    def place_item(self, item):
        self.items.append(item)

    def place_monster(self, monster):
        self.monster = monster

    def is_cleared(self):
        no_items = len(self.items) == 0
        no_living_monster = self.monster is None or self.monster.health == 0
        return no_items and no_living_monster


class Dungeon:
    def __init__(self, rooms):
        self.rooms = rooms

    def explore(self, hero):
        for room in self.rooms:
            print(f"Entering room: {room.name}")

            while room.items:
                item = room.items.pop(0)
                result = hero.pick_up(item)
                print(result)

            if room.monster is not None and room.monster.health > 0:
                hero.fight(room.monster)
                if hero.health == 0:
                    print("Game Over")
                    return

        print("Dungeon cleared!")

# room1 = Room("Armory")
# room1.place_item(Potion(30))
# room1.place_item(Sword(5))

# room2 = Room("Trap Room")
# room2.place_item(Mimic())

# room3 = Room("Boss Chamber")
# room3.place_item(Potion(50))
# room3.place_monster(Monster("Dragon", 60, 25))

# hero = Hero("Aldric")
# dungeon = Dungeon([room1, room2, room3])
# dungeon.explore(hero)

# print(f"{hero.name}'s final health: {hero.health}")
# print(f"{hero.name}'s attack: {hero.attack}")

# room_a = Room("Dark Hallway")
# room_a.place_monster(Monster("Golem", 30, 120))

# hero2 = Hero("Bren")
# dungeon2 = Dungeon([room_a, Room("Treasure Room")])
# dungeon2.explore(hero2)
# print(f"{hero2.name}'s final health: {hero2.health}")

room_x = Room("Empty Room")
print(f"Empty room cleared? {room_x.is_cleared()}")

room_x.place_item(Potion(10))
print(f"Room with item cleared? {room_x.is_cleared()}")

room_y = Room("Monster Den")
room_y.place_monster(Monster("Rat", 5, 2))
print(f"Room with alive monster cleared? {room_y.is_cleared()}")

room_y.monster.take_hit(100)
print(f"Room with dead monster cleared? {room_y.is_cleared()}")

try:
    Interactable()
except TypeError:
    print("Cannot instantiate Interactable")

try:
    Fightable()
except TypeError:
    print("Cannot instantiate Fightable")