# print odd numbers from 1 to 10
i=int(input("enter starting value"))
limit=int(input("enter limit value"))

while(i<=limit):
    if(i%2!=0):
        print(i)
    i+=1    