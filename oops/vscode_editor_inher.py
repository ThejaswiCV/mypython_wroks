class Editor:
    def __init__(self,name):
        self.name=name
        
    def spec(self):
        pass
    
    
class Vscode(Editor):
    def spec(self):
        print(f"{self.name} supports edit, debug,run and extension support")
        
    def __str__(self) :
        return self.name  
    
class pycharm(Editor)  :
     def spec(self):
        print(f"{self.name} supports edit, debug and run ")  
        
     def __str__(self) :
        return self.name  
       
    
vs_obj=Vscode("Vscode")
print(vs_obj)  
vs_obj.spec()


py_obj=pycharm("pycharm")
print(py_obj)
py_obj.spec()      
  