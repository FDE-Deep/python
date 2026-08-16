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

# What is a dunder method

# Dunder means double underscore. Method naming convention is __method-name__.
# We can override the functionality of a built-in function using dunder methods.

# For example - print(10) internally calls __rer__ method.

#  lets do some coding exercises

# Take your Rectangle class and add __repr__ returning "Rectangle(4, 5)" style output. Create one, print it.

# Add __eq__ to Rectangle so two rectangles with the same width and height are equal.
# Test: create two identical rectangles and two different ones, print both == results


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width},{self.height})"

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


rec = Rectangle(4, 5)
rec1 = Rectangle(4, 5)
rec2 = Rectangle(2, 3)
rec3 = Rectangle(1, 3)
print(rec)
print(rec1 == rec)  # True
print(rec2 == rec3)  # False


# Write a Money class: __init__(self, amount), a __repr__ showing "$50", and __add__(self, other) that returns a new Money whose amount is the sum.
# Test Money(50) + Money(30) and print it → should show $80. (Hint: __add__ should return a new Money(...) object, not just a number.)


class Money:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"${self.amount}"

    def __add__(self, other):
        amount = self.amount + other.amount
        return Money(amount)


print(Money(50) + Money(30))  # $80

# lets create objects and see

money = Money(20)
money1 = Money(40)
print(money + money1)  # $60

# My understanding is:
# When we call add method for objects ,using self and other , it access the amount from both and return the new object with sum amount
# Now, when print function prints the object, that object has the sum amount in __repr__.

# Write a Playlist class: __init__(self, songs) storing a list of song names, and __len__(self) returning how many songs. Test len(playlist).
# (This is the same __len__ that makes len([1,2,3]) work — now on your own class.)


class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


playlist = Playlist(["A", "B", "C", "D"])
print(len(playlist))  # 4

# 5. Write a Point class (a 2D point): __init__(self, x, y), __repr__ showing "Point(2, 3)", __eq__ comparing both coordinates,
# and __add__ returning a new Point with summed coordinates. Test: create points, add two together, compare two equal ones, print results.
# (This is a classic — a vector-like object that behaves naturally with + and ==.)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(2, 3)
point1 = Point(2, 3)
point2 = Point(3, 4)
print(point)
print(point == point1)  # True
print(point == point2)  # False
print(point + point1)  # Point(4, 6)


# data classes
from dataclasses import dataclass, field

# Rewrite Rectangle as a @dataclass with width: int and height: int.
# Keep the area(self) method. Create one, print it, call area().
# Notice you write no __init__ and no __repr__.


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height


# basically, now i dont need to write __init__,__repr__,__eq__.This is handled by dataclass decorator.
# Note: any behavioural change needs to be added. For example: area we are creating because we are defining the behavior and
# area is not same for other things. Behavior of __init__,__repr__,__eq will be same for almost all scenarios unless there is a specific requirement

point = Rectangle(2, 3)
point1 = Rectangle(2, 3)
print(point == point1)  # True
print(point)  # Point(width=2, height=3)
print(point.area())  # 6
# print(point + point1) # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'. __add__ we need to implement


# Rewrite Money as a @dataclass with amount: int. Keep your __add__ method (dataclass doesn't generate that — it's behavior, not boilerplate).
# Test Money(50) + Money(30) and print it.


@dataclass
class Money:
    amount: int

    def __add__(self, other):
        totalSum = self.amount + other.amount
        return Money(totalSum)


money = Money(100)
money1 = Money(110)
print(money)  # Money(amount=100)
print(money == money1)  # False
print(money + money1)  # Money(amount=210)

# 3. Write a User dataclass with name: str, age: int = 0, is_active: bool = True.
# Create one with just a name, print it. Then create one passing all three.


@dataclass
class User:
    name: str
    age: int = 0
    is_active: bool = True


onlyName = User("Xicor")
print(onlyName)  # User(name='Xicor', age=0, is_active=True)

allFields = User("Goku", 80, True)

print(allFields)  # User(name='Goku', age=80, is_active=True)


# Write a Circle dataclass with radius: float, and add an area(self) method (3.14159 * self.radius**2).
# Create one, print it, call area().


@dataclass
class Circle:
    radius: float

    def area(self):
        return 3.14159 * self.radius**2


circle = Circle(5)
print(circle)  # Circle(radius=5)
print(circle.area())  # 78.53975

# 5. Write a Book dataclass: title: str, author: str, pages: int, price: float = 0.0.
# Create two books, print them (see the auto __repr__), and test whether two books with identical fields are == (see the auto __eq__).
# (This is what a real domain object looks like — a clean, typed bundle of data, exactly the kind of thing your ETL/RAG code will be full of.)


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float = 0.0


book1 = Book("Atomic Habits", "James Clear", 100, 100)
book2 = Book("Eat That Frog", "Brian Tracy", 200, 200)
book3 = Book("Atomic Habits", "James Clear", 100, 100)

print(book1 == book2)  # False
print(book1 == book3)  # True

# Summary:

# Without dataclass, for each class, we need to write __repr__,__init__,__eq__ manually. And these methods are helpful in debugging
# because when you compare two objects and if dont write __eq__ method, then it compares objects by reference which gives false every time. Two objects cannot be
# identical. So, we write __eq__ to compare by value
# With data class, the boilerplate is alreay written. Only, the behavioral methods we need to write
# A dataclass is a decorator which we are yet to learn
# I also dont know about ETL/RAG. # TODO need to comeback here and add a explaination once i learn


# Inheritance basics

# Write an Animal class with __init__(self, name) and a speak(self) method returning "some sound".
# Then write a Cat(Animal) that overrides speak to return "meow". Create a Cat, call speak() and access name.
# (Overriding = child redefines a parent method. Note: Cat needs no __init__ of its own — it inherits Animal's.)


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "some sound"


class Cat(Animal):

    def speak(self):
        return "meow"


cat = Cat("Beerus")
print(cat.speak())  # meow  - method overriding


# Write Vehicle with __init__(self, brand) and a describe(self) returning the brand.
# Then Car(Vehicle) whose __init__ takes brand and doors, calls super().__init__(brand), and adds self.doors.
# Create a Car, print brand and doors. (This is the super() case — Car defines its own __init__, so it calls the parent's to handle brand.)


class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        return self.brand


class Car(Vehicle):  # car is a vehicle

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def info(self):
        return f"A {self.describe()} has {self.doors} doors."


car = Car("Maruti", 4)
print(car.info())  # A Maruti has 4 doors

# I assumed it can done using data class as well and i assumed it will automatically calls super for its base class memmbers. Lets discuss about this


@dataclass
class Vehicle:
    brand: str

    def describe(self):
        return self.brand


@dataclass
class Car(Vehicle):
    doors: int = 0

    def info(self):
        return f"A {self.describe()} has {self.doors} doors."


car = Car("Maruti", 4)
print(car.info())


# For each pair, decide inheritance or composition, write the class skeleton (just the headers — class X: or class X(Y):), and one line saying is-a or has-a:
# a Student and a Person  A student is a person - class Student(Person) - Inheritance
# a House and a Room     A house has a room - class House and class Room and pass room's object to house - composition
# a Circle and a Shape    # Inheritance - A circle is a shape - class Circle(Shape)


# Composition

# Write a Book dataclass (title, author) and a Library class that holds a list of Books, with add_book(self, book) and list_books(self) methods.
# Create a library, add two books, list them. (A Library HAS Books — composition.)


@dataclass
class Book:
    title: str
    author: str


@dataclass
class Library:
    # listOfBooks: list = []  # this throws default mutable error , to fix this, we need to use default_factory
    listOfBooks: list[Book] = field(
        default_factory=list
    )  # This create a fresh copy of list for each instance of Library

    def add_book(self, book):
        self.listOfBooks.append(book)

    def list_books(self):
        for book in self.listOfBooks:
            print(f"{book.title} : {book.author}")


book = Book("Atomic Habit", "James Clear")
book1 = Book("Eat that Frog", "Brian Tracy")

library = Library()
library.add_book(book)
library.add_book(book1)
print(library.list_books())  # 2

# Write a CPU dataclass (cores: int) and a RAM dataclass (size_gb: int), then a Computer class that composes both (holds a CPU object, a RAM object, and a name).
# Give Computer a describe(self) that reports its name, cores, and RAM by reaching into its parts (self.cpu.cores, etc.).
# Create the parts, build a Computer, print its description. (A Computer HAS a CPU and HAS RAM — pure composition, how most real domain objects are built.)


@dataclass
class CPU:
    cores: int


@dataclass
class RAM:
    size_gb: int


@dataclass
class Computer:
    name: str
    cpu: CPU
    ram: RAM

    def describe(self):
        return f"A {self.name} has a {self.cpu.cores} cores and {self.ram.size_gb} gigabytes."


cpu = CPU(10)
ram = RAM(16)
computer = Computer("MAC", cpu, ram)
print(computer.describe())  # A MAC has a 10 cores and 16 gigabytes.


# Polymorphism - poly means many and morph means forms - many forms

# — Polymorphism via a shared method name

# Write three classes — Circle, Square, Triangle — each with an area(self) method (circle 3.14 * r * r, square s * s, triangle 0.5 * b * h). Put instances in a list, loop over it, and print each area. (Same call .area(), different behavior per shape — that's polymorphism.)


@dataclass
class Circle:
    radius: int

    def area(self):
        return 3.14 * self.radius**2


@dataclass
class Square:
    side: int

    def area(self):
        return self.side**2


@dataclass
class Triangle:
    h: int
    b: int

    def area(self):
        return 0.5 * self.b * self.h


for instance in [Circle(5), Square(10), Triangle(10, 20)]:
    print(f"The area of {type(instance).__name__} is {instance.area()}")


# Duck typing (Python's loose polymorphism)

# Write a function describe_all(items) that loops a list and calls .describe() on each item. Then make two unrelated classes — say Book with a describe() and Car with a describe(), with no inheritance between them — and pass a mixed list [book, car] to describe_all. (This shows duck typing — the function works on unrelated types purely because they both have describe().)


def describe_all(items):
    for item in items:
        item.describe()


@dataclass
class Book:
    author: str
    title: str

    def describe(self):
        print(f"{self.author} : {self.title}")


@dataclass
class Car:
    brand: str

    def describe(self):
        print(f"The brand name of the car is {self.brand}")


describe_all([Book("A", "B"), Car("Lamborgini")])

# Your Money and Point classes both had __add__. When you write a + b, how is that polymorphism? One or two sentences.

# Explanation: When we create two objects of a class lets say Money and Point and we try to add those objects. It simply
# calls obj.__add__(). It doesnt care about the type. It looks for __add__ method and does the job.
# How is thar polymorphism? So , Money and Point are two classes. They are not dependent on each other. but if we observe
# both has __add__ dunder method which implies many forms. And it is duck typing also because when we call money1 + money2 ,
#  python doesnt care if the type of the object is money then only it should call __add__. It just check , object has access to
# __add__ and it calls.

# -----------------------------------------------------------------------------------

# Class Methods

# 1 — API response → objects (the pattern you just learned)

# You get a user from an API as a dict. Write a User dataclass (username: str, email: str) with a from_dict(cls, data) factory. Then, given a list of user dicts, turn the whole list into User objects using your factory + a comprehension.

response = [
    {"username": "xicor", "email": "x@mail.com"},
    {"username": "vegeta", "email": "v@mail.com"},
]


@dataclass
class User:

    username: str
    email: str

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["email"])

    @classmethod
    def from_list(cls, data):
        return [cls.from_dict(d) for d in data]

    def describe(self):
        return f"User = {self.username} , Email = {self.email}"


users = User.from_list(response)
for user in users:
    print(user.describe())

# name = xicor , email = x@mail.com
# name = vegeta , email = v@mail.com


# 2 — CSV line → object

# Data comes from a CSV file as a string like "Atomic Habits,James Clear,320". Write a Book dataclass (title: str, author: str, pages: int) with a from_csv_line(cls, line) factory that splits on "," and builds a Book. Remember pages must be an int. Test with Book.from_csv_line("Atomic Habits,James Clear,320").


@dataclass
class Book:

    title: str
    author: str
    pages: int

    @classmethod
    def from_csv_line(cls, line):
        title, author, pages = line.split(",")
        pages = int(pages)
        return cls(title, author, pages)


book = Book.from_csv_line("Atomic Habits,James Clear,320")
print(book)  # Book(title='Atomic Habits', author='James Clear', pages=320)

# 3 — Class-level counter (classmethod that isn't a factory)

# Not every classmethod is a factory. Write an Employee class that tracks how many employees exist. Use a class attribute count = 0, increment it in __init__ (Employee.count += 1), and add a @classmethod get_count(cls) that returns cls.count. Create three employees, then call Employee.get_count(). (This is a classmethod reading class-level state — the other main use besides factories.)


class Employee:

    count = 0

    # A question, now as i asked to create init, it means i cant use dataclass decorator?
    def __init__(self):
        Employee.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


employee1 = Employee()
employee2 = Employee()
employee3 = Employee()

print(Employee.get_count())  # 3

# 4 — Alternative constructor for a special case

# Write a Rectangle dataclass (width: float, height: float) with an area(self) method. Add two factory classmethods: square(cls, size) that makes a rectangle with equal sides, and from_dict(cls, data) that builds one from {"width": ..., "height": ...}. Test all three creation styles (normal, square(5), from_dict({...})) and print each area.


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height

    @classmethod
    def square(cls, size):
        return cls(size, size)

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["width"], dict["height"])


rectangleDict = {"height": 10, "width": 10}

rectangle = Rectangle(10, 10)
print(rectangle.area())  # 100

square = Rectangle.square(10)
print(square.area())  # 100

rectangleFromDict = Rectangle.from_dict(rectangleDict)
print(rectangleFromDict.area())  # 100

# 5 — Factory with light validation / transformation

# API sometimes sends messy data. Write a Product dataclass (name: str, price: float) with a from_dict(cls, data) factory that: strips whitespace from the name (.strip()), and converts price to float (it might arrive as a string like "9.99"). Test with Product.from_dict({"name": "  Widget  ", "price": "9.99"}) → should give Product(name='Widget', price=9.99). (Factories often clean/convert data on the way in — a mini-transform, the "T" in ETL.)


@dataclass
class Product:
    name: str
    price: float

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"].strip(), float(data["price"]))


product = Product.from_dict({"name": "  Widget  ", "price": "9.99"})
print(product)  # Product(name='Widget', price=9.99)


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
