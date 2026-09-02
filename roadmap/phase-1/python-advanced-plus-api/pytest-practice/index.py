# Pytest is a tool that is used to test the code. We can do unit testing or functional testing

# We need to install pytest tool. Run python -m pip install pytest

# We also need to install pytest-cov to check the coverage of the code. Run python -m pip install pytest-cov

# To run coverage, either mention the module in python -m pytest --cov = module or run python -m pytest --cov =. This will run all test at root directory

# Practice — test real code you've written

# Rather than toy examples, let's test your actual code. Start here:

# 1 — Basic tests + parametrize

# Take a simple function (your add, or total(nums) from earlier). Write a test_*.py file with: a couple of plain assert tests, then a @parametrize version testing several input/output pairs. Install pytest, run it, confirm they pass.


def add(a, b):
    return a + b


# 2 — Test exceptions with pytest.raises
# Take a function that raises (your set_age, or your library's borrow_item). Write a test using with pytest.raises(...) confirming the right exception fires for bad input. Also test the success case (valid input returns correctly).


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


# 3 — A fixture

# A fixture is a decorator using which we can create a fixed or setup to test something.

# Write a @pytest.fixture that creates a sample object (a Library with an item, or a Member). Write two tests that both use it, and confirm each gets a fresh instance.

import json


class Library:
    def __init__(self, name):
        self._name = name
        self._items = {}
        self.members = {}

    def add_item(self, item):
        self._items[item.name] = item

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    def save(self, filepath):
        data = {
            "name": self._name,
            "items": [item.to_dict() for item in self._items.values()],
        }
        with open(filepath, "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def load(cls, filepath):
        with open(filepath) as file:
            data = json.load(file)
        library = cls(data["name"])
        for item in data["items"]:
            book = Item.from_dict(item)
            library.add_item(book)
        return library


class Item:
    def __init__(self, name):
        self._name = name

    def to_dict(self):
        return {"type": "Book", "name": self._name}

    @property
    def name(self):
        return self._name

    @classmethod
    def from_dict(cls, item):
        return cls(item["name"])
