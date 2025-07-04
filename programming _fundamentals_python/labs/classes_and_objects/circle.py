class Circle:
    __pi = 3.14
    def __init__(self , _diameter):
        self.diameter = _diameter
        self.radius = self.diameter / 2


    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return circumference
    def calculate_area(self):
        area = Circle.__pi * self.radius ** 2
        return area
    def calculate_area_of_sector(self, _angle):
        area = (_angle / 360) * Circle.__pi * self.radius ** 2
        return area

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
