class PastryBatch :
    def __init__(self, pastry_name: str, price_per_piece: float, piece_count: int):
        self.pastry_name = pastry_name
        self.price_per_piece = price_per_piece
        self.piece_count = piece_count
        
    def __str__(self):
        return f"{self.pastry_name}: {self.piece_count} piece(s) at ${self.price_per_piece}"
    
    def __repr__(self):
        return f"PastryBatch('{self.pastry_name}', {self.price_per_piece}, {self.piece_count})"
    
    def __add__(self, other):
        if isinstance(other, PastryBatch):
            if self.pastry_name == other.pastry_name:
                return PastryBatch(
                    self.pastry_name,
                    self.price_per_piece,
                    self.piece_count + other.piece_count
                )
            return NotImplemented

        if isinstance(other, int):
            return PastryBatch(
                self.pastry_name,
                self.price_per_piece,
                self.piece_count + other
            )
        
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, PastryBatch):
            return (
                self.pastry_name == other.pastry_name and
                self.price_per_piece == other.price_per_piece
            )
        return NotImplemented
    
    def __bool__(self):
        return self.piece_count > 0
    
batch1 = PastryBatch("Croissant", 3.5, 12)
batch2 = PastryBatch("Croissant", 3.5, 6)
batch3 = PastryBatch("Muffin", 4.0, 0)

print(str(batch1))
print(repr(batch1))
print(batch1 + batch2)
print(batch1 + 10)
print(batch1 == batch2)
print(bool(batch1))
print(bool(batch3))