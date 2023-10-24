lst=[1,2,4,2,6,7,8,3]
#    0 1 2 3 4 5 6 7
#      i
#    x   z
p_count=0
v_count=0
for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if x<y>z:
        p_count+=1
    elif x>y<z:
        v_count+=1
        
print("peak count",p_count)    
print("valley count",v_count)    