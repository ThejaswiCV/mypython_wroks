num=int(input("enter a number")) #eg:123

sum=0
while(num!=0):
    last_digit=num%10 #123%10=3 #12%10=2 #1%10=1
    cube=last_digit**3 #3^3  #+2^3  #+1^3
    sum=sum+cube #0+3^3  #+2^3  #+1^3
    num=num//10 #123//=12   #12//10=1  1//10==0
print(sum)    