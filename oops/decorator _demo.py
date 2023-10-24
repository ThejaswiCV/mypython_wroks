class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept
    @property
    
    def get_name(self):
        return self.name
    
    @property
    def get_salary(self):
        return self.salary
    
Emp=Employee("hari",50000,"Dev")           
print(Emp.get_name)     
print(Emp.get_salary)
print(Emp.__class__)

