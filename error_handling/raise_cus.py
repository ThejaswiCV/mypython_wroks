age=int(input("enter the age"))

if age<18:
    raise Exception("not eligible")
else:
    print("eligible")