#3385 7526 7952
#12 digit 
#space with or with out

from re import*

aadhar_no=input("enter aadhar number")
pattern="\d{4}[\s]?\d{4}[\s]?\d{4}"

matcher=fullmatch(pattern,aadhar_no)
print("invalid" if matcher==None else "valid")
