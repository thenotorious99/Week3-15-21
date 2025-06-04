import math

class Radius:
    def __init__(self, area):
        self.area = area

    def circle_radius(self):
        return 2 * math.pi * self.area

# Object on circle
radius = Radius(5)

print("The radius of the circle is:", round(radius.circle_radius(), 2))
