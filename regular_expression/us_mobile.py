#212-456-7890

from re import*

mob=input("enter mobile number")
pattern="\d{3}[-\s]?\d{3}[-\s]?\d{4}"

matcher=fullmatch(pattern,mob)

print("invalid" if matcher==None else "valid")