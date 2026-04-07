def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is True:
            print(f"[OK] {func.__name__} successful")
        elif result is False:
            print(f"[FAIL] {func.__name__} denied")
        return result
    return wrapper


class ParkingLot:
    _all_lots = []

    def __init__(self, location, total_spots):
        self.location = location
        self.total_spots = int(total_spots)
        self._occupied = 0
        ParkingLot._all_lots.append(self)

    @log_operation
    def enter(self):
        if self._occupied == self.total_spots:
            return False
        self._occupied += 1
        return True

    @log_operation
    def exit_lot(self):
        if self._occupied == 0:
            return False
        self._occupied -= 1
        return True

    def free_spots(self):
        return self.total_spots - self._occupied

    def occupancy_rate(self):
        value = (self._occupied / self.total_spots) * 100
        return float(round(value, 1))

    @classmethod
    def from_record(cls, entry):
        location, spots = entry.split(":")
        return cls(location, int(spots))

    @staticmethod
    def is_valid_plate(plate):
        return len(plate) == 13 and plate.isdigit()

    @classmethod
    def total_free(cls):
        total = 0
        for lot in cls._all_lots:
            total += lot.free_spots()
        return total


l1 = ParkingLot("Central Mall", 2)
l2 = ParkingLot.from_record("Airport:3")

l1.enter()
l1.enter()
l1.enter()
l1.exit_lot()

l2.enter()
l2.exit_lot()
l2.exit_lot()

print(f"{l1.location}: free = {l1.free_spots()}, occupancy = {l1.occupancy_rate()}%")
print(f"{l2.location}: free = {l2.free_spots()}, occupancy = {l2.occupancy_rate()}%")

print(f"Valid plate '0123456789012': {ParkingLot.is_valid_plate('0123456789012')}")
print(f"Valid plate '012-345': {ParkingLot.is_valid_plate('012-345')}")
print(f"Total free spots: {ParkingLot.total_free()}")