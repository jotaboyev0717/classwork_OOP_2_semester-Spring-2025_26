class Student:
    def __init__(self, name, scores):
        self.name = name
        self.average = sum(scores) / len(scores) if scores else 0

    def report(self):
        return f"{self.name}: average = {self.average}"

class HonoursStudent(Student):
    def __init__(self, name, scores, bonus):
        super().__init__(name, scores)
        self.average += bonus

    def report(self):
        return f"{self.name}: average = {self.average} (honours)"


a = Student("Ali", [70, 80, 90])
print(a.report())

b = HonoursStudent("Bob", [60, 70], 10)
print(b.report())