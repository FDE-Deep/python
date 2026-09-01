import itertools

# chain

# itertools.chain() combines all the iterables and loop over it.

# This is lazy and process each item at a time.
# Chain also creates a worker and then list if we are using, iterates over it and returns the list

l = [1, 2, 3]
r = range(4, 11)

newList = itertools.chain(l, r)
print(list(newList))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# What if we have list of iterables? then we can use from_iterable()

l = [[1, 2, 3], range(4, 10)]
print(list(itertools.chain.from_iterable(l)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Practice Set

# 1 — The laziness / shared-consumption behavior

gen = (x for x in range(5))  # 0,1,2,3,4
chained = itertools.chain([10, 20], gen)

# Predict each. The last line is the key: after chain has pulled some items, what's left in gen? (Trace which items chain consumed from gen.)

print(next(chained))  # ? 10
print(next(chained))  # ? 20
print(next(chained))  # ? 0
print(
    list(gen)
)  # ? — the interesting part [1,2,3,4] it will start from 1 as 0 is already proccessed from gen

# One thing i want to confirm ?

# Gen is a generator. when we call it , it starts the execution of the function.
# So, when we call next(gen) , it executes and process the yield value and stop the execution.
# now, when we call list(gen) it starts the execution of the gen from where it was stopped and next() processes each stopped execution.

# Question is, what info a generator holds ?

# 2 — Flattening with from_iterable on a generator of ranges

result = itertools.chain.from_iterable(range(i) for i in range(4))


# range(i) for i in range(4) produces range(0), range(1), range(2), range(3). Flatten them. Predict the output. (Trace what each range(i) yields: range(0) is empty, range(1) is [0], etc.)
# range(0) []
# range(1) [0]
# range(2) [0,1]
# range(3) [0,1,2]
print(list(result))  # [0, 0, 1, 0, 1, 2]
