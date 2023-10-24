#get percentage mark from user
#according to percentage,mark the grade
#>90 ---A
#>80 <=90---B
#>60 <=80---C
#<60----D

perntage=int(input("Enter the mark percentage"))
if(perntage>90):
    print("grade is A")
elif(perntage<=90 and perntage>80):
    print("grade id B")
elif(perntage<80 and perntage>60):
    print("grade is C")
else:
    print("grade is D")