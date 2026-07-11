class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, battery_kwh):
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh
    
    def info(self):
        return f"{self.brand} {self.model} ({self.year}), battery: {self.battery_kwh} X kWh"

    @classmethod
    def from_dict(cls, data):
        key_v = ["brand", "model", "year", "battery_kwh"]
        for key in key_v:
            if key not in data:
                raise KeyError(f"Missing key: {key}")
        return cls(data["brand"], data["model"], data["year"], data["battery_kwh"])
    
    @classmethod
    def from_string(cls, data):
        
        new = data.split(",")
        if len(new) != 4:
            raise ValueError("Invalid vehicle data")
        return cls(new[0], new[1], new[2], new[3])
    

a = Vehicle("BMW", "S", 2015)
print(Vehicle.info(a))
print()
b = {"brand": "Tesla", "model": "Model 3", "year": 2023, "battery_kwh": 75}
c = ElectricVehicle.from_dict(b)
print(ElectricVehicle.info(c))
print()
d = f"Tesla,Model 3,2023,75"
e = ElectricVehicle.from_string(d)
print(ElectricVehicle.info(e))
print()
