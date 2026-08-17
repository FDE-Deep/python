from dataclasses import dataclass

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


# Multiple Inheritance


class A:

    def greet(self):
        return "I am A"


class B:

    def greet(self):
        return "I am B"


class C(A, B):

    def greet(self):
        return "I am C"


c = C()
print(c.greet())

# Even though all classes have same method but python calls the greet from C
# Internally python uses one functionality called MRO - Method Resolution Order
# Basic rule - child first, left to right

print(
    C.__mro__
)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# Python uses c3 linearization algorithm


class A:
    def greet(self):
        return "hello A"


class B(A):
    def greet(self):
        return "hello B"


class C(A):
    def greet(self):
        return "hello C"


class D(C, B):
    def greet(self):
        return "hello D"


# This is called diamond problem. D inherits C and B and C and B inerits A.

# As per rule, child first and left and right.

d = D()
print(d.greet())  # Prediction - hello D - child first


class D(C, B):
    def greet1(self):
        return "hello D"


d = D()
print(d.greet())  # Prediction - hello C - child first and then left


# It is advisable that instead of multiple inheritance , composition can be used.

# 1 — Basic multiple inheritance (no overlap)

# Write Flyer with fly(self) → "flying", Swimmer with swim(self) → "swimming", and Duck(Flyer, Swimmer) with its own quack(self). Create a Duck, call all three methods.


class Flyer:

    def fly(self):
        return "flying"


class Swimmer:

    def swim(self):
        return "swimming"


class Duck(Flyer, Swimmer):

    def quack(self):
        return "quack"


duck = Duck()
print(
    f"A duck is doing {duck.quack()} {duck.quack()} while {duck.fly()} and later it will do {duck.swim()}"
)

# A duck is doing quack quack while flying and later it will do swimming.

# 2 — Overlapping methods (which parent wins?)

# Write Father with greet(self) → "from Father" and Mother with greet(self) → "from Mother". Make Child(Father, Mother). Call child.greet() — predict which wins and why. Then make Child2(Mother, Father) (order swapped) and predict its result. Also print Child.__mro__.


class Father:

    def greet(self):
        return "from Father"


class Mother:

    def greet(self):
        return "from Mother"


class Child(Father, Mother):
    pass


child = Child()
print(
    child.greet()
)  # prediction - "from Father". As per rule child first and then left , right . There is no method for Child , so
# it goes to Father and greet is present . It returns from Father


class Child2(Mother, Father):
    pass


child2 = Child2()
print(
    child2.greet()
)  # prediction - : "from Mother" As per rule child first and then left , right . There is no method for Child , so
# it goes to Mother and greet is present . It returns from Mother
print(
    Child.__mro__
)  # (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)

# 3 — Inspect the MRO
# For your Child from #2, print Child.__mro__ and read the search order aloud. (Just confirm you can read the path.)

# I read

# 4 — A mixin (the good use)
# Write a GreetMixin with greet(self) returning f"Hi, I'm {self.name}". Write a Person class with __init__(self, name). Then FriendlyPerson(GreetMixin, Person). Create one, call greet(). (A focused mixin adding one capability — the clean use of multiple inheritance.)


class GreetMixin:
    name: str

    def greet(self):
        return f"Hi, I'm {self.name}"


class Person:

    def __init__(self, name):
        self.name = name


class FriendlyPerson(GreetMixin, Person):
    pass


friendlyPerson = FriendlyPerson("Xicor")
print(friendlyPerson.greet())

# my understanding is when we create an object for FriendlyPerson, it has now access to both __init__ from Person and great method.
# __init__ will set the name and greet prints it.

# Also , i think we dont create dataclass for person,because otherwise we need to use postinit.

#  What is a mixin, when it is useful and how it resolves diamond issue?

# Build the diamond: A with method → "A", B(A) with method → "B", C(A) with method → "C", D(B, C) with no method of its own. Call D().method() and predict the result. Print D.__mro__ and predict the full order before running. (This tests whether the C3 "grandparent last" idea landed.)


class A:

    def get(self):
        return "A"


class B(A):

    def get(self):
        return "B"


class C(A):

    def get(self):
        return "C"


class D(B, C):
    pass


print(
    D().get()
)  # Prediction - It should return "B". Because child first and left and right. D has no method. On left, it is B and B has get method. So, it will return "B"
print(D.__mro__)  # D -> B -> C -> A
