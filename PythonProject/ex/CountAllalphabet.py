name = "abrahim benjamin de villiers"
for ch in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for letter in name :
        if ch == letter:
            count +=1
    if count > 0:
            print(ch, "count =", count)


