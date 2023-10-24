from json import load

path= "C:\\Users\\Sinju\\Desktop\\mypython\\countries\\data.json"

with open(path,encoding="utf-8")as f:
    data=load(f)
    
print(len(data)) 

all_reg={c.get("region") for c in data}   
# print(all_reg)


#asian countries
asian=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian)


#independent
independ_c=[c.get("name") for c in data if c.get("independent")==True]
# print(independ_c)


#name of country with highest population
population=max(data,key=lambda p:p.get("population"))
print(population.get("name"))


#countries sharing border with india
border=[c.get("name") for c in data  if c.get("borders")=="IND"]
print(border)

