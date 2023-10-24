text="ABACD"
#first recursive character
lst=[]    #empty list

for ch in text:    #ch>>a
    ch_count=lst.count(ch)  #check whether the charcter is in the list.
                             #a is not in the list
    if ch_count==0:          # if a not in lst
        lst.append(ch)       #append ch in list   (first ch will be 'a') 
        
    else :
        print(f"{ch} is the first recursive character")  
        break                  
    

