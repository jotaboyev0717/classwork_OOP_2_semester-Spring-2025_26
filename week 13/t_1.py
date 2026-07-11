class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []   
        
    def add(self, title, minutes):
        self.songs.append((title, minutes))
    
    def total_minutes(self):
        return sum(m for _, m in self.songs)

class PlaylistFileWriter:
    def save(self, playlist: Playlist, filename: str):
        with open(filename, "w") as f:
            f.write(f"{playlist.name}\n")
            for title, minutes in playlist.songs:
                f.write(f"{title} - {minutes} min\n")
                
class PlaylistSharer:
    def share(self, playlist: Playlist):
        print(f"🎵 {playlist.name} ({playlist.total_minutes()} min)")
        for title, _ in playlist.songs:
            print(f" • {title}")
        
        
p = Playlist("Road Trip")
p.add("Highway Star", 6)
p.add("Born to Run", 5)

print(p.total_minutes())

PlaylistFileWriter().save(p, "trip.txt")
PlaylistSharer().share(p)