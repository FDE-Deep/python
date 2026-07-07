# Lets learn about class variables and class methods.

# Lets say you need a variable which needs to be accessed by all methods and its value should remain same or it should be returned by class method. Depends on the scenario

# Class Variable


class example:
    #This is a class variable
    count = 0
    
    def __init__(self,number):
        #Here number is an instance variable
        self.number = number
        
        

# Now, lets see if we can access class variable using object

e = example(3)
print(e.count) # output = 0

# We can access usng an object but value of count is not dependent on object variable

#Now, lets say for each  object creation , we want to count the total objects.

class example:
    #This is a class variable
    count = 0
    
    def __init__(self,number):
        #Here number is an instance variable
        self.number = number
        #To access class variable , we need to use classname
        example.count +=1
        
e1 = example(3)
e2 = example(4)
e3 = example(5)
print(e3.count) #output = 3

# Now, lets say ,same thing we want to do using class method

class example:
    #This is a class variable
    count = 0
    
    def __init__(self,number):
        #Here number is an instance variable
        self.number = number
        #To access class method , we need to use classname
        example.increment_count()
    
    @classmethod #Decorator
    def increment_count(cls):
        cls.count += 1
        
e5 = example(4)
e6 = example(4)

print(e6.count)