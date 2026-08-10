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

