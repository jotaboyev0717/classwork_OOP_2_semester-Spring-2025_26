from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass(order = True)
class Fighter(ABC):
    name: str
    base_attack: int
    base_defense: int
    power: int = field(init=False)
    
    @abstractmethod
    def special_bonus(self) -> int:
        pass
    
    def __post_init__(self):
        self.power = self.base_attack + self.base_defense + self.special_bonus()
 
@dataclass       
class Warrior(Fighter):
    armor: int = 10
    
    def special_bonus(self):
        return self.armor * 2
    
@dataclass   
class Assassin(Fighter):
    stealth: int=15
    
    def special_bonus(self):
        return self.stealth * 3
@dataclass
class Arena:
    name: str
    roster: list[Fighter] = field(default_factory=list)
    
    def register(self, fighter: Fighter) -> bool:
        for f in self.roster:
            if f.name == fighter.name:
                return False
        self.roster.append(fighter)
        return True
    
    def match(self, name1: str, name2: str) -> str:
        f1 = None
        f2 = None
        
        for f in self.roster:
            if f.name == name1:
                f1 = f
            if f.name == name2:
                f2 = f
        
        if f1.power > f2.power:
            winner = f1
        elif f2.power > f1.power:
            winner = f2
        
                    
        return f"{f1.name} ({f1.power}) vs {f2.name} ({f2.power}) -> {winner.name} wins"
    
    def leaderboard(self) -> list[str]:
        ranked = sorted(self.roster, key=lambda f: f.power, reverse=True)
        return [f"{i}. {fighter.name} ({fighter.power})" for i, fighter in enumerate(ranked, start=1)]

w1 = Warrior("Duncan", 85, 70, 20)
w2 = Warrior("Stilgar", 78, 65)
a1 = Assassin("Feyd", 90, 50, 25)
a2 = Assassin("Thufir", 60, 80)

arena = Arena("Arrakeen Pit")
print(arena.register(w1))
print(arena.register(a1))
print(arena.register(w2))
print(arena.register(a2))
print(arena.register(Warrior("Duncan", 50, 50)))

print(arena.match("Duncan", "Feyd"))
print(arena.match("Stilgar", "Thufir"))

for line in arena.leaderboard():
    print(line)

