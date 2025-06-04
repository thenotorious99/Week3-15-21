
class Student:
    def __init__(self, student, assessment):
        self.student = student
        self.assessment = assessment

        # Create object
student1 = Student("Alex", 5.75)

print("Name:", student1.student)
print("Assessment:", student1.assessment)