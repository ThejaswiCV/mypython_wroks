from abc import ABC,abstractmethod

class Car(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def acclerate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Fortuner(Car):
    
    def start(self):
        print("fortuner start method")
        
    def acclerate(self):
        print("fortuner accelerate method")
        
    def stop(self):
        print("fortuner stop method") 
        
obj=Fortuner()
obj.start()
obj.stop()        
print(obj.__class__)           