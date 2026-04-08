from dataclasses import dataclass, field

@dataclass
class TrainingSession:
    trainee: str
    discipline: str
    scores: list[int] = field(default_factory=list)
    average: float = field(init=False)
    rank: str = field(init=False)
    
    def __post_init__(self):
        self._update_stats()
        
    def _update_stats(self):
        if not self.scores:
            self.average = 0.0
            self.rank = "Novice"
            return
    
        self.average = sum(self.scores) / len(self.scores)
        if self.average >= 90:
            self.rank = "Elite"
        elif self.average >= 70:
            self.rank = "Skilled"
        else:
            self.rank = "Novice"
    
    def add_score(self, score: int):
        self.scores.append(score)
        self.__post_init__()
        
    def outperforms(self, other: 'TrainingSession') -> bool:
        return self.average > other.average
    
t1 = TrainingSession("Duncan", "Swordsmanship", [85, 92, 78])
print(t1)
t1.add_score(95)
print(t1.average)
print(t1.rank)

t2 = TrainingSession("Feyd", "Swordsmanship", [95, 90, 98])
print(t2.rank)
print(t1.outperforms(t2))

t3 = TrainingSession("Rabban", "Swordsmanship")
print(t3.rank)