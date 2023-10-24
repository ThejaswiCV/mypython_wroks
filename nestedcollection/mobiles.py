mobiles=[
        {"id":1,"name":"samsungs22","brand":"samsung","varients":[
            {"ram":"8gb","rom":"128gb","price":84000},
            {"ram":"8gb","rom":"256gb","price":100000},    
        ]}, 
         
         
        {"id":2,"name":"samsungA52","brand":"samsung","varients":[
            {"ram":"4gb","rom":"128gb","price":54000}, 
            {"ram":"8gb","rom":"256gb","price":65000},    
        ]}, 
        
        {"id":3,"name":"one plus nord2","brand":"one plus","varients":[
             {"ram":"8gb","rom":"128gb","price":34000}, 
             {"ram":"8gb","rom":"256gb","price":45000}, 
        ]},
           
        {"id":4,"name":"mi11","brand":"redmi","varients":[    
             {"ram":"8gb","rom":"128gb","price":24000},   
             {"ram":"8gb","rom":"256gb","price":35000},   
        ]},
        
        ]

all_mob=[mob.get("name") for mob in mobiles]
# print(all_mob)

all_brand=[br.get("brand") for br in mobiles]
# print(set(all_brand))

#20k-30k
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price")in range(20000,30001):
#             # print(mob.get("name"))
          
price_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
# print(price_filter)



#ram filter
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

ram_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
# print(ram_filter)   



#8gb ram and <40000
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="8gb" and v.get("price")<=40000:
#             print(mob.get("name"))   
            
ram_price=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="8gb" and v.get("price")<=40000]                      
# print(ram_price)            



#costly
costly=max(v.get("price") for mob in mobiles for v in mob.get("varients"))
print(costly)


            
            













