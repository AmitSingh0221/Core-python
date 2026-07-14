number = 153
n = number
r = 0
sum = 0

while n > 0:
    r = n % 10
    sum = sum+r*r*r
    n = n// 10


if sum == number:
    print("This is amstrong No....",sum)
else:
    print("This is not amstrong...??",sum)