#  What is a decorator ?

# A decorator is a wrapper function that returns the enhanced version of the function.
# This works based on closures


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("after")
        return result

    return wrapper


def add(a, b):
    return a + b


add = my_decorator(add)
print(add(2, 3))

# now this can be done also using @ decorator


@my_decorator
def multiply(a, b):
    return a * b


print(multiply(2, 3))

# @my_decorator takes the multiply function , wraps it and return the function to the same multiply.


print(multiply.__name__)  # wrapper

# Now the problem with decorator is, if we observe, the multiply function is loosing its identity. When we
# try to prints its name, we are getting wrapper not multiply.

# Question : why we get the wrapper instead of multiply ? I mean how python works here. I know it can be fixed with functools.wraps but i want to understand first why we have wrapper instead of multiply

# When we create a decorator, during definition phase, the pyton creates object for wrapper function with __name__ wrapper.
# when we call the decorator and pass the func, the wrapper calls that func and return the wrapper.
# This wrapper we re-assign to the function which we passed earlier.
# Now, func holds the reference of wrapper object. And wrapper object holds the reference of the func.
# So, it returns wrapper instead of multiply

# Question: How functools.wrap fixes it ?

#  functool.wraps copy the metadata of the func and updates the metadata of wrapper.


from functools import wraps


def my_decorator_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("after")
        return result

    return wrapper


@my_decorator_wraps
def subtract(a, b):
    return a - b


print(subtract.__name__)  # subtract


# Practice set

# 1 — A basic decorator with behavior

# Write a decorator announce that prints "calling <function name>" before running the function and "finished <function name>" after, then returns the result. Use func.__name__ inside the wrapper to get the name. Apply it to a function greet(name) that returns f"Hi {name}". Call it and predict the output.


def annouce(func):
    def wrapper(*args, **kwargs):
        print(f"calling <{func.__name__}>")
        result = func(*args, **kwargs)
        print(f"finished <{func.__name__}>")
        return result

    return wrapper


@annouce
def greet(name):
    return f"Hi {name}"


print(greet("Vegeta"))

# Prediction

# First, it will print "Calling <greet>"
# then, prints "finished <greet>"
# The, Hi Vegeta


# output

# calling <greet>
# finished <greet>
# Hi Vegeta

# 2 — Preserve metadata
# Take your announce from #1. Add @wraps(func). Then define a greet with a docstring ("""Greets a person."""), decorate it, and print greet.__name__ and greet.__doc__. Predict both — and note what they'd be without @wraps.


def annouce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling <{func.__name__}>")
        result = func(*args, **kwargs)
        print(f"finished <{func.__name__}>")
        return result

    return wrapper


@annouce
def greet(name):
    """Greets a person."""
    return f"Hi {name}"


print(greet.__name__)
print(greet.__doc__)

# prediction:
# 1. greet
# 2. Greets a person

# if we dont add wraps then greet.__name__ returns wrapper  and doc string returns None as we havent defined an y inside wrapper


# 3 — A decorator that changes the result
# Write a decorator double_result that calls the function and returns twice its result (multiply by 2). Apply it to add(a, b). Predict add(3, 4). (This shows a decorator can transform the return value, not just add side effects.)


def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@double_result
def add(a, b):
    return a + b


print(add(3, 4))

# Predcition is  14
# Output is 14


# 4 — @timer
# Write timer: the wrapper records the start time, calls the function (capturing the result), computes elapsed, prints "<name> took <elapsed> seconds", and returns the result. Use @wraps. Test it on a function slow_sum(n) that returns sum(range(n)), called with 1_000_000. Confirm it prints a time and returns the correct sum.

import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} took {elapsed}")
        return result

    return wrapper


@timer
def totalSum(n):
    return sum(i for i in range(n))


print(
    totalSum(1000000)
)  # totalSum took 0.020299434661865234 # total sum is 499999500000


# 5 — @retry (the real-world one)

# Write retry: the wrapper tries to call the function up to 3 times. On each attempt, try to call it and return the result immediately on success. If it raises, catch the exception, print something like "attempt <n> failed: <error>", and loop to try again. If all 3 attempts fail, re-raise the last exception (don't swallow it silently).
