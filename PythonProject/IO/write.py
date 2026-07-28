def writeFile():
    file = open("C:/Users/aarti singh/Desktop/IO - file/xyz.tx", "w")
    file.write("Hi\n")
    file.write("Hello amit singh\n")
    file.write("This is Python file")
    print("File Write Succssfully")
    file.close()



writeFile()