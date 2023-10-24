#int float => number type 
# string (str) => character type
#boolean (bool)

age =10 #integer

# avg = 12.3 #float

#is_done = true #boolean

# location = 'knr' #string


# print() => to print msg in console
# type() => datatype return
print(age)
print(type(age))

#swaping
num1=10
num2=20
print(f"value before swaping {num1} {num2}")  #10 20

temp=num1
num1=num2
num2=temp
print(f"value after swaping {num1} {num2}")  #20 10

#swaping without third variable
num1=num1+num2 #10+20=30
num2=num1-num2 #30-20=10
num1=num1-num2 #30-10=20
print(f"value after swaping w o third var {num1} {num2}") #20 10

#metod only use in python
(num1,num2)=(num2,num1)
print(f"value after swaping method {num1} {num2}")