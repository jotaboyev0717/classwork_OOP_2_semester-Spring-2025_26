from abc import ABC, abstractmethod

def track_attempt(func):
    def wrapper(*args, **kwargs):
        print("[ATTEMPT] Answering question...")
        result = func(*args, **kwargs)
        if result == True:
            print("[ATTEMPT] Correct!")
        else:
            print("[ATTEMPT] Wrong!")
        return result
    return wrapper

class Question(ABC):
    def __init__(self, text, points):
        self.text = text
        self.points = points
        
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        if value <= 0:
            raise ValueError("Points must be positive")
        self._points = value
        
    @abstractmethod
    def check_answer(self, answer):
        pass
    
    def __str__(self):
        return f"[{self.points}pts] {self.text}"
    
class MultipleChoice(Question):
    def __init__(self, text, points, options, correct_index):
        super().__init__(text, points)
        self.options = options
        self.correct_index = correct_index
        
    @track_attempt
    def check_answer(self, answer):
        return answer == self.correct_index
    
class FillInTheBlank(Question):
    def __init__(self, text, points, correct_answer):
        super().__init__(text, points)
        self.correct_answer = correct_answer
    
    @track_attempt
    def check_answer(self, answer):
        return self.correct_answer.strip().lower() == str(answer).strip().lower()
    
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)
        
    def __len__(self):
        return len(self.questions)
    
    def __add__(self, other):
        if isinstance(other, Exam):
            new_title = f"{self.title} + {other.title}"
            
            new_exam = Exam(new_title)
            new_exam.questions = self.questions + other.questions
            return new_exam
        return NotImplemented
    
    def total_points(self):
        return sum(q.points for q in self.questions)
        
    def grade(self, answers):
        if len(self.questions) != len(answers):
            raise ValueError("need ths same length")
            
        earned_points = 0
        
        # 2. Savollar va javoblar ro'yxatini parallel ravishda aylanamiz
        for i in range(len(self.questions)):
            question = self.questions[i]
            user_answer = answers[i]
            
            # Polimorfizm: qaysi savol turi bo'lishidan qat'i nazar check_answer ishlaydi
            # va @track_attempt dekoratori natijani ekranga chiqaradi
            if question.check_answer(user_answer):
                earned_points += question.points
                
        return earned_points
        
class Student:
    # Klass o'zgaruvchisi (hamma talabalar uchun umumiy)
    passing_percentage = 60

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # self.scores lug'ati: {"Imtihon nomi": (olingan_ball, jami_ball)}
        self.scores = {}

    def take_exam(self, exam, answers):
        # 1. Imtihonni baholaymiz
        earned = exam.grade(answers)
        # 2. Jami mumkin bo'lgan ballni olamiz
        total = exam.total_points()
        
        # 3. Natijani lug'atga saqlaymiz
        self.scores[exam.title] = (earned, total)
        return earned

    def passed(self, exam_title):
        if exam_title not in self.scores:
            print(f"Error: {exam_title} bo'yicha natija topilmadi.")
            return False
        
        earned, total = self.scores[exam_title]
        # Foizni hisoblaymiz
        percentage = (earned / total) * 100
        
        # Klass o'zgaruvchisi bilan solishtiramiz
        return percentage >= Student.passing_percentage

    @classmethod
    def from_string(cls, data):
        # Format: "Name:ID"
        name, student_id = data.split(":")
        return cls(name, student_id)

    @staticmethod
    def is_valid_id(student_id):
        # Shart: "S-" bilan boshlanishi va jami 5 ta belgi bo'lishi kerak
        return student_id.startswith("S-") and len(student_id) == 5
    
print(f"Valid ID 'S-001': {Student.is_valid_id('S-001')}")
print(f"Valid ID '12345': {Student.is_valid_id('12345')}")

try:
    bad_q = MultipleChoice("Bad?", -2, ["A", "B"], 0)
except ValueError as e:
    print(f"Error: {e}")

q1 = MultipleChoice("What is the capital of France?", 10,
                     ["London", "Paris", "Berlin", "Madrid"], 1)
q2 = FillInTheBlank("The keyword to define a function in Python is ___", 10,
                    "def")
q3 = MultipleChoice("Which data structure uses FIFO?", 5,
                     ["Stack", "Queue", "Tree", "Graph"], 1)
q4 = FillInTheBlank("Python lists are ___ (mutable/immutable)", 5,
                    "mutable")

print(q1)
print(q2)

midterm = Exam("Midterm")
midterm.add_question(q1)
midterm.add_question(q2)

quiz = Exam("Pop Quiz")
quiz.add_question(q3)
quiz.add_question(q4)

final = midterm + quiz
print(f"Final exam: '{final.title}' with {len(final)} questions worth {final.total_points()} points")

student = Student.from_string("Alisher:S-042")

earned = student.take_exam(final, [1, "  Def  ", 0, "mutable"])
print(f"Alisher earned {earned}/{final.total_points()} points")
print(f"Passed? {student.passed(final.title)}")

try:
    q_abstract = Question("Abstract?", 5)
except TypeError:
    print("Cannot instantiate abstract class")