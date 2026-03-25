from abc import ABC, abstractmethod

def audit_action(func):
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] Action: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

class Media(ABC):
    def __init__(self, title, price):
        self.title = title
        self.price = price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value< 0:
            raise ValueError("Price cannot be negative")
        self._price = value
        
    @abstractmethod
    def consume(self):
        pass
    
    def __str__(self):
        return f"{self.title} (${self._price})"
    
class Movie(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration
      
    @audit_action   
    def consume(self):
        return f"Watching {self.title} ({self.duration}m)"
    
class Song(Media):
    def __init__(self, title, price, artist):
        super().__init__(title, price)
        self.artist = artist
        
    @audit_action
    def consume(self):
        return f"Listening to {self.title} by {self.artist}"
    
class Library:
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        
    def add_item(self, media):
        self.items.append(media)
    
    def __len__(self):
        return len(self.items)
    
    def __add__(self, other):
        if isinstance(other, Library):
            new_owner = f"{self.owner} & {other.owner}"
            new_library = Library(new_owner)
            new_library.items = self.items + other.items
            return new_library
        return NotImplemented
    
    def play_all(self):
        for item in self.items:
            result = item.consume()
            
            print(result) #
        
class User:
    platform_name = "NetStream"
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        self.library = Library(username)
        
    def purchase(self, media):
        if self.balance >= media.price:
            self.balance -= media.price
            self.library.add_item(media)
        else:
             raise ValueError("Insufficient funds")
    @classmethod
    def from_string(cls, data):
        user, balance = data.split(":")
        balance = float(balance)
        return cls(user, balance)
        
    @staticmethod
    def is_valid_username(name):
        return len(name) > 5
    
print(f"Valid username 'Ali': {User.is_valid_username('Ali')}")
print(f"Valid username 'Alisher': {User.is_valid_username('Alisher')}")

user1 = User("Nodira", 20.0)
user2 = User.from_string("Jasur:15.0")

movie1 = Movie("Inception", 12.0, 148)
song1 = Song("Shape of You", 2.0, "Ed Sheeran")
song2 = Song("Blinding Lights", 3.0, "The Weeknd")

try:
    bad_movie = Movie("Bad Movie", -5.0, 90)
except ValueError as e:
    print(f"Error: {e}")

user1.purchase(movie1)
user1.purchase(song1)

try:
    user1.purchase(movie1)
except ValueError as e:
    print(f"Purchase failed: {e}")

user2.purchase(song2)

print(f"{user1.username}'s library has {len(user1.library)} items.")

shared_library = user1.library + user2.library
print(f"Shared Library Owner: {shared_library.owner}")
print(f"Shared Library Size: {len(shared_library)}")

shared_library.play_all()