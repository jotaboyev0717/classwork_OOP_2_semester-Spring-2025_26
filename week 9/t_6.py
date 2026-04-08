from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Transaction:
    amount: int
    sender: str
    receiver: str
    category: str

@dataclass
class Tracker:
    owner: str
    transactions: list[Transaction] = field(default_factory=list)
    balance: int = field(init=False)

    def __post_init__(self):
        self.balance = 0
        for transaction in self.transactions:
            if transaction.receiver == self.owner:
                self.balance += transaction.amount
            elif transaction.sender == self.owner:
                self.balance -= transaction.amount
                
    def record(self, transaction: Transaction):
        self.transactions.append(transaction)
        for transaction in self.transactions:
            if transaction.receiver == self.owner:
                self.balance += transaction.amount
            elif transaction.sender == self.owner:
                self.balance -= transaction.amount
        
    def filter_by(self, category: str) -> list[Transaction]:
        for transaction in self.transactions:
            if transaction.category == category:
                return [transaction]
    def summary(self) -> dict[str, int]:
        result = {}
        for transaction in self.transactions:
            if transaction.category not in result:
                result[transaction.category] = 0

            if transaction.receiver == self.owner:
                result[transaction.category] += transaction.amount
            elif transaction.sender == self.owner:
                result[transaction.category] -= transaction.amount

        return result
            
    def top_partners(self, n: int) -> list[tuple[str, int]]:
        partners = {}

        for transaction in self.transactions:
            if transaction.sender == self.owner:
                partner = transaction.receiver
            elif transaction.receiver == self.owner:
                partner = transaction.sender
            else:
                continue

            if partner not in partners:
                partners[partner] = 0

            partners[partner] += transaction.amount

        sorted_partners = sorted(partners.items(), key=lambda x: x[1], reverse=True)
        return sorted_partners[:n]   
t1 = Transaction(5000, "Gurney", "Duncan", "spice")
t2 = Transaction(3000, "Duncan", "Stilgar", "weapons")
t3 = Transaction(2000, "Chani", "Duncan", "spice")
t4 = Transaction(1000, "Duncan", "Gurney", "supplies")

print(sorted([t3, t1, t4, t2]))

tracker = Tracker("Duncan")
tracker.record(t1)
tracker.record(t2)
tracker.record(t3)
tracker.record(t4)
print(tracker.balance)
print(tracker.filter_by("spice"))
print(tracker.summary())
print(tracker.top_partners(2))
