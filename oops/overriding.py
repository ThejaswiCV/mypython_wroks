class Parent:
    def mobile(self):
        print("iphone 14 pro")
    
    def car(self):
        print("BMW")
        
        
class Child(Parent):
       def mobile(self):
        print("iphone 15 pro max")
        
ch=Child()
ch.mobile()
ch.car()     
        
                  