import random
import os

os.system("color 0A")
os.system("cls")
print()

PossibleLettersUppercase = "ABCDEFGHIJKLMNOPQRSTUVWXXYZ"
PossibleLettersLowercase = "abcdefghijklmnopqrstuvwxyz"
PossibleNumbers = "0123456789"
PossibleSymbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

def Password_Length():
    global UserLength
    while True:
        try:
            os.system("cls")
            print()
            UserLength = int(input("How long do you want your password to be? "))
            break
        except ValueError:
            input("Please enter a positive integer value...")
            continue
    if UserLength < 1:
        input("Please enter a positive integer value...")
        Password_Length()
def Password_Length_Statement():
    if UserLength == 1:
        print(f"Your password will be {UserLength} character long.")
    elif UserLength > 1:
        print(f"Your password will be {UserLength} characters long.")

def Uppercase_Letters():
    global UserUpper
    while True:
        try:
            UserUpper = int(input("Do you want your password to contain uppercase letters? 1Y/2N "))
            break
        except ValueError:
            input("Please enter either a 1 (Yes) or 2 (No)...")
            os.system("cls")
            print()
            continue
    if UserUpper < 1:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Uppercase_Letters()
    elif UserUpper > 2:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Uppercase_Letters()
def Uppercase_Letters_Statement():
    if UserUpper == 1:
        print("Your password will contain uppercase letters.")
    elif UserUpper == 2:
        print("Your password will not contain uppercase leters.")

def Lowercase_Letters():
    global UserLower
    while True:
        try:
            UserLower = int(input("Do you want your password to contain lowercase letters? 1Y/2N "))
            break
        except ValueError:
            input("Please enter either a 1 (Yes) or 2 (No)...")
            os.system("cls")
            print()
            continue
    if UserLower < 1:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Lowercase_Letters()
    elif UserLower > 2:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Lowercase_Letters()
def Lowercase_Letters_Statement():
    if UserLower == 1:
        print("Your password will contain lowercase letters.")
    elif UserLower == 2:
        print("Your password will not cotain lowercase letters.")

def Numbers():
    global UserNumber
    while True:
        try:
            UserNumber = int(input("Do you want your password to contain numbers? 1Y/2N "))
            break
        except ValueError:
            input("Please enter either a 1 (Yes) or 2 (No)...")
            os.system("cls")
            print()
            continue
    if UserNumber < 1:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Numbers()
    elif UserNumber > 2:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Numbers()
def Numbers_Statement():
    if UserNumber == 1:
        print("Your password will contain numbers.")
    elif UserNumber == 2:
        print("Your password will not contain numbers.")

def Specials():
    global UserSymbol
    while True:
        try:
            UserSymbol = int(input("Do you want your password to contain special characters? 1Y/2N "))
            break
        except ValueError:
            input("Please enter either a 1 (Yes) or 2 (No)...")
            os.system("cls")
            print()
            continue
    if UserSymbol < 1:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Specials()
    elif UserSymbol > 2:
        input("Please enter either a 1 (Yes) or 2 (No)...")
        os.system("cls")
        print()
        Specials()
def Specials_Statement():
    if UserSymbol == 1:
        print("Your password will contain special characters.")
    elif UserSymbol == 2:
        print("Your password will not contain special characters.")

os.system("cls")
print()
Password_Length()
os.system("cls")
print()
Password_Length_Statement()
print()
Uppercase_Letters()
os.system("cls")
print()
Password_Length_Statement()
Uppercase_Letters_Statement()
print()
Lowercase_Letters()
os.system("cls")
print()
Password_Length_Statement()
Uppercase_Letters_Statement()
Lowercase_Letters_Statement()
print()
Numbers()
os.system("cls")
print()
Password_Length_Statement()
Uppercase_Letters_Statement()
Lowercase_Letters_Statement()
Numbers_Statement()
print()
Specials()
os.system("cls")
print()
Password_Length_Statement()
Uppercase_Letters_Statement()
Lowercase_Letters_Statement()
Numbers_Statement()
Specials_Statement()
print()

print("Your randomly generated password is: ", end = "")

Looper = 0

while Looper < UserLength:
    if UserUpper == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleLettersUppercase[random.randint(0,25)], end = "")
            Looper = Looper + 1
        elif Picker == 2:
            pass
    elif UserUpper == 2:
        pass

    if Looper >= UserLength:
        break

    if UserLower == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleLettersLowercase[random.randint(0,25)], end = "")
            Looper = Looper + 1
        elif Picker == 2:
            pass
    elif UserLower == 2:
        pass

    if Looper >= UserLength:
        break

    if UserNumber == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleNumbers[random.randint(0,9)], end = "")
            Looper = Looper + 1
        elif Picker == 2:
            pass
    elif UserNumber == 2:
        pass

    if Looper >= UserLength:
        break

    if UserSymbol == 1:
        Picker = random.randint(1,2)
        if Picker == 1:
            print(PossibleSymbols[random.randint(0,29)], end = "")
            Looper = Looper + 1
        elif Picker == 2:
            pass
    elif UserSymbol == 2:
        pass

    if Looper >= UserLength:
        break

print()
print()
input("Press any key to close this window...")