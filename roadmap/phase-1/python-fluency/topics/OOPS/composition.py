from dataclasses import dataclass, field

# Composition

# Write a Book dataclass (title, author) and a Library class that holds a list of Books, with add_book(self, book) and list_books(self) methods.
# Create a library, add two books, list them. (A Library HAS Books — composition.)


@dataclass
class Book:
    title: str
    author: str


@dataclass
class Library:
    # listOfBooks: list = []  # this throws default mutable error , to fix this, we need to use default_factory
    listOfBooks: list[Book] = field(
        default_factory=list
    )  # This create a fresh copy of list for each instance of Library

    def add_book(self, book):
        self.listOfBooks.append(book)

    def list_books(self):
        for book in self.listOfBooks:
            print(f"{book.title} : {book.author}")


book = Book("Atomic Habit", "James Clear")
book1 = Book("Eat that Frog", "Brian Tracy")

library = Library()
library.add_book(book)
library.add_book(book1)
print(library.list_books())  # 2

# Write a CPU dataclass (cores: int) and a RAM dataclass (size_gb: int), then a Computer class that composes both (holds a CPU object, a RAM object, and a name).
# Give Computer a describe(self) that reports its name, cores, and RAM by reaching into its parts (self.cpu.cores, etc.).
# Create the parts, build a Computer, print its description. (A Computer HAS a CPU and HAS RAM — pure composition, how most real domain objects are built.)


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
