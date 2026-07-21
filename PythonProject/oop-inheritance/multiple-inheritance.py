class Addition:
    def sum(self, a, b):
        return a + b;

class Multiplication:
    def multiply(self, a, b):
        return a * b;


class Derived(Addition, Multiplication):
    def Divide(self, a, b):
        return a / b;


derived_obj = Derived()
print(derived_obj.sum(10, 20))
print(derived_obj.multiply(10, 20))
print(derived_obj.Divide(10, 20))