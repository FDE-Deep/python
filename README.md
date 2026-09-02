# Python Fluency Lab

A structured, self-paced curriculum for building Python fluency — from core data types through object-oriented design. The repository is organized as a progressive roadmap: each topic lives in its own file, pairs a short concept summary with runnable exercises, and builds on the topics before it.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Roadmap](#roadmap)
- [Reference](#reference)
  - [Data Types](#data-types)
  - [Comprehensions & Generators](#comprehensions--generators)
  - [Functions](#functions)
  - [Control Flow](#control-flow)
  - [Object-Oriented Programming](#object-oriented-programming)
  - [Exception Handling](#exception-handling)
  - [Context Managers](#context-managers)
  - [Type Hints](#type-hints)
  - [Interview Practice](#interview-practice)
  - [Decorators](#decorators)
  - [Itertools](#itertools)
  - [Pytest](#pytest)
  - [Foundations](#foundations)
- [Data Structure Complexity Cheatsheet](#data-structure-complexity-cheatsheet)
- [Projects](#projects)

## Overview

This repository documents a hands-on path to Python fluency. Every file under [`roadmap/`](roadmap/) pairs a short explanation of a concept with the exercises used to practice it, including the author's own predictions, mistakes, and follow-up questions — kept intact as a record of the learning process rather than cleaned into a textbook.

Topics build in roughly this order:

1. **Data types** — lists, tuples, sets, dictionaries, strings
2. **Comprehensions & generators** — concise, lazy data transformation
3. **Functions** — variadic arguments, closures, common pitfalls
4. **Control flow** — conditionals, loops, iteration protocol
5. **Object-oriented programming** — classes through abstract base classes
6. **Exception handling** — try/except/else/finally, raising and defining custom exceptions
7. **Context managers** — `__enter__`/`__exit__`, guaranteed cleanup, the `@contextmanager` generator form
8. **Type hints** — annotating variables, containers, classes, and functions; checked by Pylance/mypy, not the interpreter
9. **Interview practice** — mixed-topic recall drills revisiting gaps found across all of the above
10. **Decorators** *(new track: Python Advanced + API)* — closures wrapping functions, `@wraps`, and real-world patterns like timing and retry
11. **Itertools** — lazy iterator-building tools: `islice`, `chain`, `groupby`, `batched`
12. **Pytest** — testing real code (not toy examples) with plain asserts, `@parametrize`, `pytest.raises`, fixtures, and `tmp_path` for file I/O

## Repository Structure

```
python/
├── roadmap/
│   └── phase-1/
│       └── python-fluency/
│           ├── topics/            # concept write-ups + exercises, one file per topic
│           │   └── OOPS/          # object-oriented programming, one file per concept
│           ├── exercise/          # focused drills (comprehensions)
│           ├── facts/             # short, single-concept deep dives
│           └── interview-practice/ # mixed-topic recall drills, one file revisiting gaps across all topics
│       └── python-advanced-plus-api/
│           ├── topics/            # concept write-ups + exercises, one file per topic
│           │   └── itertools/     # one file per itertools function (islice, chain, groupBy, batched)
│           └── pytest-practice/   # tests against real code from earlier topics, not toy examples
├── basics/                        # earliest exercises (pre-roadmap), superseded by roadmap/
├── oop/                           # earliest OOP exercises, superseded by roadmap/topics/OOPS/
└── projects/                      # applied, standalone projects
    └── word-analyzer/             # separate git repository — see its own README
```

## Getting Started

Every file in this repository is a standalone, runnable Python script — there are no cross-file imports or external dependencies.

**Requirements:** Python 3.10+ (the `match`/`case` and dataclass examples rely on modern syntax).

```bash
python roadmap/phase-1/python-fluency/topics/OOPS/dataClasses.py
```

Read the file top-to-bottom: each script opens with a concept explanation in comments, followed by one or more exercises with the working solution and, frequently, the expected output written inline as a comment.

## Roadmap

### Phase 1 — Python Fluency

| Track | Status | Location |
|---|---|---|
| Core data types (list, tuple, set, dict) | ✅ Complete | `topics/` |
| Comprehensions (list, dict, set, generator) | ✅ Complete | `exercise/`, `topics/generators.py` |
| Iterables & iterators | ✅ Complete | `facts/forLoop.py` |
| Functions (`*args`, `**kwargs`, closures) | ✅ Complete | `topics/functions.py` |
| OOP: classes, dunder methods, composition | ✅ Complete | `topics/OOPS/` |
| OOP: data classes, inheritance, MRO | ✅ Complete | `topics/OOPS/` |
| OOP: polymorphism, duck typing | ✅ Complete | `topics/OOPS/` |
| OOP: class methods, factory patterns | ✅ Complete | `topics/OOPS/` |
| OOP: encapsulation, properties | ✅ Complete | `topics/OOPS/` |
| OOP: abstract base classes | ✅ Complete | `topics/OOPS/` |
| Exception handling: try/except/else/finally, custom exceptions | ✅ Complete | `topics/exception-handling/` |
| Context managers: `__enter__`/`__exit__`, `@contextmanager` | ✅ Complete | `topics/context-manager/` |
| Type hints: variables, containers, classes, functions | ✅ Complete | `topics/type-hint/` |
| Interview practice: mixed-topic recall drills | ✅ Complete | `interview-practice/` |

### Phase 1 — Python Advanced + API

| Track | Status | Location |
|---|---|---|
| Decorators: closures, `@wraps`, timing/retry patterns | 🚧 In progress | `python-advanced-plus-api/topics/decorators/` |
| Itertools: `islice`, `chain`, `groupby`, `batched` | ✅ Complete | `python-advanced-plus-api/topics/itertools/` |
| Pytest: parametrize, `pytest.raises`, fixtures, `tmp_path` | ✅ Complete | `python-advanced-plus-api/pytest-practice/` |

## Reference

Each entry below documents a single file: what it covers, the concepts it introduces, and a representative example. File paths are relative to `roadmap/phase-1/python-fluency/`, except where noted with a full path.

### Data Types

#### Lists

`topics/list.py`

Covers list creation, indexing and slicing (including negative indices), nested lists, mutation (`append`, `extend`, `insert`, `remove`, `pop`, `del`, `clear`), sorting (default, `reverse=True`, and custom `key` functions), and the difference between reference copies (`copy_fruits = fruits`) and real copies (`.copy()`, `list(...)`, slicing).

```python
fruits = ["Apple", "Banana", "Orange"]
fruits.sort(key=lambda item: "Ba" in item)

fruits_without_banana = [fruit for fruit in fruits if fruit != "Banana"]
```

#### Tuples

`topics/tuple.py`

Covers tuple immutability, creation syntax (including the single-item tuple comma trap `(1,)` vs `(1)`), indexing/slicing, the "convert to list, mutate, convert back" workaround for updates, concatenation with `+`, and unpacking — including star-unpacking to collect the remainder (`name, *rest = data`).

```python
student_data = ("Rahul", 20, 1)
name, *rest, roll_no = student_data   # name = "Rahul", rest = [20], roll_no = 1
```

#### Sets

`topics/set.py`

Covers uniqueness and unordered storage, membership testing, the identity between `True`/`1` and `False`/`0` as duplicate values, mutation (`add`, `update`, `remove`, `discard`, `clear`), and the full set-algebra toolkit: union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`), and their in-place `*_update` variants.

```python
set1 = {1, 2, 3, 7, 8}
set2 = {1, 2, 4, 5}
set1 ^ set2   # {3, 4, 5, 7, 8} — symmetric difference
```

#### Dictionaries

`topics/dictonaries.py`

Covers key-value access (`[]` vs `.get()` with defaults), the live-view behavior of `.keys()`/`.values()`/`.items()`, membership testing, updating and adding entries, removal (`pop`, `popitem`, `del`, `clear`), iteration patterns, copying (`.copy()` vs `dict()`), and nested dictionary traversal.

```python
for role, group in school.items():
    for person in group.get("data", []):
        print(person.get("name"))
```

### Comprehensions & Generators

#### List Comprehension

`exercise/listComprehension.py`

Fourteen drills covering the `[expr for item in iterable if condition]` form: mapping (squaring, unit conversion), filtering, conditional expressions in the mapped position (`"even" if ... else "odd"`), nested/flattened comprehensions over matrices and nested dictionaries, and unpacking tuples inside the loop clause (`for (name, score) in pairs`).

#### Dict Comprehension

`exercise/dictComprehension.py`

Ten drills covering `{key_expr: value_expr for item in iterable}`: building dicts from a single iterable, zipping two parallel lists (`dict(zip(keys, values))`), filtering existing dicts by value, reversing key/value pairs, and combining `enumerate()` with dict comprehensions to map items to their position.

#### Set Comprehension

`exercise/setComprehension.py`

Five drills covering `{expr for item in iterable}`, emphasizing how comprehensions naturally deduplicate — squaring numbers with repeats, case-folding strings, and labeling values (`"negative"`/`"zero"`/`"positive"`) to see how many distinct labels survive.

#### Generator Expressions

`exercise/generatorComprehension.py`

Ten drills covering `(expr for item in iterable)`: lazy evaluation and single-pass exhaustion (a second `list()` call on a spent generator returns `[]`), consuming with `next()` vs a `for` loop, and feeding generator expressions directly into `sum()` and `max()` without materializing an intermediate list.

```python
gen = (loud(n) for n in [1, 2, 3])
print("made a generator")   # prints before any computation happens
first = next(gen)           # computation happens here, lazily
```

#### Generator Functions

`topics/generators.py`

Covers `yield` and the pause/resume model: calling a generator function returns a generator object without running the body; each `next()` call resumes execution until the next `yield`, and calling `next()` after exhaustion raises `StopIteration`.

```python
def first_n(n):
    while n > 0:
        yield n
        n -= 1
```

#### Iterables vs Iterators

`facts/forLoop.py`

Explains what actually happens in a `for` loop: an **iterable** (list, dict, string, range, …) is anything you can loop over; an **iterator**, produced by `iter()`, is the stateful worker that yields one item at a time via `next()` and raises `StopIteration` once exhausted. Iterators are single-use — a second `iter()` call is required to loop again.

### Functions

`topics/functions.py`

#### Variadic Arguments (`*args`, `**kwargs`)

`*args` collects positional arguments into a tuple; `**kwargs` collects keyword arguments into a dict. Covers writing functions with both, mixing them with named parameters (`func(a, b, *args, **kwargs)`), and forwarding arguments through a wrapper function — the exact pattern a decorator relies on.

```python
def call_it(func, *args, **kwargs):
    return func(*args, **kwargs)
```

#### Closures & Decorators

Builds a minimal logging decorator (`make_log`) by hand: a function that accepts another function, defines an inner `wrapper(*args, **kwargs)` that calls it, and returns the wrapper — demonstrating how a closure retains access to the wrapped function across calls.

#### Mutable Default Arguments

Reproduces the classic mutable-default-argument bug (`def createList(item, items=[])`, where `items` is shared and accumulates across calls) and the fix: default to `None` and create a fresh list inside the function body.

```python
def createList(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Control Flow

Introduced in the earliest `basics/` exercises and exercised throughout the roadmap: `if`/`elif`/`else` and `match`/`case` for branching, `while`/`for` loops for iteration, and `continue`/`break` for flow control. See [Foundations](#foundations) for the source files.

### Object-Oriented Programming

All files below live in `topics/OOPS/`.

#### Classes & Objects

`OOPS/basics.py`

The foundation: a class is a blueprint for an object's properties and behavior. Covers `__init__`, instance attributes, calling a method two equivalent ways (`Rectangle.area(rectangle)` vs `rectangle.area()`), default arguments in constructors, and a first look at composition — a `Car` that holds an `Engine` instance and delegates to it.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

#### Dunder Methods

`OOPS/dunderMethod.py`

"Dunder" (double underscore) methods let a class plug into built-in syntax and functions. Covers `__repr__` (drives `print(obj)`), `__eq__` (value equality instead of the default reference equality), `__add__` (makes `+` work between instances), and `__len__` (makes `len(obj)` work).

```python
class Money:
    def __repr__(self):
        return f"${self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)
```

#### Data Classes

`OOPS/dataClasses.py`

The `@dataclass` decorator auto-generates `__init__`, `__repr__`, and `__eq__` from type-annotated fields, eliminating boilerplate for classes that are primarily data. Covers field defaults, and the rule of thumb: dataclasses handle structural boilerplate, but behavioral methods (`area()`, `__add__`) still need to be written by hand.

```python
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float = 0.0
```

#### Inheritance & MRO

`OOPS/inheritance.py`

Covers method overriding, `super().__init__()` for extending a parent constructor, inheritance with dataclasses (fields combine automatically, no `super()` call needed), and the inheritance-vs-composition decision rule (**is-a** → inheritance, **has-a** → composition).

The second half works through multiple inheritance and **MRO** (Method Resolution Order) — Python's C3-linearization rule for resolving which parent's method wins, including the classic diamond problem:

```python
class A:
    def get(self): return "A"

class B(A):
    def get(self): return "B"

class C(A):
    def get(self): return "C"

class D(B, C):
    pass

D().get()      # "B" — child first, then left to right
D.__mro__      # D -> B -> C -> A -> object
```

Also covers mixins — small, focused classes (like `GreetMixin`) designed to be combined via multiple inheritance to add one capability at a time.

#### Composition

`OOPS/composition.py`

"Has-a" relationships: a `Library` holds a list of `Book` objects, and a `Computer` composes a `CPU` and `RAM` into a single object that reaches into its parts (`self.cpu.cores`). Also covers the mutable-default-argument trap as it applies to dataclass fields, solved with `field(default_factory=list)`.

```python
@dataclass
class Library:
    listOfBooks: list[Book] = field(default_factory=list)
```

#### Polymorphism & Duck Typing

`OOPS/polymorhphism.py`

**Polymorphism**: unrelated classes (`Circle`, `Square`, `Triangle`) each implement `area()` with their own formula; calling `.area()` in a loop over mixed instances produces the correct result per type without any type-checking.

**Duck typing**: Python doesn't check inheritance or type — only whether the object has the method being called. A single `describe_all(items)` function works on any object with a `.describe()` method, regardless of its class hierarchy. Operator overloading (`__add__`) is framed as duck typing in action: `Money(50) + Money(30)` and `Point(2, 3) + Point(4, 5)` both work through the same `+` operator on unrelated classes.

#### Class Methods & Factory Patterns

`OOPS/classMethods.py`

`@classmethod` receives the class itself (`cls`) rather than an instance, and can be called on the class or an instance. Two main uses are covered:

- **Alternative constructors (factories)** — `from_dict()`, `from_list()`, `from_csv_line()`, and `square()` build instances from external data shapes (API responses, CSV lines) or convenience shortcuts, including light validation/transformation on the way in (stripping whitespace, casting types).
- **Class-level state** — a class attribute (`count = 0`) tracked and read via `@classmethod get_count(cls)`, incremented once per instantiation in `__init__`.

```python
@classmethod
def from_dict(cls, data):
    return cls(data["name"].strip(), float(data["price"]))
```

#### Encapsulation

`OOPS/encapsulation.py`

Covers Python's two encapsulation tools, neither of which is enforced by the interpreter:

- **Naming convention** (`_field`) — signals "don't modify this directly" without actually preventing it.
- **`@property`** — exposes a method as attribute-style access (`obj.area`, no parentheses). A getter with no setter makes a value read-only; adding a `@x.setter` allows controlled, validated writes — for example, rejecting a `Temperature` below absolute zero or a `BankAccount` balance below zero.

```python
@property
def balance(self):
    return self.balance_field

@balance.setter
def balance(self, new_value):
    if new_value < 0:
        raise ValueError("Balance cannot be less than 0")
    self.balance_field = new_value
```

#### Abstract Base Classes

`OOPS/abstractClass.py`

`ABC` and `@abstractmethod` (from the `abc` module) turn a class into a contract: subclasses **must** implement every abstract method, or instantiation fails. Contrasted directly with duck typing — abstraction *enforces* the interface at instantiation time, duck typing merely *hopes* the method exists at call time.

Covers a base `Shape(ABC)` with abstract `area()`/`perimeter()`, mixing enforced (abstract) methods with shared concrete methods (`describe()`, implemented once on the base class and inherited for free), and why code written against the abstraction (`print_all_areas(shapes)`) is safe to write — every `Shape` is guaranteed to have `area()`.

```python
class Shape(ABC):
    @abstractmethod
    def area(self): ...

    def describe(self):
        return f"Area: {self.area()}"   # concrete method, shared by all subclasses
```

### Exception Handling

`topics/exception-handling/index.py`

Covers the `try`/`except`/`else`/`finally` machinery, catching built-in exceptions by type, raising custom exceptions, and the ordering rules that govern which block runs when.

- **Basic `try`/`except`** — catching `ZeroDivisionError` and `KeyError`, returning a fallback instead of crashing.
- **Multiple `except` blocks** — matching different exception types (`ValueError` vs `ZeroDivisionError`) to different messages; the first matching block wins.
- **`raise`** — raising a built-in exception (`ValueError`) with a custom message from inside a validation function, then catching it at the call site with `except ValueError as e`.
- **`finally`** — always runs, whether the `try` succeeded, raised, or returned — including printing after a `return` from inside the `try`.
- **`else`** — runs only if the `try` block completes with no exception *and* reaches its own end. A `return` inside `try` exits the function immediately and skips `else` entirely, since `else` fires on falling off the end of `try`, not on success as such.
- **Custom exceptions** — defining `class NegativeNumberError(Exception): pass` and raising/catching it exactly like a built-in.
- **Combining it all** — a `withdraw(balance, amount)` example with two custom-ish exception types (`InsufficientFundsError`, `ValueError`) caught in separate `except` clauses, with a shared `else` for the success path.

```python
def parse_number(text):
    try:
        value = int(text)
    except ValueError:
        return "not a number"
    else:
        return f"successfully parsed {value}"   # only reached if try raised nothing
```

```python
class NegativeNumberError(Exception):
    pass

def sqrt_check(n):
    if n < 0:
        raise NegativeNumberError("n must be greater than zero")
    return n ** 0.5
```

### Context Managers

`topics/context-manager/index.py`

Covers the `with` statement's protocol — `__enter__`/`__exit__` on a class, then the same thing written as a generator with `@contextmanager` — and the property that makes context managers useful: cleanup runs even when the block raises.

- **The enter → block → exit sequence** — a class with `__enter__` (prints, returns `self`) and `__exit__` (prints); `with Greeter() as greet:` traces the order setup and teardown fire relative to the block body.
- **`as` binds whatever `__enter__` returns** — `__enter__` can return anything (`self`, a string, a connection object); `with X() as v:` just captures that return value.
- **Cleanup runs even on error** — `__exit__` still fires if the block raises; the exception only propagates *after* `__exit__` returns (unless `__exit__` itself returns a truthy value to suppress it). Same guarantee as `finally`.
- **A practical example (`Timer`)** — `__enter__` records a start time, `__exit__` computes and prints elapsed time; a real, reusable measurement tool built from the protocol.
- **`@contextmanager`** — from `contextlib`, turns a generator function into a context manager without writing a class: code before `yield` is `__enter__`, the yielded value is what `as` binds, code after `yield` is `__exit__`.
- **Guaranteed cleanup in the generator form** — a bare `yield` skips the post-`yield` cleanup entirely if the block raises, since an unhandled exception propagates out of the generator at the `yield` point; wrapping the `yield` in `try`/`finally` is what makes cleanup run unconditionally, mirroring `__exit__`'s guarantee in the class form.

```python
class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Elapsed Time - {time.time() - self.start} seconds")

with Timer():
    total = sum(range(1_000_000))
```

```python
from contextlib import contextmanager

@contextmanager
def guard():
    print("acquired")
    try:
        yield
    finally:
        print("released")   # runs even if the with-block raises

with guard():
    raise ValueError("boom")   # "released" still prints before this propagates
```

### Type Hints

`topics/type-hint/index.py`

Covers Python's optional type annotation syntax — `name: Type` for variables/parameters, `-> Type` for return values — and the key distinction that hints are a **static-analysis aid, not a runtime check**: Pylance/mypy flag a mismatched call in the editor, but the code still executes normally if run.

- **Basic types** — `stringType: str`, `intType: int`, `booleanType: bool`, `decimalType: float`.
- **Container types** — generic subscripting: `list[str]`, `list[int]`, `dict[str, int]`, `set[int]`.
- **Class types** — a variable annotated with a custom class: `b: Book = Book()`.
- **Function signatures** — parameter and return annotations together: `def add(a: int, b: int) -> int`.
- **Union types** — a parameter accepting more than one type via `|`: `def add1(a: int | str, b: int | str) -> int`.
- **Annotate = attach a hint** — "annotate `total(nums)`" just means writing out its `: Type`/`-> Type` syntax, same mechanics as the examples above, for a list-of-ints parameter, a `dict[str, float]` variable, and a function returning `list[Book]`.
- **Annotating existing methods** — retrofitting `Library.add_item`/`borrow_item` from the OOP topics with full parameter and return types, including the judgment call of picking one consistent id type (`str`) after the project had used both strings and ints for ids inconsistently.

```python
def find_item(name: str, items: dict[str, int]) -> int | None:
    return items.get(name)

class Library:
    def add_item(self, item: LibraryItem) -> None: ...
    def borrow_item(self, member_id: str, item_id: str) -> None: ...
```

### Interview Practice

`interview-practice/index.py`

A single file of mixed-topic recall drills, written after the fact to close specific gaps surfaced by an earlier interview-style Q&A — each drill traces execution by hand before running it, rather than just reading the answer. Not a new topic; it revisits closures, inheritance, context managers, generators, comprehensions, properties, custom exceptions, and type hints from the sections above, plus ten general prediction questions.

- **Closure late binding** — a loop appending `lambda: i` to a list; all three calls return `2`, because the lambdas share one cell holding `i` by reference, read only when called (after the loop has finished), not a fresh `i` per iteration — the same "shared reference, not a snapshot" trap as a mutable default argument.
- **`super()` gap** — `B.__init__` calls `super().__init__(x)` and gets `self.x`; `C.__init__` skips it, so `c.x` raises `AttributeError` — the parent's `__init__` (and whatever it sets) only runs if a subclass's `__init__` explicitly calls it.
- **Context-manager exception suppression** — `__exit__` returning `None` (the implicit default, no `return` statement) is falsy, so the exception is **not** suppressed: `"cleanup"` prints, then the exception propagates and `"after"` never prints. Only an explicit truthy `return` from `__exit__` swallows it.
- **Generator resume points** — tracing exactly which `print`s run for a given number of `next()` calls, precise to the paused line: a generator resumes right after the last `yield` and runs up to (and including) the next one.
- **MRO recall** — `class Child(Left, Right)` where both override a `Base` method: `c.greet()` returns `"Left"`, and `Child.__mro__` is `Child → Left → Right → Base → object` (child first, parents left-to-right, common base last).
- **`@property` vs direct attribute access** — `a.balance = 50` goes through the setter (validated); `a._balance = -999` bypasses it by writing the backing field directly — Python's privacy is convention, not enforcement, so a property doesn't protect against reaching past it.
- **Custom exception + `except` order** — `except TooSmallError` before `except Exception` is what lets the specific message print; swapping the order makes the broader `Exception` clause catch it first and the specific handler never runs, since Python tries `except` clauses top-to-bottom and stops at the first match.
- **`@contextmanager` without `try`/`finally`** — confirms the same gotcha from the [Context Managers](#context-managers) topic: a bare `yield` (no `try`/`finally`) means an exception in the `with` body skips the post-`yield` cleanup entirely instead of guaranteeing it.
- **Type hints don't stop runtime errors** — `process(data: list[int])` called with a string still runs and crashes with a `TypeError` inside the loop; Pylance/mypy would flag the call as a static error, but nothing stops it at runtime — hints are advisory, not enforced.
- **`dict.get` vs `[]`** — iterating a dict yields keys; `.items()` yields key/value pairs; `.get("z", 0)` returns the default for a missing key, while `data["z"]` raises `KeyError` — the same lookup, two different failure behaviors.

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print(funcs[0]())  # 2 — all three share the same `i`, read at call time, after the loop ends
```

### Decorators

`roadmap/phase-1/python-advanced-plus-api/topics/decorators/index.py`

Opens a new track (Python Advanced + API) with `@decorator` syntax: a decorator is a closure that wraps a function and returns the wrapped version, and `@func` above a `def` is sugar for `thing = decorator(thing)`.

- **The basic mechanism** — `my_decorator(func)` defines an inner `wrapper(*args, **kwargs)` that calls `func`, adding behavior before/after, and returns `wrapper`; applying it (`add = my_decorator(add)` or `@my_decorator`) rebinds the name to the wrapper, not the original function.
- **The lost-identity gotcha** — after decorating, `multiply.__name__` prints `"wrapper"`, not `"multiply"` — decorating reassigns the name to the wrapper object, which carries its own `__name__`/`__doc__`; the original function is only reachable through the wrapper's closure, not the outer name.
- **`functools.wraps`** — `@wraps(func)` on the inner `wrapper` copies `func`'s metadata (`__name__`, `__doc__`, etc.) onto the wrapper, fixing the gotcha above so `subtract.__name__` correctly reports `"subtract"`.
- **A decorator with behavior** (`announce`) — prints before/after messages using `func.__name__` for context, then returns the result unchanged — the side-effect-only decorator pattern.
- **A decorator that changes the result** (`double_result`) — calls the function and returns a transformed value (`result * 2`) instead of the original — decorators aren't limited to side effects; they can rewrite what the caller gets back.
- **`@timer`** — records a start time in the wrapper, calls the function, computes elapsed time from the difference, prints it, and still returns the original result — the general "measure around a call" shape, reused from the `Timer` context manager topic but as a decorator instead of a `with` block.
- **`@retry`** *(in progress)* — the next exercise: retry a call up to 3 times, catching and logging each failed attempt, re-raising the last exception only if every attempt fails.

```python
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start}")
        return result
    return wrapper

@timer
def total_sum(n):
    return sum(i for i in range(n))
```

### Itertools

`roadmap/phase-1/python-advanced-plus-api/topics/itertools/`

The `itertools` standard library module — a toolkit of iterator-building functions that stay lazy, processing one item at a time instead of loading a full sequence into memory. Covered across four files, each isolating one tool.

#### `islice`

`topics/itertools/islice.py`

Slices an iterator the way `[:]` slices a list, but without materializing it — the source is a generator, which can't be indexed since it only produces items on `next()`.

- **Why list slicing doesn't work on generators** — a list loads every item into memory up front, so `[:2]` works; a generator only produces a value when pulled, so there's nothing to index into ahead of time.
- **`islice` shares the underlying worker** — `itertools.islice(gen, 1)` doesn't copy `gen`, it wraps it; pulling from the `islice` object advances `gen` itself, so whatever `list(gen)` returns afterward picks up from wherever the slice left off.
- **A `range` is a reusable source, a generator is not** — three separate `islice` calls over the same `range(20)` (`islice(nums, 5)`, `islice(nums, 5, 10)`, `islice(nums, 0, 20, 3)`) don't interfere with each other, because each call re-reads from `range`'s start/stop/step rather than consuming a shared cursor.
- **Chained `islice` calls over one generator do interfere** — three `islice` calls over the same `(x * 10 for x in range(10))` each continue from where the previous one stopped, since a generator (unlike `range`) is a single, stateful worker with no way to "rewind."
- **The practical case: peeking at an infinite stream** — `islice(infinite_counter(), 5)` takes exactly 5 items from a generator that would otherwise loop forever; `islice` stops pulling once its own count is satisfied, so `list()` on the slice terminates even though `list()` on the raw infinite generator never would.

```python
gen = (i**2 for i in myList)
genSlice = itertools.islice(gen, 1)
list(genSlice)   # consumes one item from gen
list(gen)        # continues from where genSlice left off
```

#### `chain`

`topics/itertools/chain.py`

Concatenates multiple iterables into a single lazy stream, pulling from each in turn without building an intermediate combined list.

- **Basic concatenation** — `itertools.chain(l, r)` walks `l` to exhaustion, then `r`, yielding one combined sequence; `chain.from_iterable(l)` does the same for a list-of-iterables, flattening one level.
- **`chain` also shares the underlying worker** — `chain([10, 20], gen)` pulls the two literal values first, then starts drawing from `gen`; whatever `next()` calls chain has already made against `gen` are gone from it — `list(gen)` afterward only returns what's left.
- **Flattening a generator of ranges** — `chain.from_iterable(range(i) for i in range(4))` flattens `range(0), range(1), range(2), range(3)` (`[]`, `[0]`, `[0, 1]`, `[0, 1, 2]`) into a single sequence, `[0, 0, 1, 0, 1, 2]`.

```python
gen = (x for x in range(5))
chained = itertools.chain([10, 20], gen)
next(chained)  # 10 — from the list, gen untouched
next(chained)  # 20 — from the list, gen untouched
next(chained)  # 0  — first pull from gen
list(gen)      # [1, 2, 3, 4] — gen resumes from where chain left it
```

#### `groupby`

`topics/itertools/groupBy.py`

Groups **consecutive** equal items — not all items sharing a key, only runs of adjacent ones — and returns a lazy `(key, group_iterator)` pair per run.

- **Consecutive-only grouping** — unsorted `[1, 1, 2, 2, 3, 1, 1]` produces four groups (`1`, `2`, `3`, `1`), not three; the trailing `1`s form their own group because they aren't adjacent to the earlier `1`s.
- **Sorting first is the fix** — sorting brings equal items next to each other, so the same data reduces to one group per distinct value.
- **Each group is a shared, single-use iterator** — collecting `group` objects into a list *before* consuming them and then reading them afterward returns empty lists for all of them, because `groupby` only advances far enough to detect the next key change, and doing that exhausts the current group's iterator as a side effect before the loop body gets a chance to consume it.
- **Grouping by a key function** — `groupby(words, key=lambda w: w[0])` groups by first letter, after sorting by the same key; without matching sort and group keys, non-adjacent matches split into separate groups exactly like the unsorted-numbers case.
- **Counting per group** — `len(list(group))` gives a per-key count, provided the group is consumed (via `list()`) before moving to the next key.

```python
data = [1, 1, 2, 2, 3, 1, 1]
for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")
# 1 : [1, 1]
# 2 : [2, 2]
# 3 : [3]
# 1 : [1, 1]        <- trailing 1s, not merged with the first group
```

#### `batched`

`topics/itertools/batched.py`

Splits an iterable into fixed-size chunks, lazily — one batch is in memory at a time — with the final batch holding whatever remains, even if that's fewer than the requested size.

- **Partial last batch** — `batched(range(23), 5)` yields four full 5-item batches and a final batch of 3, since 23 doesn't divide evenly by 5.
- **Even division leaves no partial batch** — `batched(range(12), 4)` yields exactly three 4-item batches with nothing left over.
- **Batch size larger than the data** — `batched([1, 2, 3], 10)` yields a single batch containing everything (`(1, 2, 3)`), since there's nothing left to fill a second batch.
- **The real-world shape: batched API calls** — `documents = list(range(100))` batched by 15 and passed to a `@retry`-decorated `send_batch(batch)`; six batches of 15 followed by one of 10, tying `batched` together with the `@retry` decorator pattern from the [Decorators](#decorators) topic.

```python
for batch in itertools.batched(range(23), 5):
    print(batch)
# (0, 1, 2, 3, 4)
# (5, 6, 7, 8, 9)
# (10, 11, 12, 13, 14)
# (15, 16, 17, 18, 19)
# (20, 21, 22)          <- partial last batch
```

### Pytest

`roadmap/phase-1/python-advanced-plus-api/pytest-practice/`

Rather than toy examples, tests real code written for earlier topics (`add`, `set_age`, `Library`, `Item`, lifted straight into `index.py`) — `pytest` and `pytest-cov` installed via `python -m pip install pytest pytest-cov`, coverage run with `python -m pytest --cov=.`.

- **Basic tests + parametrize** — plain `assert add(2, 3) == 5`, then `@pytest.mark.parametrize("a,b,expected", [...])` collapsing several input/output pairs into one test function instead of repeating it per case.
- **Exceptions with `pytest.raises`** — `with pytest.raises(ValueError): set_age(-5)` confirms the bad-input path raises; separate parametrized tests cover the valid-input success path (`set_age(10) == 10`) and multiple invalid ages, keeping "raises" and "returns" assertions apart.
- **A fixture** — `@pytest.fixture def sample_library()` returns a fresh `Library("Sample")`; three tests (`test_Library`, `test_add_item`, `test_fresh_instance_library`) each receive their own instance via the fixture parameter, so mutating `.items` in one test (adding a book) doesn't leak into the next — pytest re-runs the fixture function per test rather than sharing one object.
- **File I/O with `tmp_path`** — `test_save_load_library(tmp_path)` uses pytest's built-in `tmp_path` fixture (a per-test temporary directory) to round-trip `Library.save()`/`Library.load()` through a real JSON file on disk without touching any file the repo tracks, then asserts the reloaded object matches the original (`name`, item count, item name).

```python
@pytest.fixture
def sample_library():
    return Library("Sample")

def test_add_item(sample_library):
    sample_library.add_item(Item("book"))
    assert sample_library.items["book"].name == "book"

def test_save_load_library(tmp_path):
    filepath = f"{tmp_path}/library.json"
    library = Library("Test")
    library.add_item(Item("book"))
    library.save(filepath)
    loaded = Library.load(filepath)
    assert loaded.name == "Test"
```

### Foundations

The earliest exercises, written before the `roadmap/` structure was adopted. Concepts here are superseded by the more detailed treatment above but remain as the original record.

| File | Covers |
|---|---|
| `basics/variables/index.py` | First program, variable assignment, arithmetic |
| `basics/datatypes/index.py` | Overview of `int`, `float`, `str`, `None`, `bool`, `list`, `tuple`, `set`, `dict`, `complex` |
| `basics/datatypes/list.py` | Early list operations |
| `basics/datatypes/listComprehension.py` | Introductory list comprehension |
| `basics/datatypes/tuple.py` | Early tuple operations |
| `basics/datatypes/set.py` | Early set operations |
| `basics/datatypes/string.py` | Quoting, escaping, concatenation, slicing |
| `basics/datatypes/dict.py` | Early dictionary operations |
| `basics/funtions/index.py` | First functions, parameters, `return` |
| `basics/userInput/index.py` | Reading input with `input()` |
| `basics/conditionalStatements/if-elif-else.py` | `if`/`elif`/`else`, input validation |
| `basics/conditionalStatements/match.py` | `match`/`case` (Python 3.10+) |
| `basics/operators/*.py` | Arithmetic, assignment, comparison, and logical operators |
| `basics/loop/while.py` | `while` loops, nested loops, ASCII pattern generation |
| `basics/loop/for.py` | `for` loops, `continue`, `break` |
| `oop/class.py` | First class, `self`, `__init__` |
| `oop/classMethod.py` | Class variables and class methods |
| `oop/staticMethod.py` | `@staticmethod` |

## Data Structure Complexity Cheatsheet

| Operation / Type | `list` | `tuple` | `set` | `dict` |
|---|---|---|---|---|
| Access by index `x[i]` | O(1) | O(1) | — (no index) | O(1) by *key* |
| Search / membership `v in x` | O(n) | O(n) | O(1) avg | O(1) avg (by key) |
| Insert / add | O(1) append end · O(n) mid | immutable | O(1) avg | O(1) avg |
| Delete | O(1) end · O(n) mid/value | immutable | O(1) avg | O(1) avg |
| Ordered? | yes | yes | no | yes (insertion order) |
| Duplicates? | yes | yes | no | keys unique |
| Mutable? | yes | no | yes | yes |

## Projects

### word-analyzer

`projects/word-analyzer/` — a standalone command-line tool (its own git repository) that streams a text file line-by-line via a generator and reports the most frequent words, keeping memory flat regardless of file size. See [`projects/word-analyzer/readme.md`](projects/word-analyzer/readme.md) for setup and usage.
