weight_inkg = 53
height_incm =153
height_inm = (height_incm/100)
bmi=(weight_inkg)/(height_inm**2)
print(bmi)

if (bmi<20):
    print("underweight")
elif(bmi>=20 and bmi<24):
    print("normal")
elif(bmi>=25 and bmi<29):
    print("overweight")
else:
    print("obesity")