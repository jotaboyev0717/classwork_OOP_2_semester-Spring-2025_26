class TemperatureReading:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature
        
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._temperature = value
        
r1 = TemperatureReading("Tashkent", 35.0)
print(r1.location)
print(r1.temperature)

r1.temperature = -10.5
print(r1.temperature)

try:
    r1.temperature = -300
except ValueError as e:
    print(e)