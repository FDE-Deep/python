# python

This repo is a Python learning workspace. It is organized by topic so you can quickly see what each file teaches without opening every file.

## What I am learning

- Python basics and first programs
- Variable assignment and arithmetic
- Core data types: int, float, str, None, bool, list, tuple, set, dict, complex
- List operations: concatenation, slicing, nested lists, append, extend, insert, remove, pop, reverse, sort
- Tuple properties: immutability, creation syntax, indexing, nested mutable contents
- Set behavior: uniqueness, unordered storage, membership, empty set creation
- Strings: quotes, escaping, concatenation, multiline strings, indexing, slicing, negative indices
- Dictionaries: key-value data, nested dictionaries, access, get method, default values
- Functions: defining reusable code, passing arguments, returning values
- User input: reading keyboard input with `input()` and using it in programs
- Conditional statements: if-elif-else for decision-making and flow control

## Topics and file summaries

### Variables

- `variables/index.py`
  - Prints the first Python program
  - Demonstrates variable assignment and storing values
  - Shows arithmetic with variables

### Data types overview

- `datatypes/index.py`
  - Lists the main Python data types
  - Demonstrates examples for `int`, `float`, `str`, `None`, `bool`, `list`, `tuple`, `set`, `dict`, and `complex`
  - Shows how booleans convert to integers (`True` → `1`, `False` → `0`)

### Lists

- `datatypes/list.py`
  - Defines lists and shows list creation
  - Combines lists with `+`
  - Accesses list items with indexing and slices
  - Works with nested lists
  - Adds items with `append`, `extend`, and `insert`
  - Uses `count`, `index`, `pop`, `remove`, and `del`
  - Reverses and sorts lists

### Tuples

- `datatypes/tuple.py`
  - Explains tuple immutability versus lists
  - Shows tuple creation with and without parentheses
  - Covers single-item tuple syntax
  - Demonstrates indexing and nested list mutation inside a tuple
  - Uses `len` and `count`

### Sets

- `datatypes/set.py`
  - Explains sets as unordered, unique collections
  - Shows duplicate removal and membership checks
  - Covers set length and empty set creation using `set()`
  - Notes a TODO: practice set intersections

### Strings

- `datatypes/string.py`
  - Demonstrates string creation with quotes
  - Shows printing strings multiple times using `*`
  - Covers quote escaping and file path escaping
  - Shows string concatenation and multiline strings with `"""`
  - Demonstrates indexing, slicing, negative indices, and `len`

### Dictionaries

- `datatypes/dict.py`
  - Introduces dictionaries as key-value collections
  - Demonstrates nested dictionaries for student data
  - Shows access by key and nested key lookup
  - Uses `get` with default values
  - Shows `len` on dictionaries

### Functions

- `funtions/index.py`
  - Explains what functions are and when to use them
  - Shows a simple function with no parameters
  - Demonstrates passing arguments to a function
  - Returns values from a function using `return`
  - Prints and stores the returned result

### User input

- `userInput/index.py`
  - Reads input from the user with `input()`
  - Asks for a student's name and roll number
  - Stores user input in a dictionary
  - Prints the collected student data in a formatted output

### Conditional statements (if-elif-else)

- `if-elif-else/index.py`
  - Demonstrates if-else statements for basic conditions
  - Shows how to check if a number is even or odd
  - Covers if-elif-else for multiple conditions and input validation
  - Validates user input before processing
  - Includes debugging tips using VS Code breakpoints

### Operators

- `operators/arithmaticOperators.py`
  - Demonstrates arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
  - Shows shorthand assignment forms like `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

- `operators/assignmentOperator.py`
  - Shows the assignment operator `=` and tuple-style multiple assignment (`x, y, z = 1, 2, 3`)

- `operators/comparisonOperators.py`
  - Covers comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - Demonstrates boolean results from comparisons

- `operators/logicalOperators.py`
  - Explains logical operators `and`, `or`, `not` and how to combine conditional expressions

## Next steps

- Continue learning intersections with sets
- Add more examples for loops, conditionals, functions, and modules
