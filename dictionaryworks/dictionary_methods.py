animals={"a":"apple","b":"banana","c":"cat","d":"dog","e":"elephant"}

#print all keys, keys()
for k in animals.keys():
    print(k)
    
#print all values
for v in animals.values():
    print(v)    
    
#print key and values    
for k,v in animals.items():
    print(k,v)
    
#value using key
# 1)print(animals("a"))
print(animals["a"])    
# print(animals["w"])    >> will show error

#2)get("key")    
print(animals.get("a"))
print(animals.get("w"))

# pop(key)
animals.pop("a")
print(animals)