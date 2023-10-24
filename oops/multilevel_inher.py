class P1:
    def m1(self):
        print("inside parent 1")
        
class P2(P1):
    def m2(self):
        print("inside parent 2")
        
class Child(P2): #multiple inheritance
    def m3(self):
        print("inside child")
        
ch=Child()

ch.m1()
# ch.m2()
# ch.m3()                                   
