text="ABBCDDEFFG"

wc={}
for ch in text:
    if ch not in wc:
        wc[ch]=1
    else:
        wc[ch]+=1
        
print(wc)

#non repeating character

for k,v in wc.items():
    if v==1:
        print(k)

        


 