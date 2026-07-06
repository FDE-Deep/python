#A tuple is an ordered collection of items in Python, written with parentheses

#what is a difference between list and a tuple

# A list can be mutable but a tuple is immutable

# How to declare a tuple

tup = 1,2,3
print(type(tup))

# we can add a list also. Note that if we have a single item in tuple, then we need to mention a comma in the end

tupList = [1,2,3,4],
print(type(tupList))

#Tuple can also be created using ()

tupListWithRoundBrackets = ([1,2,3,4],)

print("Bracket",type(tupListWithRoundBrackets))

#You can access the members of tuple using index

print(tupList[0])

#if you try to modify the value of a tup , it will throw error

# tupList[0] = [2,3,5] #TypeError: 'tuple' object does not support item assignment

#But you can assign a value to a member if it is a list because list is mutuable

tupList[0][0] = 100

print(tupList) #([100, 2, 3, 4],)

# you can find the len of tup

print(len(tupList))

# you can count the members

print(tupList.count(0))
