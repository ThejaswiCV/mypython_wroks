from re import*

#python variable--can start with a-z or A-Z
#then can contain  a-z ,A-Z, 0-9 and _

text=input("enter variable name")
pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,text)

if matcher == None:
    print("invalid variable")
else:
    print("valid variable")    