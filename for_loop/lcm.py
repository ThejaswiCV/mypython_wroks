num1=int(input("enter first number"))
num2=int(input("enter second number"))

sm_num=num1 if num1<num2 else num2
hcf=1
#lcm(n1,n2)=(n1 * n1)/gcd(n1 * n2)
for i in range(1,sm_num+1):
    if(num1%i==0) and (num2%i==0):
        hcf=i

lcm=(num1*num2)/(hcf) 
print(lcm)       
        
