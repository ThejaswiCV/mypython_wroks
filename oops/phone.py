data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]

def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} added succesfully"


def retrieve(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()
    return obj

#delete
def destroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()
    data.remove(obj)
    return f"{obj} removed from data"

 #list all resources   
def get(*args,**kwargs):
        return data
    
#update
def put(id,*args,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} updated sucessfully"    
    
print(create(id=105, name="oneplus", price=45000))

print(retrieve(id=101))

print(destroy(id=100))

print(get())

print(put(id=104,name="vivo V27 pro",price=40000))

print(data)