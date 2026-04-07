class Car:
    def move(self):
        return f"Driving on the road."
    
class Airplane:
    def move(self):
        return f"Flying through the sky."


def start_journey(vehicle):
        print(vehicle.move())
        
car = Car()
plane = Airplane()

start_journey(car)
start_journey(plane)

hasattr(car, "movie")
# shu object ichida bu method yoki attribute bormi
