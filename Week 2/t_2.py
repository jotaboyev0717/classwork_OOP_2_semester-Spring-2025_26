class Movie:
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating
    @property
    def title(self):          
        return self._title

    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if rating < 1 or rating >10:
            raise ValueError("Rating must be between 1 and 10")
        self._rating = rating
    
    def display(self):
        print(f"{self.title} - {self.rating}/10")
        
m = Movie("Inception", 9)
m.display()

m.rating = 7
m.display()

try:
    m.rating = 11
except ValueError as e:
    print(e)

try:
    m.title = "New Title"
except AttributeError:
    print("Cannot change title")