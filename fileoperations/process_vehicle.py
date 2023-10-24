f_read=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\vehicle_no.txt","r")

f_write=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\kerala_reg.txt","w")

for line in f_read:
    reg_no = line.rstrip("\n")
    if line.startswith('KL'):
        f_write.write(reg_no+"\n")