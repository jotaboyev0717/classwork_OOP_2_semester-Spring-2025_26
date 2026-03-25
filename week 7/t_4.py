from abc import ABC, abstractmethod

class DeliveryVehicle(ABC):
    def __init__(self, vehicle_id):
        self.veicle_id = vehicle_id
        
    @abstractmethod
    def estimated_time(self, distance):
        pass
    
    def describe(self):
        return f"{self.__class__.__name__} {self.veicle_id}"
    
class Drone(DeliveryVehicle):
    def estimated_time(self, distance):
        return distance / 50.0
    
class CargoVan(DeliveryVehicle):
    def __init__(self, vehicle_id, loading_time):
        super().__init__(vehicle_id)
        self.loading_time = loading_time
        
    def estimated_time(self, distance):
        return distance / 80 + self.loading_time
    
class CourierService:
    def __init__(self, name):
        self.name = name
        self.fleet = []
        
    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)
    
    def get_fastest_vehicle(self, distance):
        fastest = min(self.fleet, key=lambda v: v.estimated_time(distance))
        time = fastest.estimated_time(distance)

        print(f"Dispatching {fastest.describe()} - ETA: {time} hours")
        return fastest
    
service = CourierService("Express City Delivery")

drone1 = Drone("D-01")
van1 = CargoVan("V-100", loading_time=0.5)
van2 = CargoVan("V-101", loading_time=0.2)

service.add_vehicle(drone1)
service.add_vehicle(van1)
service.add_vehicle(van2)

fastest_short = service.get_fastest_vehicle(10)
fastest_long = service.get_fastest_vehicle(100)

try:
    vehicle = DeliveryVehicle("X-01")
except TypeError:
    print("Cannot instantiate abstract class")