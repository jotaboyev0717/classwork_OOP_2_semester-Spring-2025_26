class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def display_info(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration}min")
        
    def get_duration_seconds(self):
        return self.duration * 60

first = Song('Yesterday', "The Beatles", 2.5)
second = Song("Bohemian Rhapsody", "Queen", 6.0)
first.display_info()
second.display_info()
print(second.get_duration_seconds())