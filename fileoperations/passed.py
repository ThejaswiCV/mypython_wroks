f1=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\students.txt")
f2=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\failed.txt")

all_students={line.rstrip("\n") for line in f1}
failed={line.rstrip("\n") for line in f2}

passed_students=all_students.difference(failed)
print(passed_students)
