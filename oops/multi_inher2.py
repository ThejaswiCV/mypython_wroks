class P1:
    def m1(self):
        print("inside parent 1")  #same method
        
class P2: 
    def m1(self):                 #same method
        print("inside parent 2")
        
class Child(P1,P2): #multiple inheritance
    def m3(self):
        print("inside child")
        
ch=Child()
ch.m1()      #interpreter . so inside parent 1 will work
                                  