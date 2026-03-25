class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def info(self):
        return f"{self.title} ({self.year})"

class Book(Media):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author
        
    def info(self):
        base = super().info()
        return f"{base} by {self.author}"
    
class AudioBook(Book):
    def __init__(self, title, year, author, narrator):
        super().__init__(title, year, author)  
        self.narrator = narrator
    def info(self):
        base = super().info()
        return f"{base}, narrated by {self.narrator}"
      
class Library:
    def __init__(self, name):
        self.name = name
        self.media = []

    def add(self, media):
        self.media.append(media)

    def catalog(self):
        print(self.name)
        for item in self.media:
            print(item.info())

m = Media("Interstellar OST", 2014)
b = Book("Clean Code", 2008, "Robert C. Martin")
a = AudioBook("Dune", 1965, "Frank Herbert", "Scott Brick")

lib = Library("City Library")
lib.add(m)
lib.add(b)
lib.add(a)
lib.catalog()
