class GradeBook:
    def __init__(self, subject):
        self.subject = subject
        self.grades = {}
    
    def add(self, name, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades[name] = grade
        
    def __len__(self):
        return len(self.grades)
    
    def __getitem__(self, name):
        if name not in self.grades:
            raise KeyError("Student not found")
        return self.grades[name]
    
    def __setitem__(self, name, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades[name] = grade
        
    
    def __contains__(self, name):
        return name in self.grades
    
    def __add__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        
        new_book = GradeBook(self.subject)
        
        for name, grade in self.grades.items():
            if name in new_book.grades:
                if grade > new_book.grades[name]:
                    new_book.grades[name] = grade
            else:
                new_book.grades[name] = grade
        return new_book
    
    def __str__(self):
        count = len(self.grades)
        
        if count == 0:
            avg = 0
        else:
            total = sum(self.grades.values())
            avg = total / count
            
        return f"GradeBook '{self.subject}': {count} students, avg {avg:.1f}"
    
    def __eq__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        
        if len(self.grades) == 0:
            avg1 = 0
        else:
            avg1 = round(sum(self.grades.values()) / len(self.grades), 1)
            
        if len(other.grades) == 0:
            avg2 = 0
        else:
            avg2 = round(sum(self.grades.values()) / len(self.grades), 1)
            
        return avg1 == avg2
    
    def __bool__(self):
        return len(self.grades) > 0
    
    def top(self, n):
        sorted_students = sorted(self.grades.items(), key=lambda x: x[1], reverse=True)
        top_students = sorted_students[:n]
        return [name for name, grade in top_students]
    
    def passing(self, min_grade=60):
        return [name for name, grade in self.grades.items() if grade >= min_grade]
    
gb1 = GradeBook("Potions")
gb1.add("Harry", 92)
gb1.add("Ron", 78)
gb1.add("Hermione", 85)

gb2 = GradeBook("Defense Against the Dark Arts")
gb2.add("Ron", 88)
gb2.add("Draco", 95)

print(len(gb1))
print(gb1["Harry"])

gb1["Ron"] = 80
print(gb1["Ron"])

print("Harry" in gb1)
print("Voldemort" in gb1)

gb3 = gb1 + gb2
print(len(gb3))
print(gb3["Ron"])

print(gb1)

print(gb1 == gb2)

empty = GradeBook("Muggle Studies")
if not empty:
    print("No students yet")

print(gb1.top(2))
print(gb1.passing(82))