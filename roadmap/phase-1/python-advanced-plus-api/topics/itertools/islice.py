import itertools

# Itertools
# It is a standard library module of iter-building tools. It produces iters or generators and we use it for higher or infinite sequences. It helps not to load everything at once in memory.


# iSlice

#  This iter tool is used to slice generators or iterators.

data = [1, 2, 3]
print(data[:2])  # [1,2]

# the entire list is loaded in memory and we can access it using index value. This helps in slicing the list into new list

# But problem with generator is we cant use [] to slice. Generators are workers which only load items in memory when we access the items using next(). So, it is not possible to slice a generator because we dont load all the items at once in memory.

myList = [1, 2, 3]

gen = (i**2 for i in myList)

genSlice = itertools.islice(gen, 1)
print(genSlice)  # <itertools.islice object at 0x000001A946A4B330>
print(list(genSlice))
print(
    list(gen)
)  # [4, 9] as genSlice refers to the same gen worker and gen slice has already visited 1 and it has been consumed.


# Practice set

# 1 — Basic slicing forms

nums = range(20)
a = itertools.islice(nums, 5)
b = itertools.islice(nums, 5, 10)
c = itertools.islice(nums, 0, 20, 3)

# Predict all three. (islice over a range — does slicing a affect b? Think about whether range is a reusable source or a single worker.)

print(list(a))  #  [0,1,2,3,4]
print(list(b))  # [5,6,7,8,9]
print(list(c))  # [0,3,6,9,12,15,18]


# 2 — The consumption / shared-worker behavior

gen = (x * 10 for x in range(10))  # yields 0, 10, 20, ..., 90

first_three = list(itertools.islice(gen, 3))
next_two = list(itertools.islice(gen, 2))
rest = list(gen)

# Predict all three. This is the key one — trace how each islice advances the same generator, and where each pick-up starts. (Unlike #1's range, gen is a single worker — so consumption carries over.)


print(first_three)  # [0,10,20]
print(next_two)  # [30,40]
print(rest)  # [50,60,70,80,90]


# 3 — Lazy peek at a stream (the practical use)


def infinite_counter():
    n = 0
    while True:  # infinite generator — never stops on its own
        yield n
        n += 1


first_five = itertools.islice(infinite_counter(), 5)


# Predict the output. Then answer: this generator is infinite — list(infinite_counter()) alone would run forever. Why does list(first_five) finish? (This shows islice's real value — taking a finite slice from an unbounded stream.)

print(list(first_five))  # [0,1,2,3,4]

# The reason list(first_five) finishes, because when we are creating a generator or worker using iSlice , it will only yield items for 5 items. Then it will stop the execution of the function.

# now , this generator or worker has only 5 items and when  we pass this to list, list will loop over it and each next will return the n value.

# If we create a new worker, then it will start from 5
