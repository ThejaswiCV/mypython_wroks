from re import*
  #   0123456789 111315
text="abaabbbabaaabaaaa"
               #10121416

# pattern="a+"          #atleast one

# pattern="a*"          #matches for any number of a,including zero

# pattern="a?"          #optional

# pattern="a{2}"        #2 ocurrence of a

pattern="a{2,3}"        #min 2 or max 3 group of a


matcher=finditer(pattern,text)  

for m in matcher:
    print(m.start(),m.group())