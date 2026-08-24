# What is a type hint ?

# By default, python does not enforce a type check for a variable
# But for developers, to produce less errors, a type hint can be added
# and can be verified using mypy or pylance in vs code


# Basic type check

stringType: str = "data"
intType: int = 12
booleanType: bool = True
decimalType: float = 12.00

# Container type

listOfFruits: list[str] = ["Apple"]
listOfNumbers: list[int] = [1, 2, 3]
dictType: dict[str, int] = {"key": 1}
setType: set[int] = {1}

# class Type


class Book1:
    pass


b: Book1 = Book1()


# function type


def add(a: int, b: int) -> int:
    return a + b


# a parameter can have multiple types also


def add1(a: int | str, b: int | str) -> int:
    return int(a) + int(b)


# Practice set

# Write these. You have Pylance, so watch the editor flag the deliberate errors.

# 1 — Write multiply(a, b) with both parameters typed as int and return typed as int. Call it once correctly, once passing a string. Note whether Pylance flags the string call, and whether it still runs at runtime.


def multiply(a: int, b: int) -> int:
    return a * b


# multiply("12", 12) # error: Argument 1 to "multiply" has incompatible type "str"; expected "int"  [arg-type]

print(multiply(1, 1))  # Success: no issues found in 1 source file

# 2 — Write find_item(name, items) where items is a dict[str, int], returning the value if the name is a key, else None. What should the return type annotation be?


def find_item(name: str, items: dict[str, int]) -> int | None:
    return items.get(name)


items = {"apples": 12, "bananas": 10}
print(find_item("apples", items))  # 12
print(find_item("appls", items))  # None

# 3 — Annotate:

# a function total(nums) taking a list of ints, returning an int


def total(nums: list[int]) -> int:
    return sum(num for num in nums)


# a variable holding a dict mapping str to float

strToFloat: dict[str, float] = {"temperature": 12.12}

# a function get_books() returning a list of Book objects


class Books:
    pass


def get_books() -> list[Books]:
    b1 = Books()
    b2 = Books()
    return [b1, b2]


# 4 — Take Library.add_item and Library.borrow_item from your library and add full type hints — parameters and return types. Think about what each returns. For borrow_item, also decide: what type are your ids? (You've used both strings and ints for ids across the project — pick one and be consistent.)


class LibraryItem:
    pass


class Library:
    def add_item(self, item: LibraryItem) -> None: ...

    def borrow_item(self, member_id: str, item_id: str) -> None: ...
