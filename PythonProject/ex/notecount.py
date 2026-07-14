notes= [500, 200, 100, 50, 20, 10, 5, 2, 1]

amount= 2756

count = 0
for i in notes:
    count = amount // i
    if count > 0:
        print(i, " = ", count)
    amount = amount % i


