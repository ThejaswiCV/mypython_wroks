class Employee:
    id:int
    name:str
    dept:str
    salary:int
    
    def set_employee(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
        
    def display(self):
        print(self.id,self.name,self.dept,self.salary)       
        
        
#reference_name=Class name
emp1=Employee()
emp1.set_employee(100,"Theju","senior dev",50000)
emp1.display()
        
emp2=Employee()
emp2.set_employee(101,"Tintu","manager",100000)      
emp2.display()  
         