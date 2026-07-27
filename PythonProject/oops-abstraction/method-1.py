# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     def execute(self):
#         self.area()
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         rectangle_area = self.length * self.width
#         print("Rectangle  area :", rectangle_area)
#         return rectangle_area
#
#
# r = Rectangle(5, 10)
# r.execute()
#
# shape: Shape = Rectangle(5, 10)
# shape.execute()

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")

u = UPI()
u.pay(500)

c = CreditCard()
c.pay(1800)