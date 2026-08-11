# A dictionary is a collection of data which is ordered, changeable and do not allow duplicates.
# As of python version 3.7, it is ordered before that it was un-ordered.
# It allows to store data in key value pair.

student_data = {
    "name":"studen1",
    "age":"20",
    "rollNo":"12"
}

print(student_data) # {'name': 'studen1', 'age': '20', 'rollNo': '12'}
print(type(student_data)) # <class 'dict'>

# To check the length of given dictionary, use len method

print(len(student_data)) # 3


# Python - Access Dictionary Items

# Accessing items - we can access the items of a dictionary by referring to its key name inside square bracket

print(student_data["name"]) # studen1

# There is also a get method that will give us the same result

name = student_data.get("name")
print(name) # studen1

# We can also get the list of keys only by using keys() method

student_data = {
    "name":"Xicor"
}

keys = student_data.keys()
print(keys) # dict_keys(['name'])

# The list of keys is a view of the dictionary, meaning that any change
# done to the dictionary will be reflected in the keys list

student_data["class"] = "A"
print(keys) # dict_keys(['name', 'class'])

# We can also get the list of values by using values() method

values = student_data.values()
print(values) # dict_values(['Xicor', 'A'])

# The list of values is a view of the dictionary, meaning that any change
# done to the dictionary will be reflected in the keys list

student_data["rollno"] = "2"
print(values) # dict_values(['Xicor', 'A', '2'])

# Get items - we can use method items to get  each item in dictionary as tuples in a list

tuple = student_data.items()
print(tuple) # dict_items([('name', 'Xicor'), ('class', 'A'), ('rollno', '2')])

# To check if a key exist in the dictionary

print("name" in student_data) # True

# Change items

# We can change the value of an item in dictionary by accessing its key

student_data["rollno"] = 20

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': 20}

# We can also use update method.We need to pass a dictionary or iterable object with key value pair

student_data.update({"rollno":"500"})

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': '500'}

# Add items

# We can add items to the dictionary by creating new key:value pair

student_data["hasIdCard"] = True

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': '500', 'hasIdCard': True}

# We can also use update method. If key doesnt exist then it creates a new entry

student_data.update({"topTalent":"Yes"})

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': '500', 'hasIdCard': True, 'topTalent': 'Yes'}

# Removing items

# There are several methods to remove items from a dictionary

# pop() - removes the items with the specified key name

student_data.pop("topTalent")

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': '500', 'hasIdCard': True}

# popitem() methods removes the last inserted item(in version before 3.7, a random item is removed instead)

student_data.popitem()

print(student_data) # {'name': 'Xicor', 'class': 'A', 'rollno': '500'}

# The del keyword removes the item with the specified key name

del student_data["rollno"]

print(student_data) # {'name': 'Xicor', 'class': 'A'}

# It can delete the entire dictionary also

# clear method clears the dictionary but dont delete it

student_data.clear()

print(student_data) # {}

# Loop through a dictionary

# When we use for loop , it returns all the keys only

student_data = {
    "name":"Xicor",
    "rollNo":"5",
    "dateOfBirth":"01/01/2000"
}

for key in student_data:
    print(key,end=" ") # name rollNo dateOfBirth 
    
for key in student_data:
    print(student_data[key],end=" ") # Xicor 5 01/01/2000
    
# To get a key value pair, we can use items()

print()
for key,value in student_data.items():
    print(key," = ",value)
    
# name  =  Xicor
# rollNo  =  5
# dateOfBirth  =  01/01/2000

# Python - Copy Dictionaries

# We cannnot copy a dictionary simply by typing dict2 = dict1, because
# dic2 will only be a reference to dict1, and any changes made in dict1
# will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dcitionary method copy()

student_data_copy = student_data.copy()

print(student_data_copy) # {'name': 'Xicor', 'rollNo': '5', 'dateOfBirth': '01/01/2000'}

# Another way to make a copy is to use the built in function dict()

student_data_copy_dict = dict(student_data_copy)

print(student_data_copy_dict) # {'name': 'Xicor', 'rollNo': '5', 'dateOfBirth': '01/01/2000'}

# Python - Nested Dictionaries

# Lets say , we have school data which includes students, teachers.

students = {
    "data": [{
        "name":"Xicor"
    }, {
        "name": "Vegeta"
    }]
}

teachers = {
    "data": [
        {
            "name":"Master Roshi"
        }, {
            "name": "Korin"
        }
    ]
}

# nested dictionary

school = {
    "students":students,
    "teachers":teachers
}

# loop

for role,group in school.items():
    print(f"{role}:")
    for person in group.get("data",[]):
        print(f"{person.get("name"," ")}")


