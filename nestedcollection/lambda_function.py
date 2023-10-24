def add_num(n1,n2):
    return n1+n2
print(add_num(10,20))

#lambda function
add_number=lambda n1,n2:n1+n2
print(add_number(10,5))

min=lambda n1,n2:n1 if n1<n2 else n2
print(min(100,200))

odd=lambda n:"odd" if n%2!=0 else "even"
print(odd(101))