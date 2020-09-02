class Shape:
    """A class defining Shapes"""
    def __str__(self):
        return f"I am a {self.__class__.__name__}"

    def area(self):
        raise NotImplementedError()

    def perimiter(self):
        raise NotImplementedError()


class Rectangle(Shape):
    """A rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimiter(self):
        return 2 * (self.width + self.height)

s = Shape()
print(s)

r = Rectangle(3, 4)
print(r)
print(f"area = {r.area()}")
print(f"perimiter = {r.perimiter()}")
