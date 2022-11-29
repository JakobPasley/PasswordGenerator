import random
import os

os.system("color 0A")
os.system("cls")
print()

PossibleLettersUppercase = "ABCDEFGHIJKLMNOPQRSTUVWXXYZ"
PossibleLettersLowercase = "abcdefghijklmnopqrstuvwxyz"
PossibleNumbers = "0123456789"
PossibleSymbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

Looper = 0

UserLength = int(input("How long do you want your password to be? "))
os.system("cls")
UserUpper = int(input("Do you want your password to contain uppercase letters? 1Y/2N "))
os.system("cls")
UserLower = int(input("Do you want your password to contain lowercase letters? 1Y/2N "))
os.system("cls")
UserNumber = int(input("Do you want your password to contain numbers? 1Y/2N "))
os.system("cls")
UserSymbol = int(input("Do you want your password to contain special characters? 1Y/2N "))
os.system("cls")

print("Your randomly generated password is: ", end = "")

while Looper < UserLength:
    if UserUpper == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleLettersUppercase[random.randint(1,26)], end = "")
            Looper = Looper + 1
    if UserLower == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleLettersLowercase[random.randint(1,26)], end = "")
            Looper = Looper + 1
    if UserNumber == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleNumbers[random.randint(1,10)], end = "")
            Looper = Looper + 1
    if UserSymbol == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleSymbols[random.randint(1,30)], end = "")
            Looper = Looper + 1

print()
print()
input("Press any key to close this window...")