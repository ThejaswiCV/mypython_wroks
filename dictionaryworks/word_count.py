words=["hello","hai","hello","hai","hai","good","verygood","nice"]

wc={}
for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
        
print(wc)