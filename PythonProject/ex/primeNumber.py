number = 571
count = 0

for i in range (2 , number):
    if number % i == 0:
        count += 1
        print (i)

if count ==0 :
    print("Prime number:", number)
else :
    print("Not Prime number:", number)
