from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fee(self, hours): ...
    
class Bike(Vehicle):
    def fee(self, hours):
        return hours * 1000
    
class Car(Vehicle):
    def fee(self, hours):
        return hours * 3000
    
class Truck(Vehicle):
    def fee(self, hours):
        return hours * 7000

class ParkingFeeCalculator:
    def calculate(self, vehicle: Vehicle, hours):
        return vehicle.fee(hours)

class Scooter(Vehicle):
    def fee(self, hours):
        return hours * 500

calc = ParkingFeeCalculator()

print(calc.calculate(Bike(), 2))
print(calc.calculate(Car(), 3))
print(calc.calculate(Truck(), 1))
print(calc.calculate(Scooter(), 4))
