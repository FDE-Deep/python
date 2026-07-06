#Lets learn about Object Oriented Programming in python
# What is a class ?
# Before we understand what is a class, we need to understand what is an object. An object is a real world entity. For example, a pen, a chair, a table, a laptop etc. All these are objects.
# Now, a class is a blueprint or template for creating objects. It defines the properties and behaviors of the objects that are created from it.

class student:
    pass

#lets call this class

s = student

print(type(s)) # This is returning <class 'type'> . But it should return the type "student". Issue is we are not calling the class . We are assigning it to a variable .

#In order to call a class, we need to use () paranthesis

s = student()

print(type(s)) # output : <class '__main__.student'>

# Now ,as we discussed earlier, we know a class should have properties and some behavior. Behavior is nothing but functions defined in class and known as methods

class student:
    def printName():
        print("My name is student one")
        

# Now, lets call this printName method

#printName() # NameError: name 'printName' is not defined. Because it is the part of class.


#In order to call a method of a class, we can use classname .

student.printName() # output: My name is student one

#But as we mentioned earlier, it should have an object.. So, lets create an object of a class

student_1 = student();

# Now, in the above statement when we are calling the student.printName(), it should access the object also which we have created.Because we can have multiple students.
#And each object represents a student

#student.printName(student_1) #TypeError: student.printName() takes 0 positional arguments but 1 was given.
#In the above statement, we got an error. This is because, when we pass an object to a class, its context or object should be passed to methods.
#In python, the argument name which is being used mostly by python developers is "self". Self is nothing but an current object created for a class

class student:
    def printName(self):
        print("MY name is student one")
        

student_1 = student()
student.printName(student_1) # Output: MY name is student one

#There is a better way to call a method of a class by directly calling the method using object

student_1.printName() 

# Now, here we have one problem. Even though , i create 100 objects and call printName method, i will get the same name. 
# But i want name to be dynamic. We can do this by adding __init__ method in the class. This gets called everytime when we create an instance of a class

class student:
    def __init__(self):
        self.studentName = "student_one"
        
    def printName(self):
        print("My name is ",self.studentName)
        
student_one = student()
student_one.printName()

#Again the problem is same. We have a static name. So,to make it dynamic, we need to pass name in () paranthesis as argument sot that __init__ can accept it

class student:
    def __init__(self,student_name):
        print("Init called")
        self.studentName = student_name
        
    def printName(self):
        print("My name is ",self.studentName)
        

student_one = student("student_one")
student_two = student("student_two")
student_one.printName() # My name is  student_one
student_two.printName() # My name is  student_two