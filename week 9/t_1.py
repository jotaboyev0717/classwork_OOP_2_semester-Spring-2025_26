from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    
b1 = Book("asd", "asv", 150)
b2 = Book("asd", "asv", 150)

print(b1)
print(b1 == b2)