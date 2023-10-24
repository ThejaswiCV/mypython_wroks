class School:
    name:str
    place:str
    pincode:int
    state:str="KERALA"
    
    def __init__(self,name,place,pincode):
        self.name=name
        self.place=place
        self.pincode=pincode
        
    def display(self):
        print(self.name,self.place,self.pincode,School.state) 
        
obj1=School("cet","thalassery",670641)
obj1.display()           

obj2=School("cev","vadakara",640529)
obj2.display()            
