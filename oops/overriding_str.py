class Book(object):
    def __init__(self,name) :
        self.name=name
        
    # def __str__(self) :               #overriding
    #        return self.name          
        
ob=Book("Alchemist")
print(ob)        #invoke __str__() method of parent class object #show address
        