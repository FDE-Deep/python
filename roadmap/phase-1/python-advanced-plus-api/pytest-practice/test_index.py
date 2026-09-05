import pytest
from unittest.mock import patch, Mock
from index import add, set_age, Library, Item, get_doubled, retry

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


# Mock

# Practice set

# 1 — Basic mock with patch
# Write get_doubled() that calls fetch_value() and returns its result × 2. In a test, patch fetch_value to return 5, and assert get_doubled() returns 10. (Tests your × 2 logic without the real fetch_value.)


def test_get_doubled():
    with patch("index.fetch_value") as mock:
        mock.return_value = 5
        assert get_doubled() == 10
        assert mock.call_count == 1


# 2 — side_effect to test retry recovering
# Take your @retry. Use Mock(side_effect=[...]) to make a fake fail twice (raise) then succeed. Apply retry, and assert (a) it returns the success value, (b) call_count == 3.


def test_testRetry():
    with patch("index.time.sleep"):
        mock = Mock(
            side_effect=[
                ValueError("Count is less than 2"),
                ValueError("Count is less than 2"),
                3,
            ]
        )
        wrapper = retry(attempts=3)(mock)
        assert wrapper() == 3
        assert mock.call_count == 3


# 3 — Test retry re-raises when all attempts fail
# Use Mock(side_effect=SomeError(...)) (raises every call). Apply retry(attempts=3). Assert that calling it raises (with pytest.raises), confirming your "re-raise when exhausted" logic. Also assert call_count == 3.


def test_retry_fails():
    with patch("index.time.sleep"):
        mock = Mock(side_effect=ValueError("Catch value error when retry exhausts"))
        wrapper = retry(attempts=3)(mock)
        with pytest.raises(ValueError):
            wrapper()
        assert mock.call_count == 3
