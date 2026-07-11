def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))