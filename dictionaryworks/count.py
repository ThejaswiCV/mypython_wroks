text="hello, hallo hello hai hlo, hlo hai.."
words=text.casefold().replace(",","").split()
print(words)

wc={}
for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
        
print(wc)        
