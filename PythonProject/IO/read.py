def readfile():
    file = open("C:/Users/aarti singh/Desktop/IO - file/xyz.tx",'r')

    text = file.read()
    print(text)
    file.close()


readfile()
