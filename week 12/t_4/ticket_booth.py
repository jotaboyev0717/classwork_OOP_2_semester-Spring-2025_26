class TicketBooth:
    def __init__(self, event: str, capacity: int):
        self.event = event
        self._capacity = capacity
        self._sold = 0

    @property
    def remaining(self) -> int:
        return self._capacity - self._sold

    @property
    def is_sold_out(self) -> bool:
        return self._sold >= self._capacity

    def sell(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.remaining:
            raise ValueError("Not enough tickets")
        self._sold += quantity

    def __len__(self) -> int:
        return self._sold
