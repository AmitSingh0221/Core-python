class Shape:
    def __init__(self, Color= " ", BorderWidth=" "):
        self.Color= Color
        self.BorderWidth= BorderWidth

    def getColor(self):
            return self.Color

    def getBorderWidth(self):
            return self.BorderWidth

class Rectangle(Shape):
    def __init__(self, Color=" ", BorderWidth="0", length="0", breadth="0"):
            self.length= length
            self.breadth= breadth
            super().__init__(Color, BorderWidth)

    def getlength(self):
                return self.length
    def getbreadth(self):
                return self.breadth
r = Rectangle("red", 100, 30,10)
print("Rectangle:")
print("length:", r.getlength())
print("width:", r.getbreadth())
print("Color:", r.getColor())
print("BorderWidth:", r.getBorderWidth())



