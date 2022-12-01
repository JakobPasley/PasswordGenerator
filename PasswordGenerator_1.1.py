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

def Password_Length():
    if UserLength == 1:
        print(f"Your password will be {UserLength} character long.")
    elif UserLength > 1:
        print(f"Your password will be {UserLength} characters long.")
def Uppercase_Letters():
    if UserUpper == 1:
        print("Your password will contain uppercase letters.")
    elif UserUpper == 2:
        print("Your password will not contain uppercase leters.")
def Lowercase_Letters():
    if UserLower == 1:
        print("Your password will contain lowercase letters.")
    elif UserLower == 2:
        print("Your password will not cotain lowercase letters.")
def Numbers():
    if UserNumber == 1:
        print("Your password will contain numbers.")
    elif UserNumber == 2:
        print("Your password will not contain numbers.")
def Specials():
    if UserSymbol == 1:
        print("Your password will contain special characters.")
    elif UserSymbol == 2:
        print("Your password will not contain special characters.")

UserLength = int(input("How long do you want your password to be? "))
os.system("cls")
print()
Password_Length()
print()
UserUpper = int(input("Do you want your password to contain uppercase letters? 1Y/2N "))
os.system("cls")
print()
Password_Length()
Uppercase_Letters()
print()
UserLower = int(input("Do you want your password to contain lowercase letters? 1Y/2N "))
os.system("cls")
print()
Password_Length()
Uppercase_Letters()
Lowercase_Letters()
print()
UserNumber = int(input("Do you want your password to contain numbers? 1Y/2N "))
os.system("cls")
print()
Password_Length()
Uppercase_Letters()
Lowercase_Letters()
Numbers()
print()
UserSymbol = int(input("Do you want your password to contain special characters? 1Y/2N "))
os.system("cls")
print()
Password_Length()
Uppercase_Letters()
Lowercase_Letters()
Numbers()
Specials()
print()

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