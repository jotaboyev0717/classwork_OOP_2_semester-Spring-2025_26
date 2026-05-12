from contextlib import contextmanager

class CashRegister:
    def __init__(self,name):
        self.name = name
    
    def _accumulator(self):
        total = 0
        while True:
            value = yield total
            # if value is not None:
            total += value
            
    def __enter__(self):
        self.gen = self._accumulator()
        next(self.gen)
        self.history = []
        return self
    
    def add(self, amount):
        running_total = self.gen.send(amount)
        self.history.append((amount, running_total))
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.gen.close()
        print(f"=== {self.name} ===")
        totalt = 0
        for amount, total in self.history:
            print(f" {amount:+d} -> {total}")
            totalt += amount
        print(f"Final: {totalt}")
        
with CashRegister("Daily Sales") as reg:
    reg.add(100)
    reg.add(50)
    reg.add(-30)
    reg.add(200)
