# What is exception handling ?

# It is a way to catch an exception thrown by the program

# Example

worker = iter([1, 2, 3, 4])

print(next(worker))
print(next(worker))
print(next(worker))
print(next(worker))
# print(next(worker))  # StopIteration

# if you observe , when we call the next 5th time for the worker, it throws error - StopIteration because there is no item to process.

try:
    worker = iter([1, 2, 3, 4])
    print(next(worker))
    print(next(worker))
    print(next(worker))
    print(next(worker))
    print(next(worker))
except StopIteration:
    print("No more item to go through")  # No more item to go through

# So, now instead of throwing the error , it catches the exception and print the message

# Practice set — part 1 (the basics)

# Predict outputs, and note which line raises and which except catches.

# 1 — Basic try/except
# Write a function safe_divide(a, b) that tries a / b and catches ZeroDivisionError, returning "Cannot divide by zero" instead. Test with safe_divide(10, 2) and safe_divide(10, 0).


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero

# 2 — Catching specific exceptions

# Write code that takes a dict prices = {"pen": 10, "book": 50} and tries to look up a key the user provides. Catch KeyError and print a friendly "item not found" message. Test with an existing key and a missing key.

prices = {"pen": 10, "book": 50}


def lookUpForKey(key, data):
    try:
        return data[key]
    except KeyError:
        return "item not found"


print(lookUpForKey("pen", prices))  # 10
print(lookUpForKey("pencil", prices))  # item not found


# 3 — Multiple except blocks

# Write a function parse_and_divide(text, divisor) that does int(text) / divisor. Catch ValueError (if text isn't a number) and ZeroDivisionError (if divisor is 0) separately, with different messages. Test all three cases: valid, bad text, zero divisor.


def parse_and_divide(text, divisor):
    try:
        return int(text) / divisor
    except ZeroDivisionError:
        return "cannot divide by zero"
    except ValueError:
        return "text is not a number"


print(parse_and_divide("12", 2))  # 6.0
print(parse_and_divide("12", 0))  # cannot divide by zero
print(parse_and_divide("text", 2))  # text is not a number

# 4 — raise your own

# Write a function set_age(age) that raises a ValueError with a message if age is negative or over 150, otherwise returns the age. Test with a valid age, a negative one (wrap the call in try/except to catch it), and confirm the raised message shows.


def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age should be greater than 0 and less than 150")
    return age


try:
    print(set_age(100))  # 100
except ValueError as e:
    print(e)

try:
    print(set_age(-100))  # 100
except ValueError as e:
    print(e)

try:
    print(set_age(155))  # 100
except ValueError as e:
    print(e)


# 5 — finally runs always

# Write a function that opens a try, does 10 / b, catches ZeroDivisionError, and has a finally that prints "done". Call it with b=2 and b=0 — predict what prints in each case. (Note whether finally runs when there's no error.)


def can_b_divide(b):
    try:
        return 10 / b
    except ZeroDivisionError:
        return "b cannot divide as b is zero"
    finally:
        print("done")


print(can_b_divide(10))
# It prints the done first and then prints the result 1.0

print(can_b_divide(0))  # done - b cannot divide as b is zero

# 6 — else on success
# Write a function parse_number(text) with a try doing int(text), an except ValueError printing "not a number", and an else printing "successfully parsed {value}". Test with "42" and "abc" — predict which block runs for each.


def pars_number(text):
    try:
        value = int(text)
    except ValueError:
        return "not a number"
    else:
        return f"successfully parsed {value}"


print(pars_number(42))  # successfully parsed 42
print(pars_number("abc"))  # not a number

# one issue i faced here is, i wrote return value in try block only. Due to which the code was unreachable to else
# Then i asked claude agent and it explained me that if we return the value then the function exits and it never
# goes to else block
# So i understood that only the value we should parse and while parsing if we get an exception, it will get caught
# otherwise it will go to else block and return success message


# 7 — a custom exception
# Define NegativeNumberError(Exception). Write sqrt_check(n) that raises it (with a message) if n < 0, otherwise returns n ** 0.5. Test with 16 and -4, catching your custom exception in the caller and printing the message.


# in order to create a custom exception, a class should inherit Exception common base class.
class NegativeNumberError(Exception):
    pass


def sqrt_check(n):
    if n < 0:
        raise NegativeNumberError("n must be greater than zero")
    return n**0.5


try:
    print(sqrt_check(16))  # 4.0
except NegativeNumberError as e:
    print(e)

try:
    print(sqrt_check(-4))
except NegativeNumberError as e:
    print(e)  # n must be greater than zero


# 8 — combining it all

# Write withdraw(balance, amount) that raises a custom InsufficientFundsError if amount > balance, raises a ValueError if amount <= 0, otherwise returns the new balance. In the caller, catch both exception types separately (different messages). Test: a valid withdrawal, an overdraw, and a zero/negative amount.


class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not Enough Balance.")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    return balance - amount


try:
    newBalance = withdraw(100, 50)
except ValueError as e:
    print(e)
except InsufficientFundsError as e:
    print(e)
else:
    print(f"Your new balance is {newBalance}")  # Your new balance is 50

try:
    newBalance = withdraw(100, 150)
except ValueError as e:
    print(e)
except InsufficientFundsError as e:  # Not Enough Balance.
    print(e)
else:
    print(f"Your new balance is {newBalance}")

try:
    newBalance = withdraw(100, -100)
except ValueError as e:  # # Amount must be greater than 0
    print(e)
except InsufficientFundsError as e:
    print(e)
else:
    print(f"Your new balance is {newBalance}")
