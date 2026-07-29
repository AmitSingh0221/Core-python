import re                            #Regular Expression
# import os                          #Operating System


def readLine():

    input_file = open("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/gmail.py", 'r')
    output_file = open("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/onlygmail.py", "w")
    output_files = open ("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/hotmail.py", "w")
    Output_Files = open("C:/Users/aarti singh/PycharmProjects/PythonProject/raw file/outlook.py", "w")

    for line in input_file:
        if (re.search("@gmail.com", line)):
            output_file.write(line)
            print(line)

        if (re.search("@hotmail.com", line)):
            output_files.write(line)
            print(line)
        if (re.search("@outlook.com", line)):
            Output_Files.write(line)
            print(line)
    input_file.close()
    output_file.close()
    output_files.close()
    Output_Files.close()


readLine()
