f_read=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\years.txt","r")
#read from file years.txt


f_write=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\leap_years.txt","w")
#creating a file named leap_years.txt

for line in f_read:                         #read from file 
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0:
        f_write.write(str(year)+"\n")
    elif year%100!=0 and year%4==0:
        f_write.write(str(year)+"\n")  