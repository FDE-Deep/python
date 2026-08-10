# A tuple is a collection of data which is ordered.
# A tuple is indexed based and unchangeable(It cannot be updated once created)
# To create a tuple, we use round brackets

student_data = ("Rahul",20,1) # name,age,roll_no

print(student_data)

# As a tuple is indexed based, we can access it using index value starting from 0

print("Student name is = ",student_data[0]) # Student name is =  Rahul
print("Student Age is = ",student_data[1]) # Student Age is =  20
print("Student Roll no is = ",student_data[2]) # Student Roll no is =  1


# We can access tuple items using range as well

print(student_data[:2]) # ('Rahul', 20) If we dont mention the starting index, it starts with 0 and end index item doesnt include in the range

print(student_data[1:2]) # (20,)

# We can also use negative index as well . -1 means last item in the tupple

print(student_data[-1])

# We can also check if an item is present in tuple

if "Rahul" in student_data:
    print("Yes")
else:
    print("No")
    
# Also, lets say we want to add only one item in tuple

data = (1)
print(type(data)) # <class 'int'>

# If we observe the data type of data is int not tuple. The reason, python recgonize a tuple when we add a comma as well

data = (1,)

print(type(data)) # <class 'tuple'>

# Update a tuple.

# A tuple is unchangeabe and immutable. It cannot be updated directly. But there is a workaround for it.
# We can convert a tuple into a list and then makes changes to that list and convert it back to tuple

student_data = ("Rahul",20,1)# Name,Age,Roll_No

# Lets say , we want to update the Roll_No, as we found out that it is wrong

student_data_list = list(student_data)

student_data_list[2] = 12

student_data = tuple(student_data_list)

print(student_data) # ('Rahul', 20, 12)

# Lets say we want to append class name

student_data_list = list(student_data)
student_data_list.append("Section-A")
student_data = tuple(student_data_list)

print(student_data) # ('Rahul', 20, 12, 'Section-A')

# We can add two tupples

tupple1 = ("Apple",)
tupple2= ("ORange",)

tupple1 += tupple2
print(tupple1) # ('Apple', 'ORange')


# Unpacking a tuple

student_data = ("Rahul",20,15) # Name,Age,Roll_No

(name,age,roll_no) = student_data
print(name,age,roll_no) #Rahul 20 15

# Now, lets say ,we want only the name and rest of the data we want to keep in another variable. We can use asterik to store the rest of the data as list

(name,*rest) = student_data
print(name,rest) # Rahul [20, 15]

(name,*rest,roll_no) = student_data

print(name,rest,roll_no) # Rahul [20] 15 basically, python stores all the data in rest until it founds the last item mentioned

# We can also loop through a tuple

for item in student_data:
    print(item)
    
    
# We can join tuples also

tuple1 = (1,)
tuple2 =(2,)

tuple3 = tuple1 + tuple2
print(tuple3) # (1, 2)

# Other methods

# index

print(student_data.index("Rahul")) # 0

# count

print(student_data.count("Rahul")) # 1