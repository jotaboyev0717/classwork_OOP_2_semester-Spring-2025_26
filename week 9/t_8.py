from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Cargo:
    value: int
    cargo_type: str
    weight: int

@dataclass  
class Ship:
    name: str
    capacity: int
    hold: list[Cargo] = field(default_factory=list)
    
    @property
    def remaining_capacity(self):
        current_weight = sum(cargo.weight for cargo in self.hold)
        return self.capacity - current_weight
    
    @classmethod
    def from_string(cls, text: str) -> 'Ship':
        name, capacity = text.split(":")
        return cls(name.strip(), int(capacity.strip()))
    
    def load(self, cargo: Cargo) -> bool:
        if cargo.weight <= self.remaining_capacity:
            self.hold.append(cargo)
            return True
        return False

    def __add__(self, other: 'Ship') -> 'Ship':
        if not isinstance(other, Ship):
            return NotImplemented
        new_name = f"{self.name} & {other.name}"
        new_capacity = self.capacity + other.capacity
        new_hold = self.hold + other.hold
        return Ship(new_name, new_capacity, new_hold)
    
    def __contains__(self, cargo_type: str) -> bool:
        return any(cargo.cargo_type == cargo_type for cargo in self.hold)
    
    def transfer(self, other: 'Ship', cargo_type: str) -> bool:
        for cargo in self.hold:
            if cargo.cargo_type == cargo_type:
                if other.load(cargo):
                    self.hold.remove(cargo)
                    return True
        return False
c1 = Cargo(5000, "Spice", 30)
c2 = Cargo(2000, "Water", 50)
c3 = Cargo(8000, "Artifacts", 20)

s1 = Ship.from_string("Atreides Frigate:80")
s1.load(c1)
s1.load(c2)
print(s1.remaining_capacity)

s2 = Ship("Smuggler", 60)
s2.load(c3)
print(s2.remaining_capacity)

print("Spice" in s1)
print("Spice" in s2)

print(s1.transfer(s2, "Spice"))
print("Spice" in s1)
print("Spice" in s2)
print(s1.remaining_capacity)
print(s2.remaining_capacity)

print(s1.transfer(s2, "Water"))
print(s1.transfer(s2, "Weapons"))
