class Dog:
    def __init__(self, name, dog_breed):
        self.name = name
        self.breed = dog_breed

    def bark(self):
        print("Woof!")

kind_of_dog = Dog("Archie", "Pitbull")

kind_of_dog.bark()