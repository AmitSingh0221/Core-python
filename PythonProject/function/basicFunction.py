                                      # call function with multiple times
def greet() :
    print("Hello, Amit ")
greet()
greet()

                                      #function with parameters
def greet (name):                                  #(name) is a parameter.
    print("Hello", name)
greet("lamine")
greet("zalatan")

                                      #positional arguments
def student(name, city):
    print (name, "lives in", city)
student("Steve Smith", "Melbourne")
student("Joe Root", "Edgebaston")
student("Sydney", "Aeron Finch")                   #No error occurs because Python matches values by position, not by their meaning.

                                      #keyword arguments
def team(name, tournament, ranking):
    print(name, tournament, "ranks in", ranking)
team(name= "India", tournament="ODI", ranking=1)
team(name="Austrailia", tournament= "Test", ranking= 1)
team(tournament= "T20i", ranking= 1, name= "England")       #we used parameter names directly, so order does not matter

                                          #default Arguments
def student(name, city="Sydney"):                          #default value given
    print (name, "lives in", city)
student("Steve Smith", "Melbourne")
student("Joe Root")                                        # if user does not give the value use defalut value

                                         # *args-(unlimited inputs)
def total_marks(*marks):
    print(marks)
total_marks(1,48, 25,45,)

                                        # **kwargs- (named ulimited inputs)
def student_info(**data):
    print(data)
student_info(name="Amit", city="Indore", state="Madhya Pradesh")


                                        #return Statement
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

                                         #multiple return values
def student():
    return "Amit", 21, "Python"

name, age, course = student()

print(name)
print(age)
print(course)
                                                            #multiple return values in Arithmetic operations
def add(a, b):
    return a + b, a - b

result = add(200, 120)
print(result)

                                                           #multiple return values in different data types
def student():
    return "Amit", 21, 78.5, "CBSE"
name, age, marks, board =student()

print(name)
print(age)
print(marks)
print(board)


                                      #local variable
def demo():
    x=10, "amit", 54.5
    print(x)
demo()
                                     #global variable
college="sage university"                                  #created outside function
def show():
    print(college)                                         #can be used multiple times
def display():
    print(college)                                         #can be used multiple times
show()
display()
