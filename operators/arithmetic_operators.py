num1=25
num2=5

num3=13
num4=2

#addition
add_res=num1+num2
print(f"addition result {add_res}")

#sub
sub_res=num1-num2
print(f"subbtraction result {sub_res}")

#div
div_res=num1/num2
print(f"division result {div_res}")

#mul
mul_res=num1*num2
print(f"multiplication result {mul_res}")

#modu
mod_res=num1%num2
print(f"modulus result {mod_res}")

#exponential
exp_res=num1**num2
print(f"exponential is {exp_res}")
 
# floor
flo_res=num3//num4
print(f"floor division result is {flo_res}")


#degree to fahrenheit
temp_indegree=32
#(0°C × 9/5) + 32 = 32°F
far=(temp_indegree*9/5)+32
print(f"temp in farhenheit is {far}")

#fahrenheit to degree
# (32°F − 32) × 5/9 = 0°C
temp_infarhen = 40
deg=(temp_infarhen-32)*5/9
print(f"temp in degree is {deg}")


#bmi
weight_inkg=53
height_incm=153
height_inm=(height_incm/100)
# bmi=(w in kg)/h in m**2
bmi=(weight_inkg)/(height_inm)**2
print(f"bmi is {bmi}")

#sellingprice
cost_price=300
dis_perentage=10
discount_price=cost_price*(dis_perentage/100)
selling_price=(cost_price-discount_price)
print(f"selling price is {selling_price}")


