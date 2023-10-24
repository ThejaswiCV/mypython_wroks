# *      *       *       *       *
# *      *       *       *       *
# *      *       *       *       *
# *      *       *       *       *
# *      *       *       *       *
# *      *       *       *       *

for row in range(1,7):
    for col in range(1,6):
        print("*",end="\t")
    print()   

    
# 1     1       1       
# 2     2       2       
# 3     3       3   
# 4     4       4

for row in range(1,5): #row1 #row2
    for col in range(1,4): #col1 col2 col3
        print(row,end="\t")  #1 1 1 #2 2 2 
    print() #1st row end     
    
    
# 1     2       3
# 1     2       3
# 1     2       3  

for row in range(1,4):
    for col in range(1,4):
        print(col,end="\t") 
    print()    
    
    
 # 1 2 3 4
 # 1 2 3
 # 1 2
 # 1
 
for row in range(5,0,-1):   #5 #4
     for col in range(1,row): #(1,5) #(1,4)
         print(col,end="\t")
     print() 