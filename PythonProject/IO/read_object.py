import pickle
from write_object import Employee    #if any method is not called then use this

with open("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/bianryfile.py", 'rb') as file:
    obj = pickle.load(file)
    print("Printing Employee information after unpickling")

obj.display()