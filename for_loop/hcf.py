num1=int(input("enter first no"))
num2=int(input("enter second no"))

small_no=num1 if num1<num2 else num2
hcf=1
for i in range(1,small_no+1):
    if(num1%i==0) and (num2%1==0):
        hcf=i
print(hcf)        
