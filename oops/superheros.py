class SuperHeros:
    
    def __init__(self,name): 
       self.name=name
       
    def super_powers(self):
        self.context=["fly","jump","run"]
        return self.context

class SpiderMan(SuperHeros):
    
    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("spread web") 
        return self.context   
    
class Minnal(SuperHeros):
    def super_powers(self):
        self.context=super().super_powers()
        self.context.remove("fly")
        self.context.append("speed")
        return self.context

su=SpiderMan("Spide man")
print(su.super_powers())

mi=Minnal("Minnal murali")
print(mi.super_powers())