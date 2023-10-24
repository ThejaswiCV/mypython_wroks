def add(*args):
#     print(args)
    
# add(10,20,30)   
    return sum(args)
print(add(10,20))


def product(*args):
    res=1
    for num in args:
        res=res*num
    return res
print(product(20,20))   
print(product(20,20,20))  


def concat_str(*args):
#     str=""
#     for s in args:
#         str+=s
#     return str
# print(concat_str("hai","hello","good","morning"))

    return "#".join(args)
print(concat_str("hai","hello","good","morning"))
    
    
#str> join()

data="is".join(("tea","good","hot"))    
# print(data)

hashh="#".join(("hai","hello","hai"))
# print(hashh)


#reverse concatenate
def reverse_concate(*args):
    data=list(args)
    data.reverse()
    return "".join(data)
    
print(reverse_concate("hai","hello","dear"))    