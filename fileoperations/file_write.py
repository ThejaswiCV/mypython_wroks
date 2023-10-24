f=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\data.txt","w")

lst=["hai","hello","hai","how are you?"]

for w in lst:
    f.write(w+"\n")
    
#write years from 2000 -2023 in data.txt file
for y in range(2000,2024):
    f.write(str(y)+"\n")
        
print("completed")    