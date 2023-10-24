from re import*
#rule for entering mobile number
#can start with or without 91
#should contain 10 digit


text=input("enter mobile number")
pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else "valid")