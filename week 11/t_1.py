class RepeatWord:
    def __init__(self, word, n):
        self.word = word
        self.n = n
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= self.n:
            raise StopIteration
        self.counter += 1
        return self.word

for w in RepeatWord('hello', 4):
    print(w)
