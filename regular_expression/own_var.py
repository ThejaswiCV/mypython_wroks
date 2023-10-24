#starts with k,l,m,n
#second must be digit and divisible by 3
#then folllowed by any number of alphabet and digit

from re import*

text=input("enter the variable")
pattern="[k-n][369][a-zA-Z0-9]*"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else "valid")
