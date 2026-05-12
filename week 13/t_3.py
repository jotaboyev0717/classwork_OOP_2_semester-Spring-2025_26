from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base):
        self.name = name
        self.base = base
    
    @abstractmethod
    def salary(self): ...
    
class FullTime(Employee):
    def salary(self):
        return self.base + 500000
    
class PartTime(Employee):
    def salary(self):
        return self.base * 0.5
    
class Contractor(Employee):
    def salary(self):
        return self.base * 1.2
    
class PayslipPrinter:
    def display(self, employee):
        print(f"--- Payslip for {employee.name} ---\nSalary: ${employee.salary()}")
        
class PayrollRepository:
    def save(self, employee):
        print(f"INSERT INTO payroll VALUES ('{employee.name}', {employee.salary()})")
        
class Intern(Employee):
    def salary(self):
        return self.base * 0.3
    
employees = [
    FullTime("Aziz", 4_000_000),
    PartTime("Malika", 3_000_000),
    Contractor("Rustam", 5_000_000),
    Intern("Dilnoza", 2_000_000),
]

printer = PayslipPrinter()
repo = PayrollRepository()

for e in employees:
    printer.display(e)
    repo.save(e)
