class Team:
    _total = 0
    def __init__(self, name):
        self.name = name
        self.player_count = 0
        Team._total += 1
        
    def register_player(self):
        self.player_count += 1

    @classmethod
    def total_teams(cls):
        return cls._total
    
    
a = Team("Lions")
a.register_player()
a.register_player()
b = Team("Tigers")
b.register_player()
print(f"Lions players: {a.player_count}")
print(f"Total teams: {Team.total_teams()}")
    