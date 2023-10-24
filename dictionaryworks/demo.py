#dict={"key":"value","key":"value"}
student={"name":"Thejaswi cv","roll no":"17","dept":"electronics"}


employee={"id":"kavn1551","name":"Thejaswi cv","age":22,"designaton":"inter"}


print(employee["name"])

print("age" in employee)   #in>>>membership operator

if "salary" in employee:
    print("present")
else:
    print("not present")
    
employee["salary"] =15000 
print(employee) 