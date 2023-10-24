class Books:
    name:str
    author:str
    price:int
    publisher:str
    
    def set_book(self,name,author,price,publisher):
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher
        
    def display(self):  
        print(self.name,self.author,self.price,self.publisher)  
        
    def __str__(self) : #string representation of an objecet( for str only)
        return self.name
        
book1=Books()
book1.set_book("Alchemist","Paulo coehlo",500,"ws books")
book1.display()   
print(book1)       #print book name only