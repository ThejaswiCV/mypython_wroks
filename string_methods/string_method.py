name="Thejaswi CV"         #lowercase the entire letters
print(name.casefold())

place="thalassery"         #captitalize first letter
print(place.capitalize())

print(place.count('s'))    #count specified character

print(name.startswith('The')) #check whether the string starts with the specified sequence of character

print(name.endswith('CV'))


street="gandinagar101"
print(place.isalpha()) #check whether only string or not>>true if it only contain string
print(street.isalpha())  #false
print(street.isdigit())  #false
print(street.isalnum())#check if it contain only alphabet and digit

night="Good night sweet dreams"
wish1=night.split(" ")
print(wish1)

for n in wish1:
    print(n)



mrng="Good,morning,Dear"
wish2=mrng.split(",")
print(wish2)

for m in wish2:
    print(m)


text="good afternoon\n"
#strip()
#lstrip()
#rstrip()
print(text.rstrip("\n"))
