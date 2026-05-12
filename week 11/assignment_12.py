from dataclasses import dataclass, field
from contextlib import contextmanager
class FlightError(Exception):
    pass

@dataclass
class Flight:
    code: str
    destination: str
    distance: int
    _status: str = field(default="SCHEDULED", init=False)
    
    def __post_init__(self):
        if self.distance <= 0:
            raise FlightError(f"Invalid distance for {self.code}")
        
    @property
    def is_long_haul(self):
        return self.distance > 5000
        
    def __str__(self):
        return f"Flight {self.code} to {self.destination} ({self.distance}km) [{self._status}]"
        
    def __gt__(self, other):
        if not isinstance(other, Flight):
            return NotImplemented
        return self.distance > other.distance
        
class BoardingChecker():
    def __init__(self, flights, min_dis):
        self.flights = flights
        self.min_dis = min_dis
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self.flights):
            raise StopIteration
        current_flight = self.flights[self._index]
        if current_flight.distance >= self.min_dis:
            current_flight._status = "CONFIRMED"
        else:
            current_flight._status = "DELAYED"
        self._index += 1
        return current_flight
    
def boarding_report(checker):
    confirmed_count = 0
    delayed_count = 0
    for flight in checker:
        if flight._status == "CONFIRMED":
            confirmed_count += 1
        elif flight._status == "DELAYED":
            delayed_count += 1
        yield str(flight)
    yield f"Report: {confirmed_count} confirmed, {delayed_count} delayed"
    
@contextmanager
def gate_session(name):
    print(f"[BOARD] {name}")
    flights = []
    
    try:
        yield flights
    except FlightError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"[GATE] {name} ({len(flights)} flights)")
        
with gate_session("Morning Departures") as flights:
    flights.append(Flight("AA100", "Paris", 2500))
    flights.append(Flight("BB200", "Tokyo", 5800))
    flights.append(Flight("CC300", "Dublin", 450))

    for line in boarding_report(BoardingChecker(flights, 1000)):
        print(line)

    print(flights[1] > flights[0])

print()

with gate_session("Evening Departures") as flights:
    flights.append(Flight("DD400", "London", -100))
