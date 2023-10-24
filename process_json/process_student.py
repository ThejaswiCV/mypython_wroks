from json import load

# f=open("C:\\Users\\Sinju\\Desktop\\mypython\\process_json\\student.json")

# data=load(f)

# print(data)   #now it is converted from json format to list of dictionaries


#another method to open( so no need to close the file like f.close())

path="C:\\Users\\Sinju\\Desktop\\mypython\\process_json\\student.json"

with open(path) as f:
   data=load(f)
   
print(data)    
    