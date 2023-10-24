#CAB P T 8859 B
#P C A F H T
from re import*

pan=input("enter pancard number")
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan)

print("invalid" if matcher==None else "valid")