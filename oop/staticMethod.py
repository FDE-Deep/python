# lets learn about static method

# A static method is like a normal function which doesnt have access to class or object unless it is passed as an argument explicitly

# lets say you have student data and you just want to check if a student has cleared the exam or not.

class student_data:
    
    def __init__(self,name,clearedExam):
        self.name = name
        self.clearedExam = clearedExam
        
    def printStudentName(self):
        print("Name of the student is ",self.name)
        
    @staticmethod
    # Reason why we created a static method is , because its just a utility function which is just determining whether student has cleared the exam or not
    def hasStudentClearedExam(obj):
        if(obj.clearedExam == 'Yes'):
            return True
        return False
    

s = student_data("Name_One","Yes")
if(student_data.hasStudentClearedExam(s)):
    s.printStudentName()
    
        