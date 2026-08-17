# What is an object ?
# An object is a real world entity for example: pen, cup, tea. An object has properties and behavior.

# What is a class ?
# A class is a blueprint of object's properties and behavior.


# Exercises:

# Write a Rectangle class: __init__(self, width, height), and a method area(self) returning width × height. Create Rectangle(4, 5), print its area.


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Now, there are two ways we can create an object and call the class methods

# First

rectangle = Rectangle(2, 3)
print(Rectangle.area(rectangle))  # 6

# Second - we can directly call a method using an object. Python internally does the above

rectangle_two = Rectangle(10, 20)
print(rectangle_two.area())  # 200

# Write a BankAccount class: __init__(self, owner, balance=0), plus deposit(self, amount) and withdraw(self, amount) that modify self.balance.
# Make an account, deposit 100, withdraw 30, print the balance. (Your default-argument knowledge applies — balance=0.)


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"The deposited amount must be greater than 0")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal amount must be greater than 0")
        elif amount > self.balance:
            print(f"Insufficient Balance")
        else:
            self.balance -= amount

    def printBalance(self):
        print(f"{self.owner}'s account balance is {self.balance}")


customer = BankAccount("Xicor")
customer.deposit(100)
customer.withdraw(30)
customer.printBalance()  # Xicor's account balance is 70

# Write a Counter class: __init__(self) sets self.count = 0; increment(self) adds 1; get(self) returns the count.
# Make one, increment three times, print the result.


class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count


count = Counter()
count.increment()
count.increment()
count.increment()
print(count.get())  # 3

# Write a Person class: __init__(self, name, birth_year), and a method age_in(self, current_year) returning current_year - self.birth_year.
# Make a person born in 1990, call age_in(2025).


class Person:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age_in(self, current_year):
        if current_year < self.birth_year:
            return -1
        return current_year - self.birth_year


person = Person("Xicor", 1990)
age = person.age_in(2025)

if age == -1:
    print("Invalid current year")
else:
    print(f"The age of {person.name} is {age}")  # The age of Xicor is 35

# Write Engine with __init__(self, horsepower) and describe(self) returning "{horsepower} HP engine".
# Then Car with __init__(self, make, engine) taking a make string and an Engine object.
# Give Car a describe(self) returning the make plus the engine's description (call self.engine.describe()).
# Create an Engine, pass it into a Car, print the car's description. (A Car HAS an Engine — this is composition, which we'll dig into properly soon.)


class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def describe(self):
        return f"{self.horsepower} HP engine"


class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine

    def describe(self):
        return f"A {self.make} has {self.engine.describe()}"


engine = Engine(2000)
car = Car("Ferari", engine)  # A Ferari has 2000 HP engine

print(car.describe())
