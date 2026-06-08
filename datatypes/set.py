#What is a set ?

# A set is a collection of unique data in unordered manner.

# How to create a set

set22 = {1,2,3,4}

print(set22)

# Now , lets say if it can handle duplicate data and return unique data

set1 = {1,1,1,2,3,4,4,4}

print(set1) # {1, 2, 3, 4}

#Python uses hashing machanism to store the values. Thats why they come in unordered way because they are sort based on hash value

#Lets say you want to check something in set

print(1 in set1) #True

#Length of set

print(len(set1))

#How to declare empty set

set3 = {};

print(type(set3)) #<class 'dict'> this is a dictionary not a set

# TO create empty set , we use set()

set4 = set()

print(type(set4)) #<class 'set'>

#TODO to understand the intersections in set. 