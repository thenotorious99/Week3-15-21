
class Student:
    def __init__(self, student, assessment):
        self.student = student
        self.assessment = assessment

    def checking_assessment(self):
        if self.assessment >= 5.50:
            return f"{self.student} is excellent student!"
        else:
            return f"{self.student} isn't has big score this year."

student = Student("Andrey", 5.50)
student2 = Student("Ivaylo", 5.00)

print(student.checking_assessment())
print(student2.checking_assessment())


