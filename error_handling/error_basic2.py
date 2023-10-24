n1=int(input("enter first num"))
n2=int(input("enter second num"))


try:
    res=n1/n2
    print(f"{res} is the answer")   
except Exception as e:
    n2=int(input("enter second num"))    #again chance to put n2=0, no exception for this block.
    res=n1/n2                               #so error will show but "finally" block will work 
    print(f"{res} is the answer")   

finally:   #this block will work, no matter what the error
    
    print("data base commit")
    print("file transaction")