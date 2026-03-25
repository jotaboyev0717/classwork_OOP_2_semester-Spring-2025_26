class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def describe(self):
        print(f"{self.name}, salary: {self.salary}")
        

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def describe(self):
        super().describe()
        print(F"Department: {self.department}")
        
e = Employee("Ali", 5000)
m = Manager("Nilufar", 9000, "Engineering")
e.describe()
print("---")
m.describe()
