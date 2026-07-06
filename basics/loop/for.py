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
    
    
#Lets say we have student data and we want to only print student data who has taken the admission

student_data = [{
    'name':'name_1',
    'age':'age_1',
    'takenAdmission':True
},
{
    'name':'name_1',
    'age':'age_1',
    'takenAdmission':False
}]

#we will use continue to skip the student who has not taken the admission

for student in student_data:
    if(student['takenAdmission'] == False):
        continue
    print("Name is: ",student['name'])
    print("Age is: ",student['age'])
    print("Taken Admission",student['takenAdmission'])
    
# Now lets say some student have incorrect data and we want to return student name for that

name=''

student_data = [{
    'name':'name_1',
    'age':'age_1',
},
{
    'name':'name_1',
    'age':'age_1',
    'takenAdmission':False
}]

for student in student_data:
    if(student.get('takenAdmission',False) == False):
        name=student['name']
        break
    if(student['takenAdmission'] == False):
        continue
    print("Name is: ",student['name'])
    print("Age is: ",student['age'])
    print("Taken Admission",student['takenAdmission'])
    
if(name != ''):
    print(name," has incorrect data. Please fix it")
else:
    print("All good")