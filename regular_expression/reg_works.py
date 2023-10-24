from re import*
text="abababcabb"
    # 0123456789
pattern="ab"

matcher=finditer(pattern,text)

count=0
for m in matcher:
    print(m.start(), m.group())
    count+=1
    
print("ocurrence of pattern",count)    