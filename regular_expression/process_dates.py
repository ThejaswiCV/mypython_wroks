from re import*

f=f=open("C:\\Users\\Sinju\\Desktop\\mypython\\regular_expression\\dates.txt")

# pattern="\d{2}[-\s./]\d{2}[-\s./]\d{4}"

# pattern="\d{2}[-\s./]\d{2}[-\s./](20)(0[0-9]|1[0-9]|2[0-3])"  #2000 to 2023

# pattern="\d{2}[-\s./]\d{2}[-\s./](20)([01][0-9]|2[0-3])"  #2000 to 2023

pattern="([0][1-9]|[12][0-9]|3[01])[-\s./](0[1-9]|1[0-2])[-\s./](20)(0[0-9]|1[0-9]|2[0-3])"  #date 01-31,month 01 to 12 ,2000-2023

for line in f:
    date=line.rstrip("\n")
    
    matcher=fullmatch(pattern,date)
    if matcher!=None:
        print(date)
    