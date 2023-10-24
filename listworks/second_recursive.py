text="ABACCD"

lst=[]
duplictae_lst=[]

for ch in text:
    ch_count=lst.count(ch)
    if ch_count==0:
        lst.append(ch)
        
    else:
      duplictae_lst.append(ch)


print(duplictae_lst)           #print the list of recursive characters
print(duplictae_lst[1])        #second recursive