st1={"red","green","orange","blue"}
st2={"purple","white","red","green"}

st3={"red","green","blue"}
st4={"blue","red","green","yellow","black"}

#add
st1.add("black")
print(st1)

#remove
st2.remove("purple")
print(st2)

#subset
print(st3.issubset(st4))

#superset
print(st4.issuperset(st1))

#union
union_set=st1.union(st2)
print(union_set)

#intersection
inter_set=st1.intersection(st2)
print(inter_set)

#difference
diff_set=st1.difference(st2)
print(diff_set)

#common in a list
lst1=[5,10,15,20,25,30]
lst2=[10,20,30]

lst1_set=set(lst1)       #list to set
lst2_set=set(lst2)
inter=lst1_set.intersection(lst2_set)
print(inter)

#or
print(set(lst1).intersection(set(lst2)))