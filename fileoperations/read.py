f=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\data.txt")

# for line in f:
#     print(line)
# f.close() 
    
words=[line.rstrip("\n") for line in f]    
print(words)
   