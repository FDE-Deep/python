from dataclasses import dataclass, field

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
