cakes=[
    {"id":1, "name":"bluberry","shape":["round","square","heart"],"varients": [
        {"weight":"0.5","price":500},
        {"weight":"1","price":1000}
    ]},
    
    {"id":2, "name":"blackberry","shape":["round","square","heart"],"varients": [
        {"weight":"0.5","price":400},
        {"weight":"1","price":800}
    ]},
    
    {"id":3, "name":"red velvet","shape":["round","square","heart"],"varients": [
        {"weight":"0.5","price":700},
        {"weight":"1","price":1400}
    ]},
    
    {"id":4, "name":"black forest","shape":["round","square","heart"],"varients": [
        {"weight":"0.5","price":350},
        {"weight":"1","price":700}
    ]},
    
    {"id":5, "name":"white forest","shape":["round","square","heart"],"varients": [
        {"weight":"0.5","price":600},
        {"weight":"1","price":1200}
    ]}
]

#all cake weigh 1
all_1kg=[ck.get("name") for ck in cakes for v in ck.get("varients") if v.get("weight")=="1"]
# print(all_1kg)


#max price
max_price=max(v.get("price")  for ck in cakes for v in ck.get("varients") )
# print(max_price)


#all shape
all_shape=[ck.get("shape") for ck in cakes ]
# print(all_shape)


#weight 1 and price less than 1000
price_weight_filter=[ck.get("name") for ck in cakes for v in ck.get("varients") if v.get("weight")=="1" and v.get("price")<=1000]
# print(price_weight_filter)

#print all cake name
cake_name=[ck.get("name") for ck in cakes]
print(cake_name)


#price sorted
sorted_price=sorted(cakes, reverse=False, key=lambda pr:pr.get("price")) 
print(sorted_price) 
