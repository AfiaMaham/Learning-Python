# Create a class called Student with the following instance variables:
# name (string)
# age (integer)
# grade (string)
# Define a method student_info() that prints the student's name, age, and grade.
# Add a method update_grade() that updates the student's grade.
# Create an object of the Student class, print the student info, update the grade, and print the updated info.

class Student:
    name = "Afia"
    age = 19
    grade = "A"

    def student_info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Grade: ",self.grade)

    def update_grade(self):
        update = input("Update the grade: ")
        self.grade = update

obj = Student()
obj.student_info()
obj.update_grade()
obj.student_info()