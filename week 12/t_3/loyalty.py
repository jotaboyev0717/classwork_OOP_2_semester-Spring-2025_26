class LoyaltyCard:
    def __init__(self, owner: str):
        self.owner = owner
        self._points = 0

    @property
    def points(self) -> int:
        return self._points

    def earn(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Earned amount must be positive")
        self._points += amount

    def redeem(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Redeem amount must be positive")
        if amount > self._points:
            raise ValueError("Not enough points")
        self._points -= amount
