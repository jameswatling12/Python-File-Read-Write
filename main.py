import random
import time
import os
import sys
print("File Helper")
login = input("USERNAME: ")
if login == "james":
    password = input("PASSWORD: ")
    if password == "python":
        print("ACCESS CONFIRMED")
        while True:
            time.sleep(1)
            command = input("COMMAND: ")
            if command == "new file":
                name = input("FILE NAME: ")
                print(str(name))
                info1 = input("DETAILS: ")
                print(str(info1))
                file = open(name + ".txt", "w")
                file.write(info1)
            elif command == "access file":
                openname = input("FIlE NAME: ")
                file = open(str(openname) + ".txt", "r")
                print (file.read())
            elif command == "edit file":
                editname = input("FILE NAME: ")
                file = open(str(editname) + ".txt", "a")
                addition = input("NEW INPUT: ")
                file.write(str(addition))
            elif command == "delete file":
                remfile = input("FILE NAME: ")
                os.remove(str(remfile) + ".txt")
            elif command == "create folder":
                directory = input("FOLDER NAME: ")
                os.mkdir(str(directory))
            elif command == "close":
                exit()
            elif command == "access folder":
                dirName = input("FOLDER NAME: ")
                command2 = input("FOLDER COMMAND: ")
                if command2 == "new file":
                    name = input("FILE NAME: ")
                    print(str(name))
                    info1 = input("DETAILS: ")
                    print(str(info1))
                    with open(str(dirName) + "/" + str(name) + ".txt", "w") as file:
                        file.write(str(info1))
                elif command2 == "access file":
                    openname = input("FIlE NAME: ")
                    with open(str(dirName) + "/" + str(openname) + ".txt", "r") as file:
                        print (file.read())
                elif command2 == "edit file":
                    editname = input("FILE NAME: ")
                    with open(str(dirName) + "/" + str(editname) + ".txt", "a") as file:
                        addition = input("NEW INPUT: ")
                        file.write(str(addition))
                elif command2 == "delete file":
                    remfile = input("FILE NAME: ")
                    print(str(remfile))
                    os.remove(str(dirName) + "/" + str(remfile) + ".txt")
                else:
                    print("COMMAND NOT RECOGNISED")
            else:
               print("COMMAND NOT RECOGNISED") 
    else:
        print("ACCESS DENIED")
else:
    print("ACCESS DENIED")
