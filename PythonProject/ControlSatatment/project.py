#program to find maximum of two numbers
num1 =int("56")
num2 =int("500")

if num1>num2 :
    print("greater is", num1)

else:
    print("greater is", num2)


#program to find smallest of two numbers
num3 =int("548")
num4 =int("89")

if num3<num4 :
    print("smaller integer is", num3)

else:
    print("smaller integer is", num4)

#program to reverse the number
number = 154
n = number
r = 0
sum = 0

while n > 0:
    r = n % 10
    sum = (sum*10)+r
    n = n//10

print(sum)

#program to make a Amstrong number
number = 153
n = number
r = 0
sum = 0
while n > 0:
    r= n % 10
    sum = sum+r*r*r
    n= n//10

if sum == number:
    print("This is amstrong No....",sum)
else:
    print("This is not amstrong...??",sum)
