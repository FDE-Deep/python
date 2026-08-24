# What is a context manager ?
# A context manager is an object acts like a setup and have defined  __enter__ and __exit__() dunder methods.
# A context manager is used when we need open or close a file, connect or disconnect database etc.
# For example : with open(File) as file: so, here with block executes __enter__ dunder method and once it finishes reaches the end of line in the with block ,it  executes __exit__() dunder method


# Practice set

# Predict outputs and trace when __enter__ and __exit__ fire.

# 1 — Understand the flow

# Write a Greeter context manager: __enter__ prints "entering" and returns self; __exit__ prints "exiting". Use it in a with block that prints "inside". Predict the order of the three prints. (This shows the enter → block → exit sequence.)


class Greeter:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with Greeter() as greet:
    print("Inside")

# output:
# Entering - > Inside - > Exiting

# 2 — The as binding
# Write a context manager Resource whose __enter__ returns the string "the resource". Use with Resource() as r: and print r inside. Predict what r is. (Shows that as binds whatever __enter__ returns.)


class Resource:

    def __enter__(self):
        return "the resouce"

    def __exit__(self, exc_type, exc_value, traceback):
        print("DoNe")


with Resource() as r:
    print(r)  # the resouce -> DoNe


# 3 — Cleanup runs even on error
# Write a context manager Guard: __enter__ prints "acquired", __exit__ prints "released". Inside the with block, print("working") then raise ValueError("boom"). Wrap the whole with in a try/except ValueError. Predict the order of prints — does "released" still print even though the block raised? (This is the key property — cleanup is guaranteed, like finally.)


class Guard:

    def __enter__(self):
        print("acquired")

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value)
        print("released")


try:
    with Guard():
        print("working")
        raise ValueError("boom")
except ValueError as e:
    print(e)

# Output: acquired -> working -> released

# 4 — A practical one: the Timer
# Write the Timer context manager (like the example) and use it to time a loop that sums range(1_000_000). Confirm it prints an elapsed time. (A real, useful context manager.)

import time


class Timer:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"Elapsed Time - {elapsed} seconds")


def totalSum(n):
    return sum(number for number in range(n))


# i could have written sum as comprehension also return sum([number for number in range(n)]). But i think this increases the complexity as first we create the list then sum again iterate over list. So, time complexity and space complexity is affected in this approach. Even though it looks tempting to write in single line but it has more cost.


with Timer():
    totalSum(1000000)  # Elapsed Time - 0.02309131622314453 seconds


# @contextmanager

# context manager can be written as function using following import

# context manager functions are generators. When a context manager invokes, it starts the execution and stops at yield
# when with calls the exit, it resumes the execution from yield to exit the process.

from contextlib import contextmanager

# 1 — Basic @contextmanager

# Rewrite your Greeter as a @contextmanager generator function instead of a class. It should print "entering" (setup, before yield), then yield, then print "exiting" (cleanup, after yield). Use it in a with block that prints "inside". Predict the order of the three prints.


@contextmanager
def Greeters():
    print("entering")
    yield
    print("exiting")


with Greeters():
    print("inside")

# output is -> entering -> inside -> exit. Basically enter -> with block -> exit

# 2 — Yielding a value for as
# Write a @contextmanager function get_connection() that prints "connecting", yields the string "DB connection", then prints "disconnecting" after. Use with get_connection() as conn: and print conn inside. Predict the output order and what conn is.


@contextmanager
def get_connection():
    print("connecting")
    yield "DB connection"
    print("disconnecting")


with get_connection() as conn:
    print(conn)

# connecting -> DB connection -> disconnecting

# 3 — Guaranteed cleanup with try/finally
# Write a @contextmanager function guard() that prints "acquired", yields, then prints "released" — but make "released" run even if the block raises, by wrapping the yield in try/finally. Test it by raising a ValueError inside the with (catch it outside the with), and confirm "released" still prints.

# lets try first without try/finally


@contextmanager
def guard():
    print("acquired")
    yield
    print("released")


# with guard():
#    raise ValueError("Error")

# so here , the execution stopped because inside with block, we raised an exception which terminated the execution


@contextmanager
def guardFinally():
    try:
        yield
    finally:
        print("released")


try:
    with guardFinally():
        raise ValueError("Error")
except ValueError as e:
    print(e)
