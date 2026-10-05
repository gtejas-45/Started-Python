class Student:
    institute_name = "CodeSpyder Technologies"
    total_students = 220
    
    def __init__(self,student_id,name,course,marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks
        Student.total_students += 1
        
    
    def stud_info(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        
    def update_marks(self):
        if(self.marks > 80):
            self.marks += 5
        elif(self.marks > 60):
            self.marks += 8
        else:
            self.marks += 10
            
    def institute_info(self):
        print("Institute :", Student.institute_name)
            
    def __str__(self):
        return f"Student ID : {self.student_id}\nName       : {self.name}\nCourse     : {self.course}\nMarks      : {self.marks}"
    
    
student1 = Student(101,"Rahul","Python",88)
print("Institute :", Student.institute_name)
print(student1)
print("Total Students : " ,Student.total_students)

# OUTPUT-------------------------------

# Institute : CodeSpyder Technologies
# Student ID : 101
# Name       : Rahul
# Course     : Python
# Marks      : 88
# Total Students :  221

# --------------------------------------
    
            
            
        
    