# day 1: Learn about lists in python

# A list is a collection of various data types. Usually , we keep the same data type in a list. Otherwise. it will be
# difficult to do some operations on list unless we have added data as as tuple.

# lets say we have some fruits and we want to store fruits name in the list.

fruits = ["Oranges","Apple","Kiwi"] # I love apples

# we should be thinking now, how to access any of these fruits. So, in programmming language when we use a list or array,
# the data can be accessed using index value

# Index starts with 0 .

print(fruits[0]) #output: Oranges
print(fruits[1]) #output: Apple

# basically the range of a list is from 0 to list size - 1

# we can also iterate over a list

for fruit in fruits:
    print(fruit)
    
# Easier way to do this is:

print(fruits[:1]) # If we dont provide the start index, then by default it starts from 0 and the end index doesnt included in the range. end index - 1

# we can also give range in negative number

print(fruits[-3:-2]) # -1 starting from the end and -3 is the first item in the given example

# What if we need the length of the list

print(len(fruits)) # 3

# check the data type of a list

print(type(fruits)) # <class 'list'>


# Lets change an item in the list

fruits[2] = "Mango"

print(fruits) # ['Oranges', 'Apple', 'Mango']

# we can also update the items based on range

fruits[0:3] = ["Banana","Watermelon","Grapes"] 

print(fruits) # ['Banana', 'Watermelon', 'Grapes']

# To insert an item without replacing , we can use insert function

fruits.insert(2,"Apple") # We need to specify the index and time complexity to insert is O(n)

print(fruits) # ['Banana', 'Watermelon', 'Apple', 'Grapes']

# Lets say , we dont want to mention the index for insertion and we just want to add any item to the list

fruits.append("Kiwi") # This will add new item in the end

print(fruits) # ['Banana', 'Watermelon', 'Apple', 'Grapes', 'Kiwi']

# Lets say, we want to remove an item from the list

fruits.remove('Watermelon') # ['Banana', 'Apple', 'Grapes', 'Kiwi']
print(fruits)

# now, we can remove based on index as well

fruits.pop(0) # ['Apple', 'Grapes', 'Kiwi']

print(fruits)

# if we dont specify the index, then it will pop the last item

fruits.pop()

print(fruits) # ['Apple', 'Grapes']

# we can use del keyword also to delete an item

del fruits[1]

print(fruits) # ['Apple']

# We can clear the list as well

fruits.clear()

print(fruits) # []

# Iteration

fruits = ["Apple","Banana","Orange"]

# we can print each item in the list

for fruit in fruits:
    print(fruit)
    
# We can also iterate using index values:

for i in range(len(fruits)): # range is from 0 to 3 where 3 is excluded
    print(fruits[i])
    
 # we can do this by using list comprehension
 
print("List Comprehension")
[print(fruit) for fruit in fruits]

# List Comprehension

# This is basically a shorter index to generate a new list from an existing list

# For example, lets say we want the list of fruits where Banana is not included

fruitsWithoutBanana = []

for fruit in fruits:
    if fruit != "Banana":
        fruitsWithoutBanana.append(fruit)
        
print(fruitsWithoutBanana)

# Now, this can be done using list comprehension

# [expression iterable condition]

# Expression is nothing but the item we want to store in new list
# iterable is the existing list
# Condition is to filter the data based on any condition

fruitsWithoutBanana = [fruit for fruit in fruits if fruit != "Banana"]
print(fruitsWithoutBanana)

# Sorting a list

# By default, sort method sorts the data in alphabetical order or ascending order
fruits.sort()
print(fruits) # ['Apple', 'Banana', 'Orange']

# We can also sort in descending order by mention reverse

fruits.sort(reverse=True)
print(fruits) # ['Orange', 'Banana', 'Apple']

# we can sort based on specified condition by writing our own funtion

def customSort(item):
    return "Ba" in item

fruits.sort(key = customSort)
print(fruits)