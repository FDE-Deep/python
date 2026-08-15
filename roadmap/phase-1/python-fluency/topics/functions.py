# whta is *args and **kwargs in python ?

# *args is the arguments in a function and used as tuple.
# **kwargs is the arugments in a function used as dict.

# Write multiply(*args) that returns the product of all numbers passed. Test with multiply(2, 3, 4) and multiply(5). (Hint: start result = 1, loop args.)

def mulitply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(mulitply(2,3,4)) # 24
print(mulitply(5)) # 5

# Write make_profile(**kwargs) that loops over the pairs and prints "key: value" for each. Test with make_profile(name="Xicor", city="Tokyo", age=22).

def make_profile(**kwargs): # kwargs is dicitonary
    for key,value in kwargs.items():
        print(key,":",value)
        
make_profile(name="Xicor", city="Tokyo", age=22)
# name : Xicor 
# city : Tokyo
# age : 22

# Write greet(greeting, *names) where greeting is a single word and *names collects any number of names, printing "{greeting}, {name}!" for each. Test with greet("Hello", "Amy", "Ben", "Cara").

def greet(greeting,*names):
    for name in names:
        print(f"{greeting}, {name} !")
        
greet("Hello", "Amy", "Ben", "Cara")

# Hello, Amy !
# Hello, Ben !
# Hello, Cara !

# Write func(a, b, *args, **kwargs) that prints all four of a, b, args, kwargs separately. Predict the output of func(1, 2, 3, 4, x=10, y=20) before running — specifically, what lands in args vs kwargs.

def func(a,b,*args,**kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    
func(1, 2, 3, 4, x=10, y=20)
# prediciton 1,2 are the part of a,b. (3,4) = args, kwargs = {"x":10,"y":20}    

# 6. Write call_it(func, *args, **kwargs) that takes any function plus any arguments, and calls that function with them: func(*args, **kwargs). Test it two ways: call_it(add, 1, 2, 3) and call_it(make_profile, name="X", age=22). (This is the exact pattern a decorator uses — a wrapper that forwards whatever arguments to whatever function. Notice you gather with *args/**kwargs in the definition, then spread them back with *args/**kwargs in the call.)

def add(*args):
    return sum(args)
    
def call_it(func,*args,**kwargs):
    return func(*args,**kwargs)

addIt = call_it(add,1,2,3,4)
print(addIt)
call_it(make_profile, name="X", age=22)


def make_log(func):
    def wrapper(*args,**kwargs):
        print("Calling ...")
        result = func(*args,**kwargs)
        return result
    return wrapper

sum_log = make_log(add)
print(sum_log(1,2,3))

profile_log = make_log(make_profile)
print(profile_log( name="X", age=22))

# make_log accepts a function , pass it to the wrapper definition , calls the functions and return the result from wrapper and make_log returns the wrapper
# when we call make_log , it returns the wrapper having access to the func which we pass as argument
# Now, this wrapper can have access to all the arguments and can be passed down to the func which is passed to make_log
# Then , we call the function created using make_log and pass our desired data.

# Mutable-default trap

# how to reproduce this error. This error is not a syntax error so you wont see in console

def createList(item,items = []): # By default items we are setting it as empty array.
    items.append(item)
    return items

print(createList(1)) # [1]
print(createList(2)) # [1, 2]
print(createList(3)) # [1, 2, 3]

# if we observe, instead of creating a new list, it has added all the items in one list
# Reason is, list is mutable. When we define it as empty by default during definition, when we call the function, it will refer to the same default list.
# which is why it keeps on adding the items to the same list

# How to fix it.

# set items as None because this is immutable

def createList(item,items = None):
    if(items is None):
        items = [] #  create a fresh list
    items.append(item)
    return items

print(createList(1)) # [1]
print(createList(2)) # [2]
print(createList(3)) # [3]

# In my brain, am thinking like we have a big box and i put one small box into that and i mentioned whatever i put it will go to that small box by default
# but in reality, we are looking to add new box every time in a big box

# now the big box is set to none
# It will always be empty for each function call