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
