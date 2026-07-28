def KeyboardToFileCopy():
    file = open("C:/Users/aarti singh/Desktop/IO - file/abc.txt", "w")
    text = input('Enter your message = ')

    while (text != "quit"):
        file.write(text)
        file.write("\n")
        text = input('')
    file.close()


KeyboardToFileCopy()