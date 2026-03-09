class BankAccount:
    bank_name = "Urgench Bank"
    total_accounts = 0
    min_balance = 10 
    
    def __init__(self, owner, inital_balance):
        self.owner = owner
        self.balance = inital_balance
        
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
            
    def withdraw(self, amount):
        remaining_balance = self.balance - amount
        if remaining_balance >= BankAccount.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or below minimum balance")
    def display_account_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}, Bank: {BankAccount.bank_name}")


acc1 = BankAccount("Ali", 100)
acc2 = BankAccount("Vali", 50)
acc1.display_account_info()
acc1.deposit(50)
acc1.withdraw(80)
acc2.display_account_info()
acc2.withdraw(100)
print(f"Total accounts created: {BankAccount.total_accounts}")