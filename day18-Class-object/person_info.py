class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return (f"Hello, my name is {self.name}, and I'm {self.age} years old.")

name_age = Person("Ivo", 25)

print("Person info:", name_age.person_info())