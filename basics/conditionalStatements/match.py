#we can use match case also instead of if elif else statements in python 3.10 and above.

# lets say we want to create a basic arithmatic operators on two numbers based on user input

def add(a,b):
    return a+b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a/b

def userInterface():
    a =  input("Enter first integer ");
    b = input("Enter second integer ");
    a = int(a)
    b = int(b)
    print("1. Add 2. Subtract 3. Multiplication 4. Division")
    choice = input("Enter your choice -- ")
    match choice:
        case '1': print(add(a,b))
        case '2': print(sub(a,b))
        case '3': print(multiply(a,b))
        case '4': print(division(a,b))
        case _: print("Incorrect inputs")

userInterface()
