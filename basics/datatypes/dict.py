#What is a dictionary?

# A dictionary is a collection of data in the form of key value pair

dict1 = {};

print(type(dict1)) #<class 'dict'>

#Lets say you have student data which includes name and age and there are 3 students

students = {1: {
    'name':'A',
    'age':'20'
    },
    2:{
        'name':'B', 
        'age':'21'
    },3:{
        'name':'C',
        'age':'22'
    }
    }

print(students)

#Now lets say you want to access student 1 data

print("\n---- Student 1 Data is as following ------\n")

print(students[1])

print("\n---- Student 2 Data is as following ------\n")

print(students[2])

print("\n---- Student 3 Data is as following ------\n")

print(students[3])

#, access the name only for student 1

print("Name of student 1 is: ",students[1]['name'])


# We can use get method also

print(students.get(1))

# Lets say you are trying to access the key which is not present. In this case, we can set default value

print(students.get(10,'not found'))

print(len(students))