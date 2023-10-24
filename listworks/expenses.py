#          0       1     2     3    4    5      6     7
expenses=[12000,13000,25000,30000,55000,60000,78000,450000]

count=len(expenses)
for i in range(0,count):
    print(expenses[i])
    
expenses[1]=20000
print(expenses)    

total=0
for i in range(0,len(expenses)):
    total=total+expenses[i]
   
print(total)  

total=sum(expenses)
print(total)  

sm_exp=min(expenses)
print(sm_exp)

lg_exp=max(expenses)
print(lg_exp)

srt_exp=sorted(expenses)
print(srt_exp)

rev_exp=sorted(expenses,reverse=1)
#0>>>false   #other than 0>>> true    
print(rev_exp)

