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

## Repository Structure

```
python/
├── roadmap/
│   └── phase-1/
│       └── python-fluency/
│           ├── topics/            # concept write-ups + exercises, one file per topic
│           │   └── OOPS/          # object-oriented programming, one file per concept
│           ├── exercise/          # focused drills (comprehensions)
│           └── facts/             # short, single-concept deep dives
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

## Reference

Each entry below documents a single file: what it covers, the concepts it introduces, and a representative example. File paths are relative to `roadmap/phase-1/python-fluency/`.

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
