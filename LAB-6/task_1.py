class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student1 = Student(name, roll_no, marks)

# Display student details
student1.display_details()

# Calculate and display grade
grade = student1.calculate_grade()
print(f"Grade: {grade}")