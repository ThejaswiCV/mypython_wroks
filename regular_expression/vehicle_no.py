from re import*

#KL 58 C 7898

veh_no=input("enter vehicle number")
pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"

matcher=fullmatch(pattern,veh_no)

print("invalid" if matcher==None else "valid")