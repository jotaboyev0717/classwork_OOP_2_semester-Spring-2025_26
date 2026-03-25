class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = capacity
    def use(self, amount):
        if self.charge >= amount:
            self.charge -= amount
            return True
        return False
    
    def is_empty(self):
        return self.charge <= 0
    
class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.position = 0
        self.battery = battery
        
    def move(self):
        if self.battery.use(1):
            self.position += 1
            print(f"{self.name} moves to position {self.position}")
        else:
            print(f"{self.name} is out of charge!")
            
class TurboBot(Robot):
    def move(self):
        if self.battery.use(2):
            self.position += 3
            print(f"{self.name} moves to position {self.position}")
        else:
            print(f"{self.name} is out of charge!")
            
class SteadyBot(Robot):
    def __init__(self, name, battery):
        super().__init__(name, battery)
        self._step_count = 0
    def move(self):
        self._step_count += 1
        if self._step_count == 3:
            print(f"{self.name} rests")
            self._step_count = 0
        else:
            if self.battery.use(1):
                self.position += 2
                print(f"{self.name} moves to position {self.position}")
            else:
                print(f"{self.name} is out of charge!")
                
class Racetrack:
    def __init__(self, name, finish_line):
        self.name = name
        self.finish_line = finish_line
        
    def race(self, robots):
        print(f"=== {self.name} (finish: {self.finish_line}) ===")
        round_number = 1
        
        while True:
            print(f"-- Round {round_number} --")
            
            for robot in robots:
                robot.move()
                
                if robot.position >= self.finish_line:
                    print(f"Winner: {robot.name}")
                    return
            if all(robot.battery.is_empty() for robot in robots):
                print("No one finished!")
                return
            
            round_number += 1
blaze = TurboBot("Blaze", Battery(4))
pixel = SteadyBot("Pixel", Battery(6))

track = Racetrack("Robo Rally", 7)
track.race([blaze, pixel])