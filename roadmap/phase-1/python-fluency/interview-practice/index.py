# Drill 1 — closure late binding (Q2 gap)

funcs = []

for i in range(3):
    funcs.append(lambda: i)


# Predict all three outputs. Then answer: at the moment each lambda runs, what is the value of i, and why?

print(funcs[0]())  # 2

# Lets break it down.

# when for loop runs, it appends the lamba function to the func array
# Now, lambda has access to i by reference
# So, when first iteration happens, the value of i is zero which means whenever we refer to i we get the zero.
# When third iteration finishes, the i value becomes 2

# so , now when we call funcs[0]() the value fo i was 2 and it returns 2

print(funcs[1]())  # 2
# So, when first iteration happens, the value of i is zero which means whenever we refer to i we get the zero.
# When third iteration finishes, the i value becomes 2

# so , now when we call funcs[1]() the value fo i was 2 and it returns 2
print(funcs[2]())  # 2
# So, when first iteration happens, the value of i is zero which means whenever we refer to i we get the zero.
# When third iteration finishes, the i value becomes 2

# so , now when we call funcs[2]() the value for i was 2 and it returns 2


# is it same as default mutable trap? i value is dynamic here and during memory allocation, i gets the address, only value changes later . It does not create new i for each iteration.

# During lamba call, when it refers to i, it has value 2


# Drill 2 (the super() gap from the interview). Here it is again; predict each print and identify which line crashes:


class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


class C(A):
    def __init__(self, x, y):
        self.y = y  # no super() call


# Trace it: what does print(b.x, b.y) show? What about print(c.y)? And print(c.x) — does it work or crash, and why?

b = B(1, 2)
print(b.x, b.y)
# This print 1,2. Reason is, when we create an object of class, it first calls the __init__ dunder method. This takes care of assigning values to the ojbect. Now, class B has inherited class A. Using super().__init__() we call the init method of class A and assign value to x. So, B is subclass of A so it has access to its and base class variables.

c = C(1, 2)
print(c.y)
# This will print 2 because c.y is defined in init method.
# print(c.x)
# This will return error c object has no attribute x. because we didnt call the super().__init__() and assign value of x to self.x which belongs to base class


# Drill 3 (the context-manager exception-suppression gap, Q8):


class CM:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print("cleanup")
        # note: no return statement → returns None


with CM():
    print("before")
# raise ValueError("x")
print("after")

# Predict what prints, in order. Then answer the crucial part: does "after" print? Does the program crash? Explain what __exit__ returning None means for the ValueError — does it get suppressed or does it propagate?


# Output:

# As there is no print statement in __enter__, so nothing from here.
# then , it moves to the body of with block.
# exception will be raised but __exit__ works as finally. So, it will print "cleanup"
# print("after") will not work as exception is raised before that and python terminates the execution there


# Drill 4 (the generator resume-points gap, Q4):


def g():
    print("1")
    yield "a"
    print("2")
    yield "b"
    print("3")
    yield "c"


gen = g()
print(next(gen))
print(next(gen))

# Predict every line that prints, in order. Be precise about what does not print and why — there are only two next() calls, so trace exactly where execution pauses each time.


# Explanation: gen is a generator. When we call next(gen) , it executes the function till first yield , then next() call next yield  and so on. Basically, gen is like a worker which has O(1) space. The next() calls and updated where function execution should be stopped.

# output:
# 1
# a
# 2
# b


# Question 1 of 10.


def f(a, b=[]):
    b.append(a)
    return b


# Predict all four outputs, line by line.

print(
    f(1)
)  # [1] appended the 1 to the default list. So, here , during definition only, python will assign the empty array to b and for any next function calls it will not create new list.It will just return the reference of that list
print(
    f(2)
)  # [1,2] as i explained above, pointing to the same list in the memory instead of creating new list
print(f(3, []))  # [3] now, we are assigning new empty list again to b.
print(f(4))  # [3,4]

# Question 2 of 10.

x = 5


def outer():
    x = 10

    def inner():
        print(x)

    x = 20
    inner()


outer()

# What does this print, and why? Be specific about which x inner sees and when it's read.

# This question is an example of closure. Closure holds the value of outer functions.
# This will print the value 20 as during definition the value of x is 10 but during call it is 20. So, during call, it will get access to x which holds the value 20


class Base:
    def greet(self):
        return "Base"


class Left(Base):
    def greet(self):
        return "Left"


class Right(Base):
    def greet(self):
        return "Right"


class Child(Left, Right):
    pass


c = Child()
print(c.greet())
print(Child.__mro__)

# Predict what c.greet() returns, and write out the full MRO order (all classes in the chain).

# First i will write MRO to understand , it is referring to which parent class.

# As per rule child -> left -> right , MRO is Child -> Left -> Right -> Base

# print(c.greet()) will print "Left"
# print(Child.__mro__) MRO is Child -> Left -> Right -> Base


# Question 4 of 10.

nums = [1, 2, 3, 4, 5]
result = [x * 2 for x in nums if x % 2 == 0]
print(result)  # [4,8]

squared = {x: x**2 for x in nums}
print(squared)  # {1:1,2:4,3:9,4:16,5:25}

evens = {x for x in nums if x % 2 == 0}
print(evens)  # {2,4}

# Predict all three outputs.


# Question 5 of 10.


def genn():
    yield 1
    yield 2
    yield 3


gn = genn()


# Predict both outputs. The second one is the interesting part — think about what state g is in by then.
print(
    list(gn)
)  # List is a iterable. When list gets a worker or iter i can say, it loops over it and gets everything. so, output is [1,2,3]
print(
    list(gn)
)  # [] This will be empty as gn generator has already been loop over and moved to garbage collection


# Question 6 of 10.


class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("negative")
        self._balance = value


# Predict all three prints. The last two lines are the interesting part — trace carefully what each one does.
a = Account(100)
print(
    a.balance
)  # 100. balance is a property which refers to the interal member _balance . This member holds the value of 100 as we have defined its value in __init__()
a.balance = 50  # As balance property has a setter defined, its value can be updated. But it is implicit. It is updating the value of _balance.
print(a.balance)  # 50
a._balance = (
    -999
)  # -999 We are directly updating the internal member of the class which python allows.
print(a.balance)  # -999

# Question 7 of 10.


class TooSmallError(Exception):
    pass


def check(n):
    if n < 10:
        raise TooSmallError(f"{n} is too small")
    return n


try:
    print(check(5))
except TooSmallError as e:
    print("caught:", e)
except Exception as e:
    print("general:", e)

# Predict the output. Also answer: there are two except blocks — why does the order matter here, and which one runs?

# Output will be "caught: 5 is too small"

# Why order matters? I tried running it in both ways. When i added Exception as e before TooSmallError then the exception was caught as general exception. But we have raise a specific exception. So, we should look for that first and it doesnt find then it should fallback to general exception.

from contextlib import contextmanager


@contextmanager
def managed():
    print("setup")
    yield "resource"
    print("teardown")


with managed() as r:
    print("using", r)

# Two parts:
# (a) Predict the output in order.
# Output : setup -> resource -> using -> teardown. Whatever comes before yield acts as enter and after yield exit.
# (b) Now: what if the with body raised an exception (instead of print("using", r)) — would "teardown" still print? Explain, and say how you'd fix it if not.
# Answer is No. because we need to add finally in context manager .If not added, then it stops the execution of the function. After adding finally, it will print teardown but still throws the exception error and if we want to catch the exception then caller needs to add try except block for with managed()


# Question 9 of 10.


def process(data: list[int]) -> int:
    total = 0
    for x in data:
        total += x
    return total


print(process([1, 2, 3]))
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# Two parts:
# (a) The first print — what does it output?
# output: 6
# (b) The second print passes a string where list[int] is expected. Does this crash at runtime? Does the type hint stop it? What would Pylance/mypy say? Trace what actually happens when process("hello") runs.

# It will crash at run time. No type hint wont stop it. mypy pylance say you cannot assign a string data to int type.


# Question 10 of 10 (final):

data = {"a": 1, "b": 2, "c": 3}

for k in data:
    print(k)  # a,b,c

print("---")

for k, v in data.items():
    print(k, v)  # a 1 b 2 c 3

print("---")

result = data.get("z", 0)
print(result)  # 0

value = data["z"]
print(value)  # keyerror
