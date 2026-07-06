#Lets say you want to add a string to your program. Syntax is to assign a value to a variable using single quotes or double quoutes

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

# Lets say you have two strings and you want to concatinate them:
str1="Hello "
str2="World"

print(str1+str2)

# how to add a string in multiple lines

str = "Hello, My name is Deep Singh.\nI am a good person"
print(str)

# there is an another way to do it by using """

str3="""Hello How you doing?
I am doing good. Thank you for asking."""

print(str3)

# lets say you want to just print first character of the string. We can do it by using the index values. Index value starts from  0 to string length - 1.

print(str3[0])

#print first five characters. SO range should be from 0 to 4 + 1 = 5. We are adding plus 1 so that it can print first 5 characters and in normal language 1 to 5 are our characters but as per index logic 0 to 4 are our characters. So we give 0 to 5 and 5 is exclusive.


print(str3[0:5])

#Also, if our starting index is always 0 , then we can ignore it also

print(str3[:5])

#Now lets say start index is different and end index will always be the str.length - 1

print(str3[5:])

#we can print letter in reverse order also by using negative index. it starts from -1 to str length.

print(str3[-1:-6:-1])

#to find the len of string:

print(len(str3))