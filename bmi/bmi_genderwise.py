gender="women"
tummy_size=60
buttocks_size=75
value=tummy_size/buttocks_size
print(value)

if (gender=="men"):
    if(value<0.95):
        print("low health risk")
    elif(value>=0.95 and value<1):
        print("moderate health risk")
    else:
        print("high health risk")
elif(gender=="women"):
    if(value<0.80):
        print("low health risk")
    elif(value>=0.80 and value<0.85):
        print("moderate health risk")
    else:
        print("high health risk")
            
        
            
