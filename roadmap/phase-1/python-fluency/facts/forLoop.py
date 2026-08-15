# Do we know what happens when we run the for loop?

# There are two things called iterables and iterators

# An iterable is anything you can loop over. For example - list, dict,string,tuple,range etc

# An iterator is an acutal worker that produces item one at a time

nums = [1, 2, 3]
listIter = iter(nums)

print(list(listIter))  # [1, 2, 3]
print(list(listIter))  # []

# Now, if you observe, the above listIter was spent only once. Once it does its job, it exhausts.
# If we want again, then we need to create new iter for that

# Now, next() returns the next element from the iterator and advances its position by one. When there are no elements left, it raises StopIteration.

it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it)) # StopIteration

# In the last print statement, if you see , we get the StopIteration error. This is because there is no element to iterate over.

# Summary:

# An iter produces a worker which points to the first item in the list
# Whenever you call next() , it returns the item and move the pointer to the next position
# If there is nothing to move to next, it throws StopIteration exception
