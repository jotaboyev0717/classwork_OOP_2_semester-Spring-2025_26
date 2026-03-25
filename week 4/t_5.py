class Handler:
    def process(self, package):
        print(f"Handling: {package.label}")
        
class Scanner(Handler):
    def process(self, package):
        print(f"Scanning {package.label}")
        super().process(package)
        
class Weigher(Handler):
    def process(self, package):
        print(f"Weighing {package.label}: {package.weight}kg")
        super().process(package)
        
class AutomatedStation(Scanner, Weigher):
    def process(self, package):
        print("--- Automated Station ---")
        super().process(package)
        
class Package:
    def __init__(self, label, weight):
        self.label = label
        self.weight = weight
        
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.stations = []
        
    def add_station(self, station):
        self.stations.append(station)
        
    def process_package(self, package):
        print(f"Warehouse: {self.name}")
        for station in self.stations:
            station.process(package)
            
pkg = Package("PKG-001", 3.5)

auto = AutomatedStation()
manual = Scanner()

wh = Warehouse("Central Hub")
wh.add_station(auto)
wh.add_station(manual)
wh.process_package(pkg)