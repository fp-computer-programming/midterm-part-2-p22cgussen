# Author: CCG 12/14/21

import random


def clone_namer(command):
    total = []
    numb = random.randint(0,9999)
    if numb < 10:
        number = "000" + str(numb)
    elif numb < 100:
        number = "00" + str(numb)
    elif numb < 1000:
        number = "0" + str(numb)
    while command == "y":
        total += "CT-" + str(number)
        return(number)


command = input("Name a clone? ")
if command.lower() == "y":
    print("New clone trooper name: CT-{0}".format(clone_namer(command)))
elif command.lower() == "n":
    print()

