from dataclasses import dataclass, field

@dataclass(order=True)
class Flight:
    airline: str
    code: str
    scheduled_time: str

    def __post_init__(self):
        parts = self.scheduled_time.split(":")
        if len(parts) != 2 or not (0 <= int(parts[0]) <= 23 and 0 <= int(parts[1]) <= 59):
            raise ValueError("Invalid time format, expected: HH:MM")
        
    def time_in_minutes(self):
        parts = self.scheduled_time.split(":")
        total_min = int(parts[0]) * 60 + int(parts[1])
        return total_min
    
class Gate:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def conflicting_flight(self, flight):
        new_parts = flight.scheduled_time.split(":")
        new_min = int(new_parts[0]) * 60 + int(new_parts[1])

        for existing in self.flights:
            parts = existing.scheduled_time.split(":")
            existing_min = int(parts[0]) * 60 + int(parts[1])
            if abs(new_min - existing_min) < 30:
                return existing

        return None
    def assign(self, flight):
        conflict = self.conflicting_flight(flight)
        if conflict is None:
            self.flights.append(flight)
            return True
        else:
            print(f"Conflict with {conflict.code} at {conflict.scheduled_time}")
            return False
    
    def schedule(self):
        for flight in sorted(self.flights):
            print(f"{flight.scheduled_time} — {flight.airline} ({flight.code})")


a = Gate("B3")
f1 = Flight("AZ101", "Azur Air", "08:00")
flights = [Flight("AZ101", "Azur Air", "08:00"),
           Flight("TR205", "Turkish Airlines", "08:15"),
           Flight("TR205", "Turkish Airlines", "08:45"),
           Flight("UZ777", "Uzbekistan Airways", "09:20"),
           Flight("FR304", "Ryanair", "09:00")]
for flight1 in flights:
    a.assign(flight1)
a.schedule()
