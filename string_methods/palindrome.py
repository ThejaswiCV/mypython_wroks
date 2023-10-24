word="abba"
count=len(word)
p_strr=""

for i in range(count-1,-1,-1):
    p_strr+=word[i]    #append word to p_strr
    
print("palindrome " if word==p_strr else "not palindrome")    