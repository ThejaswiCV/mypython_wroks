lst1=[10,15,25,35,30,5]
lst2=[15,20,40,45,50,30]

lst1.sort()
lst2.sort()

p1,p2=0,0
while(p1<len(lst1) and p2<len(lst2)):
    if (lst1[p1]==lst2[p2]):
        print("common",lst1[p1])
        p1+=1
        p2+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    else:
        p2+=1