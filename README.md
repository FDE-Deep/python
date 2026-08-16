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

      - Generator:
        - Introduces generator functions with `yield` and lazy iteration.

          ```python
          def first_n(n):
              while(n > 0):
                  yield n
                  n -= 1

          worker = first_n(5)
          print(next(worker)) # 5
          print(next(worker)) # 4
          print(next(worker)) # 3
          print(next(worker)) # 2
          print(next(worker)) # 1
          ```

        - Demonstrates how `next()` resumes the generator and eventually raises `StopIteration` when exhausted.

      - Fact:
        - Explains iterables vs iterators and how `iter()` creates an iterator from a collection.
          ```python
          nums = [1, 2, 3]
          listIter = iter(nums)
          print(list(listIter)) # [1, 2, 3]
          print(list(listIter)) # []
          ```
        - Shows that iterators are consumed once and `next()` advances the worker through items.
          ```python
          nums = [1, 2, 3]
          it = iter(nums)
          print(next(it)) # 1
          print(next(it)) # 2
          print(next(it)) # 3
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
      - Exercises:
        - listComprehension:
          - Square each number: Given `nums = [1, 2, 3, 4, 5]`, build a list of each number squared.

            ```python
            nums = [1, 2, 3, 4, 5]
            squaredNums = [num*num for num in nums ]

            print(squaredNums) # [1, 4, 9, 16, 25]
            ```

          - Word lengths: Given `words = ["hello", "world", "python"]`, build a list of the length of each word.

            ```python
            words = ["hello", "world", "python"]

            lengthOfWords = [len(word) for word in words]

            print(lengthOfWords) # [5, 5, 6]
            ```

          - Celsius to Fahrenheit: Given `celsius = [0, 20, 37, 100]`, convert each temperature.

            ```python
            celsius = [0, 20, 37, 100]

            fahrenheit = [c * 9/5 + 32 for c in celsius]

            print(fahrenheit) # [32.0, 68.0, 98.6, 212.0]
            ```

          - Even numbers only: From `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, keep only the even numbers.

            ```python
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            even = [num for num in nums if num % 2 == 0]

            print(even) # [2, 4, 6, 8, 10]
            ```

          - Longer words: From `words = ["cat", "elephant", "dog", "giraffe", "ox"]`, keep only words longer than 3 letters.

            ```python
            words = ["cat", "elephant", "dog", "giraffe", "ox"]

            longerThanThree = [word for word in words if len(word) > 3]

            print(longerThanThree) # ['elephant', 'giraffe']
            ```

          - Divisible by 2 and 3: From `nums = range(1, 21)`, keep numbers divisible by both 2 and 3.

            ```python
            nums = range(1, 21)

            numsDivisibleByTwoAndThree = [num for num in nums if num % 2 == 0 and num % 3 == 0]
            print(numsDivisibleByTwoAndThree) # [6, 12, 18]
            ```

          - Negative to zero: From `nums = [-5, 3, -2, 8, -1, 0]`, make negatives 0 and keep non-negatives unchanged.

            ```python
            nums = [-5, 3, -2, 8, -1, 0]

            integers = [0 if num < 0 else num for num in nums]
            print(integers) # [0, 3, 0, 8, 0, 0]
            ```

          - Even / odd labels: From `nums = [1, 2, 3, 4, 5, 6]`, produce a list of "even" or "odd" labels.

            ```python
            nums = [1, 2, 3, 4, 5, 6]

            listOfEvenOdd = ["even" if num % 2 == 0 else "odd" for num in nums]
            print(listOfEvenOdd) # ['odd', 'even', 'odd', 'even', 'odd', 'even']
            ```

          - Capitalize names: Given `names = ["xicor", "vegeta", "korin"]`, capitalize each name.

            ```python
            names = ["xicor", "vegeta", "korin"]

            capitalizeNames = [name.capitalize() for name in names]
            print(capitalizeNames) # ['Xicor', 'Vegeta', 'Korin']
            ```

          - First letters: Given `sentence = "the quick brown fox"`, build a list of the first letter of each word.
            ```python
            sentence = "the quick brown fox"
            firstLetterOfEachWord = [s[0] for s in sentence.split(" ")]
            print(firstLetterOfEachWord) # ['t', 'q', 'b', 'f']
            ```
          - Flatten matrix: Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, flatten it into a single list.

            ```python
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            singleList = [y for x in matrix for y in x]
            print(singleList) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```

          - Nested school names: From a nested `school` structure, build a flat list of every person's name.

            ```python
            students = {
                "data": [{"name":"Xicor"}, {"name": "Vegeta"}]
            }

            teachers = {
                "data": [{"name":"Master Roshi"}, {"name": "Korin"}]
            }

            school = {
                "students": students,
                "teachers": teachers
            }

            names = [d["name"] for _, value in school.items() for d in value["data"]]
            print(names) # ['Xicor', 'Vegeta', 'Master Roshi', 'Korin']
            ```

          - Filtered flattening: From `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, build a flat list of even numbers multiplied by 10.

            ```python
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            flatList = [y * 10 for x in matrix for y in x if y % 2 == 0]
            print(flatList) # [20, 40, 60, 80]
            ```

          - Filter tuple pairs: Given `pairs = [("amy", 88), ("ben", 32), ("cara", 71)]`, build a list of names with score 40 or above.

            ```python
            pairs = [("amy", 88), ("ben", 32), ("cara", 71)]

            names = [name for (name, score) in pairs if score >= 40]
            print(names) # ['amy', 'cara']
            ```

        - dictComprehension:
          - Cube numbers: Given `nums = [1, 2, 3, 4, 5]`, build a dict mapping each number to its cube.

            ```python
            nums = [1, 2, 3, 4, 5]
            cubeNums = {num: num*num*num for num in nums}
            print(cubeNums) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
            ```

          - Word lengths: Given `words = ["cat", "elephant", "dog"]`, build a dict mapping each word to its length.

            ```python
            words = ["cat", "elephant", "dog"]
            wordsLength = {word: len(word) for word in words}
            print(wordsLength) # {'cat': 3, 'elephant': 8, 'dog': 3}
            ```

          - Capitalized names: Given `names = ["xicor", "vegeta", "korin"]`, build a dict mapping each name to its capitalized form.

            ```python
            names = ["xicor", "vegeta", "korin"]
            capitalizedNames = {name: name.capitalize() for name in names}
            print(capitalizedNames) # {'xicor': 'Xicor', 'vegeta': 'Vegeta', 'korin': 'Korin'}
            ```

          - Product prices: Given `products = ["pen", "book", "bag"]` and `prices = [10, 50, 120]`, build a dict mapping each product to its price.

            ```python
            products = ["pen", "book", "bag"]
            prices = [10, 50, 120]
            pricesOfProducts = dict(zip(products, prices))
            print(pricesOfProducts) # {'pen': 10, 'book': 50, 'bag': 120}
            ```

          - Zip keys and values: Given `keys = ["name", "age", "city"]` and `values = ["Xicor", 22, "Tokyo"]`, build a dict from the pairs.

            ```python
            keys = ["name", "age", "city"]
            values = ["Xicor", 22, "Tokyo"]
            personInfo = dict(zip(keys, values))
            print(personInfo) # {'name': 'Xicor', 'age': 22, 'city': 'Tokyo'}
            ```

          - Filter scores: Given `scores = {"amy": 88, "ben": 32, "cara": 71, "dan": 45}`, build a dict with only scores 50 or above.

            ```python
            scores = {"amy": 88, "ben": 32, "cara": 71, "dan": 45}
            onlyFiftyOrAbove = {key: value for key, value in scores.items() if value >= 50}
            print(onlyFiftyOrAbove) # {'amy': 88, 'cara': 71}
            ```

          - Under 100 prices: Given `prices = {"pen": 10, "book": 50, "bag": 120, "pin": 5}`, build a dict of the items priced under 100.

            ```python
            prices = {"pen": 10, "book": 50, "bag": 120, "pin": 5}
            pricesUnderHundered = {key: value for key, value in prices.items() if value < 100}
            print(pricesUnderHundered) # {'pen': 10, 'book': 50, 'pin': 5}
            ```

          - Increase prices: Given `prices = {"pen": 10, "book": 50}`, build a new dict with every price increased by 10%.

            ```python
            prices = {"pen": 10, "book": 50}
            pricesIncreased = {key: value * 1.1 for key, value in prices.items()}
            print(pricesIncreased) # {'pen': 11.0, 'book': 55.00000000000001}
            ```

          - Pass or fail: Given `scores = {"amy": 88, "ben": 32}`, build a dict mapping each name to "pass" or "fail".

            ```python
            scores = {"amy": 88, "ben": 32}
            passOrFail = {key: "pass" if value >= 40 else "fail" for key, value in scores.items()}
            print(passOrFail) # {'amy': 'pass', 'ben': 'fail'}
            ```

          - Reverse codes: Given `codes = {"IN": "India", "JP": "Japan", "US": "USA"}`, build the reverse dict.

            ```python
            codes = {"IN": "India", "JP": "Japan", "US": "USA"}
            reverseCodes = {value: key for key, value in codes.items()}
            print(reverseCodes) # {'India': 'IN', 'Japan': 'JP', 'USA': 'US'}
            ```

          - Fruit positions: Given `fruits = ["apple", "banana", "cherry"]`, map each fruit to its index.

            ```python
            fruits = ["apple", "banana", "cherry"]
            fruitsAtPosition = {item: index for index, item in enumerate(fruits)}
            print(fruitsAtPosition) # {'apple': 0, 'banana': 1, 'cherry': 2}
            ```

          - Word lengths filtered: Given `sentence = "the quick brown fox"`, map words longer than 3 letters to their length.

            ```python
            sentence = "the quick brown fox"
            wordsLength = {word: len(word) for word in sentence.split() if len(word) > 3}
            print(wordsLength) # {'quick': 5, 'brown': 5}
            ```

          - Even or odd > 5: From `nums = range(1, 11)`, map numbers greater than 5 to "even" or "odd".

            ```python
            nums = range(1, 11)
            evenOrOddGreaterThanFive = {num: "even" if num % 2 == 0 else "odd" for num in nums if num > 5}
            print(evenOrOddGreaterThanFive) # {6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
            ```

        - setComprehension:
          - Square unique numbers: Given `nums = [1, 2, 2, 3, 3, 3, 4]`, build a set of each number squared.

            ```python
            nums = [1, 2, 2, 3, 3, 3, 4]
            uniqueNumsSquared = {num*num for num in nums}
            print(uniqueNumsSquared) # {16, 1, 4, 9}
            ```

          - Lowercase unique words: Given `words = ["Hello", "WORLD", "hello", "World"]`, build a set of the words all lowercased.

            ```python
            words = ["Hello", "WORLD", "hello", "World"]
            lowerCaseWords = {word.lower() for word in words}
            print(lowerCaseWords) # {'hello', 'world'}
            ```

          - Divisible by 3: From `nums = range(1, 21)`, build a set of only the numbers divisible by 3.

            ```python
            nums = range(1, 21)
            numsDivisibleByThree = {num for num in nums if num % 3 == 0}
            print(numsDivisibleByThree) # {3, 6, 9, 12, 15, 18}
            ```

          - Distinct word lengths: Given `sentence = "the cat sat on the mat"`, build a set of the distinct word lengths.

            ```python
            sentence = "the cat sat on the mat"
            distinctWordLengths = {len(word) for word in sentence.split()}
            print(distinctWordLengths) # {2, 3}
            ```

          - Negative/zero/positive labels: From `nums = [-5, 3, -2, 8, -1, 0, 4]`, build a set labeling each as "negative", "zero", or "positive".

            ```python
            nums = [-5, 3, -2, 8, -1, 0, 4]
            uniqueLabels = {"negative" if num < 0 else "zero" if num == 0 else "positive" for num in nums}
            print(uniqueLabels) # {'zero', 'negative', 'positive'}
            ```

        - generatorComprehension:
          - Double generator: Given `nums = [1, 2, 3, 4, 5]`, create a generator that yields each number doubled and then pull the first three values with next().

            ```python
            nums = [1, 2, 3, 4, 5]
            numsWorker = (num * 2 for num in nums)
            print(numsWorker)
            print(next(numsWorker))
            print(next(numsWorker))
            print(next(numsWorker))
            ```

          - Squares generator exhaustion: Create a generator of squares, convert it to a list, then convert it again.

            ```python
            nums = [1, 2, 3, 4, 5]
            numsWorker = (num * num for num in nums)
            print(list(numsWorker))
            print(list(numsWorker))
            ```

          - Odd numbers generator: From `nums = range(1, 11)`, make a generator of odd numbers and iterate it with a for loop.

            ```python
            nums = range(1, 11)
            numsWorker = (num for num in nums if num % 2 == 1)
            for num in numsWorker:
                print(num, end=" ")
            ```

          - Word length generator: Given `words = ["cat", "elephant", "dog", "giraffe"]`, yield each word's length only for words longer than 3 letters.

            ```python
            words = ["cat", "elephant", "dog", "giraffe"]
            wordsWorker = (len(word) for word in words if len(word) > 3)
            print(next(wordsWorker))
            print(next(wordsWorker))
            ```

          - Label generator: Create a generator that yields "neg", "zero", or "pos" for each number in `nums = [-3, 5, -1, 8, 0]`.

            ```python
            nums = [-3, 5, -1, 8, 0]
            numsWorker = ("neg" if num < 0 else "zero" if num == 0 else "pos" for num in nums)
            print(next(numsWorker))
            print(next(numsWorker))
            print(next(numsWorker))
            print(next(numsWorker))
            print(next(numsWorker))
            ```

          - Aggregate generator sum: Use `sum()` with a generator expression to add up all squares from `nums = [1, 2, 3, 4, 5]`.

            ```python
            nums = [1, 2, 3, 4, 5]
            sumOfNums = sum(num * num for num in nums)
            print(sumOfNums)
            ```

          - Max value generator: Use `max()` on a generator that adds 10 to each value from `nums = [4, 1, 7, 3, 9, 2]`.

            ```python
            nums = [4, 1, 7, 3, 9, 2]
            maxNum = max(num + 10 for num in nums)
            print(maxNum)
            ```

          - Count with generator: Use `sum(1 for word in words if word[0] == 'h')` to count words starting with "h".

            ```python
            words = ["hi", "hello", "hey", "howdy"]
            sumofWordsStartsWithh = sum(1 for word in words if word[0] == 'h')
            print(sumofWordsStartsWithh)
            ```

          - Generator exhaustion prediction: Predict the output of `list(gen)` twice on the same generator.

            ```python
            gen = (n * 2 for n in [1, 2, 3])
            print(list(gen))
            print(list(gen))
            ```

          - Lazy evaluation example: Predict what prints first when using a generator calling `loud(n)`.

            ```python
            def loud(x):
                print(f"  computing {x}")
                return x * x

            gen = (loud(n) for n in [1, 2, 3])
            print("made a generator")
            first = next(gen)
            print(f"got {first}")
            ```

        - generators.py:
          - Introduces generator functions and `yield`.
          - Shows how a generator pauses and resumes with `next()`.
          - Demonstrates lazy computation and StopIteration handling.

        - facts/forLoop.py:
          - Explains the difference between iterables and iterators.
          - Shows `iter()` and `next()` behavior with lists.
          - Demonstrates that iterators are exhausted after one pass and then raise `StopIteration`.

      - OOP (Object-Oriented Programming):
        - Fundamental concepts: Understanding objects as real-world entities with properties and behavior, and classes as blueprints for objects.

        - Rectangle class:
          - Demonstrates basic class definition with `__init__` constructor.
          - Implements an `area()` method that calculates width × height.
          - Shows two ways to call methods: using the class directly (passing instance) and using the instance (Python handles `self` automatically).

            ```python
            class Rectangle:
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

                def area(self):
                    return self.width * self.height

            rectangle = Rectangle(2, 3)
            print(Rectangle.area(rectangle))  # 6
            print(rectangle.area())  # 6
            ```

        - BankAccount class:
          - Demonstrates default arguments in constructors with `balance=0`.
          - Implements `deposit()` and `withdraw()` methods that validate and modify instance state.
          - Shows how methods update `self.balance` with error checking (amount validation, insufficient balance).
          - Implements a `printBalance()` method to display account information.

            ```python
            class BankAccount:
                def __init__(self, owner, balance=0):
                    self.owner = owner
                    self.balance = balance

                def deposit(self, amount):
                    if amount <= 0:
                        print(f"The deposited amount must be greater than 0")
                    else:
                        self.balance += amount

                def withdraw(self, amount):
                    if amount <= 0:
                        print(f"Withdrawal amount must be greater than 0")
                    elif amount > self.balance:
                        print(f"Insufficient Balance")
                    else:
                        self.balance -= amount

                def printBalance(self):
                    print(f"{self.owner}'s account balance is {self.balance}")

            customer = BankAccount("Xicor")
            customer.deposit(100)
            customer.withdraw(30)
            customer.printBalance()  # Xicor's account balance is 70
            ```

        - Counter class:
          - Simple class that maintains an internal counter state.
          - Implements `increment()` to add 1 to the count.
          - Implements `get()` to return the current count value.

            ```python
            class Counter:
                def __init__(self):
                    self.count = 0

                def increment(self):
                    self.count += 1

                def get(self):
                    return self.count

            count = Counter()
            count.increment()
            count.increment()
            count.increment()
            print(count.get())  # 3
            ```

        - Person class:
          - Demonstrates calculating derived values from instance attributes.
          - Implements `age_in()` method that takes a year parameter and calculates age.
          - Shows error handling for invalid input (negative age when current year is before birth year).

            ```python
            class Person:
                def __init__(self, name, birth_year):
                    self.name = name
                    self.birth_year = birth_year

                def age_in(self, current_year):
                    if current_year < self.birth_year:
                        return -1
                    return current_year - self.birth_year

            person = Person("Xicor", 1990)
            age = person.age_in(2025)
            if age == -1:
                print("Invalid current year")
            else:
                print(f"The age of {person.name} is {age}")  # The age of Xicor is 35
            ```

        - Composition (Engine and Car):
          - Demonstrates composition pattern where a `Car` object contains an `Engine` object.
          - Engine class has `__init__` and `describe()` method.
          - Car class takes a make string and an Engine object in its constructor.
          - Car's `describe()` method calls the engine's `describe()` method (object collaboration).

            ```python
            class Engine:
                def __init__(self, horsepower):
                    self.horsepower = horsepower

                def describe(self):
                    return f"{self.horsepower} HP engine"

            class Car:
                def __init__(self, make, engine):
                    self.make = make
                    self.engine = engine

                def describe(self):
                    return f"A {self.make} has {self.engine.describe()}"

            engine = Engine(2000)
            car = Car("Ferari", engine)
            print(car.describe())  # A Ferari has 2000 HP engine
            ```

        - Dunder methods (double underscore methods):
          - These are special methods that override built-in functionality.
          - Examples include `__repr__`, `__eq__`, `__add__`.

        - Rectangle with dunder methods:
          - Implements `__repr__()` to return a string representation like `"Rectangle(4,5)"`.
          - Implements `__eq__()` to compare two Rectangle objects by their dimensions.

            ```python
            class Rectangle:
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

                def __repr__(self):
                    return f"Rectangle({self.width},{self.height})"

                def __eq__(self, other):
                    return self.width == other.width and self.height == other.height

            rec = Rectangle(4, 5)
            rec1 = Rectangle(4, 5)
            rec2 = Rectangle(2, 3)
            print(rec)  # Rectangle(4,5)
            print(rec1 == rec)  # True
            print(rec2 == Rectangle(1, 3))  # False
            ```

        - Money class with arithmetic:
          - Implements `__repr__()` to display money as `"$50"` format.
          - Implements `__add__()` to add two Money objects and return a new Money object.
          - Shows that `__add__` should return a new instance, not just a number.

            ```python
            class Money:
                def __init__(self, amount):
                    self.amount = amount

                def __repr__(self):
                    return f"${self.amount}"

                def __add__(self, other):
                    amount = self.amount + other.amount
                    return Money(amount)

            print(Money(50) + Money(30))  # $80
            ```

        - Playlist class with `__len__`:
          - Implements `__len__()` to make the `len()` built-in function work on custom objects.
          - Stores a list of songs and returns the count.

            ```python
            class Playlist:
                def __init__(self, songs):
                    self.songs = songs

                def __len__(self):
                    return len(self.songs)

            playlist = Playlist(["A", "B", "C", "D"])
            print(len(playlist))  # 4
            ```

        - Point class (2D vector):
          - Implements `__repr__()` for readable output like `"Point(2, 3)"`.
          - Implements `__eq__()` to compare points by their x and y coordinates.
          - Implements `__add__()` to add two points and return a new Point with summed coordinates.

            ```python
            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                def __repr__(self):
                    return f"Point({self.x}, {self.y})"

                def __eq__(self, other):
                    return self.x == other.x and self.y == other.y

                def __add__(self, other):
                    return Point(self.x + other.x, self.y + other.y)

            point = Point(2, 3)
            point1 = Point(2, 3)
            print(point == point1)  # True
            print(point + point1)  # Point(4, 6)
            ```

        - Dataclasses:
          - The `@dataclass` decorator from the `dataclasses` module automatically generates `__init__`, `__repr__`, and `__eq__` methods.
          - Eliminates boilerplate code for simple data classes; only custom behavior methods need to be written.
          - Uses type annotations to define fields: `field_name: type`.
          - Supports default values for fields.

          - Rectangle as a dataclass:
            - Automatically generates `__init__` and `__repr__` without manual implementation.
            - Custom `area()` method is still added for behavior-specific logic.

              ```python
              from dataclasses import dataclass

              @dataclass
              class Rectangle:
                  width: int
                  height: int

                  def area(self):
                      return self.width * self.height

              rect = Rectangle(2, 3)
              print(rect)  # Rectangle(width=2, height=3)
              print(rect.area())  # 6
              ```

          - Money as a dataclass:
            - Generates automatic `__init__`, `__repr__`, and `__eq__`.
            - Custom `__add__()` method is manually implemented for arithmetic behavior.

              ```python
              @dataclass
              class Money:
                  amount: int

                  def __add__(self, other):
                      total_sum = self.amount + other.amount
                      return Money(total_sum)

              money = Money(100)
              money1 = Money(110)
              print(money)  # Money(amount=100)
              print(money + money1)  # Money(amount=210)
              ```

          - User with default values:
            - Fields can have default values using `field_name: type = default_value`.
            - Allows creating instances with fewer arguments.

              ```python
              @dataclass
              class User:
                  name: str
                  age: int = 0
                  is_active: bool = True

              user1 = User("Xicor")
              print(user1)  # User(name='Xicor', age=0, is_active=True)

              user2 = User("Goku", 80, True)
              print(user2)  # User(name='Goku', age=80, is_active=True)
              ```

          - Circle dataclass:
            - Demonstrates custom method implementation with a dataclass.
            - `area()` method calculates the area from the radius field.

              ```python
              @dataclass
              class Circle:
                  radius: float

                  def area(self):
                      return 3.14159 * self.radius**2

              circle = Circle(5)
              print(circle)  # Circle(radius=5)
              print(circle.area())  # 78.53975
              ```

          - Book dataclass:
            - Multi-field dataclass with mixed types and default values.
            - Automatic `__eq__()` compares all fields by value.
            - Two books with identical field values are considered equal.

              ```python
              @dataclass
              class Book:
                  title: str
                  author: str
                  pages: int
                  price: float = 0.0

              book1 = Book("Atomic Habits", "James Clear", 100, 100)
              book2 = Book("Eat That Frog", "Brian Tracy", 200, 200)
              book3 = Book("Atomic Habits", "James Clear", 100, 100)

              print(book1 == book2)  # False
              print(book1 == book3)  # True
              ```

          - Summary of dataclasses:
            - Without dataclass: must manually write `__init__`, `__repr__`, and `__eq__` for each class.
            - With dataclass: boilerplate methods are automatically generated from type annotations.
            - Only custom behavioral methods (like `area()`, `__add__()`) need to be implemented.
            - Dataclass equality compares by value, not by reference, which is essential for domain objects.

        - Inheritance basics:
          - Inheritance allows a child class to reuse and override parent class functionality.
          - When a child class doesn't define `__init__`, it automatically inherits the parent's.

          - Animal and Cat example:
            - Parent `Animal` class with `__init__` and `speak()` method.
            - Child `Cat` class overrides `speak()` to return "meow".
            - Cat instances can call `speak()` (overridden) and access `name` (inherited).

              ```python
              class Animal:
                  def __init__(self, name):
                      self.name = name

                  def speak(self):
                      return "some sound"

              class Cat(Animal):
                  def speak(self):
                      return "meow"

              cat = Cat("Beerus")
              print(cat.speak())  # meow (method overriding)
              ```

          - Vehicle and Car with `super()`:
            - When a child class has its own `__init__`, use `super().__init__()` to call the parent's initialization.
            - This allows the parent to set up inherited attributes while the child adds its own.

              ```python
              class Vehicle:
                  def __init__(self, brand):
                      self.brand = brand

                  def describe(self):
                      return self.brand

              class Car(Vehicle):
                  def __init__(self, brand, doors):
                      super().__init__(brand)
                      self.doors = doors

                  def info(self):
                      return f"A {self.describe()} has {self.doors} doors."

              car = Car("Maruti", 4)
              print(car.info())  # A Maruti has 4 doors
              ```

          - Inheritance with dataclasses:
            - Child dataclass automatically inherits parent's fields and can add its own.
            - No need for `super()` call in `__init__` — dataclass handles field initialization.
            - Parent and child fields are combined in the auto-generated `__init__`.

              ```python
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
              print(car.info())  # A Maruti has 4 doors
              ```

          - Inheritance vs Composition decision:
            - **Inheritance (is-a)**: Use when a child is a specific type of parent.
              - Example: `Student` is a `Person` → `class Student(Person)`
              - Example: `Circle` is a `Shape` → `class Circle(Shape)`
            - **Composition (has-a)**: Use when an object contains or uses another object.
              - Example: `House` has `Room` objects → create both classes separately, pass Room to House
              - Example: `Library` has `Book` objects → Library contains a list of Books

        - Composition examples:
          - Composition allows objects to be built by combining simpler objects.

          - Book and Library:
            - `Book` dataclass holds title and author.
            - `Library` dataclass contains a list of `Book` objects.
            - Uses `field(default_factory=list)` to avoid mutable default argument issues.
            - Library provides methods to add and list books.

              ```python
              @dataclass
              class Book:
                  title: str
                  author: str

              @dataclass
              class Library:
                  listOfBooks: list[Book] = field(default_factory=list)

                  def add_book(self, book):
                      self.listOfBooks.append(book)

                  def list_books(self):
                      for book in self.listOfBooks:
                          print(f"{book.title} : {book.author}")

              book = Book("Atomic Habits", "James Clear")
              book1 = Book("Eat That Frog", "Brian Tracy")

              library = Library()
              library.add_book(book)
              library.add_book(book1)
              library.list_books()
              ```

          - CPU, RAM, and Computer:
            - Demonstrates composition of multiple objects with different types.
            - `Computer` dataclass composes both `CPU` and `RAM` objects, plus a name.
            - `describe()` method accesses nested attributes via composition (e.g., `self.cpu.cores`).
            - Shows how complex domain objects are built from simpler, reusable pieces.

              ```python
              @dataclass
              class CPU:
                  cores: int

              @dataclass
              class RAM:
                  size_gb: int

              @dataclass
              class Computer:
                  name: str
                  cpu: CPU
                  ram: RAM

                  def describe(self):
                      return f"A {self.name} has a {self.cpu.cores} cores and {self.ram.size_gb} gigabytes."

              cpu = CPU(10)
              ram = RAM(16)
              computer = Computer("MAC", cpu, ram)
              print(computer.describe())  # A MAC has a 10 cores and 16 gigabytes.
              ```

        - Polymorphism (many forms):
          - Polymorphism allows objects of different types to respond to the same method call with different behaviors.
          - The same method name triggers different implementations depending on the object type.

          - Circle, Square, and Triangle with `area()`:
            - Three unrelated classes, each with an `area()` method using their own formulas.
            - A single loop calls `.area()` on each shape, producing the correct calculation for each type.
            - Demonstrates how polymorphism enables writing generic code that works with multiple types.

              ```python
              @dataclass
              class Circle:
                  radius: int

                  def area(self):
                      return 3.14 * self.radius**2

              @dataclass
              class Square:
                  side: int

                  def area(self):
                      return self.side**2

              @dataclass
              class Triangle:
                  h: int
                  b: int

                  def area(self):
                      return 0.5 * self.b * self.h

              for instance in [Circle(5), Square(10), Triangle(10, 20)]:
                  print(f"The area of {type(instance).__name__} is {instance.area()}")
              ```

        - Duck typing (Python's loose polymorphism):
          - "If it walks like a duck and quacks like a duck, it's a duck."
          - Python doesn't enforce type requirements; it only checks if an object has the required method or attribute.
          - Functions can work with unrelated classes as long as they implement the expected interface.
          - No inheritance or shared parent class needed — only shared method names matter.

          - Book and Car with `describe()`:
            - `Book` and `Car` are completely unrelated classes (no inheritance).
            - Both implement a `describe()` method with different behavior.
            - A single function `describe_all()` accepts any object with a `describe()` method.
            - Demonstrates that polymorphism in Python is based on behavior, not type hierarchy.

              ```python
              def describe_all(items):
                  for item in items:
                      item.describe()

              @dataclass
              class Book:
                  author: str
                  title: str

                  def describe(self):
                      print(f"{self.author} : {self.title}")

              @dataclass
              class Car:
                  brand: str

                  def describe(self):
                      print(f"The brand name of the car is {self.brand}")

              describe_all([Book("A", "B"), Car("Lamborghini")])
              ```

          - Operator overloading as duck typing:
            - When `Money(50) + Money(30)` is called, Python looks for the `__add__()` method on the left operand.
            - Similarly, `Point(2, 3) + Point(4, 5)` calls `Point.__add__()`.
            - Both Money and Point implement `__add__`, but they're unrelated classes.
            - Python doesn't care about type; it just calls the method if it exists.
            - This is polymorphism through duck typing: if the object responds to `+`, it can be added.

              ```python
              # Both classes have __add__, but they're unrelated
              print(Money(50) + Money(30))  # $80
              print(Point(2, 3) + Point(4, 5))  # Point(6, 8)
              # Same operator +, different behavior — duck typing at work.
              ```

        - Class methods (`@classmethod`):
          - Class methods receive the class itself (`cls`) as the first parameter, not an instance (`self`).
          - Marked with the `@classmethod` decorator.
          - Can be called on the class or an instance: `MyClass.method()` or `instance.method()`.
          - Commonly used as **factory methods** (alternative constructors) to create instances from external data.
          - Can also access and modify class-level state (class attributes).

          - API response to objects (factory pattern):
            - Convert a dictionary from an API into a dataclass instance.
            - `from_dict()` factory method parses a single dict.
            - `from_list()` factory method applies `from_dict()` to multiple items using a list comprehension.
            - Useful for transforming API responses into domain objects.

              ```python
              response = [
                  {"username": "xicor", "email": "x@mail.com"},
                  {"username": "vegeta", "email": "v@mail.com"},
              ]

              @dataclass
              class User:
                  username: str
                  email: str

                  @classmethod
                  def from_dict(cls, data):
                      return cls(data["username"], data["email"])

                  @classmethod
                  def from_list(cls, data):
                      return [cls.from_dict(d) for d in data]

                  def describe(self):
                      return f"User = {self.username} , Email = {self.email}"

              users = User.from_list(response)
              for user in users:
                  print(user.describe())
              ```

          - CSV line to object:
            - Parse structured string data (like CSV lines) into dataclass instances.
            - `from_csv_line()` splits a comma-separated string and converts types as needed.
            - Demonstrates data transformation on the way into the object.

              ```python
              @dataclass
              class Book:
                  title: str
                  author: str
                  pages: int

                  @classmethod
                  def from_csv_line(cls, line):
                      title, author, pages = line.split(",")
                      pages = int(pages)
                      return cls(title, author, pages)

              book = Book.from_csv_line("Atomic Habits,James Clear,320")
              print(book)  # Book(title='Atomic Habits', author='James Clear', pages=320)
              ```

          - Class-level counter (non-factory classmethod):
            - Class methods aren't always factories; they can read and modify class state.
            - Use a class attribute (shared across all instances) to track a count.
            - Increment the counter in `__init__` each time an instance is created.
            - Implement a `@classmethod get_count()` to return the class-level count.

              ```python
              class Employee:
                  count = 0

                  def __init__(self):
                      Employee.count += 1

                  @classmethod
                  def get_count(cls):
                      return cls.count

              employee1 = Employee()
              employee2 = Employee()
              employee3 = Employee()

              print(Employee.get_count())  # 3
              ```

          - Multiple factory methods (alternative constructors):
            - A single class can have multiple factory methods for different creation patterns.
            - `square(cls, size)` creates a rectangle with equal width and height.
            - `from_dict(cls, data)` creates from a dictionary.
            - Normal constructor still works for direct instantiation.

              ```python
              @dataclass
              class Rectangle:
                  width: float
                  height: float

                  def area(self):
                      return self.width * self.height

                  @classmethod
                  def square(cls, size):
                      return cls(size, size)

                  @classmethod
                  def from_dict(cls, data):
                      return cls(data["width"], data["height"])

              rectangle = Rectangle(10, 10)
              print(rectangle.area())  # 100

              square = Rectangle.square(10)
              print(square.area())  # 100

              rect_from_dict = Rectangle.from_dict({"width": 10, "height": 10})
              print(rect_from_dict.area())  # 100
              ```

          - Factory with validation and transformation:
            - Factories often clean and validate data before creating an object.
            - Use factories for the "T" (Transform) step in ETL (Extract, Transform, Load) pipelines.
            - Example: strip whitespace from strings, convert types from API responses.

              ```python
              @dataclass
              class Product:
                  name: str
                  price: float

                  @classmethod
                  def from_dict(cls, data):
                      return cls(data["name"].strip(), float(data["price"]))

              product = Product.from_dict({"name": "  Widget  ", "price": "9.99"})
              print(product)  # Product(name='Widget', price=9.99)
              ```
