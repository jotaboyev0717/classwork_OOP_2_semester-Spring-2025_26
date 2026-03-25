def validate_score(func):
    def wrapper(*args, **kwargs):
        # if len(args) > 1:
        #     score = args[1]
        # elif "score" in kwargs:
        #     score = kwargs["score"]
        # else:
        #     print("Score not provided")
        #     return
        
        if not (0 <= args[1] <= 100):
            print(f"Invalid score: {args[1]}")
            return
        return func(*args, **kwargs)
    return wrapper


class GradeTracker:
    _all_students = []
    def __init__(self, student_name):
        self.student_name = student_name
        self._scores = []
        GradeTracker._all_students.append(self)
        
    @validate_score
    def add_score(self, score):
        self._scores.append(score)
        
    def average(self):
        if not self._scores:
            return 0.0
        return round(sum(self._scores)/len(self._scores), 1)
    
    def performance_trend(self):
        if len(self._scores) < 2:
            return "Stable"
    
        up = 0
        down = 0
        
        for i in range(len(self._scores)-1):
            if self._scores[i+1] > self._scores[i]:
                up += 1
            elif self._scores[i+1] < self._scores[i]:
                down -= 1
                
        if up > down:
            return "Improving"
        elif down > up:
            return "Declining"
        else:
            return "Stable"
        
    @classmethod
    def from_transcript(cls, transcript):
        name, scores_str = transcript.split(":")
        scores = scores_str.split(",")
        scores = [int(s) for s in scores]
        
        obj = cls(name)
        for s in scores:
            obj.add_score(s)
            
        return obj
    
    @staticmethod
    def is_passing(average):
        return average > 60
    
    @classmethod
    def class_average(cls):
        total = 0
        count = 0
        
        for student in cls._all_students:
            for score in student._scores:
                total += score
                count += 1
                
        if count == 0:
            return 0.0

        return round(total/count, 1)
    
s1 = GradeTracker("Bobur")
s1.add_score(85)
s1.add_score(110)
s1.add_score(72)
s1.add_score(90)

s2 = GradeTracker.from_transcript("Nodira:70,80,92")

print(f"{s1.student_name}: {s1.average()} — {s1.performance_trend()}")
print(f"{s2.student_name}: {s2.average()} — {s2.performance_trend()}")

print(f"Bobur passing: {GradeTracker.is_passing(s1.average())}")
print(f"Nodira passing: {GradeTracker.is_passing(s2.average())}")

print(f"Class average: {GradeTracker.class_average()}")