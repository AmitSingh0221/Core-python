import pickle



class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, "\t", self.name, "\t", self.salary)


with open("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/bianryfile.py", 'wb') as file:
    emp = Employee(101, 'Amit', 50058)
    pickle.dump(emp, file)

