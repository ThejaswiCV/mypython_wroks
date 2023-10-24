lst=[11,10,20,35,12,13,15]

element=int(input("enter the element"))
is_present=False
for i in range(0,len(lst)):
    if (lst[i]==element):
        is_present=True
        break
print(is_present)