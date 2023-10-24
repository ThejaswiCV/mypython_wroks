lst=[1,2,4,2,6,7,8,3]
#    0 1 2 3 4 5 6 7
#      i
#    x   z
count=0
for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if(x<y>z or x>y<z):
        count+=1
        
print(count)        