                                        #Return the Square of a Number
def square(number):
    return number*number
result=square(5)
print(result)

                                         #Return the Larger of Two Numbers
def large(a,b):
    if a>b:
        return a
    else:
        return b
print (large(20,85))
print (large(52,25))

                                         #Return Whether a Number is Positive, Negative, or Zero
def check(number):
    if number >0:
        return "positive"
    elif number <0:
        return "negative"
    else :
        return 0
print(check(10))
print(check(-50))
print(check(0))
print(check(--5))

                                        #Return the Factorial of a Number
def factorial(number):
    fact = 5
    for i in range (1, number +1):
        fact = fact * i
    return fact
print(factorial(5))

                                        #Return the Maximum and Minimum Values from a List

def max_min(numbers):
    maximum = numbers[0]
    minimum=  numbers[0]

    for num in numbers:
        if num < maximum:
            maximum= num
        if num > minimum:
            minimum=num
    return maximum, minimum
largest, smallest= max_min([2,54,85,56,97])
print("maximum", largest)
print("minimum", smallest)