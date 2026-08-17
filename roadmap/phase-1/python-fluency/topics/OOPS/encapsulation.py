from dataclasses import dataclass

# Encapsulation

# Encapsulation is about protecting the data

# It means keeping the data and methods together in a class and controlling
# how the data and methods will be accessed

# This prevent accidental changes to the data

# For example:


@dataclass
class Example:
    data: str


e = Example("Data")
print(e)  # Example(data='Data')

# But here , we can direcly modify the member of the class
e.data = "am directly modified by an object"
print(e)  # Example(data='am directly modified by an object')

# To solve this problem, we have two things
# - naming convention - by using _ with data variables, we tell others developers not to modify
# the variable. But it can still be done. Python dont prevent it

# @property - when we use @property for a method, we can access it as a variable of the object

# Example:


@dataclass
class Rectangle:
    h: float
    b: float

    @property
    def _area(self):
        return self.h * self.b


r = Rectangle(100, 100)
print(r._area)  # 10000


# r.area = 10000 # AttributeError: property 'area' of 'Rectangle' object has no setter

# Now, the error says that area  of rectange object has no setter. It means,
# area is just a readonly property.


# Exercises

# Write a Rectangle class: __init__(self, width, height) storing both, and a @property area(self) returning width × height. Access it as rect.area — no parentheses. (A computed value accessed like an attribute.)


class Rectangle:

    def __init__(self, h, w):
        self._h = h
        self._w = w

    @property
    def area(self):
        return self._h * self._w


r = Rectangle(100, 100)
print(r.area)  # 10000

# 2. Write a Circle class storing _radius, with a @property radius getter and no setter. Create one, read radius, then try to set it (circle.radius = 10) and note what happens. (Getter only = read-only.)


@dataclass
class Circle:
    radius_field: float

    @property
    def radius(self):
        return self.radius_field


circle = Circle(10)
print(circle)  # Circle(_radius=10)
# circle.radius = 100 # AttributeError: property 'radius' of 'Circle' object has no setter

# 3. Write a Temperature class storing _celsius. Add a @property getter for celsius, and a @celsius.setter that rejects values below -273.15 (absolute zero) by raising ValueError. Test: set a valid temp, read it, then try an invalid one. (Validation on set — the core encapsulation use.)


@dataclass
class Temperature:
    celsius_field: float

    @property
    def celsius(self):
        return self.celsius_field

    @celsius.setter
    def celsius(self, new_value):
        if new_value < -273.15:
            raise ValueError("Invalid Input: Must be -273.15 or below")
        self.celsius_field = new_value


temp = Temperature(10)
print(temp)
# temp.celsius = -274  # raise ValueError("Invalid Input: Must be -273.15 or below")


# 4. Write a Person class with __init__(self, first_name, last_name). Add a @property full_name returning "{first} {last}". Access person.full_name — no parentheses. (Derived on access, not stored.)


class Person:
    def __init__(self, first_name, last_name):
        self._first = first_name
        self._last = last_name

    @property
    def full_name(self):
        return f"{self._first} {self._last}"


person = Person("Deep", "Singh")
print(person.full_name)  # Deep Singh

# Write a BankAccount storing _balance. Add a balance getter, and a setter that rejects negative values. Then add deposit(self, amount) that uses the setter (self.balance = self.balance + amount) so deposits go through validation. Test a deposit, then try to force a negative balance. (Your BankAccount, now with balance actually protected — validation can't be bypassed.)


@dataclass
class BankAccount:
    balance_field: float

    @property
    def balance(self):
        return self.balance_field

    @balance.setter
    def balance(self, new_value):
        if new_value < 0:
            raise ValueError("Balance cannot be less than 0")
        self.balance_field = new_value

    def deposit(self, amount):
        self.balance = self.balance + amount
        # self.balance gets the updated amount because balance returns self._balance which we update in setter


account = BankAccount(100)
print(account.balance)  # 100
# account.balance = -100 # ValueError: Balance cannot be less than 0
# account.deposit(-101) # ValueError: Balance cannot be less than 0
account.deposit(100)
print(account.balance)  # 200

# my understanding is - when we create an instance or object of a class, _balance gets that value
# Then we create a property balance which returns _balance. It will be from self only so wont write again and again in explanation
# then we create a setter which validates the input.
# Then we have a deposit method.
# When we call deposit and call self.balance it gets the updated value from _balance and amount adds into the updated value.
# So, self.balance on right side calls the setter to update the value
# self.balance in arithmetic expression calls the getter to get the value
