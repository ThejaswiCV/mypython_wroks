def swap_nums(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper    

@swap_nums
def sub(n1,n2):
    return n1-n2

@swap_nums
def div(n1,n2):
    return n1/n2

print(sub(2,12))
print(div(2,12))



def capitalize(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res 
    return wrapper  
    
@capitalize
def morning_greetings():
    return "good morning"

@capitalize
def afternoon_greetings():
    return "good afternoon"

print(morning_greetings())
print(afternoon_greetings())