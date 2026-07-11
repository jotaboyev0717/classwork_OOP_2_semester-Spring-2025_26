# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
    
#     def report(self):
#         average = sum(self.scores) / len(self.scores) if self.scores else 0
#         return f"{self.name}: average={average:.2f}"
    
# class HonoursStudent(Student):
#     def __init__(self, name, scores, bonus_score):
#         super().__init__(name, scores)
#         self.bonus_score = bonus_score

#     def bonus(self):
#         self.scores.append(self.bonus_score)
#         return f"{self.name} receives a bonus for outstanding performance!"
    
#     def report(self):
#         base_report = super().report()
#         return f"{base_report} (honours)"
    
# a = Student("Ali", [70, 80, 90])
# print(a.report())
# b = HonoursStudent("Bob", [60,70], 10)
# b.bonus()
# print(b.report())

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.average = sum(scores) / len(scores) if scores else 0

    def report(self):
        return f"{self.name}: average={self.average}"


class HonoursStudent(Student):
    def __init__(self, name, scores, bonus):
        super().__init__(name, scores)
        self.average += bonus

    def report(self):
        return f"{super().report()} (honours)"


a = Student("Ali", [70, 80, 90])
print(a.report())

b = HonoursStudent("Bob", [60, 70], 10)
print(b.report())