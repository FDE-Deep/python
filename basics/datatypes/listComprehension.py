#List Comprehension is a concise way to create lists in python. It is a syntactic construct which allows us to create a new list based on the values of an existing list.

## The basic syntax of list comprehension is as follows:

#[expression for item in iterable if condition]

#lets say you have some student data and you want to create a list of students who have passed the exams

student_data = [{'name':'name_one','pass':True},{'name':'name_two','pass':False}]

#Without list comprehension

student_passed = []

for student in student_data:
    if(student['pass']):
        student_passed.append(student)
        
print(student_passed)

#with list comprehension:

student_passed = [student for student in student_data if student['pass']]

print("list comprehension ")
print(student_passed)

#few more examples of list comprehension


#lets add only even  number

even_numbers = [number for number in range(20) if(number % 2 == 0)]

print(even_numbers)


even_numbers_booleans = [number if number% 2== 0  else False for number in range(20)]

print(even_numbers_booleans)