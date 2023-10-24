#print last digit

num=int(input("enter a number"))
last=(num%10)
print(f"last digit of number {last}")

#last digit divisble by 3 or not

if(last%3==0):
    print(f"{last} is divisible by 3")
else:
    print(f"{last} is not divisible by 3")



