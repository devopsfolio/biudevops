
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_area(self):
        print(self.width * self.height)

    def count_perimeter(self):
        print(self.width * 2 + self.height * 2)

rec1 = Rectangle(27, 60)
rec1.count_area()
rec1.count_perimeter()



