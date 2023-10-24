class Operations:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=Operations()
# op.add(10,20)    #n3 and n4 missing error
print(op.add(10,20,3,4))