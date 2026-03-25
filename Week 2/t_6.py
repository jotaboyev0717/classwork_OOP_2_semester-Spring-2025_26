class BankAccount:
    def __init__(self, owner: str, initial_balance: float, pin: str) -> None:
        if initial_balance < 0:
            raise ValueError("Balance cannot be negative")
        
        self._owner = owner
        self._balance = initial_balance
        self.__pin = pin
        self.__transactions = []
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount: float, pin: str) -> None:
        if self.__pin != pin:
            raise ValueError("Invalid PIN")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self._balance += amount
        
        self.__transactions.append(("deposit", amount, self._balance))
        
    def withdraw(self, amount: float, pin: str) -> None:
        if self.__pin != pin:
            raise ValueError("Invalid PIN")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self._balance < amount:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        
        self.__transactions.append(("withdraw", amount, self._balance))
        
    @property
    def transaction_count(self) -> int:
        return len(self.__transactions)
    
    def get_statement(self, pin:str) -> str:
        if pin != self.__pin:
            raise ValueError("Invalid PIN")
        
        if len(self.__transactions) == 0:
            return "No transactions yet"
        
        result = ""
        
        for t_type, amount, balance in self.__transactions:
            result += f"{t_type}: ${amount} | Balance: ${balance}\n"
            
        return result.strip()
    
    def transfer(self, amount: float, pin: str, other_account: "BankAccount") -> None:
        if pin != self.__pin:
            raise ValueError("Invalid PIN")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self.__transactions.append(
            ("withdrawal", amount, self._balance)
            )

        other_account._balance += amount
        other_account._BankAccount__transactions.append(
            ("deposit", amount, other_account._balance)
        )
        
a1 = BankAccount("Dilnoza", 1000.0, "1234")
a2 = BankAccount("Jasur", 500.0, "5678")

print(a1.owner)
print(a1.balance)
print(a1.transaction_count)

a1.deposit(250.0, "1234")
print(a1.balance)
print(a1.transaction_count)

a1.withdraw(100.0, "1234")
print(a1.balance)

print(a1.get_statement("1234"))

a1.transfer(200.0, "1234", a2)
print(a1.balance)
print(a2.balance)
print(a1.transaction_count)
print(a2.transaction_count)

try:
    a1.deposit(50.0, "wrong")
except ValueError as e:
    print(e)

try:
    a1.withdraw(5000.0, "1234")
except ValueError as e:
    print(e)

try:
    a1.withdraw(-10.0, "1234")
except ValueError as e:
    print(e)

try:
    a1.balance = 999999
except AttributeError:
    print("Cannot set balance directly")

try:
    a1.owner = "Hacker"
except AttributeError:
    print("Cannot change owner")

try:
    print(a1.__pin)
except AttributeError:
    print("Cannot access private PIN")

try:
    print(a1.get_statement("wrong"))
except ValueError as e:
    print(e)