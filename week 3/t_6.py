class MovieQueue:
    def __init__(self):
        self.movies = []
        
    def add(self, movie):
        self.movies.append(movie)
        
    def __str__(self):
        return f"MovieQueue: {len(self.movies)} movies"
    
    def __getitem__(self, index):
        return self.movies[index]
        
q = MovieQueue()
q.add("Inception")
q.add("Interstellar")
q.add("The Matrix")
print(q[0])
print(q[2])
print(q)