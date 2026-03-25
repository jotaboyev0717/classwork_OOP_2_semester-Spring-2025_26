class Instrument:
    def __init__(self, name):
        self.name = name
        
    def play(self):
        return f"Playing the {self.name}."
    

class Guitar(Instrument):
    def play(self):
        return f"Strumming the {self.name}."
    
class Drum(Instrument):
    def play(self):
        return f"Beating the {self.name}."
    
def concert(instruments):
    for i in instruments:
        s = i.play()
        print(s)

instruments = [
    Instrument("flute"),
    Guitar("acoustic guitar"),
    Drum("snare drum")
]

concert(instruments)