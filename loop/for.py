#lets say we have a data in a dictionary in array and we want to print the values 

student_data = [{
    'name':'name_1',
    'age':'age_1'
},
{
    'name':'name_1',
    'age':'age_1'
}]

for student in student_data:
    print("Name is: ",student['name'])
    print("Age is: ",student['age'])