num1=10
num2=40
num3=70

if(num1>num2) and (num1>num3): #possibility for second large is num 2 and num3
    if(num2>num3):
        print("num2 is second largest")
    else:
        print("num3 is second largest")
elif(num2>num1) and (num2>num3): #possibility is for num1 and num3
    if(num1>num3):
        print("num1 is second largest")
    else:
        print("num3 is second largest")
elif(num3>num1) and (num3>num2): #possibilty is for num1 and num2
    if(num1>num2):
        print("num1 is second largest")
    else:
        print("num2 is second largest")            

