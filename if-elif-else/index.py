# Lets learn about if elif else statements in python
# Lets say you want to find out a number is even or odd.



def evenOrOdd(number):
    if(int(number)%2 == 0):
        print("It is even")
    else:
        print("It is odd")

num = input("Enter an integer")
evenOrOdd(num)

# Now lets say , i want to take care of any other incorrect input.

def evenOrOddOrIncorrectInput(number):
    if(number.isdigit() == False):
        print("It is not an integer")
    elif(int(number) % 2 == 1):
        print("It is odd")
    else:
        print("It is even")

num  = input("Enter an integer")
evenOrOddOrIncorrectInput(num)


# We can debug this also using debugger.
# step 1: Enable debug mode from vs code.
# step 2: add breakpoints
# step 3: debug