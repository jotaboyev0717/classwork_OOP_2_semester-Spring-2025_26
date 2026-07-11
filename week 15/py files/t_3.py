class DimmerSwitch:
    def __init__(self, brightness):
        self.brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if not (0 <= value <= 100):
            print("Warning: brightness must be between 0 and 100")
        else:
            self._brightness = value

    def increase(self, amount):
        self.brightness = self._brightness + amount  # setter orqali


a = DimmerSwitch(50)
print(f"Current: {a.brightness}")
a.increase(30)
print(f"Current: {a.brightness}")
a.brightness = 150
print(f"Current: {a.brightness}")