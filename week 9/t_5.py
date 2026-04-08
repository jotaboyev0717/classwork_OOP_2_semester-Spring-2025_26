from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Bounty:
    reward: int
    target: str
    danger: int
@dataclass
class Hunter:
    name: str
    completed: list[Bounty] = field(default_factory=list)#
    total_earnings: int = field(init=False)
    
    def __post_init__(self): #
        self.total_earnings = sum(b.reward for b in self.completed)
    
    def take_bounty(self, bounty: Bounty):
        self.completed.append(bounty)
        self.total_earnings += bounty.reward
        
    def best_catch(self) -> Bounty:
        return max(self.completed)
    
    def resume(self) -> str:
        best = self.best_catch()
        return (
            f"Hunter: {self.name}\n"
            f"Bounties: {len(self.completed)}\n"
            f"Earnings: {self.total_earnings}\n"
            f"Best: {best.target} ({best.reward} credits)"
        )
b1 = Bounty(5000, "Stilgar", 8)
b2 = Bounty(3000, "Liet", 5)
b3 = Bounty(8000, "Irulan", 3)

print(sorted([b3, b1, b2]))

h = Hunter("Gurney")
h.take_bounty(b1)
h.take_bounty(b2)
h.take_bounty(b3)
print(h.total_earnings)
print(h.best_catch())
print(h.resume())
