class Teacher:
    def __init__(self, name, predmet, experience):
        self.name = name
        self.predmet = predmet
        self.experience = experience

    def experience_teacher(self):
        if self.experience >= 10:
            return f"{self.name} has {self.experience} years experience like {self.predmet} teacher."
        else:
            return f"{self.name} doesn't have enough experience"

teacher1 = Teacher("Jony", "Math", 11)
teacher2 = Teacher("George", "Paint", 9)

print(teacher1.experience_teacher())
print(teacher2.experience_teacher())