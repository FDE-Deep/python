# Lets learn about functions

# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def add():
    a = 2
    b = 2
    c = a + b
    print(c)

add()

# the above function only add the numbers which are static a and b. What if we want a and b to be dynamic values
# by making it dynamic, we add call function with different values
def add(a,b):
    c = a + b;
    print(c)

add(2,3)
add(4,5)

# Now, lets say , we want the result back from a function so that it can used somewhere
# To do this, we need to return the result by using return keyword

def add(a,b):
    return a + b

result = add(4,500)
print("Result = ",result)