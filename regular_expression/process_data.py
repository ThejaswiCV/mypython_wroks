from re import*

f=open("C:\\Users\\Sinju\\Desktop\\mypython\\regular_expression\\data.txt")

pattern="[a-z0-9_.]+@[a-z]{2,}.com"

for line in f:
    email=line.rstrip("\n")
    # print(email)
    matcher=fullmatch(pattern,email)
    if matcher!=None:
        print(email)