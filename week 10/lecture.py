class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Miqdor musbat bo'lishi kerak")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Miqdor musbat bo'lishi kerak")
        if amount > self.balance:
            raise InsufficientFundsError("Mablag' yetarli emas")
        self.balance -= amount

acc = BankAccount("Sevara", 500)

try:
    acc.withdraw(-1000)
except InsufficientFundsError as e:
    print(f"Mablag' yetmadi: {e}")
except NegativeAmountError as e:
    print(f"Noto'g'ri miqdor: {e}")
