class RangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start += 1
        return value
    
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return RangeIterator(self.start, self.end)

r = Range(1, 4)

for x in r:
    print(x)

print('---')

for x in r:
    print(x)