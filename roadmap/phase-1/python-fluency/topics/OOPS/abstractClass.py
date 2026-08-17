# Abstract Class - is kind of contract that all the subclass must implement abstracts methods into the class. Abstraction enforces the interface whereas duck typing hopes for it.
from dataclasses import dataclass
from abc import ABC, abstractmethod

# 1 — Basic ABC
# Abstract Animal(ABC) with abstract speak(self). Then Dog(Animal) returning "Woof" and Cat(Animal) returning "Meow". Create a Dog and Cat, call speak(). Then try Animal() directly — what happens?


class Animal(ABC):

    @abstractmethod
    def speak():  # This means, every subclass which inherits the Animal class now must implement speak
        pass


class Dog(Animal):

    def speak(self):
        return f"{type(self).__name__} Woof"


class Cat(Animal):

    def speak(self):
        return f"{type(self).__name__} Meow"


dog = Dog()
print(dog.speak())  # Dog Woof

cat = Cat()
print(cat.speak())  # Cat Meow

# animal = Animal()
# print(animal.speak()) # Can't instantiate abstract class Animal without an implementation for abstract method 'speak' Please explain more about this


# 2 — Enforcement (missing method)
# Same Animal(ABC). Write Fish(Animal) that forgets speak (body is just pass). Try to create Fish() — predict the result.


class Fish(Animal):

    def speak(self):
        pass


fish = Fish()
# prediction is it will throw error.Cannot create object without implemention of speak

fish.speak()  # But it allowed. I think the reason is when we created object for Animal class
# we didnt actually inherited the abstract class.
# But for fish, we inherited and as per rule we should implement speak and we did.it just that
# it does nothing.

# But honestly am still confused . So, lets discuss about this.

# 3 — Multiple abstract methods
# Abstract Shape(ABC) with abstract area(self) and perimeter(self). Implement Rectangle(Shape) with both. Create one, call both.


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


@dataclass
class Rectangle(Shape):
    l: float
    b: float

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * self.area()


rectangle = Rectangle(10, 10)
print(rectangle.area())  # 100
print(rectangle.perimeter())  # 200

# Extend #3: add a concrete (non-abstract) describe(self) to Shape returning f"Area: {self.area()}, Perimeter: {self.perimeter()}". Rectangle inherits it free. Create a Rectangle, call describe(). (Enforce the variable parts, share the common parts.)


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"


@dataclass
class Rectangle(Shape):
    l: float
    b: float

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * self.area()


rectangle = Rectangle(10, 10)
print(rectangle.describe())  # Area: 100, Perimeter: 200


# Write print_all_areas(shapes) that loops a list of shapes and prints each .area(). Pass a list of two different Shape subclasses. (Because abstraction guarantees every Shape has area(), this function is safe — that's the payoff.)


def print_all_areas(shapes):
    for shape in shapes:
        print(f"Area of {type(shape).__name__} is {shape.area()}")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Shape):
    l: float
    b: float

    def area(self):
        return self.l * self.b


@dataclass
class Square(Shape):
    side: float

    def area(self):
        return self.side**2


rectangle = Rectangle(10, 20)
square = Square(100)

print_all_areas(
    [rectangle, square]
)  # Area of Rectangle is 200 /n  Area of Square is 10000
