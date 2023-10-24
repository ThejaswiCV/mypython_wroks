word="hello"
#     01234

print(word.index("e"))
print(word.index("l"))

print(word[0])
print(word[4])

count=len(word)

for i in range(0,count):
    print(word[i],end="")
 
print()   

for i in range(count-1,-1,-1):
    print(word[i],end="")    
    
print()
#####################################

for ch in word:
    cnt=word.count(ch)
    if cnt>1:
        print(ch)    