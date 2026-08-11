# python

This repo is a Python learning workspace. It is organized by topic so you can quickly see what each file teaches without opening every file.

## What I am learning

- Python basics and first programs
- Variable assignment and arithmetic
- Core data types: int, float, str, None, bool, list, tuple, set, dict, complex
- List operations: concatenation, slicing, nested lists, append, extend, insert, remove, pop, reverse, sort
- List comprehension: concise list creation from iterables with optional filtering and conditional expressions
- Tuple properties: immutability, creation syntax, indexing, nested mutable contents
- Set behavior: uniqueness, unordered storage, membership, empty set creation
- Strings: quotes, escaping, concatenation, multiline strings, indexing, slicing, negative indices
- Dictionaries: key-value data, nested dictionaries, access, get method, default values
- Functions: defining reusable code, passing arguments, returning values
- User input: reading keyboard input with `input()` and using it in programs
- Conditional statements: if-elif-else and match-case for decision-making and flow control
- Loops: while loops and for loops for iterative processing and pattern generation
- Loop control: continue and break statements for controlling loop flow
- Object-oriented programming: classes, objects, methods, the `self` parameter, constructors, class methods, and static methods

## Topics and file summaries

### Variables

- `basics/variables/index.py`
  - Prints the first Python program
  - Demonstrates variable assignment and storing values
  - Shows arithmetic with variables

### Data types overview

- `basics/datatypes/index.py`
  - Lists the main Python data types
  - Demonstrates examples for `int`, `float`, `str`, `None`, `bool`, `list`, `tuple`, `set`, `dict`, and `complex`
  - Shows how booleans convert to integers (`True` → `1`, `False` → `0`)

#### Data structure comparison

| Operation / Type             | list                       | tuple     | set          | dict              |
| ---------------------------- | -------------------------- | --------- | ------------ | ----------------- |
| Access by index `x[i]`       | O(1)                       | O(1)      | — (no index) | O(1) by _key_     |
| Search / membership `v in x` | O(n)                       | O(n)      | O(1) avg     | O(1) avg (by key) |
| Insert / add                 | O(1) append end · O(n) mid | immutable | O(1) avg     | O(1) avg          |
| Delete                       | O(1) end · O(n) mid/value  | immutable | O(1) avg     | O(1) avg          |
| Ordered?                     | yes                        | yes       | no           | yes (insertion)   |
| Duplicates?                  | yes                        | yes       | no           | keys unique       |
| Mutable?                     | yes                        | no        | yes          | yes               |

### Lists

- `basics/datatypes/list.py`
  - Defines lists and shows list creation
  - Combines lists with `+`
  - Accesses list items with indexing and slices
  - Works with nested lists
  - Adds items with `append`, `extend`, and `insert`
  - Uses `count`, `index`, `pop`, `remove`, and `del`
  - Reverses and sorts lists

- `basics/datatypes/listComprehension.py`
  - Introduces list comprehension syntax for creating lists from iterables
  - Demonstrates filtering values with `if` clauses
  - Shows how to include conditional expressions inside a comprehension
  - Compares list comprehension to equivalent loop-based code

### Tuples

- `basics/datatypes/tuple.py`
  - Explains tuple immutability versus lists
  - Shows tuple creation with and without parentheses
  - Covers single-item tuple syntax
  - Demonstrates indexing and nested list mutation inside a tuple
  - Uses `len` and `count`

### Sets

- `basics/datatypes/set.py`
  - Explains sets as unordered, unique collections
  - Shows duplicate removal and membership checks
  - Covers set length and empty set creation using `set()`
  - Notes a TODO: practice set intersections

### Strings

- `basics/datatypes/string.py`
  - Demonstrates string creation with quotes
  - Shows printing strings multiple times using `*`
  - Covers quote escaping and file path escaping
  - Shows string concatenation and multiline strings with `"""`
  - Demonstrates indexing, slicing, negative indices, and `len`

### Dictionaries

- `basics/datatypes/dict.py`
  - Introduces dictionaries as key-value collections
  - Demonstrates nested dictionaries for student data
  - Shows access by key and nested key lookup
  - Uses `get` with default values
  - Shows `len` on dictionaries

### Functions

- `basics/funtions/index.py`
  - Explains what functions are and when to use them
  - Shows a simple function with no parameters
  - Demonstrates passing arguments to a function
  - Returns values from a function using `return`
  - Prints and stores the returned result

### User input

- `basics/userInput/index.py`
  - Reads input from the user with `input()`
  - Asks for a student's name and roll number
  - Stores user input in a dictionary
  - Prints the collected student data in a formatted output

### Conditional statements

- `basics/conditionalStatments/index.py`
  - Demonstrates if-else statements for basic conditions
  - Shows how to check if a number is even or odd
  - Covers if-elif-else for multiple conditions and input validation
  - Validates user input before processing
  - Includes debugging tips using VS Code breakpoints

- `basics/conditionalStatments/match.py`
  - Introduces match-case statements (Python 3.10+) as an alternative to if-elif-else
  - Demonstrates a simple arithmetic calculator using match-case
  - Shows pattern matching with different cases
  - Uses the default case (`_`) to handle incorrect input

### Operators

- `basics/operators/arithmaticOperators.py`
  - Demonstrates arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
  - Shows shorthand assignment forms like `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

- `basics/operators/assignmentOperator.py`
  - Shows the assignment operator `=` and tuple-style multiple assignment (`x, y, z = 1, 2, 3`)

- `basics/operators/comparisonOperators.py`
  - Covers comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - Demonstrates boolean results from comparisons

- `basics/operators/logicalOperators.py`
  - Explains logical operators `and`, `or`, `not` and how to combine conditional expressions

### Loops

- `basics/loop/while.py`
  - Demonstrates while loops for iterative processing
  - Creates a triangle pattern using nested while loops
  - Shows how to control loop iterations and nested loop logic
  - Uses loop counters and conditional logic to build ASCII art patterns

- `basics/loop/for.py`
  - Demonstrates for loops for iterating over data structures
  - Shows how to iterate through a list of dictionaries
  - Accesses nested data within each dictionary during iteration
  - Prints structured data from collections using for loops
  - Uses `continue` statement to skip iterations based on conditions
  - Uses `break` statement to exit loops when specific conditions are met

### Object-oriented programming

- `oop/class.py`
  - Introduces the concept of classes and objects in Python
  - Demonstrates how to create a class and instantiate an object
  - Explains why methods need the `self` parameter
  - Shows how to use the `__init__` constructor to initialize object attributes dynamically

- `oop/classMethod.py`
  - Introduces class variables and class methods
  - Demonstrates counting instances using a `@classmethod`
  - Shows how class methods access shared class state via `cls`

- `oop/staticMethod.py`
  - Introduces static methods as utility functions inside a class
  - Demonstrates a `@staticmethod` that checks if a student passed without accessing instance state
  - Shows how static methods are called from the class directly

## Roadmap

Roadmap to become an awesome python developer:

- Phase 1
  - Python Fluency
    - Topics covered so far:
      - List:
        - Creating a list: Lists store multiple values in order.
          ```python
          fruits = ["Apple", "Banana", "Orange"]
          print(fruits)
          ```
        - Accessing items with index and slicing: You can read values using indexes or slices.
          ```python
          print(fruits[0])
          print(fruits[1:3])
          ```
        - Updating and inserting values: You can replace existing values or add new ones.
          ```python
          fruits[2] = "Mango"
          fruits.insert(1, "Kiwi")
          print(fruits)
          ```
        - Removing items: Use remove, pop, or delete to remove values.
          ```python
          fruits.remove("Banana")
          fruits.pop(0)
          print(fruits)
          ```
        - List comprehension: A shorter way to create a new list from an existing one.
          ```python
          fruits_without_banana = [fruit for fruit in fruits if fruit != "Banana"]
          print(fruits_without_banana)
          ```
        - Sorting and copying: You can sort a list and make a safe copy.
          ```python
          fruits.sort()
          copy_fruits = fruits.copy()
          print(copy_fruits)
          ```

      - Tuple:
        - Creating a tuple: Tuples are ordered and immutable.
          ```python
          student_data = ("Rahul", 20, 1)
          print(student_data)
          ```
        - Accessing values: You can read tuple values using indexes and slices.
          ```python
          print(student_data[0])
          print(student_data[:2])
          ```
        - Checking membership: You can test whether an item exists in the tuple.
          ```python
          print("Rahul" in student_data)
          ```
        - Single-item tuple: Add a comma so Python treats it as a tuple.
          ```python
          data = (1,)
          print(type(data))
          ```
        - Updating through conversion: Convert to a list to change the values, then convert back to a tuple.
          ```python
          student_data_list = list(student_data)
          student_data_list[2] = 12
          student_data = tuple(student_data_list)
          print(student_data)
          ```
        - Unpacking and joining: You can unpack values into variables and join tuples together.
          ```python
          name, age, roll_no = student_data
          combined = student_data + (3,)
          print(name, age, roll_no)
          print(combined)
          ```

      - Set:
        - Creating a set: Sets store unique values and ignore duplicates.
          ```python
          data = {1, 2, 3, 3}
          print(data)
          ```
        - Checking membership: Use in to see whether a value exists.
          ```python
          print(1 in data)
          ```
        - Adding values: Use add or update to insert new items.
          ```python
          data.add(4)
          data.update([5, 6])
          print(data)
          ```
        - Removing values: Use remove, discard, clear, or delete to remove items.
          ```python
          data.remove(1)
          data.discard(2)
          print(data)
          ```
        - Union and intersection: Combine sets or find the common values.
          ```python
          set1 = {1, 2, 3}
          set2 = {3, 4}
          print(set1 | set2)
          print(set1 & set2)
          ```
        - Difference and symmetric difference: Find what is unique or different between sets.
          ```python
          print(set1 - set2)
          print(set1 ^ set2)
          ```

      - Dictionary:
        - Dictionary basics: Dictionaries store ordered, changeable data as key-value pairs.
          ```python
          student_data = {"name": "student1", "age": "20", "rollNo": "12"}
          print(student_data)
          ```
        - Checking dictionary length: Use `len()` to count how many entries are present.
          ```python
          print(len(student_data))
          ```
        - Accessing items by key: Look up values with square brackets.
          ```python
          print(student_data["name"])
          ```
        - Using `get()` for safe access: `get()` returns `None` or a default value if the key is missing.
          ```python
          print(student_data.get("name"))
          print(student_data.get("address", "not found"))
          ```
        - Viewing keys, values, and items: `keys()`, `values()`, and `items()` return live views of the dictionary.
          ```python
          keys = student_data.keys()
          values = student_data.values()
          print(keys)
          print(values)
          ```
        - Checking membership: Use `in` to test whether a key exists.
          ```python
          print("name" in student_data)
          ```
        - Changing values: Assign a new value to an existing key.
          ```python
          student_data["rollNo"] = "20"
          print(student_data)
          ```
        - Updating dictionaries: Use `update()` to change or add multiple entries.
          ```python
          student_data.update({"rollNo": "500", "topTalent": "Yes"})
          print(student_data)
          ```
        - Adding items: Assign a value to a new key to add it.
          ```python
          student_data["hasIdCard"] = True
          print(student_data)
          ```
        - Removing items: Use `pop()`, `popitem()`, `del`, or `clear()` to remove entries.
          ```python
          student_data.pop("topTalent")
          student_data.popitem()
          del student_data["rollNo"]
          student_data.clear()
          print(student_data)
          ```
        - Iterating dictionaries: Loop over keys, values, or key-value pairs with `items()`.
          ```python
          for key, value in student_data.items():
              print(key, "=", value)
          ```
        - Copying dictionaries: Use `copy()` or `dict()` to make a separate copy.
          ```python
          copied = student_data.copy()
          copied2 = dict(student_data)
          print(copied)
          print(copied2)
          ```
        - Nested dictionaries: Store structured data and loop through nested entries.
          ```python
          school = {
              "students": {"data": [{"name": "Xicor"}, {"name": "Vegeta"}]},
              "teachers": {"data": [{"name": "Master Roshi"}, {"name": "Korin"}]}
          }
          for role, group in school.items():
              print(role)
              for person in group.get("data", []):
                  print(person.get("name", ""))
          ```

      - Data structure comparison:
        | Operation / Type | list | tuple | set | dict |
        |---|---|---|---|---|
        | Access by index `x[i]` | O(1) | O(1) | — (no index) | O(1) by _key_ |
        | Search / membership `v in x` | O(n) | O(n) | O(1) avg | O(1) avg (by key) |
        | Insert / add | O(1) append end · O(n) mid | immutable | O(1) avg | O(1) avg |
        | Delete | O(1) end · O(n) mid/value | immutable | O(1) avg | O(1) avg |
        | Ordered? | yes | yes | no | yes (insertion) |
        | Duplicates? | yes | yes | no | keys unique |
        | Mutable? | yes | no | yes | yes |
