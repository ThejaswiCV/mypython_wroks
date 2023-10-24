num=123

while(num!=0):#123!=0 true  #12!=0 true #1!=0 true #0!=0 false
    last_digit=num%10 #123%10=3 #12%10=2 #1%10=1
    print(last_digit)#3 #2 #1
    num=num//10 #123//10=12 #12//10=1 #1//10=0