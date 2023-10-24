#validate gmail id
from re import*

gmail=input("enter gmail id")
pattern="\w+[@](gmail|live).com"

matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")