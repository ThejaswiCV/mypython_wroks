class Student:
    roll:int
    name:str
    course:str
    
    def __init__(self,roll,name,course):
        self.roll= roll
        self.name=name
        self.course=course
        
    def display(self):
        print(self.roll,self.name,self.course)
        
obj1=Student(17,"Thejaswi","Electronics")
obj1.display()            