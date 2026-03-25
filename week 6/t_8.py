def ensure_active(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        if not self._active:
            print(f"Auction closed for {self.name}")
            return
        return func(*args, **kwargs)
    return wrapper

class AuctionItem:
    def __init__(self, name, starting_price):
        self.name = name
        self.starting_price = starting_price
        