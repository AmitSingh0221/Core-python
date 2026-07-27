class Shape:
    def execute(self):
        if self.validate():
            self.area()
        else:
            print('Validation Failed')

    def validate(self):
        return False

    def area(self):#
        print('Shape Area Method')


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate(self):
        if self.length > 0 and self.width > 0:
            return True
        else:
            return False

    def area(self):
        rectangle_area = self.length * self.width
        print('Rectangle Area:', rectangle_area)
        return rectangle_area


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        if self.radius > 0:
            return True
        else:
            return False

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print('Circle Area:', circle_area)
        return circle_area


class Test(Shape):
    pass


print("\n--- Rectangle ---")
r = Rectangle(10, 20)
r.execute()

print("\n--- Circle ---")
c = Circle(10)
c.execute()

print("\n--- Invalid Rectangle ---")
r_invalid = Rectangle(-5, 10)
r_invalid.execute()
#
# print("\n--- Invalid Circle ---")
# c_invalid = Circle(0)
# c_invalid.execute()
#
print("\n--- Test ---")
t = Test()
t.execute()