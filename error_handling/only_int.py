val=input("enter number")

#only int allowed

# if val.isdigit()==False:
#     raise Exception("only intergers allowed")
# else:
#     print("sucess")


#Alphabet and number

if val.isalnum()==False:
    raise Exception("only alphabet and numbers allowed")

else:
    print("success")
    
