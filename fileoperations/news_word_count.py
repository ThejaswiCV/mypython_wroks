f=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\news.txt","r")

wc={}
for line in f:
    word=line.rstrip("\n").split(" ")
    # print(word)
    for w in word:
        if w not in wc:
           wc[w]=1
        else:
            wc[w]+=1 

print(wc) 

# for w in word :
#     if wc[w]>=2:
#         print(w)

      