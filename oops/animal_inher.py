class Animal:
    def __init__(self,name):
        self.name=name   #attribute
    
    def sound(self):  #method
        pass
    
    
class Dog(Animal):
    
    def sound(self):  #method overriding
        print(f"{self.name} barks")
        
                    
class Frog(Animal):
    
     def sound(self):
        print(f"{self.name} croaks")
                           
 
do_obj=Dog("Dog")
do_obj.sound()            #calling a method , so need ()
print(do_obj)             #address
print(do_obj.__class__)   #which class the object belongs to  #it is attribute not method

fr_obj=Frog("Frog")
fr_obj.sound()                         