source_word="chicken"
target_word="hen"

# is_kangaroo=True

source_word_lst=[]
for ch in source_word:
    source_word_lst.append(ch)
    
for ch in target_word:
    char_count=source_word_lst.count(ch)
        
    if char_count>0:
        source_word_lst.remove(ch)
            
    else:
        print(f"{target_word} is not a kangaroo word") #for-else combinaton
        # is_kangaroo=False
        break
else:
    print(f"{target_word} is a kangaroo word")        
# print(is_kangaroo)        
        
