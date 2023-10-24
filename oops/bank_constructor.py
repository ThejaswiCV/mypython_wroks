class Bank:
    ac_no:int
    ac_type:str
    bank_name:str
    ifsc:str
    name:str
    balance:int
    
    def __init__(self, ac_no,ac_type,bank_name,ifsc,name,balance):
        self.ac_no=ac_no
        self.ac_type=ac_type
        self.bank_name=bank_name
        self.ifsc=ifsc
        self.name=name
        self.balance=balance
        
    def widraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"your {self.bank_name} account {self.ac_no} has debited an amount of {amount}.avilable balance is {self.balance}")  
        else:
            print("transaction declined..!")
            
    def deposit(self,amount):
        self.balance+=amount         
        print(f"your {self.bank_name} account {self.ac_no} has credited an amount of {amount}.avilable balance is {self.balance}")  
          
    def balance_enq(self):
        print(f"your {self.bank_name} acno {self.ac_no} current balance is {self.balance}")     
        
        
        
obj=Bank(1234578911,"savings","canara","CNRB12345","Thejaswi",25000)
obj.balance_enq()    
obj.widraw(5000)
obj.deposit(10000)



















 
