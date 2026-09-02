import pytest
from index import add, set_age, Library, Item

# 1 — Basic tests + parametrize

# Take a simple function (your add, or total(nums) from earlier). Write a test_*.py file with: a couple of plain assert tests, then a @parametrize version testing several input/output pairs. Install pytest, run it, confirm they pass.


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (10, 20, 30),
    ],
)
def test_add_parameterize(a, b, expected):
    assert add(a, b) == expected


# 2 — Test exceptions with pytest.raises
# Take a function that raises (your set_age, or your library's borrow_item). Write a test using with pytest.raises(...) confirming the right exception fires for bad input. Also test the success case (valid input returns correctly).


def test_set_age_negative():
    with pytest.raises(ValueError):
        set_age(-5)


@pytest.mark.parametrize("age,expected", [(10, 10), (20, 20)])
def test_set_age_valid(age, expected):
    assert set_age(age) == expected


@pytest.mark.parametrize("bad_age", [-10, -20])
def test_set_age_invalid(bad_age):
    with pytest.raises(ValueError):
        set_age(bad_age)


# 3 # Write a @pytest.fixture that creates a sample object (a Library with an item, or a Member). Write two tests that both use it, and confirm each gets a fresh instance.


@pytest.fixture
def sample_library():
    library = Library("Sample")
    return library


def test_Library(sample_library):
    assert sample_library.name == "Sample"


def test_add_item(sample_library):
    item = Item("book")
    sample_library.add_item(item)
    assert len(sample_library.items) > 0
    assert sample_library.items["book"].name == "book"


def test_fresh_instance_library(sample_library):
    assert len(sample_library.items) == 0


# 4 — Test file I/O with tmp_path
# Test your library's save/load using tmp_path — save a library to a temp file, load it back, assert the loaded data matches. This tests real persistence without touching real files.


def test_save_load_library(tmp_path):
    filepath = f"{tmp_path}/library.json"
    library = Library("Test")
    item = Item("book")
    library.add_item(item)
    library.save(filepath)
    load = Library.load(filepath)
    assert load.name == "Test"
    assert len(load.items) > 0
    assert load.items["book"].name == "book"
