class StudentTranscript:
    university_name = "Al-Khwarizmi University"
    max_courses = 6
    grade_map = {"A": 4.0, 
                 "B": 3.0, 
                 "C": 2.0, 
                 "D": 1.0, 
                 "F": 0.0
                 }
    
    def __init__(self, name, student_id, major, completed_courses=None):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.completed_courses = []
        
        if completed_courses is not None:
            for course in completed_courses:
                if 1 <= course["credits"] <= 4 and course["grade"] in StudentTranscript.grade_map:
                    self.completed_courses.append(course)
                else:
                    print(f"Invalid course skipped: {course}")
    
    def add_course(self, course_name, credits, grade):
        if len(self.completed_courses) >= StudentTranscript.max_courses:
            print("Maximum number of courses reached")
            return
        
        if credits < 1 or credits > 4:
            print(f"Invalid credits {credits}. Must be between 1 and 4")
            return
        
        if grade not in StudentTranscript.grade_map:
            print(f"Invalid grade {grade}. Must be A, B, C, D, or F")
            return
        
        course = {
            "name": course_name,
            "credits":credits,
            "grade": grade
        }
        
        self.completed_courses.append(course)
        print(f"Added {course_name} ({credits} credits): {grade}")

    def calculate_gpa(self):
        if len(self.completed_courses) == 0:
            return 0.0
        
        total_points = 0
        total_credits = 0
        
        for course in self.completed_courses:
            grade = course["grade"]
            credits = course["credits"]
            
            points = StudentTranscript.grade_map[grade]
            
            total_points += points * credits
            total_credits += credits
            
        gpa = total_points / total_credits
        return round(gpa, 2)

    def get_standing(self, gpa = None):
        if gpa is None:
            gpa = self.calculate_gpa()
            
        if gpa >= 3.5:
            return "Excellent"
        elif gpa >= 3.0:
            return "Good"
        elif gpa >= 2.0:
            return "Satisfactory"
        elif gpa >= 1.0:
            return "Poor"
        else:
            return "Failing"
    
    def get_honors_status(self):
        if len(self.completed_courses) < 4:
            return "No Honors"
        
        gpa = self.calculate_gpa()
        
        if gpa >= 3.8:
            return "Highest Honors"
        elif gpa >= 3.5:
            return "High Honors"
        elif gpa >= 3.0:
            return "Honors"
        else:
            return "No Honors"
        
    def generate_transcript(self):
        print("\nOFFICIAL TRANSCRIPT - ", StudentTranscript.university_name)
        print(f"Name: {self.name} | ID: {self.student_id} | Major: {self.major}")
        print("-" * 50)
        
        for course in self.completed_courses:
            print(f"{course['name']:<20} | Credits: {course['credits']} | Grade: {course['grade']}")
        
        print("-" * 50)
        
        total_credits = 0
        for course in self.completed_courses:
            total_credits += course['credits']
            
        gpa = self.calculate_gpa()
        standing = self.get_standing(gpa)
        
        print(f"Total Credits: {total_credits}")
        print(f"GPA: {gpa:.2f}/4.00\n")
        print(f"Standing: {standing}")
        
courses = [
    {"name": "Programming I", "credits": 3, "grade": "A"},
    {"name": "Math", "credits": 4, "grade": "B"},
    {"name": "Invalid", "credits": 5, "grade": "A"}
]       
student = StudentTranscript("Dilshod Rahimov", "2024001", "Computer Science", courses)
student.add_course("Database Systems", 3, 'A')
student.add_course("Algorithms ", 3, 'B')
student.add_course("Invalid Grade", 3, 'E')
student.add_course("Networks", 3, 'A')

student.generate_transcript()
print(f"\nHonors: {student.get_honors_status()}")