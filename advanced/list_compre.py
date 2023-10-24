# list comprehension

lst=[3,4,5,6,7,8,9]

# cube=[]
# for num in lst:
#     num=num**3
#     cube.append(num)
# print(cube)   

ev=[]
for num in lst:
    if num%2==0:
        ev.append(num)
print(ev)  
    
even=[num for num in lst if num%2==0]   
print(even) 
    
odd=[num for num in lst if num%2!=0] 
print(odd)

cubes=[num**3 for num in lst]
print(cubes)

squares=[num**2 for num in lst]
print(squares)

add_two=[num+2 for num in lst]
print(add_two)