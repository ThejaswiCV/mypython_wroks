#0 1 1 2 3 5 8 13 21 34

prev=0
curr=1
print(prev)
print(curr)
i=1

while(i<=10):
    next=prev+curr
    print(next)
    prev=curr
    curr=next
    i+=1