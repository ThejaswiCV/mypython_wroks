for i in range(1,5):#for-else combination will work when for loop doesnt conatin any break statemnet
    print(i)
        
else:
    print("executed")    
    
    
lst=[10,12,14,15]

num=3
for j in range(0,len(lst)):
   if  num==lst[j]:
       print("found")
       break
else:
    print("not found")   
    
    
    
    