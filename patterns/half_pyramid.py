# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

# for row in range(1,7):
#     for col in range(1,7):
#         if (row==col):
#             print(row*"*",end="")
#             # break
#     print() 
    
for row in range(1, 7):
    for col in range(1, row + 1):
        print("*", end="\t")
    print()       