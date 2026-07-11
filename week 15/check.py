# class Pet:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age
    
#     def __repr__(self):
#         return f"{self.name} is a {self.species} aged by {self.age}"
    
#     def birthday(self):
#         self.age += 1
#         return f"{self.name} is a {self.age} years old!"

# a = Pet("Buddy", "Dog", 3)
# print(a)
# b = Pet("Whiskers", "Cat", 2)
# print(b.birthday())

# class Team:
# 	_total = 0
	
# 	def __init__(self, name):
# 		self.name = name
# 		self.player_count = 0
# 		Team._total += 1

# 	def register_player(self):
# 		self.player_count += 1

# 	@classmethod
# 	def total_teams(cls):
# 		return cls._total

# a = Team("Lions")
# a.register_player(2)

# b = Team("Tigers")
# b.register_player(1)

# print(f"Lions players: {a.player_count}")
# print(f"Total teams: {Team._total}")

class DimmerSwitch:
	def __init__(self):
		self._brightness = 0

	@property
	def brightness(self):
		return self._brightness

	@brightness.setter
	def brightness(self, value):
		if not (0 <= value <= 100):
			print("Invalid ")
		else:
			self._brightness = value

	def increase(self, amount):
		if self._brightness + amount > 101:
			print("Warning")
		else:
			self._brightness += amount

a = DimmerSwitch()
a.brightness = 50
print(a.brightness)
a.increase(30)
print(a.brightness)
a.brightness = 150
print(a.brightness)

	