# Here we write a program to create a class creation of student and also student with filedssuch as enrollment number, USS name, Branch name Student Name, 

class Student:
    def __init__(self, enrollment_number, branch_name, student_name, age, email):
        self.enrollment_number = enrollment_number
        self.branch_name = branch_name
        self.student_name = student_name
        self.age = age
        self.email = email

    def display_details(self):
        print("Student Details")
        print("Enrollment Number:", self.enrollment_number)
        print("Student Name:", self.student_name)
        print("Branch Name:", self.branch_name)
        print("Age:", self.age)
        print("Email:", self.email)



s1 = Student("ENR2025001", "Computer Science", "Chaitanya", 20, "chaitanya@example.com")


s1.display_details()
