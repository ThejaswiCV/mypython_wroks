for row in range(1,7): #1 #2
    for space in range(5,row-1,-1): #(5,0,-1)#(5,1,-1)
       print(end=" ")#
    for col in range(1,row+1):#(1,2)#(1,3)
        print("* ",end="")
    print()       