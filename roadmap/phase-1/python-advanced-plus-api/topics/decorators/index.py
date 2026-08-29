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
        print(f"{func.__name__} took {elapsed:.4f}")
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


def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 3
        for attempt in range(1, attempts + 1):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt == attempts:
                    raise

    return wrapper


@retry
def countNumbers(item):
    if len(item) < 5:
        raise ValueError("Length of list is less then 5")
    return len(item)


# countNumbers([1, 2, 3])
print(countNumbers([1, 2, 3, 4, 5, 6]))  # 6

# output:

# Attempt 1 failed: Length of list is less then 5
# Attempt 2 failed: Length of list is less then 5
# Attempt 3 failed: Length of list is less then 5

# A decorator can accept arugments as well. But then it adds a one more layer.

# For example:


def multiplier(n=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return [x * n for x in result]

        return wrapper

    return decorator


def generateList(n):
    return [i for i in range(n)]


decorator = multiplier(2)
print(decorator)  # <function multiplier.<locals>.decorator at 0x000001B3774328D0>
wrapper = decorator(generateList)
print(
    wrapper
)  # <function multiplier.<locals>.decorator.<locals>.wrapper at 0x00000234302F2980>
print(wrapper(5))  # [0, 2, 4, 6, 8]

generateList = multiplier(2)(generateList)
print(generateList(4))


@multiplier(2)
def createList(n):
    return [i for i in range(n)]


print(createList(10))
# Practice

# 1 — Configurable @retry
# Rewrite your @retry to take an attempts argument (default 3), using the three-layer structure. Test it with @retry(attempts=2) on a function that always fails — confirm it tries exactly 2 times then raises. Then @retry(attempts=4) — confirm 4 attempts.


def retryCalls(attempts=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f"Attempt : {attempt} failed - {e}")
                    if attempt == attempts:
                        raise

        return wrapper

    return decorator


@retryCalls(2)
def justTestRetry(value):
    if value != "test":
        raise ValueError("Value doesnt match")
    return value


@retryCalls(4)
def justTestRetryattempt4(value):
    if value != "test":
        raise ValueError("Value doesnt match")
    return value


try:
    print(justTestRetry("tt"))
except ValueError as e:
    print("Failed after all attempts")

# output -

# Attempt : 1 failed - Value doesnt match
# Attempt : 2 failed - Value doesnt match
# Failed after all attempts
try:
    print(justTestRetryattempt4("tt"))
except ValueError as e:
    print("Failed after all attempts")

# output -

# Attempt : 1 failed - Value doesnt match
# Attempt : 2 failed - Value doesnt match
# Attempt : 3 failed - Value doesnt match
# Attempt : 4 failed - Value doesnt match
# Failed after all attempts


# 2 — Add a configurable exception type
# Extend it: retry(attempts=3, exceptions=ValueError) — so the caller specifies which exception(s) to retry on. Use except exceptions as e: (you can pass a single exception type or a tuple). Test @retry(attempts=2, exceptions=KeyError) on a function that raises KeyError, and confirm it retries; then confirm a different exception (say ValueError) is not retried (propagates immediately, because it's not in the caught types).


def retryOnlyValidException(attempts, exceptions):
    def decorator(func):
        @wraps(func)  # fixed. when will i stop doing sill mistakes
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt - {attempt} failed : {e}")
                    if attempt == attempts:
                        raise

        return wrapper

    return decorator


@retryOnlyValidException(4, KeyError)
def hasKey(data, key):
    if data.get(key) == None:
        raise KeyError(f"key : {key} is not present")
    return data.get(key)


data = {"name": "Deep"}

try:
    print(hasKey(data, "date"))
except KeyError as e:
    print("Failed after all attempts")

# output -

# Attempt - 1 faile : 'key : date is not present'
# Attempt - 2 faile : 'key : date is not present'
# Attempt - 3 faile : 'key : date is not present'
# Attempt - 4 faile : 'key : date is not present'
# Failed after all attempts


@retryOnlyValidException(4, KeyError)
def hasValue(data, key):
    if data.get(key) == None:  # fixed , silly mistake here as well
        raise ValueError(f"key : {key} is not present")
    return data.get(key)


try:
    print(hasValue(data, "date"))
except ValueError as e:
    print(
        "Didnt attempt because the exception doesnt match in decorator. So, function execution stops."
    )

# output - Didnt attempt because the exception doesnt match in decorator. So, function execution stops.


# 3 — A @repeat(n) decorator
# Simpler one to reinforce the pattern: write @repeat(n) that runs the decorated function n times (printing each result, or collecting them). @repeat(3) on a function that prints "hi" should print it 3 times. This is pure three-layer practice without the retry complexity.


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(n)]

        return wrapper

    return decorator


@repeat(3)
def hi():
    return "hi"


hi()

# output:
# hi
# hi
# hi


# Rate Limit - Time Delay


def retryWithDelayAndBackOff(attempts=1, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{e}")
                    if attempt == attempts:
                        raise
                    print(f"Retry after {current_delay} seconds ...")
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator


call_count = {"n": 0}


@retryWithDelayAndBackOff(attempts=5, delay=1, backoff=2)
def testFlakyApi():
    call_count["n"] += 1
    if call_count.get("n", 0) < 3:
        raise ValueError(f"Rate Limited : attempt {call_count["n"]} failed")
    print("Successful ..........")


testFlakyApi()

# Dry Run:

# For each attempt, the wrapper calls the testFlakyApi function
# It checks , if call_count["n"] < 5
# Yes, raise the exception
# Then exception is caught for each attempt
# And we delay it by current_delay
# And update the current_delay for next attempt using backoff

# And for each attempt after current delay , it will call the function again and see if it raises the exception or gets successful.
