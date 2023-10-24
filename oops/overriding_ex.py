class Parent:
    def vehicle(self):
        self.context=["suzuki","tata"]
        return self.context
    
class child(Parent):
    def vehicle(self):
        self.context=super().vehicle()
        self.context.append("hyundai")    
        return self.context
    
p=Parent()
print(p.vehicle())

c=child()
print(c.vehicle())

#self >>currrent object
#super() >>parent object