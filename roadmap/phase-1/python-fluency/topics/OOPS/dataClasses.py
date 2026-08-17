# data classes
from dataclasses import dataclass

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
