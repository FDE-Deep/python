# Lets print our first python program
print("Hello World")

# Variables are used to store data in a program. They can be of different types such as integers, floats, strings, etc.

# you can store a number in a variable. Syntax is very simple . Just think of a variable name and assign a value to it.
num = 0
print(num)

# num can be used for arithmatic operations also

print(5 + num)
print(5 - num)
print(5 * num)
print(num * 5)

# Now, lets say you want to add a string to your program. Syntax is to assign a value to a variable using single quotes or double quoutes

name="Deep "
print(name)

# We can print the name multiple times

print(name)
print(name)

# but this is hectic and we want to do it in better way . We can tell python to print any number of times by just mentioning * n.

print(name* 10)

# There are some other problems also with strings.

# problem 1: What if you have created a string variable with single quotes and you need another single quotes in the value

#singleQuoteProblem = 'Hi , is this your's';
#print(singleQuoteProblem)

#  File "d:\Plan\projects\python\variables\index.py", line 35
 #   singleQuoteProblem = 'Hi , is this your's';
#                                             ^
#SyntaxError: unterminated string literal (detected at line 35)

# Reason for above error is, Python starts reading the string from first single quotes and it looks for matching closing quote which ended at your and then we are left with one more opening single quote which doesnt have the matching pair"

# To fix this, we do the following :

singleQuoteProblem = "Hi, is this your's"
print(singleQuoteProblem)

# now lets say you want to add double quotes inside the above string

#doubleQuoteProblem = "Hi, "Hello"";
#$print(doubleQuoteProblem)

#   File "d:\Plan\projects\python\variables\index.py", line 52
  #  doubleQuoteProblem = "Hi, "Hello"";
 #                              ^^^^^
#SyntaxError: invalid syntax. Is this intended to be part of the string?

# we can fix this by adding a single quote
doubleQuoteProblem = 'Hi, "Hello"'
print(doubleQuoteProblem)

# Lets try to add file path

#filePath = "C:\user\name"
#print(filepath)

#We get the following error:

#File "d:\Plan\projects\python\variables\index.py", line 66
 #   filePath = "C:\user\name"
  #             ^^^^^^^^^^^^^^
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

#Reason is \n is an escape character which means new line and \u also is an escape character
# to fix this , we add extra back slash so that python can ignore it

filepath="C:\\user\\name"
print(filepath)