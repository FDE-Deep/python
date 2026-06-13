# Write a python program that does the following:
    # Ask the user to enter the student's name
    # Ask the user to enter the student's roll number
    # Print the result

def askForStudentData():
    name = input("Enter the name of the student = ")
    rollNo = input("Enter the roll number of the student = ")
    return {'name': name,'rollNo': rollNo}

def printStudentData(data):
    print("---------------------------------------------")
    print("Name of the student is = ",data['name'])
    print("Roll of the student is = ",data['rollNo'])

studentData = askForStudentData()
printStudentData(studentData)