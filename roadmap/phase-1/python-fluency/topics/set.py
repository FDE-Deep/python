# A set is a collection of data which is unordered, unchangeable and unique

# how to declare a set

data = {1,2,3,3} 

print(data) # {1, 2, 3} Even though we declared a duplicate value of 3, set doesnt allow duplicate and remove it

# As set is un-ordered, it cannot be accessed using index value

# So, we can check whether an item is present in set or not

print(1 in data) # True
print(20 in data) # False

# We can also iterate to get all items

for d in data:
    print(d)
    
# Few things to remember while creating set:

# 1. True or 1 are considered as duplicate value

data = {1,2,3, True}
print(data) # {1, 2, 3}

# 2. Same for False and 0

data = {1,2,3,0,False}
print(data) # {0, 1, 2, 3}

# Now, set cannot be changed but we can add items to it

data = {1,2,3}

data.add(4)

print(data) # {1, 2, 3, 4}

# if we have another list,tuple or set, that can also be added to set using update method

list = [4,5,6,7]
data = {1,2,3}

data.update(list)
print(data) # {1, 2, 3, 4, 5, 6, 7}

# Remove set items

# remove method

data.remove(1)
print(data) # {2, 3, 4, 5, 6, 7}

# data.remove(1) # this throws an error because 1 doesnt exist

# But what if we dont want to throw error, then use discard method

data.discard(1) # It doesnt throw an error
print(data) # {2, 3, 4, 5, 6, 7}

data.discard(2) # {3, 4, 5, 6, 7}
print(data)

# We can clear the entire set also

data.clear()
print(data) # set()

# To delete the set, use del

del data
# print(data)  NameError: name 'data' is not defined as it got deleted

# Join sets

# Union - Returns all items from both sets

set1 = {1,1,2,3,4,5,6,7}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3) # {1, 2, 3, 4, 5, 6, 7} union removes the duplicate

# We can also | operator

set3 = set1 | set2
print(set3)  # {1, 2, 3, 4, 5, 6, 7}

# We can join tuples or list as well but we cant use | operator then. | operator only works with set

set = {1,2,3}
tuple = (4,5,1)

newSet = set.union(tuple)
print(newSet) # {1, 2, 3, 4, 5}

# Intersection - only return the items which are present in both sets

set1 = {1,2,3}
set2 = {1,2}

# if we are using sets then we can use & operator for itersection

set = set1 & set2
print(set) # {1, 2}

tuple = (1,2)

set = set1.intersection(tuple)
print(set) # {1, 2}

# Intesection Update - only keeps the duplicates but update the existing set

set1 = {1,2,3}
set2 = {3}

set1.intersection_update(set2)
print(set1) # {3}

# Difference - return items from first set which are not present in other sets

set1 = {1,2,3}
set2 = {4,5}
set3 = {2,3}

# we can use - sign only for sets

set = set1 - set2 - set3
print(set) # {1}

# for other data types we need to use difference

list = [4,5]

set = set1.difference(list)
print(set) # {1, 2, 3}

# Difference Update - return items from first set that are not present in other set but update the first set

set1 = {1,2,3}
set2 = {2,3}

set1.difference_update(set2)
print(set1) # {1}

# Symmetric Difference - returns items from all sets which are not present.Which are not common in sets.

set1 = {1,2,3,7,8}
set2 = {1,2,4,5}

# only for sets, we can use ^ sign 

set = set1 ^ set2
print(set) # {3, 4, 5, 7, 8}

# Symmetric Difference Update

set1.symmetric_difference_update(set2)
print(set1) # {3, 4, 5, 7, 8}