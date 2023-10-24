colors=["red","green","blue","red"]

#append()
colors.append("yellow")
print(colors)

#count()
print(colors.count("red"))

#index
print(colors.index("green"))

#insert
colors.insert(2,"black")
print(colors)

#sort
colors.sort()
print(colors)

#remove
colors.remove("red")
print(colors)

#pop()
colors.pop(2)
print(colors)
# pop()   >>>>by default it is pop(index=-1) so it will remove last element if we give colors.pop()

# copy
cpy_col=colors.copy()
print(cpy_col)

a=10
b=10

print(id(a))
print(id(b))

print(a==b)
print(a is b)