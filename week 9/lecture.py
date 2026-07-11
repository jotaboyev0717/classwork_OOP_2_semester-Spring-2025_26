from dataclasses import dataclass
@dataclass
class A:
    x: int = 5

@dataclass
class B(A):
    y: int = 10

b = B()
print(b.x, b.y)