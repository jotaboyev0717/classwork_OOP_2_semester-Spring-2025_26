from dataclasses import dataclass, field

@dataclass
class Supply:
    name: str
    liters: float
    cost_per_liter: float
    
    def total_cost(self) -> float:
        return self.liters * self.cost_per_liter

@dataclass
class Event:
    title: str
    guests: int
    supplies: list[Supply] = field(default_factory=list)
    total_cost: float = field(init=False)
    
    def __post_init__(self):
        self._refresh()
    
    def _refresh(self):
        self.total_cost = 0
        for supply in self.supplies:
            self.total_cost += supply.total_cost()
            
    def add_supply(self, supply: Supply):
        self.supplies.append(supply)
        self._refresh()
        
    def cost_per_guest(self) -> float:
        return self.total_cost / self.guests
    
    def scale(self, new_guests: int):
        ratio = new_guests / self.guests
        
        for supply in self.supplies:
            supply.liters *= ratio
            
        self.guests = new_guests
        self._refresh()
        
    def display(self) -> str:
        result = f"{self.title} ({self.guests} guests):\n"
        
        for supply in self.supplies:
            result += f"  {supply.name}: {supply.liters}L (${supply.total_cost()})\n"
            
        result += f"Per guest: ${self.cost_per_guest()}"
        return result
    
e = Event("Gala Dinner", 50)
e.add_supply(Supply("Juice", 25.0, 4.0))
e.add_supply(Supply("Water", 50.0, 1.5))
e.add_supply(Supply("Coffee", 15.0, 6.0))

print(e.total_cost)
print(e.cost_per_guest())
print(e.display())

e.scale(25)
print(e.display())