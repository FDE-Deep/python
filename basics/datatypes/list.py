#What is a list?
#A list is a collection of items which are ordered and changeable. It allows duplicate members.

list = [10,20,30,40,50]

print(list)

# we can also combine two lists

list2= [60,70,80,90,100]

newList = list + list2
print(newList)

# We can access each member of the list by accessing their index

print(newList[0]) # This will print 10

# We can print using range as well

print(newList[:4]) # This mean from 0 to 3

print(newList[4:]) # This means from 4th index till end

print(newList[2:4]) # This means from 2nd to 3rd

#We can also include multiple lists in one list

multipleLists = [list,list2]

print(multipleLists)

# We can access this list using two indexes

print(multipleLists[0][0]) # This will go to the first list and pick the first element from multiple lists

#We can also add a new member to the list

newList.append(110)

print(newList)

#we can also add multiple members

newList.extend([120,130])

print(newList)

#We can also insert an element anywhere in the list using index

newList.insert(1,15)

print(newList)

# we can count the frequency of a member

print(newList.count(15))

#We can get the index of a member

print(newList.index(10))

#We can remove a member from the new list .

newList.pop() # This uses the stack property LIFO. Last In First Out. 

print(newList)

#You can specify the index also

newList.pop(0)

print(newList)

#This removes the element from its first occurence

newList.remove(15)

print(newList)

# WE can delete multiple members also by telling the range of indices

del newList[:4]

print(newList)

#We can revers a list

newList.reverse()

print(newList)

# You can replace members also

newList[5:6] = [10,20]

print(newList)

# you can sort the list also

newList.sort()

print(newList)

#you can sort the list of strings also

stringList = ['b','a','c']

stringList.sort()

print(stringList)