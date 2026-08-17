from dataclasses import dataclass

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
