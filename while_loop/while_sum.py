#print sum between 2 numbers including that numbet

start=int(input("enter starting value"))
end=int(input("enter end value"))

sum=0
while(start<=end):
    sum=sum+start
    start+=1
    
print(sum)    