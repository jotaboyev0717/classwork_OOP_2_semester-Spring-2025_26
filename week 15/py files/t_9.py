from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class WeatherReading:
    station_id: str
    temperature: float
    humidity: int

class WeatherWatcher(ABC):
    @abstractmethod
    def update(self, event):
        pass

class TemperatureAlert(WeatherWatcher):
    def __init__(self, threshold: float):
        self.threshold = threshold
    def update(self, event):
        if event.temperature > self.threshold:
            print(f"ALERT: {event.station_id} temperature {event.temperature}C exceeds {self.threshold}C")
class StormLogger(WeatherWatcher):
    def __init__(self):
        self.log = []
        
    def update(self, event):
        self.log.append(event)
        print(f"LOG: {event.station_id} — temp={event.temperature}C, humidity={event.humidity}%")

class WeatherStation:
    def __init__(self):
        self._watchers = []

    def subscribe(self, watcher):
        self._watchers.append(watcher)
    
    def unsubscribe(self, watcher):
        self._watchers.remove(watcher)

    def broadcast(self, event):
        for watcher in self._watchers:
            watcher.update(event)

station = WeatherStation()
alert = TemperatureAlert(30.0)
logger = StormLogger()

station.subscribe(alert)
station.subscribe(logger)
station.broadcast(WeatherReading("Station-A", 32.5, 80))

print()
station.unsubscribe(alert)
station.broadcast(WeatherReading("Station-B", 35.0, 90))