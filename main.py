import time
import os

def macintosh(first_line, second_line):
    print(" _______________________ ")
    print("|  ___________________  |")
    print("| |$ " + first_line, end="")
    for _ in range(17-len(first_line)):
        print(" ", end="")
    print("| |")
    print("| |" + second_line, end="")
    for _ in range(19-len(second_line)):
        print("", end=" ")
    print("| |")
    print("| |                   | |")
    print("| |___________________| |")
    print("|                       |")
    print("|                       |")
    print("|            ________   |")
    print("|                       |")
    print("| apple                 |")
    print("|_______________________|")
    print(" |                     | ")
    print(" |_____________________| ")

command = "echo helloworld"
output = "helloworld"

for i in range(len(command)):
    macintosh(command[:i], "")
    time.sleep(0.25)
    os.system("clear")

macintosh(command, output)
time.sleep(0.5)