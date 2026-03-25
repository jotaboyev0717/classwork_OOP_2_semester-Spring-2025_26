class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False   
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def status(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.name}: {state}"


class SmartLight(Device):
    def __init__(self, name, brightness):
        super().__init__(name)
        self.brightness = brightness   
    
    def status(self):
        if self.is_on:
            return f"{self.name}: ON (brightness: {self.brightness})"
        else:
            return f"{self.name}: OFF"


class House:
    def __init__(self, name):
        self.name = name
        self.devices = []  
    
    def add_device(self, device):
        self.devices.append(device)
    
    def report(self):
        print(self.name)
        for device in self.devices:
            print(device.status())
            
light = SmartLight("Living Room Light", 75)
fan = Device("Ceiling Fan")

light.turn_on()

house = House("My Home")
house.add_device(light)
house.add_device(fan)
house.report()
