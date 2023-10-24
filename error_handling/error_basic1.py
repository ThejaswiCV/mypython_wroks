n1=int(input("enter first num"))
n2=int(input("enter second num"))
loc=int(input("enter index position"))

lst=["10","20","30"]
 

try:
    res=n1/n2
    print(f"{res} is the answer")
    
except Exception as e:
    print("exception occurred")    
    
try:
    print(lst[loc])
except Exception as e:
    print(e.args)       #show error details
    

print("data base commit")
print("file transaction")