import itertools

# What is groupby in intertools ?

# groupby creates a group of consecutive items in the data. It returns a key and group iterator. It is lazy.
# If the items are not sorted and are not adajacent to each other, then it creates a new group for the same key.

# Examples:

data = ["a", "a", "a", "b", "b", "c"]

for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")

# output

# a : ['a', 'a', 'a']
# b : ['b', 'b']
# c : ['c']

# In this, group is a iterator and once it is exhausted , cannot be reused again

groups = []

for key, group in itertools.groupby(data):
    groups.append(group)

for i in groups:
    print(list(i))

# ouput:
# []
# []
# []
# Reason it is returning empty array because a group has been already processed before it moves further to create a new group
# for new item in data. The groupby has to go through the first group item lazily in order to find a new item and start creating group for it. So , we dont process a group inside the loop, its gonna exhausted by shared worker.


# non adjacent data

data = [1, 1, 2, 2, 1]

for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")

# 1 : [1, 1]
# 2 : [2, 2]
# 1 : [1]

# It didnt combine all the 1s. It only create groups for consecutive items.

# To fix, we should sort the items first

data.sort()

for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")

# output

# 1 : [1, 1, 1]
# 2 : [2, 2]


# Practice set

# 1 — Consecutive grouping (see the trap)

# Given data = [1, 1, 2, 2, 3, 1, 1], run groupby without sorting and print each (key, list(group)). Predict the output — how many groups, and note the 1s at the end. (This shows the consecutive-only behavior — the trailing 1s form a separate group.)

data = [1, 1, 2, 2, 3, 1, 1]

for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")

# prediction - 4 groups (1,2,3,1)

# output -

# 1 : [1, 1]
# 2 : [2, 2]
# 3 : [3]
# 1 : [1, 1]

# 2 — The sort fix
# Take the same data = [1, 1, 2, 2, 3, 1, 1], sort it first, then groupby. Predict the output and compare to #1. Explain why they differ.

data.sort()

for key, group in itertools.groupby(data):
    print(f"{key} : {list(group)}")


# prediction - 3 groups (1,2,3) . Reason is, now the items are sorted and adjacent to each to other.

# output -
# 1 : [1, 1, 1, 1]
# 2 : [2, 2]
# 3 : [3]

# 3 — Group by a key function
# Given words = ["cat", "car", "dog", "deer", "ant", "cow"], group by first letter. First sort by first letter, then groupby with key=lambda w: w[0]. Predict the groups.

words = ["cat", "car", "dog", "deer", "ant", "cow"]
words.sort(key=lambda w: w[0])

for key, group in itertools.groupby(words, key=lambda w: w[0]):
    print(f"{key} : {list(group)}")

# output

# a : ['ant']
# c : ['cat', 'car', 'cow']
# d : ['dog', 'deer']

# 4 — Count per group (practical)
# Given data = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"], sort by first letter and use groupby to count how many words start with each letter. Print each letter and its count. (Hint: len(list(group)) gives the count — but remember to consume the group.)

data = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]
data.sort(key=lambda d: d[0])

for key, group in itertools.groupby(data, key=lambda d: d[0]):
    print(f"{key} : {len(list(group))}")


# output
# a : 3
# b : 2
# c : 1
