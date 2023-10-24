from json import load

path="C:\\Users\\Sinju\\Desktop\\mypython\\products\\items.json"

with open(path,encoding="utf-8") as f:
    data=load(f)
 
#total number of products    
# print(len(data))    



#print all categories
all_cat={pr.get("category") for pr in data}
# print(all_cat)



#electronic cat products name
electr=[pr.get("title") for pr in data if pr.get("category")=="electronics"]
# print(electr)

# for pr in data:
#     if pr.get("category").count("electronics")>0:
#         print(pr.get("title"))
        

#top rating
top_rated=max(data, key=lambda p: p.get("rating").get("rate"))
# print(top_rated.get("title"))

             
#product having woemn cat and price range(100,300)
for pr in data:
   if pr.get("category")=="women's clothing" and  pr.get("price")>20 and pr.get("price")<=100 :
       print(pr.get("title"))
       
       
#which product got most number of rating(count)
top_count=max(data,key=lambda p: p.get("rating").get("count"))
# print("TOP COUNT:" ,top_count.get("title"))


#jew product with rating >3
for pr in data:
    if pr.get("category")=="jewelery" and pr.get("rating").get("rate")>=3:
        print(pr.get("title"))


#sort product wrt price in desc order
sorted_data=sorted(data,reverse=True,key=lambda p:p.get("price"))
# print(sorted_data)
# for sr in sorted_data:
#     print(sr.get("title"),sr.get("price"))



orders={"vb":10, "bh":15, "rh":80}
# val_key=[(v,k) for k,v in orders.items()]
# print(max(val_key))
print(max([(v,k) for k,v in orders.items()]))


#category wise product count
wc={}
for pr in data:
    category=pr.get("category")
    if category not in wc:
       wc[category]=1
    else:
       wc[category]+=1
print(wc)     
#max product in which category
# print(max([(v,k) for k,v in wc.items()])) # >== last one will be max among and first min value will be first when we aplly min
  
val_key=[(v,k) for k,v in wc.items()]     
print(max(val_key, key=lambda lst:lst[0])) #first large value will be max ,here(electronics: 6, womens:6 ) so ans elecronics    
                                         #explicitly mentioned 
