# class Student:
#     def __init__(self, name, student_id):
#         Student.name = name
#         Student.student_id = student_id
#         return name, student_id
# eshmat = Student('eshmat', '561852')
# print(eshmat)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def say_hello(self):
        print(f"Hello! My name is {self.name}.")
    
    def has_grades(self):
        return len(self.grades) > 0
eshmat = Student("Eshmat", "2024001")
eshmat.say_hello()